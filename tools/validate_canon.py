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
CHK_ENVELOPE     Every `book_context` file carries a band-shaped
                 `escalation_permissions` block with a `basis`. `CHK_BANDS` returns
                 early on a missing or flat block, so without this a deleted envelope
                 would read as zero violations rather than as a deletion.
CHK_CONTAINMENT  A book's derived envelope is compared against its trilogy container.
                 Reported as NOTICES: six of nine books breach as of 2026-09-20, and
                 which layer gives way is an open author question, not a format error.
CHK_GRID_THREAD  Every milestone row names a thread from `controlled_vocab.threads`.
                 `UNSCORED` is a member, so an unsettled row states that it is
                 unsettled; an EMPTY cell is a violation, because it cannot be told
                 apart from an oversight.
CHK_RETIRED_TERMS  Names retired by ruling (`retired_terms` in canon_rules.json) are
                 a violation in canon scope and a notice in all-scope, where quoting
                 them as evidence is legitimate. Case-insensitive and whole-word, so
                 a capitalised heading is caught. Pinned exceptions live in
                 `retired_terms.allowlist`. Added 2026-09-25, ledger 76.
CHK_BREADCRUMB_GRID  `grids/breadcrumbs.csv` against `breadcrumb_grid` in
                 canon_rules.json: header, unique `BC-` ids, the four enums, and
                 `payoff_milestone_id` resolving to a milestone row that is not
                 retired. A LOCKED payoff must name a `ruled` row: that is what
                 makes precise planting safe. Placed plants need an introducing
                 SID. Structure only; whether a plant earns its place is
                 editorial (rules/validation_checks.json CHK_BREADCRUMBS). Added
                 2026-09-27, ledger 198.
CHK_BID_FORMAT   EBCI beat ids are `{SID}-BTnn`: the SID parses, the beat number is two
                 digits, and the SID is the packet's (or the grid row's) own. Added
                 2026-09-27 for the B01 two-packet pilot, ledger 210.
CHK_EPISODE_BAND An EBCI packet's (or beat row's) CORRIDOR, WEATHER and FX sit inside its
                 act's band in act_overlays/, or are covered by a declared exception
                 naming that episode's SID (Ruling 5). A position with no overlay (PR
                 until its overlay exists) has no band and fails.
CHK_PACKET_LINKS Every `BC-` id and milestone id a packet cites resolves (a retired
                 milestone is a notice). A LOCKED breadcrumb carried on the packet's
                 `Breadcrumbs:` line must be placed at this SID: in its introducing or
                 reinforcing SIDs, or at its payoff locator.
CHK_POV          The POV resolves to an authorised POV-capable narrative entity: a cast
                 member (a `canon/characters/` card or a person in
                 `canon/cast_registry.csv`, by name, first name or quoted nickname), or
                 an entity declared in canon_rules.json `pov_entities` (Silence and Hope,
                 metaphysical constructs kept out of the cast registry; generalised
                 2026-09-27 by the pilot review, R4). `ensemble` is not a POV.
CHK_VT_CAP       `VT` Glimpses are capped at 10-12 across all nine books
                 (`supplement_system.constraints`). Exceeding the maximum is a
                 violation; being under the minimum is not, since the saga is
                 unwritten and an empty grid is not a defect.

Scope
-----
By default the canon substrate is scanned: rules/, canon/, grids/, book_context/,
act_overlays/, templates/, source_canon/; and the EBCI production packets in ebci/
(created 2026-09-27 for the B01 pilot), which are held to canon scope.

`recovery/`, `proposals/`, `reports/`, `decisions/` and `CLAUDE.md` are excluded by default because they are
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
import glob
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
# EBCI production packets (B01 pilot released 2026-09-27, ledger 210). Not substrate
# (no rule lives there), but scanned by default and held to canon scope: a packet
# with a retired name or a malformed SID is a defect, not a quotation.
EBCI_DIRS = ["ebci"]
# reports/ and decisions/ joined all-scope 2026-09-25 (ledger 76). Before that they
# were scanned in NEITHER scope, which is how retired names re-entered reports/
# unseen: 23 then 30 Technarch occurrences with no check able to count them.
META_DIRS = ["recovery", "proposals", "reports", "decisions"]
META_FILES = ["CLAUDE.md", "README.md"]

# Ruling 10 (2026-09-21) permits prose in exactly two directories, and requires that
# neither be validated. They are listed here so the exclusion is a stated decision
# rather than an accident of what SUBSTRATE_DIRS happens to omit - a later edit that
# adds either one fails `ProseDirectoriesStayOutOfScope`.
PROSE_DIRS = ["sources", "manuscript"]

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

# One component of a SID pattern: either a numeric range or a set of literal
# alternatives. `{01-09}` is numeric; `{act:A1|A2|A3|PR|EP}` is an alternation.
COMPONENT_RX = re.compile(r"\{(?:(\d+)-(\d+)|(?:([A-Za-z_]+):)?([A-Za-z0-9|]+))\}")


