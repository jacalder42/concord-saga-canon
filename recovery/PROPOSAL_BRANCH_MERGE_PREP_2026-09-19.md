# Proposal Branch Merge — Preparation

**Status:** PREPARATION ONLY. Nothing has been merged. This is work-queue item 1
(`CLAUDE.md` §8), which is an author decision.
**Prepared:** 2026-09-19
**Branch:** `proposal/concord-2026-reconciliation` @ `9e2f345`
**Against:** `origin/main` @ `253fdf4`

---

## 1. Mergeability — confirmed clean

| Check | Result |
| --- | --- |
| Commits ahead of `main` | 50 |
| Commits behind `main` | 0 |
| Is `main` an ancestor? | Yes |
| Merge into `main` | **Fast-forward. No merge commit, no conflicts.** |
| Merge into `claude/gifted-goodall-st4n7r` | **Clean three-way merge, no conflicts** |
| Files changed | 47, **all additions** (`git diff --name-status` reports no `M` or `D`) |
| Lines | +7,835, −0 |

Two properties worth stating plainly, because they make this a low-risk merge:

**It modifies nothing.** Every one of the 47 changes is a new file. No existing canon,
rule, grid, overlay or ledger file is touched. Merging cannot alter or delete anything
currently on `main`.

**It does not collide with the work on this branch.** The two branches share zero
files. `claude/gifted-goodall-st4n7r` touches `CLAUDE.md`, the recovery ledger, the ECID
memo, `tools/` and `reports/`; the proposal branch touches only `proposals/` and new
files under `recovery/checkpoints/` and `recovery/source_exports/`. They can merge in
either order.

Verified with `git merge-tree --write-tree` in both directions; both produce a tree
with no conflict markers.

---

## 2. What merging would add

### `recovery/source_exports/html_sanitized/` — 21 exports plus a README

The sanitized ChatGPT conversation exports. **This is the irreplaceable material.**
Per `CLAUDE.md` §7 the source workspace has no export path and these conversations are
not reliably re-retrievable, so until this branch merges, the only copy of this material
in the repository is on an unmerged branch.

Includes `Episode expansion process` (the E16–E18 packets), `Saga structural archive`
(the Book 3 Act III shells), `Trilogy Act-Level Beat Backup`, `Saga Beat Expansion
Pipeline`, `Narrative Structure`, `Rebuild Beat Bibles`, `Story world development`,
`Concord Saga CSVs`, `Character involvement pacing`, `Character Vault Chat`, and
`Phase 1A Migration Plan`.

One of the 21, `ChatGPT - Story Development.html`, is the known 708-byte empty shell
(work-queue item 2).

### `recovery/checkpoints/` — 6 checkpoints, all dated 2026-09-15

`BOOK1_EPISODE_RECOVERY_STATE`, `RECOVERY_STATE_CHECKPOINT`,
`CANON_CONFLICT_AND_DECISION_LEDGER`, `SOURCE_PROVENANCE_LEDGER`,
`B9_ENDGAME_RECOVERY_LEDGER`, `RECOVERY_NEXT_ACTIONS`.

### `proposals/concord-2026/` — 19 analysis documents

Including `MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md` (the map work-queue item 4
follows), `AUTHORITY_MAP.md`, `NINE_BOOK_AUTHORITY_LAYER.md`,
`RECOVERED_SAGA_SPINE_PROPOSAL.md`, and the structural audits.

---

## 3. Conflicts with current canon — four, none blocking the merge

All four are **content** conflicts that merging would import. None is a git conflict,
and none is created by the merge — each already exists on the branch today. Merging
makes them visible on `main` rather than causing them.

### 3.1 A third artifact asserting Act I is complete

`CLAUDE.md` §6 records the Act I dispute and names two artifacts on the "complete"
side. Merging adds a third:

> `proposals/concord-2026/RECOVERED_SAGA_SPINE_PROPOSAL.md`, lines 124–129:
> "Act I E01–E16: complete in the later workflow…"

This does not change the evidence — no packet body for E00–E15 exists in any export on
either branch — but it means the correction contemplated in work-queue item 2 has three
documents to correct, not two. `CLAUDE.md` §6 should be updated to name all three when
James rules.

### 3.2 The retired D/E/F tier scheme, still contained to one file

