#!/usr/bin/env python3
"""Validate Concord Saga canon substrate against rules/canon_rules.json.

Reports violations. Never modifies anything. Exits non-zero if any are found.

Every rule this script enforces is read from `rules/canon_rules.json` at runtime —
the SID format, the ECID field list and all six controlled vocabularies. Nothing is
hardcoded. If the author changes that file, this script follows without edits.

Checks
------
CHK_SID_FORMAT   Tokens shaped like a SID are validated component by component
                 against the declared `systems.id_system.SID_format`, including the
                 two-digit book rule. Act IDs (the SID prefix ending at the act
                 component, used by act_overlays) are accepted as a valid shorter form.
CHK_ECID_FIELDS  Files that carry an ECID block must name every field in
                 `systems.id_system.ECID_fields`. Packet labels declared in
                 `ECID_field_aliases` (`U-Level` for `CORRIDOR`, `Resonance State`
                 for `RES`) are accepted and normalized.
CHK_VOCAB        Values in ECID-bearing CSV columns and in known JSON envelope keys
                 must belong to the matching controlled vocabulary — every axis,
                 including `LOAD` and the three supplement axes.
CHK_VT_CAP       `VT` Glimpses are capped at 10-12 across all nine books
                 (`supplement_system.constraints`). Exceeding the maximum is a
                 violation; being under the minimum is not, since the saga is
                 unwritten and an empty grid is not a defect.

Scope
-----
By default the canon substrate is scanned: rules/, canon/, grids/, book_context/,
act_overlays/, templates/, source_canon/.

`recovery/`, `proposals/` and `CLAUDE.md` are excluded by default because they are
meta-documentation that deliberately quotes malformed identifiers while documenting
them — a checker that flags a memo for quoting the error it describes is reporting
noise, not defects. Pass --all to include them; the report records both figures.

Usage
-----
    python3 tools/validate_canon.py                 # scan canon substrate
    python3 tools/validate_canon.py --all           # include recovery/proposals/CLAUDE.md
    python3 tools/validate_canon.py --report FILE   # also write the report to FILE
    python3 tools/validate_canon.py --quiet         # summary only

Standard library only. No third-party dependencies.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES = os.path.join(REPO, "rules", "canon_rules.json")

SUBSTRATE_DIRS = [
    "rules", "canon", "grids", "book_context",
    "act_overlays", "templates", "source_canon",
]
META_DIRS = ["recovery", "proposals"]
META_FILES = ["CLAUDE.md", "README.md"]

SCANNED_SUFFIXES = (".md", ".json", ".csv")

# ECID field name -> controlled_vocab key. Fields absent here (POV, ENV) are free text.
FIELD_VOCAB = {
    "CORRIDOR": "corridors",
    "WEATHER": "weather",
    "MODE": "modes",
    "HEAT": "heat",
    "FX": "fx",
    "RES": "res_states",
    "LOAD": "load",
}

# Supplement axes. These are not ECID fields; they live in the supplement grids and
# draw on `supplement_system` rather than `controlled_vocab`.
SUPPLEMENT_COLUMNS = {
    "SUPPLEMENT_TYPE": "supplement_types",
    "SUPPLEMENT_FUNCTION": "supplement_functions",
    "SUPPLEMENT_VEHICLE": "supplement_vehicles",
}

# JSON key -> controlled_vocab key, for the envelope files.
JSON_KEY_VOCAB = {
    "max_corridor_tier": "corridors",
    "max_weather": "weather",
    "max_fx": "fx",
    "corridor_max": "corridors",
    "weather_max": "weather",
    "default_vfx_ceiling": "fx",
    "allowed_heat_range": "heat",
}

# Placeholder values that are scaffolding, not vocabulary violations. Reported
# separately so an unpopulated skeleton is not confused with a wrong token.
PLACEHOLDERS = {"TODO", "TBD", "", "NONE", "N/A"}


class Violation:
    def __init__(self, check, path, line, token, detail):
        self.check = check
        self.path = path
        self.line = line
        self.token = token
        self.detail = detail

    def __str__(self):
        loc = f"{self.path}:{self.line}" if self.line else self.path
        return f"  {loc}\n      {self.token!r} — {self.detail}"


# --------------------------------------------------------------------------- #
# SID format, derived from the declared pattern
# --------------------------------------------------------------------------- #

class SidFormat:
    """Parses a pattern like S1.T{1-3}.B{01-09}.A{1-3}.E{01-99} into a matcher.

    A `{lo-hi}` group declares both a numeric range and a digit width, taken from
    the literal width of `lo`. So `{01-09}` requires exactly two digits, which is
    what makes the two-digit book rule enforceable rather than advisory.
    """

    def __init__(self, pattern):
        self.pattern = pattern
        self.literals = []   # literal text before each numeric component
        self.numerics = []   # (width, lo, hi) per numeric component
        parts = re.split(r"\{(\d+)-(\d+)\}", pattern)
        # parts alternates: literal, lo, hi, literal, lo, hi, ..., trailing literal
        i = 0
        while i < len(parts):
            lit = parts[i]
            if i + 2 < len(parts):
                lo, hi = parts[i + 1], parts[i + 2]
                self.literals.append(lit)
                self.numerics.append((len(lo), int(lo), int(hi)))
                i += 3
            else:
                self.trailing = lit
                break
        else:
            self.trailing = ""
        # Loose finder: same literals, digits of ANY width. Malformed identifiers
        # match this and then fail component validation, which is the point.
        loose = "".join(re.escape(l) + r"(\d+)" for l in self.literals)
        self.finder = re.compile(loose + re.escape(self.trailing))
        # Prefix forms: a token may legitimately stop at an earlier component
        # (an act ID stops before the episode component).
        self.prefixes = []
        for n in range(1, len(self.literals) + 1):
            loose_n = "".join(re.escape(l) + r"(\d+)" for l in self.literals[:n])
            self.prefixes.append(re.compile(loose_n + r"(?![\d.])"))

    def find_candidates(self, text):
        """Yield (token, start_offset) for anything SID-shaped, valid or not."""
        seen = set()
        for rx in reversed(self.prefixes):   # longest form first
            for m in rx.finditer(text):
                span = (m.start(), m.end())
                if any(s <= span[0] and span[1] <= e for s, e in seen):
                    continue
                seen.add(span)
                yield m.group(0), m.start(), m.groups()

    def validate(self, groups):
        """Return a list of problems for the numeric components of a candidate."""
        problems = []
        for idx, raw in enumerate(groups):
            width, lo, hi = self.numerics[idx]
            label = self.literals[idx].lstrip(".") or f"component {idx + 1}"
            if len(raw) != width:
                problems.append(
                    f"{label}{raw} has {len(raw)} digit(s), format requires "
                    f"{width} ({label}{str(lo).zfill(width)}..{label}{str(hi).zfill(width)})"
                )
            elif not (lo <= int(raw) <= hi):
                problems.append(
                    f"{label}{raw} out of range {lo}..{hi}"
                )
        return problems


# --------------------------------------------------------------------------- #
# Loading and file discovery
# --------------------------------------------------------------------------- #

def load_rules():
    with open(RULES, encoding="utf-8") as fh:
        return json.load(fh)


def iter_files(include_meta):
    roots = list(SUBSTRATE_DIRS)
    if include_meta:
        roots += META_DIRS
    for root in roots:
        base = os.path.join(REPO, root)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d != ".git"]
            for name in sorted(filenames):
                if name.endswith(SCANNED_SUFFIXES):
                    yield os.path.join(dirpath, name)
    if include_meta:
        for name in META_FILES:
            p = os.path.join(REPO, name)
            if os.path.isfile(p):
                yield p
    else:
        p = os.path.join(REPO, "README.md")
        if os.path.isfile(p):
            yield p


def rel(path):
    return os.path.relpath(path, REPO)


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #

def check_sids(path, text, sidfmt, out):
    for lineno, line in enumerate(text.splitlines(), 1):
        for token, _, groups in sidfmt.find_candidates(line):
            for problem in sidfmt.validate(groups):
                out.append(Violation("CHK_SID_FORMAT", rel(path), lineno, token, problem))


def split_values(raw):
    """Split a field value into candidate tokens.

    Packet values compound several ways: `INT / CIV / LORE`, `CALM -> STRAIN`,
    `U3 -> U4 in flashes`. Split on separators and keep tokens that look like
    vocabulary terms, dropping parenthetical and descriptive prose.
    """
    raw = re.sub(r"\([^)]*\)", " ", raw)
    parts = re.split(r"[/,;]|→|->|\s+", raw)
    return [p.strip().strip(".").upper() for p in parts if p.strip()]


def normalize_header(header, alias_map):
    """Map declared packet-label aliases onto their canonical schema field names."""
    return [alias_map.get(col, col) for col in header]


def check_csv(path, sidfmt, ecid_fields, vocab, supp, alias_map, out, vt_counter):
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        return
    raw_header = [h.strip().upper() for h in rows[0]]
    header = normalize_header(raw_header, alias_map)
    # An ECID-bearing CSV is one naming at least half the ECID fields.
    present = [f for f in ecid_fields if f in header]
    if len(present) >= max(2, len(ecid_fields) // 2):
        missing = [f for f in ecid_fields if f not in header]
        if missing:
            out.append(Violation(
                "CHK_ECID_FIELDS", rel(path), 1, ",".join(raw_header),
                f"ECID block missing required field(s): {', '.join(missing)}",
            ))
    col_vocab = {}
    for i, col in enumerate(header):
        if col in FIELD_VOCAB:
            col_vocab[i] = ("controlled_vocab", FIELD_VOCAB[col])
        elif col in SUPPLEMENT_COLUMNS:
            col_vocab[i] = ("supplement_system", SUPPLEMENT_COLUMNS[col])
    vehicle_col = header.index("SUPPLEMENT_VEHICLE") if "SUPPLEMENT_VEHICLE" in header else None
    for lineno, row in enumerate(rows[1:], 2):
        if vehicle_col is not None and vehicle_col < len(row):
            if row[vehicle_col].strip().upper() == "VT":
                vt_counter.append((rel(path), lineno))
        for i, (source, dim) in col_vocab.items():
            if i >= len(row):
                continue
            raw = row[i].strip()
            if raw.upper() in PLACEHOLDERS:
                continue
            allowed = allowed_tokens(source, dim, vocab, supp)
            for tok in split_values(raw):
                if not tok or tok in PLACEHOLDERS:
                    continue
                if tok not in allowed:
                    out.append(Violation(
                        "CHK_VOCAB", rel(path), lineno, tok,
                        f"column {raw_header[i]} expects one of {dim}: "
                        f"{', '.join(sorted(allowed))}",
                    ))


def allowed_tokens(source, dim, vocab, supp):
    """Permitted tokens for a dimension.

    Provisional supplement types (decisions 7: ROM, TECH, CHAR) are accepted rather
    than flagged — the instruction was to apply section 7 while marking it unratified.
    The report's configuration block names them so nothing downstream mistakes them
    for ruled vocabulary.
    """
    if source == "controlled_vocab":
        return {v.upper() for v in vocab[dim]}
    allowed = {k.upper() for k in supp.get(dim, {})}
    if dim == "supplement_types":
        allowed |= {k.upper() for k in supp.get("supplement_types_provisional", {})
                    if not k.startswith("_")}
    return allowed


def check_vt_cap(vt_rows, supp, out):
    """The one supplement constraint a script can settle: decisions 3.4."""
    cons = supp.get("constraints", {})
    cap = cons.get("vt_glimpses_max_total")
    if cap is None:
        return
    if len(vt_rows) > cap:
        for path, lineno in vt_rows[cap:]:
            out.append(Violation(
                "CHK_VT_CAP", path, lineno, "VT",
                f"VT Glimpses exceed the cap of {cap} across "
                f"{cons.get('vt_glimpses_scope', 'the saga')} "
                f"({len(vt_rows)} found)",
            ))


def walk_json(node, vocab, path, out, trail=""):
    if isinstance(node, dict):
        for key, val in node.items():
            here = f"{trail}.{key}" if trail else key
            dim = JSON_KEY_VOCAB.get(key)
            if dim:
                values = val if isinstance(val, list) else [val]
                allowed = {v.upper() for v in vocab[dim]}
                for v in values:
                    if not isinstance(v, str):
                        continue
                    if v.strip().upper() in PLACEHOLDERS:
                        out.append(Violation(
                            "CHK_VOCAB", rel(path), None, v,
                            f"{here} is an unpopulated placeholder; expects one of "
                            f"{dim}",
                        ))
                        continue
                    if v.strip().upper() not in allowed:
                        out.append(Violation(
                            "CHK_VOCAB", rel(path), None, v,
                            f"{here} expects one of {dim}: "
                            f"{', '.join(sorted(vocab[dim]))}",
                        ))
            walk_json(val, vocab, path, out, here)
    elif isinstance(node, list):
        for item in node:
            walk_json(item, vocab, path, out, trail)


def check_json(path, vocab, out):
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        out.append(Violation("CHK_JSON_PARSE", rel(path), exc.lineno, "", str(exc)))
        return
    walk_json(data, vocab, path, out)


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def build_report(violations, scanned, include_meta, rules, vt_count=0):
    idsys = rules["systems"]["id_system"]
    supp = rules.get("supplement_system", {})
    lines = []
    w = lines.append
    w("# Concord Saga — Canon Validation Report")
    w("")
    w("Generated by `tools/validate_canon.py`. Reports violations only; fixes nothing.")
    w("")
    w("## Configuration")
    w("")
    w(f"- Rules source: `rules/canon_rules.json` (schema {rules.get('schema_version')})")
    w(f"- SID format: `{idsys['SID_format']}`")
    w(f"- ECID fields: {', '.join(idsys['ECID_fields'])}")
    aliases = idsys.get("ECID_field_aliases", {})
    if aliases:
        w("- Accepted field aliases: "
          + "; ".join(f"`{a}` -> `{c}`" for c, al in aliases.items() for a in al))
    cons = supp.get("constraints", {})
    if cons.get("vt_glimpses_max_total") is not None:
        w(f"- VT Glimpses: {vt_count} found, cap "
          f"{cons.get('vt_glimpses_min_total')}-{cons['vt_glimpses_max_total']} across "
          f"{cons.get('vt_glimpses_scope', 'the saga')}")
    prov = [k for k in supp.get("supplement_types_provisional", {})
            if not k.startswith("_")]
    if prov:
        w(f"- Provisional supplement types accepted (UNRATIFIED, decisions §7): "
          f"{', '.join(prov)}")
    w(f"- Files scanned: {scanned}")
    w(f"- Scope: {'all (including recovery/, proposals/, CLAUDE.md)' if include_meta else 'canon substrate only'}")
    w("")
    by_check = {}
    for v in violations:
        by_check.setdefault(v.check, []).append(v)
    w("## Summary")
    w("")
    if not violations:
        w("No violations found.")
    else:
        w(f"**{len(violations)} violation(s)** across {len({v.path for v in violations})} file(s).")
        w("")
        w("| Check | Violations | Files |")
        w("| --- | --- | --- |")
        for check in sorted(by_check):
            vs = by_check[check]
            w(f"| `{check}` | {len(vs)} | {len({v.path for v in vs})} |")
    w("")
    for check in sorted(by_check):
        vs = by_check[check]
        w(f"## {check} — {len(vs)} violation(s)")
        w("")
        by_file = {}
        for v in vs:
            by_file.setdefault(v.path, []).append(v)
        for path in sorted(by_file):
            w(f"### `{path}`")
            w("")
            for v in by_file[path]:
                loc = f"line {v.line}" if v.line else "—"
                w(f"- {loc}: `{v.token}` — {v.detail}")
            w("")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--all", action="store_true",
                    help="include recovery/, proposals/ and CLAUDE.md")
    ap.add_argument("--report", metavar="FILE", help="write the markdown report here")
    ap.add_argument("--quiet", action="store_true", help="print the summary only")
    args = ap.parse_args()

    rules = load_rules()
    vocab = rules["controlled_vocab"]
    supp = rules.get("supplement_system", {})
    idsys = rules["systems"]["id_system"]
    sidfmt = SidFormat(idsys["SID_format"])
    ecid_fields = [f.upper() for f in idsys["ECID_fields"]]
    # reverse the declared alias map: packet label -> canonical schema field
    alias_map = {}
    for canonical, aliases in idsys.get("ECID_field_aliases", {}).items():
        for alias in aliases:
            alias_map[alias.upper()] = canonical.upper()

    violations = []
    vt_rows = []
    scanned = 0
    for path in iter_files(args.all):
        scanned += 1
        if path.endswith(".csv"):
            check_csv(path, sidfmt, ecid_fields, vocab, supp, alias_map,
                      violations, vt_rows)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        elif path.endswith(".json"):
            check_json(path, vocab, violations)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        else:
            with open(path, encoding="utf-8", errors="replace") as fh:
                check_sids(path, fh.read(), sidfmt, violations)

    check_vt_cap(vt_rows, supp, violations)

    report = build_report(violations, scanned, args.all, rules, len(vt_rows))
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(report)

    if args.quiet:
        print(f"{len(violations)} violation(s) across {scanned} file(s) scanned.")
    else:
        print(report)

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