class SidFormat:
    """Parses a pattern like S1.T{1-3}.B{01-09}.{act:A1|A2|A3|PR|EP}.E{00-99}.

    Two component forms:

    `{lo-hi}`   a numeric range. It declares both the range and a digit width,
                taken from the literal width of `lo`. So `{01-09}` requires
                exactly two digits, which is what makes the two-digit book rule
                enforceable rather than advisory.

    `{name:A|B}` an alternation over literal tokens, optionally named for error
                messages. Added 2026-09-20 for Ruling 6: the act slot holds five
                structural positions, `A1`-`A3` plus `PR` and `EP`, and three of
                them are not numeric. A purely numeric parser could not express
                that, so the pattern in `canon_rules.json` could not simply be
                edited. Ledger section 56.
    """

    # Loose matcher for one alternation token: letters, then optional digits.
    # Deliberately wider than the allowed set, so `A0` and `A4` are FOUND and
    # then fail validation rather than going unnoticed.
    ALT_LOOSE = r"([A-Za-z]{1,3}\d{0,2})"

    def __init__(self, pattern):
        self.pattern = pattern
        self.literals = []    # literal text before each component
        self.components = []  # ("num", (width, lo, hi)) | ("alt", (label, {tokens}))
        pos = 0
        for m in COMPONENT_RX.finditer(pattern):
            self.literals.append(pattern[pos:m.start()])
            lo, hi, name, alts = m.groups()
            if lo is not None:
                self.components.append(("num", (len(lo), int(lo), int(hi))))
            else:
                self.components.append(
                    ("alt", (name or "", tuple(a for a in alts.split("|") if a))))
            pos = m.end()
        self.trailing = pattern[pos:]
        # Numerics kept for callers that only care about the numeric components.
        self.numerics = [spec for kind, spec in self.components if kind == "num"]

        def loose(n):
            out = []
            for lit, (kind, _) in zip(self.literals[:n], self.components[:n]):
                out.append(re.escape(lit)
                           + (r"(\d+)" if kind == "num" else self.ALT_LOOSE))
            return "".join(out)

        # Loose finder: same literals, digits of ANY width. Malformed identifiers
        # match this and then fail component validation, which is the point.
        self.finder = re.compile(loose(len(self.literals)) + re.escape(self.trailing))
        # Prefix forms: a token may legitimately stop at an earlier component
        # (an act ID stops before the episode component).
        self.prefixes = [re.compile(loose(n) + r"(?![\d.])")
                         for n in range(1, len(self.literals) + 1)]

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
        """Return a list of problems for the components of a candidate."""
        problems = []
        for idx, raw in enumerate(groups):
            kind, spec = self.components[idx]
            if kind == "alt":
                name, allowed = spec
                if raw not in allowed:
                    problems.append(
                        f"{raw} is not a valid {name or 'component'}: "
                        f"{', '.join(allowed)}")
                continue
            width, lo, hi = spec
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
    roots = list(SUBSTRATE_DIRS) + list(EBCI_DIRS)
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
        # `EP` carried a notice-instead-of-violation carve-out here until
        # 2026-09-20. Ruling 6 removed the need for it: PR and EP are structural
        # positions in the act slot, so they are ordinary members of
        # `target_act_values` and the carve-out would now be dead code asserting
        # a superseded reading. Ledger section 56.
        if act and act not in acts:
            out.append(Violation(
                "CHK_GRID_TARGET", rel(path), lineno, act,
                f"{mid} target_act expects one of {', '.join(sorted(acts))}"))

    # --- thread must be a member of the reconciled vocabulary ------------
    # Ruling 7 of 2026-09-20. `UNSCORED` is a MEMBER, not a gap: a row whose thread the
    # author has not settled says so explicitly rather than leaving an empty cell, the
    # same posture Ruling 8 takes for provisional locations. An empty cell is a
    # violation precisely because it is indistinguishable from an oversight.
    threads = {t.upper() for t in vocab.get("threads", [])}
    if threads and "thread" in idx:
        for lineno, row in enumerate(data, 2):
            th = cell(row, "thread")
            if not th:
                out.append(Violation(
                    "CHK_GRID_THREAD", rel(path), lineno, "",
                    f"{cell(row, 'milestone_id')} thread is empty; use UNSCORED when "
                    f"the thread is not yet settled, so an unsettled row cannot be "
                    f"mistaken for an overlooked one"))
            elif th.upper() not in threads:
                out.append(Violation(
                    "CHK_GRID_THREAD", rel(path), lineno, th,
                    f"{cell(row, 'milestone_id')} thread expects one of "
                    f"{', '.join(sorted(vocab['threads']))}"))

    # --- status vocabulary -------------------------------------------------
    allowed = {v.upper() for v in vocab.get("milestone_status", [])}
    if allowed:
        for lineno, row in enumerate(data, 2):
            st = cell(row, "status")
            if st and st.upper() not in allowed:
                out.append(Violation(
                    "CHK_GRID_STATUS", rel(path), lineno, st,
                    "status expects one of " + ", ".join(sorted(allowed))))