`CLAUDE.md` §5 says the retired lettering survives in exactly one file. That holds
after merge. `recovery/checkpoints/RECOVERY_STATE_CHECKPOINT_2026-09-15.md` lines 16–18
carry it; `proposals/concord-2026/AUTHORITY_MAP.md` uses the current A–E scheme with
Tier E as "ChatGPT project memory / summaries", which is compatible with the ledger.

No new instances arrive with the merge. Work-queue item 2 is unchanged in scope.

### 3.3 One-digit book SIDs in the analysis layer

Five occurrences of the `S1.T1.B1.A…` form across the proposal documents, plus the
numbering rule in `BOOK1_EPISODE_RECOVERY_STATE_2026-09-15.md`, which states operational
expansion uses `S1.T1.B1.A{act}.E{episode}` — the one-digit form `CLAUDE.md` §3 rules
wrong.

After merge, `python3 tools/validate_canon.py --all` will report these. They are
documentation quoting recovered identifiers, the same category as the 15 already in the
baseline, so they belong outside the default scan scope rather than being rewritten.
`reports/README.md` explains why.

### 3.4 The migration map's method depends on a rule set currently broken

`MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md` instructs that `escalation_permissions`
(`max_corridor_tier`, `max_weather`, `max_fx`) "must be cross-derived from Mechanica v4
+ trilogy envelope rules" and should remain `TODO` until systems reconciliation is
complete.

That instruction is sound and matches the validator baseline — those 27 `TODO`
placeholders are the entire substrate violation count, and they are deliberate. But the
trilogy envelope rules it points at are the ones `CLAUDE.md` §9.1 records as
self-contradictory: `trilogy_context_T1/T2/T3` all carry identical `weather_max: W3`
and `corridor_max: U5`, while `Mechanica-v4.md` §7.3 describes Loom as corridor-failure
territory.

**No document on the proposal branch addresses this.** A repository-wide search of the
proposal and checkpoint files for `weather_max`, `corridor_max`, `U6` or `W4` returns
nothing. So merging does not resolve the envelope defect, and work-queue item 4 cannot
complete until it is resolved — the map tells you to derive values from rules that do
not currently agree.

---

## 4. Conflicts with §8 of the ECID memo — none

The corrections in `recovery/ECID_VOCABULARY_COLLISION_2026.md` §8 concern the `BRUSH`
count, `LORE` as a beat-level `Function` value, the evidentiary basis for `STRAIN`, and
`STRAIN`'s positional behaviour. Each was checked against the branch:

- **No proposal or checkpoint document contains any out-of-vocabulary ECID token.**
  A search for `STRAIN`, `LORE`, `POL`, `VT-BRUSH` and `SHARD-EDGE` across all 25
  documents returns one apparent hit, which is the substring inside the word
  `CONSTRAINT`. The vocabulary collision lives entirely in the exports, not in the
  analysis layer.
- Nothing on the branch makes a competing claim about where `STRAIN` sits, or about
  the beat `Function` field.

So merging neither contradicts nor supports the memo's corrections. It supplies the
exports the memo's counts were derived from, which is an argument for merging: today
those counts cite evidence reachable only from an unmerged branch.

---

## 5. What is recommended, and what is not

**Not recommended by this document:** whether to merge. That is work-queue item 1 and
`CLAUDE.md` §4 reserves it.

**What the evidence supports, for James to weigh:**

Arguments for merging: the exports are irreplaceable and currently single-copy on a
branch; the merge is a fast-forward that modifies nothing; three work-queue items (4,
5, 5a) read from files only available there; and the ECID memo's evidence base is
currently unreachable from `main`.

Arguments for keeping it separate: everything under `proposals/` is explicitly marked
`PROPOSAL / NON-CANONICAL`, and merging places 19 unapproved analysis documents on the
main line where a later reader may mistake them for settled canon. If that is the
concern, it is addressable — `CLAUDE.md` §1 already documents `proposals/` as an
analysis folder, and the tier scheme in §5 covers it.

**If the decision is to merge**, the mechanics are: `git checkout main && git merge
--ff-only proposal/concord-2026-reconciliation`. No conflict resolution is required. A
follow-up commit should then update `CLAUDE.md` §6, which currently describes the branch
as unmerged and lists what `main` lacks.

**If the decision is to keep it separate**, `CLAUDE.md` §8 item 1 asks that the reason
be recorded, and items 4, 5 and 5a need restating to say which branch they run on.
