# Narrative Build Priorities — Assessment and Sequence

**Status:** PROPOSAL / PRIORITIZATION — NONCANONICAL UNTIL AUTHOR APPROVAL
**Date:** 2026-09-19
**Written against:** James's 2026-09-19 direction — extract the best versions, organize
them, build a saga timeline with arcs and milestones, then cascade
saga → trilogy → book → act → episode.

**Premise, stated plainly.** Recent sessions have produced a great deal of bookkeeping
analysis — authority letterings, classification vocabularies, ledger hygiene — and
comparatively little that moves the build forward. This document reorganizes around the
pipeline and says which of the open questions actually block it.

---

## 1. The build pipeline has containers for every layer but its root

The five-level cascade already has homes in the repository — except the top one.

| Level | Container today | State |
| --- | --- | --- |
| **Saga** | **none** — only `canon/saga_overview.md`, **22 lines** | **MISSING** |
| Trilogy | `rules/trilogy_context_T1/T2/T3.json` | envelopes populated; each still carries `"TODO": "Populate trilogy-specific ceilings and exceptions."` |
| Book | `book_context/book_context_B01..B09.json` | 9 skeletons, byte-identical but for IDs, every field `TODO` |
| Act | `act_overlays/*.json` × 27 | `escalation_permissions` populated 2026-09-19; `act_thesis`, `deltas`, `act_success_criteria`, `forbidden_shortcuts` all `TODO` |
| Episode | `grids/episode_beats.csv` | header-only, **0 rows** |

**The saga timeline — step 3, the thing everything else descends from — has nowhere to
live.** `canon/saga_overview.md` is 22 lines of purpose, structural frame, invariants and
three one-line trilogy summaries. It is an orientation page, not a timeline.

This is the single highest-value structural gap, and it is cheap to close because the
content mostly exists and is merely scattered.

### 1.1 The book container already anticipates what is missing

`book_context_B01.json` has these fields, all `TODO`:

```
entry_state: { world, key_character_states }
exit_state_locks: [ ]
locations_in_play: [ ]
continuity_hooks: [ ]
pov_targets
```

Those five **are** the book-level timeline. The schema was designed for this cascade; it
has simply never been filled. So step 4 does not need new structure at book level — it
needs content and a saga/trilogy layer above it to derive from.

---

## 2. The five extraction categories, assessed against the substrate

| Category | Where it lives | Resolution | Verdict |
| --- | --- | --- | --- |
| **Rules** | `rules/` — 25 files, `canon_rules.json`, Mechanica v4, Resonance v1, 5 Emotion, 4 resonance, 5 symbols, 5 Channels | **High** | Best-developed layer. Extraction is mostly done; needs consolidation, not recovery |
| **Context** | trilogy/book/act containers above | **Containers yes, contents no** | Blocked on the narrative layer, not on schema |
| **Characters** | `canon/characters/` — **62 files across 14 characters**; `canon/pov/` — 15 POV files | **High for who is covered** | Three load-bearing absences: **Silence**, **Hope**, **Threadnaut** |
| **Environments** | **nothing** | **ABSENT** | See §3.1 — this is the largest unbuilt layer |
| **Narrative** | scattered across `recovery/` and `proposals/`; **0 rows in all six grids** | **Recovered but unorganized** | This is the whole of steps 1–2 |

### 2.1 Character coverage is stronger than any other layer — use it as the template

Fourteen characters carry a consistent four-file pattern (`*ID`, `*EBCI`, `*Appearance`,
`*Render`) plus a POV file. That is the only place in the repository where a layer is
actually *finished*, and it is the obvious model for what "optimal format" means for the
layers that are not.

The gaps are not marginal characters. **Silence and Hope** define `VT` and drive the
endgame (work-queue 9b); **Threadnaut** is the persona the entire B01–B03 reveal
architecture depends on, with 84 references in `proposals/` and `recovery/` and zero canon
files (ledger §27.4).

---

## 3. Dimensions not yet considered

James named three. All three confirm, and an audit finds four more.

### 3.1 Narrative locations vs character locations — NO LAYER EXISTS

There is **no `canon/locations/` directory**. Locations appear only incidentally inside
character files: 8 canon files mention "location" at all, 6 mention New Orleans, 3 Santa
Fe, 1 Honey Island. Zero in `rules/`, zero in `grids/`.

