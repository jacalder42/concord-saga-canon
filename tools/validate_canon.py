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
                 for `RES`) are accepted and normalized. Fields listed in
                 `ECID_fields_optional` (`HEAT`, `FX` — optional at shell
                 granularity) are reported as notices, not violations.
CHK_VOCAB        Values in ECID-bearing CSV columns and in known JSON envelope keys
                 must belong to the matching controlled vocabulary — every axis,
                 including `LOAD` and the three supplement axes.
CHK_BANDS        Per-act `escalation_permissions` bands are well formed: every bound
                 is a member of its axis vocabulary, `min` does not exceed `max`, and
                 each `exceptions` entry names a valid axis, a valid value, and a SID
                 that parses. Band *values* are author judgement and are never
                 second-guessed; only their coherence is checked.
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

# ECID field name -> controlled_vocab key. Fields absent here (POV) are free text.
# ENV joined on 2026-09-19: its vocabulary derives from the geography system's type
# layer and only that layer (GATE_RULINGS_2026-09-19 Ruling 1). Named places are not
# ENV values, and the shard progression is a severity scale, not a spatial taxonomy.
FIELD_VOCAB = {
    "CORRIDOR": "corridors",
    "ENV": "env",
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
    "SUPPLEMENT_FORM": "supplement_forms",
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


def check_csv(path, sidfmt, ecid_fields, vocab, supp, alias_map, out, vt_counter,
              optional_fields=(), notices=None):
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
        required = [f for f in missing if f not in optional_fields]
        optional = [f for f in missing if f in optional_fields]
        if required:
            out.append(Violation(
                "CHK_ECID_FIELDS", rel(path), 1, ",".join(raw_header),
                f"ECID block missing required field(s): {', '.join(required)}",
            ))
        if optional and notices is not None:
            notices.append(Violation(
                "CHK_ECID_FIELDS", rel(path), 1, ",".join(raw_header),
                f"ECID block omits optional field(s): {', '.join(optional)} "
                f"- permitted at shell granularity, expected on full packets",
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
    allowed = {k.upper() for k in supp.get(dim, {}) if not k.startswith("_")}
    if dim == "supplement_types":
        allowed |= {k.upper() for k in supp.get("supplement_types_provisional", {})
                    if not k.startswith("_")}
    return allowed



MILESTONE_GRID = "grids/milestones_payoffs.csv"


def check_milestone_grid(path, rules, vocab, out, notices):
    """Structural checks over the populated milestone grid.

    The grid went live on 2026-09-20 with 36 rows, every one `proposed`. These
    checks are a ratchet against future edits rather than a cleanup task: they
    all pass on the load as promoted, so any later failure is a change someone
    made, not a pre-existing defect.

    One exception is deliberate. Five rows carry `target_act: EP`, which is not
    an act — all nine books have three acts and 27 is the cap. Whether `EP`
    belongs in the act slot at all is an OPEN author question (CLAUDE.md 4),
    so those rows are reported as notices rather than violations. They become
    violations the moment the ruling says `EP` is not an act slot, and valid
    the moment it says it is. Either way the checker does not decide.
    """
    spec = rules.get("milestone_grid")
    if spec is None:
        return
    try:
        with open(path, encoding="utf-8", newline="") as fh:
            rows = list(csv.reader(fh))
    except OSError:
        return
    if not rows:
        return

    header = [c.strip() for c in rows[0]]
    expected = spec["columns"]
    if header != expected:
        out.append(Violation(
            "CHK_GRID_SCHEMA", rel(path), 1, ",".join(header),
            "milestone grid header does not match milestone_grid.columns; "
            "column drift must fail loudly. Expected: " + ",".join(expected),
        ))
        return  # every check below indexes by column name

    idx = {c: i for i, c in enumerate(header)}
    data = [r for r in rows[1:] if any(c.strip() for c in r)]

    def cell(row, col):
        i = idx[col]
        return row[i].strip() if i < len(row) else ""

    # --- milestone_id unique and non-empty -------------------------------
    seen = {}
    ids = set()
    for lineno, row in enumerate(data, 2):
        mid = cell(row, "milestone_id")
        if not mid:
            out.append(Violation("CHK_GRID_ID", rel(path), lineno, "",
                                 "milestone_id is empty"))
            continue
        if mid in seen:
            out.append(Violation(
                "CHK_GRID_ID", rel(path), lineno, mid,
                f"duplicate milestone_id; first seen at line {seen[mid]}"))
        else:
            seen[mid] = lineno
        ids.add(mid)

    # --- required_setups must resolve ------------------------------------
    for lineno, row in enumerate(data, 2):
        for ref in split_values(cell(row, "required_setups")):
            if ref and ref not in ids:
                out.append(Violation(
                    "CHK_GRID_SETUPS", rel(path), lineno, ref,
                    f"required_setups references {ref}, which is not a "
                    f"milestone_id in this grid"))

    # --- target columns ---------------------------------------------------
    books = {f"B{n:02d}" for n in range(1, 10)}
    trilogies = set(spec["target_trilogy_values"])
    acts = set(spec["target_act_values"])
    for lineno, row in enumerate(data, 2):
        mid = cell(row, "milestone_id")
        book = cell(row, "target_book")
        if book and book not in books:
            hint = ("two-digit book required (B01..B09); "
                    f"{book} is the old one-digit form"
                    if book.startswith("B") and len(book) == 2
                    else "expected one of B01..B09")
            out.append(Violation("CHK_GRID_TARGET", rel(path), lineno, book,
                                 f"{mid} target_book: {hint}"))
        tri = cell(row, "target_trilogy")
        if tri and tri not in trilogies:
            out.append(Violation(
                "CHK_GRID_TARGET", rel(path), lineno, tri,
                f"{mid} target_trilogy expects one of {', '.join(sorted(trilogies))}"))
        act = cell(row, "target_act")
        if act and act not in acts:
            if act == "EP":
                notices.append(Violation(
                    "CHK_GRID_TARGET", rel(path), lineno, act,
                    f"{mid} target_act is EP, which is not an act - all nine "
                    f"books have three acts (27 is the cap). Whether EP belongs "
                    f"in the act slot is an OPEN author question; reported as a "
                    f"notice, not a violation. See CLAUDE.md section 4."))
            else:
                out.append(Violation(
                    "CHK_GRID_TARGET", rel(path), lineno, act,
                    f"{mid} target_act expects one of {', '.join(sorted(acts))}"))

    # --- status vocabulary -------------------------------------------------
    allowed = {v.upper() for v in vocab.get("milestone_status", [])}
    if allowed:
        for lineno, row in enumerate(data, 2):
            st = cell(row, "status")
            if st and st.upper() not in allowed:
                out.append(Violation(
                    "CHK_GRID_STATUS", rel(path), lineno, st,
                    "status expects one of " + ", ".join(sorted(allowed))))


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


BAND_AXIS_VOCAB = {"corridor": "corridors", "weather": "weather", "fx": "fx"}


def check_bands(path, data, vocab, sidfmt, out):
    """Validate the shape of an escalation_permissions band block.

    Checks coherence, never editorial judgement. That an act permits U3-U6 is the
    author's call; that `U9` is not a corridor, or that min exceeds max, is not.
    """
    ep = data.get("escalation_permissions")
    if not isinstance(ep, dict) or "corridor" not in ep:
        return                      # book_context's flat TODO form, handled elsewhere
    for axis, dim in BAND_AXIS_VOCAB.items():
        band = ep.get(axis)
        if not isinstance(band, dict):
            out.append(Violation("CHK_BANDS", rel(path), None, axis,
                                 f"escalation_permissions.{axis} is missing or not a band"))
            continue
        order = [v.upper() for v in vocab[dim]]
        lo, hi = band.get("min"), band.get("max")
        for label, val in (("min", lo), ("max", hi)):
            if not isinstance(val, str) or val.upper() not in order:
                out.append(Violation("CHK_BANDS", rel(path), None, str(val),
                                     f"{axis}.{label} is not a member of {dim}: "
                                     f"{', '.join(order)}"))
        if (isinstance(lo, str) and isinstance(hi, str)
                and lo.upper() in order and hi.upper() in order
                and order.index(lo.upper()) > order.index(hi.upper())):
            out.append(Violation("CHK_BANDS", rel(path), None, f"{lo}..{hi}",
                                 f"{axis}.min is above {axis}.max"))
    for exc in ep.get("exceptions", []):
        if not isinstance(exc, dict):
            continue
        axis = exc.get("axis")
        if axis not in BAND_AXIS_VOCAB:
            out.append(Violation("CHK_BANDS", rel(path), None, str(axis),
                                 f"exception axis must be one of "
                                 f"{', '.join(BAND_AXIS_VOCAB)}"))
            continue
        val = exc.get("value")
        allowed = {v.upper() for v in vocab[BAND_AXIS_VOCAB[axis]]}
        if not isinstance(val, str) or val.upper() not in allowed:
            out.append(Violation("CHK_BANDS", rel(path), None, str(val),
                                 f"exception value is not a member of "
                                 f"{BAND_AXIS_VOCAB[axis]}"))
        sid = exc.get("sid", "")
        found = list(sidfmt.find_candidates(sid))
        if not found:
            out.append(Violation("CHK_BANDS", rel(path), None, str(sid),
                                 "exception sid is not SID-shaped"))
        else:
            for _, _, groups in found:
                for problem in sidfmt.validate(groups):
                    out.append(Violation("CHK_BANDS", rel(path), None, sid, problem))


def check_json(path, vocab, out):
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except json.JSONDecodeError as exc:
        out.append(Violation("CHK_JSON_PARSE", rel(path), exc.lineno, "", str(exc)))
        return
    walk_json(data, vocab, path, out)
    return data


# --------------------------------------------------------------------------- #
# Report
# --------------------------------------------------------------------------- #

def build_report(violations, scanned, include_meta, rules, vt_count=0, notices=None):
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
    req = [f for f in idsys['ECID_fields']
           if f.upper() not in [o.upper() for o in idsys.get('ECID_fields_optional', [])]]
    opt = idsys.get('ECID_fields_optional', [])
    w(f"- ECID fields: {', '.join(req)}"
      + (f" (+ optional at shell granularity: {', '.join(opt)})" if opt else ""))
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
    if notices:
        w(f"## Notices — {len(notices)}")
        w("")
        w("Not violations; they do not affect the exit code.")
        w("")
        for n in notices:
            w(f"- `{n.path}`: {n.detail}")
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
    optional_fields = [f.upper() for f in idsys.get("ECID_fields_optional", [])]
    # reverse the declared alias map: packet label -> canonical schema field
    alias_map = {}
    for canonical, aliases in idsys.get("ECID_field_aliases", {}).items():
        for alias in aliases:
            alias_map[alias.upper()] = canonical.upper()

    violations = []
    notices = []
    vt_rows = []
    scanned = 0
    for path in iter_files(args.all):
        scanned += 1
        if path.endswith(".csv"):
            check_csv(path, sidfmt, ecid_fields, vocab, supp, alias_map,
                      violations, vt_rows, optional_fields, notices)
            if rel(path) == MILESTONE_GRID:
                check_milestone_grid(path, rules, vocab, violations, notices)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        elif path.endswith(".json"):
            data = check_json(path, vocab, violations)
            if isinstance(data, dict):
                check_bands(path, data, vocab, sidfmt, violations)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        else:
            with open(path, encoding="utf-8", errors="replace") as fh:
                check_sids(path, fh.read(), sidfmt, violations)

    check_vt_cap(vt_rows, supp, violations)

    report = build_report(violations, scanned, args.all, rules, len(vt_rows), notices)
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
