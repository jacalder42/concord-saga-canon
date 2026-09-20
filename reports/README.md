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
| `VALIDATION_BASELINE_ALL_2026-09-19.md` | everything, incl. `recovery/`, `proposals/`, `CLAUDE.md` | 243 | 61 |

The `--all` figure rose from 196/45 to 224/52 when the proposal branch merged into the
working branch, and again to 243/61 when the parallel narrative-recovery session added
its ten documents. **The substrate figure has not moved from 27 through any of it**,
which is the point: the banded envelopes, the 27 `escalation_permissions` blocks and
2,800 lines of narrative recovery added zero substrate violations.

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
- **`CHK_BANDS`** validates the per-act `escalation_permissions` bands ruled 2026-09-19:
  every bound is a member of its axis vocabulary, `min` does not exceed `max`, and each
  exception names a valid axis, a valid value and a parseable SID. It checks
  **coherence, never judgement** — that an act permits `U3`–`U6` is the author's call,
  and a test asserts the checker will not second-guess it. A pinned band (`FX3`–`FX3`,
  as `B08.A1` uses) is legal.
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

### What the extra 34 violations under `--all` are

All 34 are `CHK_SID_FORMAT`, across 12 files. Thirty-two are one-digit book numbers
(`B1`, `B3` where the format requires `B01`, `B03`), in `CLAUDE.md`, the recovery ledger,
the ECID memo, `recovery/CANON_DECISIONS_2026-09-18.md`, the envelope question, the
2026-09-19 recovery bundles, the 2026-09-15 checkpoint, two proposals and the two
milestone load CSVs.

Two are a different shape: `S1.T3.B09.A4.E16` in `recovery/NOTION_RECOVERY_2026-09-19.md`
and in the ledger, flagged `A4 out of range 1..3`. Those quote the Book 9 Final Beat
Bible's "ACT IV", which **ledger §25 ruled is the epilogue, not a fourth act** — so they
are now quotations of a ruled-out form, exactly like the one-digit SIDs.

**Every one of the 34 is an intentional quotation.** These files document the wrong forms
in order to rule against them — `CLAUDE.md` §3 quotes the one-digit book as the wrong
form, and the ledgers and memos quote recovered SIDs verbatim as evidence. Rewriting them
would destroy the evidence they exist to preserve.

The two milestone CSVs deserve a note, because they are staged for `grids/` rather than
for the record: their hits are in the free-text `notes` column citing a recovered packet
(`Recovered packet S1.T1.B3.A3.E14`). Their **structured** columns are correct —
`target_book` reads `B03`, `B08`, `B09`. ~~Loading them will not import a malformed SID.~~

> **Corrected 2026-09-20.** That conclusion was wrong. The validator scans file *text*,
> not only structured fields, so loading v2 raised canon-scope 27→28 on the first
> attempt. The `notes` typo was ruled a typo and fixed (`B3`→`B03`) in both the grid and
> its staging source. `grids/milestones_payoffs.csv` is now **live** at canon-scope 27,
> and all-scope fell 62→61. Ledger §41.

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
- **`POV` is unchecked.** `canon_rules.json` defines no vocabulary for it, so the
  checker has nothing to validate against. **`ENV` joined the checked fields on
  2026-09-19**: its vocabulary derives from the geography system's type layer and only
  that layer (`recovery/GATE_RULINGS_2026-09-19.md` Ruling 1). Named places are not `ENV`
  values, and the shard progression contributes nothing. Enforcement adds **zero**
  violations today because `episode_beats.csv` is header-only — but see the migration
  note below.
- **JSON vocabulary checking is keyed to known field names** (`max_weather`,
  `corridor_max`, `default_vfx_ceiling`, and the rest in `JSON_KEY_VOCAB`). A new
  envelope key would go unchecked until it is added to that map.
- **The five checks named in `rules/validation_checks.json` are not these checks.**
  `CHK_HUMANITY`, `CHK_BREADCRUMBS`, `CHK_CHANNELS`, `CHK_ANTAG` and `CHK_EMO_CIRCUIT`
  are editorial judgements about story content. This validator enforces the mechanical
  layer — identifier format, field names, controlled vocabulary — which is the part a
  script can settle. The editorial five still need a reader.
- **Band values are not judged, only checked for coherence.** `CHK_BANDS` cannot tell
  a well-reasoned band from a careless one. 18 of the 27 act bands are marked
  `basis: inferred` and are placeholders; the checker treats them exactly like the 9
  marked `observed`. Read the `basis` field before trusting a band.
- **Recovered packets carry free-text `ENV` and will not satisfy the new vocabulary.**
  The E16 packet's `ENV` reads *"Streets leading away from the square (night)"* — a scene
  setting, not a zone or corridor type. Under Ruling 1 that is not an `ENV` value.
  **Every packet migrated from here on needs its `ENV` mapped to a type**, and that is
  migration work which did not exist before 2026-09-19. It is also why the validator's own
  fixtures moved from `Square` to `ZONE_BLUE_PULSE`. Expect the substrate count to rise at
  migration time unless the mapping is done as part of it.

- **The milestone grid is checked from 2026-09-20.** `CHK_GRID_SCHEMA`,
  `CHK_GRID_ID`, `CHK_GRID_SETUPS`, `CHK_GRID_TARGET` and `CHK_GRID_STATUS` cover
  `grids/milestones_payoffs.csv`: header drift, duplicate or empty `milestone_id`,
  `required_setups` that resolve to a real row, two-digit `target_book`, `T1`–`T3`,
  `A1`–`A3`, and `status` from `controlled_vocab.milestone_status`. **All pass on the
  grid as promoted** — they are a ratchet against future edits, not a cleanup task, so any
  failure is a change someone made.

  **One deliberate exception:** five rows carry `target_act: EP`, which is not an act —
  all nine books have three acts and **27 is the cap** (confirmed 2026-09-20). Whether
  `EP` belongs in the act slot at all is an **open author question** (`CLAUDE.md` §4), so
  those rows are **notices, not violations**. They become violations the moment the ruling
  says `EP` is not an act slot, and valid the moment it says it is. The checker reports;
  it does not decide.

- **Episode-level band conformance is not checked yet.** Nothing verifies that an
  episode's `CORRIDOR` sits inside its act's band, because no episode rows exist —
  `episode_beats.csv` is still header-only. That check becomes possible, and worth
  adding, the moment migration writes the first row.
- **The 150–600 word supplement range is not enforced.** No supplement text exists in
  the repository to measure, and per `CLAUDE.md` §1 none ever will — this repo holds no
  prose. The constraint is recorded in `supplement_system.constraints` for whatever
  tool does hold the text.
- **Per-book supplement intensity is not enforced.** "Light" through "extreme" is a
  judgement, not a countable threshold.