BREADCRUMB_GRID = "grids/breadcrumbs.csv"


def load_milestone_status(path=None):
    """milestone_id -> status, read from the milestone grid; {} if unreadable."""
    path = path or os.path.join(REPO, MILESTONE_GRID)
    try:
        with open(path, encoding="utf-8", newline="") as fh:
            return {r.get("milestone_id", "").strip(): r.get("status", "").strip().lower()
                    for r in csv.DictReader(fh) if r.get("milestone_id", "").strip()}
    except OSError:
        return {}


def check_breadcrumb_grid(path, rules, out, milestone_status=None):
    """Structural checks over the breadcrumb ledger (activated 2026-09-27).

    Episode numbers in a breadcrumb are locators, not identity, so nothing here
    pins a plant to an episode; CHK_SID_FORMAT already checks the SIDs' shape.
    """
    spec = rules.get("breadcrumb_grid")
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
    if header != spec["columns"]:
        out.append(Violation(
            "CHK_BREADCRUMB_GRID", rel(path), 1, ",".join(header),
            "breadcrumb grid header does not match breadcrumb_grid.columns. "
            "Expected: " + ",".join(spec["columns"])))
        return
    idx = {c: i for i, c in enumerate(header)}

    def cell(row, col):
        i = idx[col]
        return row[i].strip() if i < len(row) else ""

    if milestone_status is None:
        milestone_status = load_milestone_status()
    id_re = re.compile(spec.get("id_pattern", r"^BC-"))
    enums = {
        "type": set(spec.get("type_values", [])),
        "visibility_level": set(spec.get("visibility_values", [])),
        "status": set(spec.get("status_values", [])),
        "payoff_dependency": set(spec.get("payoff_dependency_values", [])),
    }
    seen = {}
    for lineno, row in enumerate(rows[1:], 2):
        if not any(c.strip() for c in row):
            continue
        bid = cell(row, "breadcrumb_id")
        if not id_re.match(bid):
            out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, bid,
                                 "breadcrumb_id must match " + spec.get("id_pattern", "")))
        elif bid in seen:
            out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, bid,
                                 f"duplicate breadcrumb_id; first seen at line {seen[bid]}"))
        else:
            seen[bid] = lineno
        for col, allowed in enums.items():
            val = cell(row, col)
            if allowed and val not in allowed:
                out.append(Violation(
                    "CHK_BREADCRUMB_GRID", rel(path), lineno, val,
                    f"{bid} {col} expects one of {', '.join(sorted(allowed))}"))
        mid = cell(row, "payoff_milestone_id")
        dep = cell(row, "payoff_dependency")
        if mid:
            st = milestone_status.get(mid)
            if st is None:
                out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, mid,
                                     f"{bid} payoff_milestone_id is not a milestone_id"))
            elif st == "retired":
                out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, mid,
                                     f"{bid} pays off a retired milestone"))
            elif dep == "LOCKED" and st != "ruled":
                out.append(Violation(
                    "CHK_BREADCRUMB_GRID", rel(path), lineno, mid,
                    f"{bid} is LOCKED but {mid} is `{st}`; LOCKED needs a ruled payoff"))
        elif dep == "LOCKED":
            out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, "",
                                 f"{bid} is LOCKED but names no payoff_milestone_id"))
        if cell(row, "status") in ("placed", "provisional") and not cell(row, "introduced_in_SID"):
            out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, "",
                                 f"{bid} is {cell(row, 'status')} but has no introduced_in_SID"))
        if not cell(row, "payoff_function"):
            out.append(Violation("CHK_BREADCRUMB_GRID", rel(path), lineno, "",
                                 f"{bid} has no payoff_function: a plant without a payoff is an orphan"))


# --------------------------------------------------------------------------- #
# EBCI packets and beat rows (B01 two-packet pilot, 2026-09-27, ledger 210)
# --------------------------------------------------------------------------- #

EPISODE_BEATS_GRID = "grids/episode_beats.csv"
BID_RX = re.compile(r"\b(S1\.[A-Za-z0-9.]+?)-BT([A-Za-z0-9]+)\b")
BC_ID_RX = re.compile(r"\bBC-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")
MILESTONE_ID_RX = re.compile(r"\bM\d{2}\b")
PACKET_NAME_RX = re.compile(r"^S1\..+\.md$")
BAND_FIELDS = {"CORRIDOR": "corridor", "WEATHER": "weather", "FX": "fx"}
TITLE_WORDS = {"dr", "director", "officer", "councilwoman", "ms", "mme", "mr", "mrs"}
OBLIGATION_LABELS = ("Continuity:", "Protected reveals:", "Amendments applied:")


def _words(text):
    return [w for w in re.split(r"[\s\"“”'‘’()]+", text) if w]