Three consequences, each already biting:

1. **`ENV` is an ECID field with no vocabulary.** `reports/README.md` records it: *"`POV`
   and `ENV` are unchecked — `canon_rules.json` defines no vocabulary for them."* Every
   episode packet will carry an `ENV` value that nothing can validate.
2. **`book_context.locations_in_play` is `TODO` in all nine books** because there is no
   location canon to list.
3. **The distinction James raised is not currently expressible.** A narrative location
   (Honey Island swamp as the Mending locus; the Warehouse; Santa Fe) is a different kind
   of object from a character location (where Lucien is in Book 2). The first is a place
   with narrative function and constraints; the second is a *state* that belongs on a
   character-arc timeline. Today the repo has neither, and no field distinguishes them.

**The saga is geographically dense** — New Orleans, Vienna, Santa Fe, Honey Island,
Marrakech, Singapore, Iceland, St. Louis, Mound City, Serpent Mound all appear in
recovered material — so this is recovery work, not invention.

### 3.2 Combat — NO SYSTEM

3 canon files mention "combat", 1 rules file, **0 grids**, 0 hits for "fight". Yet the
recovered Loom material is full of confrontation: siege lines around the swamp, Dominion's
final push, Virelli attempting to capture Seraphine, Choirless interception, and the
Kade-attacks-Rex sequence just ruled on.

The open question is not "what are the combat rules" but **what kind of system this saga
needs** — whether conflict resolves through resonance mechanics already in Mechanica, or
needs its own axis. That is an author call and has never been put.

### 3.3 Antagonist milestones and arcs — MATERIAL EXISTS, STRUCTURE DOES NOT

`canon/factions/` holds 10 files (Brightbreak, Choirless + subtypes, Concord Dominions,
Manufactured Metas + creators + variants, Technarc, filaments). `episode_beats.csv` has an
`antagonist_pressure` column. Nothing connects them.

The richest existing material is ND-020 through ND-029 in
`NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT` — systemic-antagonism-first, Brightbreak as three
distinct things, the Elias three-book causal chain, Choirless originating in Neon,
Manufactured Metas as institutional failure. **That is an antagonist arc in prose form
with no grid to carry it.**

### 3.4 Four more found in the audit

- **Character arcs have no structured layer.** 66 canon files mention "arc" — they exist
  as prose inside character files. There is no arc grid, no per-book character state, and
  `act_overlays.deltas.character_state_deltas` is an empty array in all 27 overlays.
- **POV allocation is unplanned.** `pov_targets` is `TODO` in all nine books; 15 POV files
  exist with no distribution model, though `canon/pov/` implies one was intended.
- **Chronology has no artifact.** No timeline anywhere in the substrate. Three timeskips
  are open right now: B03→B04 (Baz's death discovery), the B09 epilogue (three days vs
  6–12 months vs 1–2 years), and Neon's internal spacing.
- **Motifs are unbound.** `episode_beats.csv` has `motif_1`/`motif_2`; `rules/symbols/`
  has 5 files. No vocabulary links them, so motif values will be free text.

---

## 4. Which open questions actually block the build

The accumulated question list mixes two very different things. Sorted by whether the
pipeline stops without an answer:

### BLOCKING — the build cannot proceed correctly past these

| # | Question | Blocks |
| --- | --- | --- |
| B1 | **Merge `proposal/concord-2026-reconciliation`** (work-queue item 1) | Everything. Still unperformed on `main` |
| B2 | **Which Veil draft is canon** — now **three** drafts (ledger §27.6) | All of T1: books 1–3 at every cascade level |
| B3 | **Does `EP` go in the act slot** | The milestone load — which is step 3's raw material. Five rows use `target_act: EP` |
| B4 | **Does the `MT`→`LT` rename complete in the B09 epilogue** | The held Post-Mending era file, the `LT` three-referent problem, and all of B09's act/episode layer |

B1 and B2 are the real gates. B3 and B4 are narrow and book-specific.

### DEFERRABLE — real, but they do not stop the cascade

