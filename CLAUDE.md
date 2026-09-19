# CLAUDE.md — Concord Saga Canon

Standing instructions for any Claude session working in this repository.
Read this before touching files. It is the working agreement, not canon.

---

## 1. What this repository is

Non-prose canon substrate for the Concord Saga, a nine-book serial.

| Folder | Holds |
| --- | --- |
| `rules/` | JSON rules, invariants, validation checks, trilogy envelopes; system docs (Mechanica, Resonance, Emotion, Channels, symbols) |
| `canon/` | Markdown canon: tier-1 cards, codex, trilogy summaries, POV and faction files |
| `source_canon/` | High-resolution exploratory source material. **Declared non-authoritative by its own README** — see §1.1 |
| `grids/` | CSV structure and telemetry grids, including `episode_beats.csv` |
| `book_context/` | `book_context_B01.json` .. `B09.json` |
| `act_overlays/` | 27 per-act JSON overlays, `act_overlay_S1_T1_B01_A1.json` form |
| `templates/` | Hand-authored templates for audits and bundles. Edit these freely; the **generated artifacts** produced from them are what must not be hand-edited |
| `proposals/` | Analysis and proposal documents (`proposals/concord-2026/`). Present on the proposal branch only — see §6 |
| `recovery/` | Recovery ledgers, migration audits, checkpoints, and sanitized source exports |
| `tools/` | Validation scripts. `validate_canon.py` checks the substrate against `rules/canon_rules.json`; `test_validate_canon.py` is its self-test |
| `reports/` | Generated validation reports — do not hand-edit, regenerate (see `reports/README.md`) |

**No prose, scene text, or dialogue is stored here.** If a task would put
narrative prose in this repo, stop and say so instead.

### 1.1 `source_canon/` has an unresolved authority conflict — do not resolve it

`source_canon/README.md` declares the directory `NON-AUTHORITATIVE`, permits
redundancy and contradiction, forbids linking to it from temporal canon, and
gives its contents the lifecycle `Extract → Reason → Distill → Archive / Discard`.

But `source_canon/characters/seraphine_full.md` — the only populated file in the
directory, 830 lines — is stamped `FINAL CANON · LOSSLESS · EXPORT READY`
on all four of its blocks. The other eight `*_full.md` files are identical
261-byte stubs.

So the directory is declared disposable while its one real file is declared
locked. **Both readings are recorded here; neither wins.** Until James rules:

- Do not delete, prune, or "clean up" anything under `source_canon/`.
- Do not cite `source_canon/` as authority in `canon/` or `rules/`.
- Do not promote `seraphine_full.md` into tier-1 canon, and do not downgrade it.

This is work-queue item 9 (§8). It is not a housekeeping task.

---

## 2. Autonomy and git

Work without asking for step-by-step approval. Standing rules:

- **Commit after each finished unit of work**, not once at the end of a long session.
- **Write real commit messages.** Say what changed and why, in the style already in
  the log (`Update recovery ledger after targeted archaeology`). Never `Auto-sync`,
  `wip`, or `update files`.
- **Pull before pushing.** Other sessions and the author push to this repo.
- **Push to `main`, unless the session is scoped to a branch.** Some harnesses
  (Claude Code on the web, GitHub Actions) pin a session to a feature branch; when
  they do, that scope wins and the work lands there for review. Never force-push.
  Never rewrite published history.
- **Never delete recovered source material.** Empty or broken files get flagged in the
  ledger, not removed, unless the author says otherwise.
- If a task turns out to need a canon decision (see §4), commit the analysis and stop.

---

## 3. Identifier conventions

> **Provenance gap:** the three rules in this section are written as settled, but no
> artifact in the repository records who approved them or when. §4 makes that
> provenance load-bearing. James: record the approval here, or these read as
> unsourced to any session following §4 strictly.

**SID format is `S1.T{1-3}.B{01-09}.A{1-3}.E{01-99}` — two-digit book numbers.**
This is decided. `B1` is the old one-digit form and is wrong wherever it appears.

- Trilogies: `T1` Veil, `T2` Neon, `T3` Loom
- Books: `B01`..`B09` — always two digits
- Acts: `A1`..`A3`
- Episodes: `E01`..`E99`, **numbered continuously across the whole book**, not
  restarting at `E01` in each act. Episode numbering restarting per act is the old,
  corrected form.