def load_known_cast(rules=None):
    """Names of authorised POV-capable narrative entities.

    Cast members (first names, full names and quoted nicknames), plus the entities
    declared in canon_rules.json `pov_entities`.

    Sources: the Tier-1 cards in canon/characters/ (file stems) and the people in
    canon/cast_registry.csv. Registry bundle G is places and relationships, not
    people, and is skipped.
    """
    known = set()
    rules = load_rules() if rules is None else rules
    for ent in rules.get("pov_entities", {}).get("entities", []):
        if isinstance(ent, dict) and ent.get("name"):
            known.add(ent["name"].casefold())
    cdir = os.path.join(REPO, "canon", "characters")
    if os.path.isdir(cdir):
        for name in os.listdir(cdir):
            m = re.match(r"^([A-Z][a-z]+)(?:[A-Z][a-z]*)?(?:ID|EBCI|Render|Appearance|Backstory|Identity)?\.md$", name)
            if m:
                known.add(m.group(1).casefold())
            stem = re.match(r"^([A-Za-z]+?)(?:ID|EBCI|Render|Appearance|Backstory|Identity)\.md$", name)
            if stem:
                known.add(stem.group(1).casefold())
    try:
        with open(os.path.join(REPO, "canon", "cast_registry.csv"), encoding="utf-8",
                  newline="") as fh:
            for r in csv.DictReader(fh):
                if r.get("cast_id", "").startswith("G"):
                    continue
                name = re.sub(r"\([^)]*\)", " ", r.get("name", "")).strip()
                if not name:
                    continue
                known.add(name.casefold())
                for nick in re.findall(r"[\"“]([^\"”]+)[\"”]", name):
                    known.add(nick.casefold())
                for alt in name.split("/"):
                    words = [w for w in _words(alt)
                             if w.strip(".").casefold() not in TITLE_WORDS]
                    if words:
                        known.add(words[0].casefold())
    except OSError:
        pass
    return known


def pov_is_known(value, known):
    parts = [p.strip() for p in re.split(r"\s\+\s|,|\s/\s", value) if p.strip()]
    if not parts:
        return False
    for part in parts:
        if part.casefold() in known:
            continue
        if not any(w.strip(".").casefold() in known for w in _words(part)):
            return False
    return True


def _check_pov(value, where, path, line, known, out):
    if value.strip().upper() in PLACEHOLDERS or not pov_is_known(value, known):
        out.append(Violation("CHK_POV", rel(path), line, value,
                             f"{where}: POV must resolve to an authorised POV-capable "
                             "narrative entity (a cast member, or canon_rules.json "
                             "pov_entities)"))


def _check_bid(sid, bt, expected_sid, path, line, sidfmt, out):
    m = sidfmt.finder.fullmatch(sid)
    if not m:
        out.append(Violation("CHK_BID_FORMAT", rel(path), line, f"{sid}-BT{bt}",
                             "beat id's SID does not parse"))
        return
    for problem in sidfmt.validate(m.groups()):
        out.append(Violation("CHK_BID_FORMAT", rel(path), line, f"{sid}-BT{bt}", problem))
    if not re.fullmatch(r"\d{2}", bt):
        out.append(Violation("CHK_BID_FORMAT", rel(path), line, f"{sid}-BT{bt}",
                             "beat number must be two digits (BTnn)"))
    if expected_sid and sid != expected_sid:
        out.append(Violation("CHK_BID_FORMAT", rel(path), line, f"{sid}-BT{bt}",
                             f"beat id belongs to {sid}, not to {expected_sid}"))


def _act_band(sid, cache):
    """escalation_permissions for the act or position a SID sits in, or None."""
    m = re.fullmatch(r"S1\.(T\d)\.(B\d\d)\.(A[1-3]|PR|EP)\.E\d\d", sid or "")
    if not m:
        return None
    key = "_".join(m.groups())
    if key not in cache:
        p = os.path.join(REPO, "act_overlays", f"act_overlay_S1_{key}.json")
        try:
            with open(p, encoding="utf-8") as fh:
                cache[key] = json.load(fh).get("escalation_permissions")
        except (OSError, json.JSONDecodeError):
            cache[key] = None
    return cache[key]


def _check_episode_band(sid, values, path, line, vocab, out, cache):
    ep = _act_band(sid, cache)
    if not isinstance(ep, dict):
        out.append(Violation("CHK_EPISODE_BAND", rel(path), line, sid,
                             "no act band exists for this SID's position "
                             "(no act_overlays file for it)"))
        return
    for field, axis in BAND_FIELDS.items():
        raw = values.get(field, "")
        if not raw or raw.strip().upper() in PLACEHOLDERS:
            continue
        band = ep.get(axis) or {}
        dim = BAND_AXIS_VOCAB[axis]
        lo, hi = _rank(vocab, dim, band.get("min")), _rank(vocab, dim, band.get("max"))
        for tok in split_values(raw):
            r = _rank(vocab, dim, tok)
            if r is None or lo is None or hi is None or lo <= r <= hi:
                continue
            declared = [e for e in ep.get("exceptions") or []
                        if isinstance(e, dict) and e.get("axis") == axis
                        and e.get("sid") == sid
                        and (_rank(vocab, dim, e.get("value")) or -1) >= r]
            if not declared:
                out.append(Violation(
                    "CHK_EPISODE_BAND", rel(path), line, tok,
                    f"{field} {tok} is outside the act band "
                    f"{band.get('min')}-{band.get('max')} and no exception is declared "
                    f"for {sid} (Ruling 5)"))


