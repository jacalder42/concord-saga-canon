# Proposal Branch Merge — Preparation

**Status:** PREPARATION ONLY. Nothing has been merged.
**Prepared:** 2026-09-19 · **Re-verified:** 2026-09-19 against
`recovery/CANON_DECISIONS_2026-09-18.md`
**Ruled:** §6.1 — *"`proposal/concord-2026-reconciliation` merges, as its own folder."*
The merge itself is decided; the mechanics and the conflicts it imports are below, and
performing it remains James's call.
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

## 3. Conflicts with current canon — five, none blocking the merge

All five are **content** conflicts that merging would import. None is a git conflict,
and none is created by the merge — each already exists on the branch today. Merging
makes them visible on `main` rather than causing them.

**One is new since the 2026-09-18 rulings and is the only one that undoes work already
done on this branch:** see §3.5.

### 3.1 A third artifact asserting Act I is complete — now consistent with the ruling

`proposals/concord-2026/RECOVERED_SAGA_SPINE_PROPOSAL.md` lines 124–129 assert
"Act I E01–E16: complete in the later workflow…", a third artifact beside the two
`CLAUDE.md` §6 named.

**Decisions §5.5 ruled on 2026-09-18 that "recovered complete" means the beat text
exists but is unexported.** Under that ruling this document is not wrong — it is
describing existence, not export state. It should still gain the exported/unexported
distinction when it is next touched, because on its own it reads as a claim about the
repository.

The file-level evidence is unchanged: no packet body for E00–E15 appears in any export
on either branch.

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

### 3.5 The merge reintroduces the retired `Technarch` spelling — 43 occurrences

**New, and the one worth deciding before merging rather than after.**

Decisions §6.4 ruled `Technarc` canonical, and commit `a83f78d` on this branch
corrected all 9 occurrences across the 6 canon and rules files it named. The repository
now reads 73 `Technarc`, 0 `Technarch`.

The proposal branch carries 43 more:

| Location | Occurrences | Files |
| --- | --- | --- |
| `proposals/concord-2026/` | 23 | 7 |
| `recovery/checkpoints/` | 1 | 1 |
| `recovery/source_exports/html_sanitized/` | 19 | 6 |

Heaviest: `NINE_BOOK_AUTHORITY_LAYER.md` (7), `NOTION_TARGETED_RECOVERY_PASS2.md` (6),
`NOTION_SOURCE_AUDIT_2026.md` (4).

**The 19 in the exports must not be touched.** They are the sanitized source
conversations — irreplaceable per `CLAUDE.md` §7, and §6.1 is explicit that exports are
never pruned in place. A spelling sweep across them would be exactly the in-place
alteration that rule forbids.

**The 24 in the analysis layer are a judgement call**, and it is James's:

- *Leave them.* They are `proposals/` and `checkpoints/` — analysis written before the
  ruling, in a folder `CLAUDE.md` §5 tiers as D. Their spelling is a historical record
  of when they were written.
- *Correct the 24.* `Technarc` then holds everywhere except the exports, and the
  ruling reads as fully applied.

Either way the exports keep the old spelling, so `grep Technarch` will never return
zero repository-wide. The validator does not check spelling, so nothing enforces this
mechanically either way.

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

**Decided at §6.1:** the branch merges, as its own folder. What remains is the timing,
which is James's, and three mechanical points.

**1. The mechanics.** `git checkout main && git merge --ff-only
proposal/concord-2026-reconciliation`. No conflict resolution is required. A follow-up
commit should then update `CLAUDE.md` §6, which still describes the branch as unmerged
and lists what `main` lacks.

**2. "As its own folder" needs one clarification.** §6.1 says the recovery material
keeps its own top-level folder. The branch actually lands in **two**: `recovery/`,
which already exists on `main` and would gain `checkpoints/` and `source_exports/`
subfolders; and `proposals/`, which would be new at top level. That matches the intent
as far as this document can tell — the analysis layer stays separable from canon — but
if §6.1 meant a single folder holding both, say so before merging, because moving them
afterwards rewrites paths that this branch's documents already cite.

**3. Pruning, per §6.1.** The sanitized exports are **never pruned in place**. Any
pruning copies them to a separate folder and prunes the copy. The ChatGPT Business
workspace has no export path and the share-link route was tested and closed — these
files are the only copy that exists anywhere. This applies to the `Technarch` question
in §3.5 as much as to any size-driven pruning.

**Ordering note.** This branch and the proposal branch share zero files and merge
cleanly in either order, so neither blocks the other.