- Episodes live in grids, not in filenames.

**Scope warning.** The recovered material uses the old forms pervasively, not
occasionally: one-digit books throughout, and per-act restarts such as
`S1.T1.B3.A3.E01` through `E18` in the `Saga structural archive` export. Treat the
rewrite as a migration pass with its own ledger entry, not an incidental find-and-replace.

**`E00` is currently out of spec.** Recovered Book 1 Act I opens with
`E00 Prologue — The Conversation in the Sky`, but `E{01-99}` excludes it. Either the
range widens to `E{00-99}` or prologues get their own rule. Unresolved — flag it
when migrating, do not pick one.

**Beat IDs — unresolved, awaiting a ruling.** The current form in
`rules/canon_rules.json` is `{SID}-B{BeatNumber}`, e.g. `S1.T1.B1.A1.E13-B01`. It
reuses `B` for both Book and Beat. A `BT` prefix has been **proposed** as a fix but
not approved; it is recorded as an open item in `recovery/RECOVERY_LEDGER_2026.md`
§14, alongside the four ECID rulings.

Until James rules: **write beat IDs in the current `-B{n}` form**, matching
`canon_rules.json`. Do not write `BT` IDs, and do not edit `BID_format`. No beat IDs
exist anywhere in the repository yet, so whichever way the ruling goes costs nothing
today — that stops being true the moment the first packet is migrated.

---

## 4. What requires the author

James makes canon decisions. Claude does not.

Never decide, invent, or quietly resolve:

- Anything about characters, factions, metaphysics, plot, or world rules not already
  written in `source_canon/` or `canon/`
- Contradictions between two canon sources — record both readings and where each came
  from, then flag it
- Whether unapproved or assistant-generated material becomes canon
- **The controlled-vocabulary collision.** See §4.1 — it blocks the migration queue.
- **E19 and beyond.** E19 is named but never built. Do not generate, draft, or outline
  it. The prohibition stands until James lifts it.

Findings are observational. When two sources conflict, write down what each one says
and ask; do not pick a winner. That rule binds this document too: where an earlier
version of this file overruled a repository artifact, §6 now records both readings
instead.

### 4.1 Controlled-vocabulary collision — blocks work-queue items 4 and 5

The recovered episode packets use ECID tokens that are **not** in the controlled
vocabulary at `rules/canon_rules.json`. Counted across the sanitized exports:

| Token | Field | Occurrences | Status |
| --- | --- | --- | --- |
| `STRAIN` | Resonance State | 17 | Not in `res_states` — more frequent than `CALM` (12) |
| `LORE` | Mode | 5 | Not in `modes` |
| `POL` | Mode | 1 | Not in `modes` |
| `EDGE` | Resonance State | 1 | Not in `res_states` |
| `BRUSH` | Resonance State | 1 | Not in `res_states` |

`canon_rules.json` allows `res_states` of `CALM / BLOOM / SHARD / RUPTURE / NODE /
VT / LT`, matching `rules/Mechanica-v4.md` §33. It allows `modes` of
`ROM / HUM / ACT / SCI / CIV / INT / HOR / SLICE`.

Migrating E16–E18 hits this on the first ECID block. Either the vocabulary is
incomplete or the packets are out of spec — that is a canon decision, so **stop and
ask**. Do not silently map `STRAIN` onto `SHARD`, do not widen the vocabulary, and do
not migrate the packets with the tokens stripped.

---

## 5. Source tiers

One scheme only. `recovery/RECOVERY_LEDGER_2026.md` defines it:

| Tier | Meaning |
| --- | --- |
| A | Explicit locked source canon |
| B | Explicitly approved development outputs |
| C | Existing GitHub canon |
| D | Assistant-generated but unapproved material |
| E | Memory summaries |

A second, conflicting lettering exists in
`recovery/checkpoints/RECOVERY_STATE_CHECKPOINT_2026-09-15.md` (lines 16–18), where D
is "earlier Notion", E is "assistant-generated", and F is "memory". That file is the
only place it survives. **That scheme is retired.** When converting it, rewrite to the
table above, note the conversion in the commit message, and record it in the ledger —
commit messages alone are too easy to lose.

---

## 6. Known state, as of 2026-09-17