def check_episode_beats_grid(path, sidfmt, vocab, out, known_cast=None, cache=None):
    try:
        with open(path, encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))
    except OSError:
        return
    known_cast = load_known_cast() if known_cast is None else known_cast
    cache = {} if cache is None else cache
    for lineno, r in enumerate(rows, 2):
        sid = (r.get("SID") or "").strip()
        if not sid:
            continue
        bid = (r.get("BID") or "").strip()
        m = BID_RX.fullmatch(bid)
        if not m:
            out.append(Violation("CHK_BID_FORMAT", rel(path), lineno, bid,
                                 "BID must be {SID}-BTnn"))
        else:
            _check_bid(m.group(1), m.group(2), sid, path, lineno, sidfmt, out)
        _check_episode_band(sid, {f: r.get(f, "") for f in BAND_FIELDS}, path, lineno,
                            vocab, out, cache)
        _check_pov(r.get("POV", ""), "beat row", path, lineno, known_cast, out)


def _sections(text):
    """Group a packet's lines under their nearest `##` or `###` heading.

    Keyed by the heading's first word, lower-cased: `header`, `ecid`, `beats`,
    `obligations`. The two-layer template (2026-09-27) nests Beats under the
    Narrative brief and ECID and Obligations under the Control layer.
    """
    sections, current = {}, ""
    for lineno, line in enumerate(text.splitlines(), 1):
        m = re.match(r"^#{2,3} (.+)$", line)
        if m:
            current = m.group(1).strip().split(" ")[0].strip("()").lower()
            continue
        sections.setdefault(current, []).append((lineno, line))
    return sections


def load_breadcrumb_rows():
    try:
        with open(os.path.join(REPO, BREADCRUMB_GRID), encoding="utf-8", newline="") as fh:
            return {r["breadcrumb_id"].strip(): r for r in csv.DictReader(fh)
                    if r.get("breadcrumb_id", "").strip()}
    except OSError:
        return {}


def _placed_here(row, sid):
    locs = [row.get("introduced_in_SID", "")] + re.split(r"[;,]\s*",
                                                        row.get("reinforced_in_SIDs", ""))
    if sid in [l.strip() for l in locs]:
        return True
    m = re.fullmatch(r"S1\.T\d\.(B\d\d)\.(?:A[1-3]|PR|EP)\.(E\d\d)", sid)
    loc = row.get("payoff_locator", "")
    return bool(m and m.group(1) in loc and re.search(rf"\b{m.group(2)}\b", loc))