The Book 9 epilogue timeskip, the Threadnaut naming conflict, whether the three
`ACT * SUMMARY — VEIL I` pages are superseded, prologue/epilogue symmetry. Each blocks one
artifact, not the pipeline.

### THE BOOKKEEPING QUESTIONS — one of them is real, and it is a step-1 question

Ledger §26.4, §26.5 and §26.12 asked about authority letterings, classification labels and
ND supersession. **Two of those three can wait indefinitely.** The third cannot, and it is
worth saying why in pipeline terms rather than hygiene terms:

> **Step 1 is "extract the best versions." That presupposes we can tell which version is
> best. Right now we cannot, reliably.**

`ND-032` is the proof. It was a decision-ledger entry marked `SUPERSEDED` that protected
the **wrong** sequence, and nothing in the format could mark it once a later pass
disproved it. James caught it. An extraction pass run before that ruling would have pulled
Kade→Elias into canon as a sourced decision.

So the useful form of that question is not "do the ledgers need a supersession field" but:

> **What is the rule for deciding which of two conflicting recovered versions wins?**

`NARRATIVE_DECISION_LEDGER_PASS3` ND-045 already proposes one, and it is good:

- later explicit author decisions beat earlier "Final Canon" labels
- exact user-pasted canonical backups beat assistant summaries
- unique Notion detail with no later contradiction survives as recovered candidate
- Notion conflicting with later evidence is marked superseded or unresolved, never merged

**Ratifying that as the extraction rule is the single most valuable bookkeeping decision
available, and it is a step-1 enabler, not hygiene.** The lettering and label questions can
then be dropped or deferred without cost.

---

## 5. Proposed sequence

Each phase produces something the next one consumes.

### Phase 0 — unblock (author, small)
- **B1** merge ruling; **ratify ND-045** as the extraction rule (§4).
- These two together let extraction start without re-litigating provenance per item.

### Phase 1 — extract and consolidate (steps 1–2)
Per category, produce one consolidated, sourced artifact:
1. **Rules** — consolidate; this layer is nearly done. Lowest effort, do it first to
   establish the format.
2. **Characters** — fill the three absences (Silence, Hope, Threadnaut) using the existing
   four-file pattern as the template.
3. **Locations** — **new layer.** Build `canon/locations/`, distinguishing narrative
   locations from character-location states, and give `ENV` a controlled vocabulary.
4. **Antagonists** — promote ND-020–ND-029 from prose into a faction/arc structure.
5. **Narrative** — this is the recovered beat material, and it feeds Phase 2 directly.

### Phase 2 — the saga layer (step 3)
- **Create the missing root.** A saga-level container — arcs, milestones, era boundaries,
  the three timeskips — that the trilogy contexts descend from.
- **Load the milestones.** 36 rows are staged at
  `proposals/concord-2026/milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv` and blocked
  only on **B3**. This is the closest thing to a saga timeline that already exists.
- **Add the missing arc dimensions**: character arcs, antagonist arcs, location arcs.

### Phase 3 — cascade down (step 4)
Trilogy → book → act → episode, in that order, each deriving from the layer above.
The containers already exist at every level; **Phase 2 is what makes filling them
derivation rather than invention.**

Veil cannot start until **B2**. Loom Book 9 cannot finish until **B4**. Neon is the least
blocked trilogy and may be the right place to prove the cascade end-to-end.

### What to stop doing
Further Notion searching for Book 1 episode packets. Ledger §27.5 closed it: all three
`ACT * SUMMARY — VEIL I` pages and the Book 1 Final Beat Bible are macro-only, four
confirmations. `Archive Veil Book 1` in the ChatGPT workspace is the only candidate left,
which is work-queue items 6 and 7.

---

## 6. What this document does not decide

Nothing here is canon. The sequence is a proposal; the phase boundaries are a suggestion;
and the three genuinely new layers — locations, combat, antagonist arcs — need author
direction on **shape** before anyone builds them:

1. **Locations:** do narrative locations and character-location states live in one layer
   with a type field, or two?
2. **Combat:** does conflict resolve through existing resonance mechanics, or does it need
   its own axis the way `LOAD` did?
3. **Antagonist arcs:** do antagonists get the same arc treatment as protagonists, or a
   pressure-curve model tied to `antagonist_pressure`?

END OF DOCUMENT