> Verify with `git` before trusting this section; it dates quickly.

**The recovery work is not on `main`. It is on the branch
`proposal/concord-2026-reconciliation`, 50 commits ahead and 0 behind, unmerged.**

That branch holds, and `main` does not:

- `recovery/source_exports/html_sanitized/` — 21 sanitized ChatGPT exports plus a
  README, split into parts, including `Episode expansion process`,
  `Trilogy Act-Level Beat Backup`, `Saga Beat Expansion Pipeline`,
  `Saga structural archive`, `Narrative Structure`, `Rebuild Beat Bibles`,
  `Story world development`, `Concord Saga CSVs`, `Character involvement pacing`,
  `Character Vault Chat`, `Phase 1A Migration Plan`
- `recovery/checkpoints/` — `BOOK1_EPISODE_RECOVERY_STATE`, `RECOVERY_STATE_CHECKPOINT`,
  `CANON_CONFLICT_AND_DECISION_LEDGER`, `SOURCE_PROVENANCE_LEDGER`,
  `B9_ENDGAME_RECOVERY_LEDGER`, `RECOVERY_NEXT_ACTIONS`, all dated 2026-09-15
- `proposals/concord-2026/` — 19 analysis and proposal documents, including the
  migration map for book contexts and act overlays, the authority map, and the
  structural audits

Check out that branch before concluding anything is missing. A handoff document written
against `main` alone will understate what has been recovered.

**The seven exports once reported missing are present on that branch** at
`recovery/source_exports/html_sanitized/`: `Trilogy Act-Level Beat Backup`,
`Rebuild Beat Bibles`, `Saga Beat Expansion Pipeline`, `Story world development`,
`Narrative Structure`, `Concord Saga CSVs`, `Character involvement pacing`. That is
verifiable with `git ls-tree`, so state it that way in the ledgers rather than citing
an external handoff.

**On `main`:**

- `recovery/` holds only `RECOVERY_LEDGER_2026.md` and `MECHANICA_MIGRATION_AUDIT_2026.md`
- `book_context_B01.json`..`B09.json` and the 27 act overlays exist as skeletons
- Act overlays already use the correct two-digit `S1.T1.B01.A1` form
- `rules/canon_rules.json` already carries the correct two-digit SID pattern

**Act I recovery status — conflict, unresolved.**

Two repository artifacts say Act I is complete:

- `recovery/checkpoints/BOOK1_EPISODE_RECOVERY_STATE_2026-09-15.md` — "Act I —
  recovered complete", listing E00–E16
- `recovery/RECOVERY_LEDGER_2026.md` §5 — "FULLY EPISODE-EXPANDED THROUGH E16"

A file-level search of the exports says otherwise:

- E16, E17, E18 have **full packets** with complete ECID blocks, in
  `Story Development - Episode expansion process__part01/02.html`. E18 ends with
  "END EPISODE 18 … Next episode: EPISODE 19."
- E00–E15 appear as **titles only**. No packet body for any of them is present in any
  export on either branch; the Act I episode titles return zero content matches.
  The ledger names `Archive Veil Book 1` and `Hold until release` as their likely home,
  and neither has been exported.

The likely reconciliation is that "recovered complete" meant the title list, not the
packets. **That is a reading, not a ruling.** James: confirm it and the ledgers get
corrected to the E00–E15 / E16–E18 / E19 split. Until then, both readings stand
recorded, per §4.

E19 is named only, never built. Prohibited — see §4.

---

## 7. Source constraint

All Concord Saga source conversations live in a single **ChatGPT Business workspace**.
Business workspaces have no data export and no working public share links; both routes
were tested and closed. Recovery runs through the browser-console export script against
the logged-in session, or manual re-save, or copy-paste.

This means: **source conversations are one-way storage and are not reliably
re-retrievable.** Treat anything recovered from them as irreplaceable. Commit recovered
material before transforming it, so the raw form survives in history.

---

## 8. Work queue

**Items 2 and 3 are unblocked.** Items 4 and 5 read from files that exist only on the
unmerged proposal branch, so they depend on item 1. Items 4 and 5 additionally depend
on §4.1.

1. Decide the fate of `proposal/concord-2026-reconciliation` — merge it into `main`, or
   record why it stays separate. Everything below assumes its contents are reachable.
   **This is an author decision; prepare the merge and ask.**