def check_ebci_packet(path, text, sidfmt, vocab, out, notices, known_cast=None,
                      breadcrumbs=None, milestone_status=None, cache=None):
    known_cast = load_known_cast() if known_cast is None else known_cast
    breadcrumbs = load_breadcrumb_rows() if breadcrumbs is None else breadcrumbs
    milestone_status = load_milestone_status() if milestone_status is None else milestone_status
    cache = {} if cache is None else cache
    sec = _sections(text)

    sid, sid_line = "", None
    for lineno, line in sec.get("header", []):
        m = re.match(r"^SID:\s*(\S+)", line)
        if m:
            sid, sid_line = m.group(1), lineno
        m = re.match(r"^POV:\s*(.+?)\s*$", line)
        if m:
            _check_pov(m.group(1), "packet header", path, lineno, known_cast, out)
    if not sid:
        out.append(Violation("CHK_BID_FORMAT", rel(path), None, "",
                             "packet has no `SID:` line in its Header"))
    elif not sidfmt.finder.fullmatch(sid):
        out.append(Violation("CHK_BID_FORMAT", rel(path), sid_line, sid,
                             "packet SID does not parse"))

    ecid = sec.get("ecid", [])
    for i, (lineno, line) in enumerate(ecid):
        cols = [c.strip().upper() for c in line.split("|")]
        if "CORRIDOR" in cols and "POV" in cols:
            vals = next(((ln, l) for ln, l in ecid[i + 1:] if "|" in l), None)
            if vals is None:
                break
            vline, vtext = vals
            values = dict(zip(cols, [v.strip() for v in vtext.split("|")]))
            for field, dim in FIELD_VOCAB.items():
                raw = values.get(field, "")
                if not raw or raw.upper() in PLACEHOLDERS:
                    continue
                allowed = {v.upper() for v in vocab[dim]}
                for tok in split_values(raw):
                    if tok and tok not in PLACEHOLDERS and tok not in allowed:
                        out.append(Violation("CHK_VOCAB", rel(path), vline, tok,
                                             f"ECID {field} expects one of {dim}"))
            if sid:
                _check_episode_band(sid, values, path, vline, vocab, out, cache)
            _check_pov(values.get("POV", ""), "ECID block", path, vline, known_cast, out)
            break

    for lineno, line in sec.get("beats", []):
        for m in BID_RX.finditer(line):
            _check_bid(m.group(1), m.group(2), sid, path, lineno, sidfmt, out)

    for lineno, line in enumerate(text.splitlines(), 1):
        for bc in BC_ID_RX.findall(line):
            if bc not in breadcrumbs:
                out.append(Violation("CHK_PACKET_LINKS", rel(path), lineno, bc,
                                     "breadcrumb id does not resolve in grids/breadcrumbs.csv"))
        for mid in MILESTONE_ID_RX.findall(line):
            st = milestone_status.get(mid)
            if st is None:
                out.append(Violation("CHK_PACKET_LINKS", rel(path), lineno, mid,
                                     "milestone id does not resolve in the milestone grid"))
            elif st == "retired" and notices is not None:
                notices.append(Violation("CHK_PACKET_LINKS", rel(path), lineno, mid,
                                         "cites a retired milestone"))

    carrying, carried = False, []
    for lineno, line in sec.get("obligations", []):
        if line.startswith("Breadcrumbs:"):
            carrying = True
        elif line.startswith(OBLIGATION_LABELS):
            carrying = False
        if carrying:
            carried += [(lineno, bc) for bc in BC_ID_RX.findall(line)]
    for lineno, bc in carried:
        row = breadcrumbs.get(bc)
        if row and row.get("payoff_dependency") == "LOCKED" and sid \
                and not _placed_here(row, sid):
            out.append(Violation(
                "CHK_PACKET_LINKS", rel(path), lineno, bc,
                f"LOCKED breadcrumb carried here is not placed at {sid} in the ledger "
                "(introduced, reinforced or payoff locator)"))


def _rank(vocab, dim, token):
    order = [v.upper() for v in vocab[dim]]
    return order.index(token.upper()) if isinstance(token, str) \
        and token.upper() in order else None


def _covers(vocab, dim, exceptions, axis, child_max, owner_id):
    """Is this breach declared? Ruling 5's form: sid, axis, value, scope, reason.

    An exception covers a breach when it names the same axis, permits at least as
    much as the breaching band claims, and sits inside the entity that breaches.
    The SID check is what stops an exception granted for one episode from silently
    licensing a band across a whole act.
    """
    want = _rank(vocab, dim, child_max)
    for exc in exceptions or []:
        if not isinstance(exc, dict) or exc.get("axis") != axis:
            continue
        got = _rank(vocab, dim, exc.get("value"))
        if got is None or want is None or got < want:
            continue
        if owner_id and not str(exc.get("sid", "")).startswith(owner_id):
            continue
        return exc
    return None


