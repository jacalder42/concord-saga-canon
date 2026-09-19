# Validation Reports

Generated artifacts. **Do not hand-edit** — regenerate instead:

```sh
python3 tools/validate_canon.py --report reports/VALIDATION_BASELINE_<date>.md
python3 tools/validate_canon.py --all --report reports/VALIDATION_BASELINE_ALL_<date>.md
```

The validator reports violations and never fixes them. It exits non-zero whenever any
violation is found, so it is safe to wire into a pre-commit hook or CI step.

## Baseline, 2026-09-19 (regenerated after the 2026-09-18 rulings)

Two reports, because scope changes the answer.

| Report | Scope | Files | Violations |
| --- | --- | --- | --- |
| `VALIDATION_BASELINE_2026-09-19.md` | canon substrate | 190 | 27 |
| `VALIDATION_BASELINE_ALL_2026-09-19.md` | everything, incl. `recovery/`, `CLAUDE.md` | 196 | 45 |

### What the rulings changed in the checker

`recovery/CANON_DECISIONS_2026-09-18.md` widened what is checkable:

- **`LOAD`** is a ninth ECID field with its own vocabulary (`L0`–`L3`), checked like
  any other axis. This is where `STRAIN`'s meaning now lives (§1.1, §1.4).
- **`E00`** validates, because the SID episode range widened (§2.1). The self-test
  asserts both that `E00` passes now and that it would have failed under the old
  range — so the widening is doing the work, not a loosened matcher.
- **Field aliases** are honoured: a grid header using the packet labels `U-Level` and
  `Resonance State` satisfies the ECID check and still has its values vocabulary-checked
  (§2.4).
- **The three supplement axes** are checked against `supplement_system`. The
  provisional types `ROM`, `TECH` and `CHAR` are **accepted, not flagged** — §7 was to
  be applied while marked unratified — and the report's configuration block names them
  on every run so they cannot be mistaken for ruled vocabulary.
- **`CHK_VT_CAP`** enforces the one supplement constraint a script can settle: 10–12
  `VT` Glimpses across all nine books (§3.4). Exceeding the maximum is a violation.
  Being under the minimum is **not** — the saga is unwritten, and an empty grid is not
  a defect. Currently 0 of 12 used.

### What the 27 substrate violations are

All 27 are `CHK_VOCAB`, and all are the same thing: the nine `book_context_B0*.json`
skeletons each carry three `TODO` placeholders in `escalation_permissions`
(`max_corridor_tier`, `max_weather`, `max_fx`). These are unpopulated scaffolding, not
wrong values. They are reported separately from real vocabulary violations, and they
resolve when the book contexts are populated — work-queue items 4 and 5a.

**The canon substrate currently contains zero malformed SIDs and zero out-of-vocabulary
tokens.** That is not a claim that the project is clean; it is a consequence of the
grids being header-only and the migration not having started. The violations arrive
with the migration.

### What the extra 18 violations under `--all` are

All 18 are `CHK_SID_FORMAT`, all one-digit book numbers (`B1`, `B3` where the format
requires `B01`, `B03`), across four files — `CLAUDE.md`, the recovery ledger, the ECID
memo, and now `recovery/CANON_DECISIONS_2026-09-18.md` itself, which quotes recovered
SIDs in its §1.5 migration mapping.

**Every one is an intentional quotation.** These files document the one-digit form in
order to rule against it — `CLAUDE.md` §3 quotes it as the wrong form, and the ledger
and memo quote the recovered SIDs verbatim as evidence. Rewriting them would destroy
the evidence they exist to preserve.

This is why `recovery/`, `proposals/` and `CLAUDE.md` sit outside the default scope. A
checker that flags a memo for quoting the error it documents is reporting noise. The
`--all` run is kept so the count is visible rather than hidden.

### What this baseline is for

It is the "before" picture. The four rulings that were pending when this baseline was
first taken have since been made, so what migration should now produce is different:
applying the §1.5 mapping converts every recovered `STRAIN` into a `RES` + `LOAD` pair
that validates, and `LORE`/`POL` move out of `MODE` into `supplement_type`.

**A migration that is done right should therefore add no new violations.** If the
substrate report goes red after a migration commit, the mapping was misapplied.
Comparing against this baseline is how to tell that from a pre-existing problem.

## Known limitations

Recorded so the reports are not read as stronger than they are.

- **The epilogue SID form is invisible to the checker.** `S1.T1.B3.EP.E01` puts `EP`
  where the format requires a digit, so it does not match the SID finder at all and
  cannot be flagged as malformed. Tracked as a ruling in
  `recovery/RECOVERY_LEDGER_2026.md` §15 instead. The same applies to any identifier
  malformed in its non-numeric structure rather than its digits.
- **`POV` and `ENV` are unchecked.** `canon_rules.json` defines no vocabulary for
  them, so the checker has nothing to validate against.
- **JSON vocabulary checking is keyed to known field names** (`max_weather`,
  `corridor_max`, `default_vfx_ceiling`, and the rest in `JSON_KEY_VOCAB`). A new
  envelope key would go unchecked until it is added to that map.
- **The five checks named in `rules/validation_checks.json` are not these checks.**
  `CHK_HUMANITY`, `CHK_BREADCRUMBS`, `CHK_CHANNELS`, `CHK_ANTAG` and `CHK_EMO_CIRCUIT`
  are editorial judgements about story content. This validator enforces the mechanical
  layer — identifier format, field names, controlled vocabulary — which is the part a
  script can settle. The editorial five still need a reader.
- **No semantic checks.** The validator will not catch the trilogy-envelope
  contradiction in `CLAUDE.md` §9.1: `W3`/`U5` are valid tokens everywhere they appear,
  and whether Loom should permit more than Veil is a canon question, not a format one.
  This is the open item at decisions §8 item 1.
- **The 150–600 word supplement range is not enforced.** No supplement text exists in
  the repository to measure, and per `CLAUDE.md` §1 none ever will — this repo holds no
  prose. The constraint is recorded in `supplement_system.constraints` for whatever
  tool does hold the text.
- **Per-book supplement intensity is not enforced.** "Light" through "extreme" is a
  judgement, not a countable threshold.