2. Correct the Act I overstatement once James rules on §6, plus any one-digit SIDs, the
   duplicate tier scheme, and the empty `ChatGPT - Story Development.html` source file
   (708 bytes, shell only), per §3, §5 and §6
3. Close the missing-source gap in the ledgers, per §6
4. Migrate the Veil Consolidated Beat Bible into `book_context_B01/B02/B03.json` and the
   nine Veil act overlays, following `proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md`
   — **blocked on items 1 and §4.1**
5. Migrate the E16–E18 packets into the canon structure — **blocked on items 1 and §4.1**
5a. Migrate the Book 3 Act III structural shells — `S1.T1.B3.A3.E01`–`E18`, plus the
   four-episode Veil→Neon epilogue, from the `Saga structural archive` export. This is
   the Book 3 analogue of item 5 and sits downstream of item 4, which sets the act
   envelope these episodes must fit inside. **Blocked on items 1 and 4, on §4.1, and on
   two structural rulings recorded in `recovery/RECOVERY_LEDGER_2026.md` §15** — the
   shells omit the required `HEAT` and `FX` ECID fields, and the epilogue uses `EP` in
   the act slot, which the SID format does not allow
6. Run the ChatGPT console export in list mode; produce the full workspace inventory
7. Extract remaining Tier 1 conversations, `Archive Veil Book 1` first — this is where
   the E00–E15 packets are expected to be
8. Migrate E01–E15 packets
9. Resolve the `canon/` vs `source_canon/` authority conflict (§1.1) and the Mechanica
   provenance question
10. Resume episode construction at E19 — **author-gated, see §4**

---

## 9. Working style

- Read the relevant ledger or audit before editing what it describes.
- Prefer editing a file in place over regenerating it.
- When correcting an artifact, record what was wrong and what replaced it, so the
  correction is auditable later.
- Keep the ledgers current. A change to canon state that leaves the ledger stale is
  half-finished work.

### 9.1 Known defects on `main`, unfixed

Flagged, not yet ruled on. Do not silently fix these while doing other work; they each
need their own ledger entry.

- **Faction name drift.** `Technarc` (64 uses) vs `Technarch` (9). The faction file is
  `canon/factions/Technarc.md`. The variant appears in `canon/characters/RexID.md` (3),
  `canon/characters/VirelliID.md`, `canon/trilogy_veil.md`, `canon/trilogy_neon.md`,
  `canon/factions/Dominions.md`, and `rules/symbols/GEOMETRY_MOTIFS.md` (1 each).
- **Trilogy envelopes contradict the escalation model.** `rules/trilogy_context_T1_veil.json`,
  `T2_neon.json` and `T3_loom.json` all carry identical `weather_max: "W3"` and
  `corridor_max: "U5"`; only the FX ceiling escalates. `rules/Mechanica-v4.md` §7.3
  describes Loom as corridor-failure and resonance-storm territory, which is U6/W4.
  As written, `U6`, `U7` and `W4` are unreachable in every trilogy despite being in
  the controlled vocabulary.
- **All six grid CSVs are header-only**, so `CHK_BREADCRUMBS` and `CHK_EMO_CIRCUIT` in
  `rules/validation_checks.json` cannot run against any data.
- **All 27 act overlays are byte-identical** apart from their ID fields, as are all 9
  book contexts. Every act caps `fun`/`slice_of_life`/`wonder` at `LOW`, including the
  Book 9 climax.
- ~~**No validation tooling exists.**~~ **Addressed 2026-09-19.** `tools/validate_canon.py`
  now enforces the mechanical layer — SID format including the two-digit book rule, ECID
  field names, and controlled-vocabulary membership for all six dimensions — reading every
  rule from `rules/canon_rules.json` rather than hardcoding it. Run it before any
  migration commit:

  ```sh
  python3 tools/validate_canon.py            # exits non-zero on any violation
  python3 tools/test_validate_canon.py       # 27 self-tests
  ```

  Baseline as of 2026-09-19: 27 violations in the substrate, all of them `TODO`
  placeholders in the nine book-context skeletons. See `reports/README.md`. It does not
  catch the other four defects above — the faction drift is a spelling question and the
  envelope contradiction is a semantic one, and neither is a format violation.