def check_declared_exceptions(vocab, violations, notices):
    """Ruling 5: a container ceiling is SOFT, but every breach must be DECLARED.

    "The ceiling is a tripwire, not a wall." A band may exceed its container - what
    it may not do is exceed it silently. An UNDECLARED breach is a violation; a
    DECLARED one is a notice, so the crossing stays visible without failing the run.

    Checks both rungs of the cascade: act inside book, book inside trilogy. `fx` is
    excluded at the trilogy rung only, where the container is a default rather than
    a ceiling. Ledger section 58.
    """
    books = {}
    for b in range(1, 10):
        p = os.path.join(REPO, BOOK_CONTEXT_DIR, f"book_context_B{b:02d}.json")
        try:
            with open(p, encoding="utf-8") as fh:
                books[f"B{b:02d}"] = (p, json.load(fh))
        except (OSError, json.JSONDecodeError):
            continue

    def compare(child_path, child_ep, child_id, cont_ep, cont_label, axes):
        for axis in axes:
            dim = BAND_AXIS_VOCAB[axis]
            cb, pb = child_ep.get(axis), cont_ep.get(axis)
            if not isinstance(cb, dict) or not isinstance(pb, dict):
                continue
            ci, pi = _rank(vocab, dim, cb.get("max")), _rank(vocab, dim, pb.get("max"))
            if ci is None or pi is None or ci <= pi:
                continue
            declared = (_covers(vocab, dim, child_ep.get("exceptions"), axis,
                                cb["max"], child_id)
                        or _covers(vocab, dim, cont_ep.get("exceptions"), axis,
                                   cb["max"], child_id))
            if declared:
                notices.append(Violation(
                    "CHK_DECLARED", rel(child_path), None, cb["max"],
                    f"{axis}.max {cb['max']} exceeds {cont_label} {pb['max']}, and is "
                    f"DECLARED at {declared.get('sid')}: {declared.get('reason')}. "
                    f"Ruling 5 permits this; reported so the crossing stays visible."))
            else:
                violations.append(Violation(
                    "CHK_DECLARED", rel(child_path), None, cb["max"],
                    f"{axis}.max {cb['max']} exceeds {cont_label} {pb['max']} with NO "
                    f"declared exception. Ruling 5 makes the ceiling soft but requires "
                    f"every breach to be declared: add an exception naming sid, axis, "
                    f"value, scope and reason, inside {child_id}."))

    # Rung 1: each act inside its book.
    for path in sorted(glob.glob(os.path.join(REPO, "act_overlays", "*.json"))):
        m = re.search(r"_(T\d)_B(\d\d)_A(\d)", os.path.basename(path))
        if not m:
            continue
        entry = books.get(f"B{m.group(2)}")
        if not entry:
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                act = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        ep = act.get("escalation_permissions")
        if not isinstance(ep, dict):
            continue
        compare(path, ep, f"S1.{m.group(1)}.B{m.group(2)}.A{m.group(3)}",
                entry[1].get("escalation_permissions", {}),
                f"book B{m.group(2)}", ("corridor", "weather", "fx"))

    # Rung 2: each book inside its trilogy. `fx` is skipped - the trilogy carries a
    # default, not a ceiling, and exceeding a default is not a breach.
    for bid, (path, data) in sorted(books.items()):
        tri = data.get("trilogy_id")
        if tri not in TRILOGY_CONTEXTS:
            continue
        try:
            with open(TRILOGY_CONTEXTS[tri], encoding="utf-8") as fh:
                container = json.load(fh)
        except (OSError, json.JSONDecodeError):
            continue
        ep = data.get("escalation_permissions")
        if not isinstance(ep, dict):
            continue
        compare(path, ep, f"S1.{tri}.{bid}",
                container.get("environment_envelope", {}),
                f"trilogy {tri}", ("corridor", "weather"))


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


BOOK_CONTEXT_DIR = "book_context/"

# Resolved against REPO, not the working directory: a cwd-relative path would make
# the containment check fall silent when the validator runs from elsewhere, which is
# the exact failure mode this check exists to prevent.
TRILOGY_CONTEXTS = {
    "T1": os.path.join(REPO, "rules", "trilogy_context_T1_veil.json"),
    "T2": os.path.join(REPO, "rules", "trilogy_context_T2_neon.json"),
    "T3": os.path.join(REPO, "rules", "trilogy_context_T3_loom.json"),
}


def check_book_envelope(path, data, out):
    """A book context must carry a band-shaped `escalation_permissions` block.

    `check_bands` returns early when the block is absent or not band-shaped, and
    that early return is exactly what let the nine flat `TODO` skeletons through
    before the book layer was derived. Now that it is derived, a missing block is
    not scaffolding, it is a deletion - and with only `check_bands` looking, the
    report would read zero violations. Ledger section 54.
    """
    if not rel(path).startswith(BOOK_CONTEXT_DIR):
        return
    ep = data.get("escalation_permissions")
    if not isinstance(ep, dict):
        out.append(Violation(
            "CHK_ENVELOPE", rel(path), None, "",
            "book context has no escalation_permissions block. It is derived from "
            "the three acts beneath the book and must be present."))
        return
    missing = [ax for ax in BAND_AXIS_VOCAB if not isinstance(ep.get(ax), dict)]
    if missing:
        out.append(Violation(
            "CHK_ENVELOPE", rel(path), None, ", ".join(missing),
            "book context escalation_permissions is missing a band. Expected "
            "{min, max} on each of corridor, weather, fx."))
    if not ep.get("basis"):
        out.append(Violation(
            "CHK_ENVELOPE", rel(path), None, "",
            "book context escalation_permissions carries no basis field, so a "
            "derived block cannot be told from a hand-set one."))


def container_band(container, axis):
    """The trilogy's band for an axis, or None if that axis has no ceiling.

    `fx` deliberately returns None. There is no trilogy `fx_max`: the era envelope
    carries `default_vfx_ceiling`, which is a DEFAULT - the level to assume when
    nothing says otherwise - and exceeding a default is not a breach. Treating it as
    one produced three spurious notices before 2026-09-20. Ledger section 57.
    """
    if axis == "fx":
        return None
    band = container.get("environment_envelope", {}).get(axis)
    return band if isinstance(band, dict) else None


