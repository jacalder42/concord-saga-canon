# Validation Reports

Generated artifacts. **Do not hand-edit** — regenerate instead:

```sh
python3 tools/validate_canon.py --report reports/VALIDATION_BASELINE_<date>.md
python3 tools/validate_canon.py --all --report reports/VALIDATION_BASELINE_ALL_<date>.md
```

The validator reports violations and never fixes them. It exits non-zero whenever any
violation is found, so it is safe to wire into a pre-commit hook or CI step.

## Baseline, 2026-09-19

Two reports, because scope changes the answer.

| Report | Scope | Files | Violations |
| --- | --- | --- | --- |
| `VALIDATION_BASELINE_2026-09-19.md` | canon substrate | 189 | 27 |
| `VALIDATION_BASELINE_ALL_2026-09-19.md` | everything, incl. `recovery/`, `CLAUDE.md` | 193 | 42 |

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

### What the extra 15 violations under `--all` are

All 15 are `CHK_SID_FORMAT`, all one-digit book numbers (`B1`, `B3` where the format
requires `B01`, `B03`), in three files:

| File | Count |
| --- | --- |
| `CLAUDE.md` | 4 |
| `recovery/RECOVERY_LEDGER_2026.md` | 5 |
| `recovery/ECID_VOCABULARY_COLLISION_2026.md` | 6 |

**Every one is an intentional quotation.** These files document the one-digit form in
order to rule against it — `CLAUDE.md` §3 quotes it as the wrong form, and the ledger
and memo quote the recovered SIDs verbatim as evidence. Rewriting them would destroy
the evidence they exist to preserve.

This is why `recovery/`, `proposals/` and `CLAUDE.md` sit outside the default scope. A
checker that flags a memo for quoting the error it documents is reporting noise. The
`--all` run is kept so the count is visible rather than hidden.

### What this baseline is for

It is the "before" picture. When migration starts writing recovered material into the
substrate, the substrate report is expected to go red with real violations — 17
`STRAIN`, 5 `LORE`, 1 `POL`, and the `SHARD-EDGE` / `VT-BRUSH` qualifiers, plus
one-digit book SIDs throughout. Those are the subject of the four rulings in
`recovery/ECID_VOCABULARY_COLLISION_2026.md` §7. Comparing against this baseline is how
to tell a migration defect from a pre-existing one.

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