def check_trilogy_containment(path, data, vocab, notices):
    """Does a book's derived envelope fit inside its trilogy container?

    Since 2026-09-20 both layers are derived by the same rollup, so a book cannot
    exceed a container computed from itself and this should be silent. It is kept
    as a ratchet: if either layer is later hand-edited out of agreement, the
    disagreement surfaces instead of sitting in the data.

    Reported as NOTICES. Under Ruling 5 a trilogy ceiling is soft, so exceeding it
    is not by itself an error - `check_declared_exceptions` is what decides whether
    a breach is declared. Ledger section 53 part 2, section 57.
    """
    if not rel(path).startswith(BOOK_CONTEXT_DIR):
        return
    ep = data.get("escalation_permissions")
    tri = data.get("trilogy_id")
    if not isinstance(ep, dict) or tri not in TRILOGY_CONTEXTS:
        return
    try:
        with open(TRILOGY_CONTEXTS[tri], encoding="utf-8") as fh:
            container = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return                      # the trilogy file has its own checks
    for axis, dim in BAND_AXIS_VOCAB.items():
        cap_band = container_band(container, axis)
        band = ep.get(axis)
        if cap_band is None or not isinstance(band, dict):
            continue
        order = [v.upper() for v in vocab[dim]]
        hi, cap = band.get("max"), cap_band.get("max")
        if not isinstance(hi, str) or not isinstance(cap, str):
            continue
        if hi.upper() not in order or cap.upper() not in order:
            continue
        if order.index(hi.upper()) > order.index(cap.upper()):
            notices.append(Violation(
                "CHK_CONTAINMENT", rel(path), None, hi,
                f"{axis}.max {hi} exceeds the {tri} container's {axis}.max {cap}. "
                f"Both layers are derived by the same rollup, so this should be "
                f"impossible - it means one of them was hand-edited. Ruling 5 makes "
                f"the ceiling soft, so see CHK_DECLARED for whether it is declared."))


RULES_FILE_REL = "rules/canon_rules.json"


def compile_retired_terms(rules):
    """Return [(term_dict, compiled_regex)] and the allowlist from the rules file."""
    block = rules.get("retired_terms", {})
    terms = [(t, re.compile(t["pattern"], re.IGNORECASE))
             for t in block.get("terms", [])]
    return terms, block.get("allowlist", [])


def check_retired_terms(path, text, terms, allowlist, canon_scope, out, notices):
    """CHK_RETIRED_TERMS. Violation in canon scope, notice elsewhere.

    The rules file itself is skipped: it names every retired term by design.
    An allowlist entry exempts one term on lines of one file containing a pinned
    substring, so a NEW occurrence elsewhere in the same file is still caught.
    """
    rp = rel(path).replace(os.sep, "/")
    if rp == RULES_FILE_REL:
        return
    for lineno, line in enumerate(text.splitlines(), 1):
        for term, rx in terms:
            for m in rx.finditer(line):
                if any(a["path"] == rp and a["term"] == term["retired"]
                       and a.get("line_contains", "") in line for a in allowlist):
                    continue
                v = Violation(
                    "CHK_RETIRED_TERMS", rp, lineno, m.group(0),
                    f"retired name; canonical form is {term['canonical']} "
                    f"({term['ruling']})")
                (out if canon_scope else notices).append(v)


def is_canon_scope(path):
    top = rel(path).replace(os.sep, "/").split("/", 1)[0]
    return top in SUBSTRATE_DIRS or top in EBCI_DIRS or top == "README.md"


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

    retired, retired_allow = compile_retired_terms(rules)

    violations = []
    notices = []
    vt_rows = []
    scanned = 0
    known_cast = load_known_cast()
    band_cache = {}
    for path in iter_files(args.all):
        scanned += 1
        with open(path, encoding="utf-8", errors="replace") as fh:
            check_retired_terms(path, fh.read(), retired, retired_allow,
                                is_canon_scope(path), violations, notices)
        if path.endswith(".csv"):
            check_csv(path, sidfmt, ecid_fields, vocab, supp, alias_map,
                      violations, vt_rows, optional_fields, notices)
            if rel(path) == MILESTONE_GRID:
                check_milestone_grid(path, rules, vocab, violations, notices)
            if rel(path) == BREADCRUMB_GRID:
                check_breadcrumb_grid(path, rules, violations)
            if rel(path) == EPISODE_BEATS_GRID:
                check_episode_beats_grid(path, sidfmt, vocab, violations,
                                         known_cast, band_cache)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        elif path.endswith(".json"):
            data = check_json(path, vocab, violations)
            if isinstance(data, dict):
                check_bands(path, data, vocab, sidfmt, violations)
                check_book_envelope(path, data, violations)
                check_trilogy_containment(path, data, vocab, notices)
            with open(path, encoding="utf-8") as fh:
                check_sids(path, fh.read(), sidfmt, violations)
        else:
            with open(path, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            check_sids(path, text, sidfmt, violations)
            parts = rel(path).replace(os.sep, "/").split("/")
            if parts[0] in EBCI_DIRS and PACKET_NAME_RX.match(parts[-1]):
                check_ebci_packet(path, text, sidfmt, vocab, violations, notices,
                                  known_cast, None, None, band_cache)

    check_vt_cap(vt_rows, supp, violations)
    check_declared_exceptions(vocab, violations, notices)

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
