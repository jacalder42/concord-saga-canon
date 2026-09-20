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
| `proposals/` | **Distilled versions.** Analysis and proposal documents worked up from the originals (`proposals/concord-2026/`) |
| `recovery/` | **Originals.** Ledgers, migration audits, checkpoints, and the sanitized source exports — never pruned or altered in place |
| `tools/` | Validation scripts. `validate_canon.py` checks the substrate against `rules/canon_rules.json`; `test_validate_canon.py` is its self-test |
| `reports/` | Generated validation reports — do not hand-edit, regenerate (see `reports/README.md`) |

**No prose, scene text, or dialogue is stored here.** If a task would put
narrative prose in this repo, stop and say so instead.

### 1.0 `recovery/` holds originals, `proposals/` holds distilled versions

Ruled 2026-09-19. The two folders are a pipeline, not a duplication:

- **`recovery/`** is where source material lands unaltered. The sanitized exports in
  `recovery/source_exports/` are **never pruned or edited in place** (decisions §6.1) —
  the ChatGPT Business workspace has no export path and the share-link route was tested
  and closed, so these files are the only copy that exists anywhere. Any pruning copies
  them elsewhere and prunes the copy.
- **`proposals/`** is where distillation of that material lives. Editable, revisable,
  and tiered D under §5.

This is why the `Technarch` correction of 2026-09-19 touched
`proposals/concord-2026/` and `recovery/checkpoints/` but left
`recovery/source_exports/` alone. The same rule governs every future cleanup: if it
would alter an original, it does not happen in place.

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

Ruled 2026-09-18 — `recovery/CANON_DECISIONS_2026-09-18.md` §2. The provenance gap
previously flagged here is closed.

**SID format is `S1.T{1-3}.B{01-09}.A{1-3}.E{00-99}` — two-digit book numbers.**
`B1` is the old one-digit form and is wrong wherever it appears.

- Trilogies: `T1` Veil, `T2` Neon, `T3` Loom
- Books: `B01`..`B09` — always two digits
- Acts: `A1`..`A3`
- Episodes: `E00`..`E99`, **numbered continuously across the whole book**, not
  restarting at `E01` in each act. Episode numbering restarting per act is the old,
  corrected form.
- Episodes live in grids, not in filenames.

> **Confirmed 2026-09-19.** `B{01-09}` is correct; the `B{00-09}` in §2.1 of the
> decisions document was a transcription slip. There is no book zero. Ledger §17.

**Scope warning.** The recovered material uses the old forms pervasively, not
occasionally: one-digit books throughout, and per-act restarts such as
`S1.T1.B3.A3.E01` through `E18` in the `Saga structural archive` export. Treat the
rewrite as a migration pass with its own ledger entry, not an incidental find-and-replace.

**The Prologue is `E00`, titled `The Conversation in the Sky`** (§2.2). The episode
range widened to `E{00-99}` to admit it. This supersedes `Silence & Hope` from the Veil
Master Beat Bible, whose Act I numbering starts the Prologue at `EP 01` and is
therefore **offset by one** — that bible renumbers to the `E00` convention on
migration, not the reverse. `pre01`/`post01` was considered and rejected: the Prologue
is narrative, and non-narrative material is supplements, which carry their own
identifiers. Epilogues take the next sequential episode number.

**The three channels are three Threads.** Ruled 2026-09-19
(`recovery/CHANNEL_NAMES_RULING_2026-09-19.md`):

- **MT** — MissingThread, the public mortal channel (early Tahl)
- **VT** — VeilThread, the private channel between Silence and Hope that Tahl discovers
- **LT** — LuminousThread, the post-Mending channel

`Veil-Touch` is retired and corrected in `rules/`, including two occurrences in
Mechanica. `Mortal Technology` is **not yet** retired — see §4, the `MT` reconciliation
is open.

**Field names: the schema is canonical, packet labels are aliases** (§2.4).
`canon_rules.json` keeps `CORRIDOR` and `RES`. `U-Level` and `Resonance State` are
recognized input aliases recorded in `ECID_field_aliases`; tooling normalizes on the
way in. Do not rewrite the schema to match packet labels.

**`SUPP` is a mode** (ruled 2026-09-19, hedged as *"mode, i think"*), added to
`controlled_vocab.modes`. Treat it as a soft ruling: no beat carries the tag yet, so it
reopens cheaply if tagging shows it behaving as a marker rather than a register.

**The ECID carries a `LOAD` axis** (§1.4): `L0` unloaded, `L1` carrying/sustainable,
`L2` strained with visible cost, `L3` shard precursor. Nothing else in the ECID carried
emotional load — `HEAT` is the romance ladder, `FX` and `WEATHER` are environmental,
`MODE` is register — which is why `STRAIN` was drafted as a pseudo-state. `LOAD` is
where it goes.

**Character names: `canon/characters/` is final.** Ruled 2026-09-19 — *"names in repo
canon/character can be considered final and other references can be adjusted to match."*
**Check `canon/characters/` first on any identity question**, before concluding a name
from recovered sources. Three divergent forms were corrected on 2026-09-19 —
`Caro Gauthier` → **Carolina "Caro" Alvarez**, `Kade Rios` → **Kade Harper**, and
`Koro Ito` → **Ito Masayuki** — the last of which a proposal document had ruled the other
way from a memory export without checking `ItoID.md`. Source quotations keep the old form
as evidence; the author-uploaded bundles and `recovery/source_exports/` are not edited in
place.

**`Foix` is retired as a Baz surname** — ruled 2026-09-19,
`recovery/GATE_RULINGS_2026-09-19.md` **Amendment 1**. `Bastien "Baz" Arnaud` is canon and
the manifest's preference for `Basil "Baz" Foix` is overruled. §31 had left `Foix`
**deliberately not swept**, on the reading that the references documented an already-locked
rename; that is superseded. The proposal layer is corrected; statements *about* the
superseded Notion-side name stay, because they remain true and are the provenance record.
`Janvier "Jan" Foix` renamed to `Janvier "Jan" Arnaud` as a consequence. Ledger §38–§40.

**Beat IDs use `BT`.** Ruled 2026-09-18 (`recovery/CANON_DECISIONS_2026-09-18.md`
§2.3). The form is `{SID}-BT{BeatNumber}`, and `rules/canon_rules.json` carries it.

This resolves the collision where `B` meant both Book and Beat: the old
`S1.T1.B1.A1.E13-B01` becomes `S1.T1.B01.A1.E13-BT01`. No beat IDs existed in the
repository when the ruling landed, so nothing needed rewriting. Recovered beat IDs in
the old form convert during migration.

---

## 4. What requires the author

James makes canon decisions. Claude does not.

Never decide, invent, or quietly resolve:

- Anything about characters, factions, metaphysics, plot, or world rules not already
  written in `source_canon/` or `canon/`
- Contradictions between two canon sources — record both readings and where each came
  from, then flag it
- Whether unapproved or assistant-generated material becomes canon
- **Who performs the Mending.** **Answered from source 2026-09-19 — awaiting only a
  correction pass.** `BOOK 9 — LOOM III (Final Beat Bible)` E14 carries both halves in one
  beat, so there was never a fork to merge. It assigns **five** named human functions —
  Seraphine opens, Lucien shapes structure, Caro modulates, **Elisabet grounds all three
  as "the human heart of the mending", Kade holds humanity through MT** — and then
  "Silence dissolves into Lucien. Hope dissolves into Caro … They form the membrane with
  Seraphine."

  So **the trio is who *ascends*, not exhaustively who *performs***; the Act III function
  line separates the two. Every existing record is too narrow: ledger §24's row, ND-013
  and this bullet all say "trio". The export's "Seraphine, Lucien, Caro complete the
  Mending" is an act-level compression. **Correcting those three artifacts is the open
  task, not the question.** Ledger §27.2.
- **The Post-Mending `res_states` list.** Open — the banded envelope work is applied,
  but the Post-Mending era file is **held**: as specified it omits `LT`, which
  Mechanica §33 lists as a resonance state and which is the era's own signature.
  Ledger §18. A proposal at
  `proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md` §4 would settle
  it by permitting `CALM · BLOOM · NODE · VT · LT`, but it is unruled.
- **How `MT` reconciles with the infrastructure layer.** Open — `recovery/CHANNEL_NAMES_RULING_2026-09-19.md`
  §2, options A/B/C. The *name* is ruled (MissingThread); what is not is whether `MT`
  means the channel, the mortal tier, or splits from the infrastructure that
  `rules/Channels/MT_RULES.md` describes. **Do not rename `MT_RULES.md` until this is
  ruled** — retitling it would leave a file called MissingThread describing phone
  networks. Ledger §20.
- **Whether `LuminousThread` and `MissingThread` close up.** Open — the ruling writes
  all three names as closed compounds, but the repository has `Luminous Thread` spaced
  19 times with zero closed, and `Missing Thread` spaced 6 against `MissingThread` 2.
  Only `VeilThread` had an unambiguous closed form to restore. Ledger §20.
- ~~**Does `EP` go in the act slot?**~~ **RULED 2026-09-20 — yes, but the slot is not an
  act slot.** `GATE_RULINGS_2026-09-20.md` Ruling 6: `PR` and `EP` are **structural
  positions alongside** `A1`–`A3`, not additional acts. All nine books have exactly three
  acts and **27 remains the cap**, because a prologue is not an act. `SID_format` and
  `milestone_grid.target_act_values` both carry `PR` and `EP`; the five `EP` milestone
  rows validate as ordinary rows and their notices are gone. Ledger §55, §56.

  This settles it without needing the export asymmetry resolved: the prologue sits inside
  ACT I in the export layer while the epilogues sit outside the acts, and under Ruling 6
  **both simply get a position**. The two follow-ups below ride on, and survive, the
  ruling. Source evidence recorded 2026-09-20 (ledger §56 §4) bears on the second: the
  `EP` rows cite `E20`, `E20` and `E21` as Notion provenance in their `notes`, suggesting
  epilogue numbering **continues** the book's sequence rather than restarting — which
  agrees with §3 above. `target_episode_or_range` is empty on all five, so that is source
  evidence, not a populated field, and **it is not ruled**.

  What follows is the pre-ruling record. The act-count half of this question is
  **ruled 2026-09-19: Book 9 has three acts**, Act IV "Afterlight" is the epilogue
  written as an act, `A{1-3}` and the 27-Act Macro Structure stand unchanged (ledger
  §25). What remains is where the epilogue lives. The recovered epilogue shells use
  `S1.T1.B3.EP.E01`, with `EP` in the act slot and numbering restarting at `E01`;
  §3 above rules that epilogues take the next sequential episode number. Both readings
  satisfy a three-act Book 9. Three options at
  `recovery/VEIL_STRUCTURE_2026-09-19.md` part 4 §3; A supersedes the `E00` prologue
  ruling too. **Source evidence found 2026-09-19 favours B, not the recommended A:** the
  export layer is asymmetric — the prologue sits as beat 1 *inside* ACT I, while both
  recovered epilogues (Book 3, Book 9) are units *outside* the acts with numbering
  restarting at `EP 01`. The exports also record this exact question being put to the
  author during Book 1 construction and **never answered**. Ledger §27.7. **Still blocks the milestone load**, five of whose rows use
  `target_act: EP`. Two follow-ups ride on it: whether Book 9's epilogue is three or
  four episodes, and whether epilogue episodes restart at `E01`. Ledger §24 and §25.
- **Which Veil draft is canon.** Still open, but **narrowed 2026-09-19** by the parallel
  narrative-recovery session — ledger §26.9. Of the four sub-questions:
  - *Does Baz die in Book 3?* **Ruled** — end of B03; the cast learns at the start of
    B04. `recovery/BAZ_DEATH_TIMING_RULING_2026-09-19.md`.
  - *Do Tahl and Caro appear in Books 1–2?* **Ruled for Tahl** — not a primary
    character in B01–B03, and may not be named before the B03 epilogue.
    `proposals/concord-2026/B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md`. **Caro is
    not addressed and stays open.**
  - *Does the Caro–Elisabet romance exist in Veil?* **High-confidence recovered, not
    ruled** — "Veil seeds attraction",
    `proposals/concord-2026/ROMANCE_RELATIONSHIP_RECONCILIATION_2026-09-19.md` §2,
    which is marked NON-CANONICAL. Needs promotion.
  - *Does Veil point at Santa Fe?* **Untouched.**

  **There is a third draft, found 2026-09-19.** The three `ACT * SUMMARY — VEIL I` Notion
  pages put **the Warehouse Incident and Baz's death in Book 1**, not Book 3, and stage
  Tahl heavily there ("Tahl, Threadnaut", "Tahl's First Threshold"). Notion's own
  last-edited stamps put them at 20:18–20:24 on 2025-11-23 against the Book 1 Final Beat
  Bible at 22:17 the same day, and the Final Beat Bible says the Baz bond is "setting up
  Book 3 tragedy". Evidence and the author's ruling both favour the later artifact, but
  **declaring those pages superseded is an author call.** Ledger §27.6.

  Migrating any Veil act overlay still writes one of three stories into canon on the parts
  that remain. `recovery/VEIL_STRUCTURE_2026-09-19.md` part 1.
- **Four author locks live only in proposal documents**, unmigrated and unqueued: the Baz
  death timing, the `Bastien "Baz" Arnaud` identity name, Tahl's B01–B03 absence, and the
  **VT contact escalation ladder** `B01 NOTICE → B02 BRUSH → B03 PUNCTURE → B04–05
  EDGE/RECURRENCE → B06 SLIP → LOOM ECHO`. The ladder has **no field anywhere in the
  schema** and retires the wording of three existing artifacts, including the
  `S1.T1.B03.A3.E14` band exception in `act_overlays/act_overlay_S1_T1_B03_A3.json`. Its
  own source says not to touch Tier-1 rules until the recovery phase ends, so it is held.
  Ledger §26.6.
- **The Book 9 epilogue — timeskip, and whether the `MT`→`LT` rename completes there.**
  Open. The *length* question is no longer the hard part: Notion's `ACT IV — Afterlight`
  and its separate `Book 9 Epilogue — "Luminous Thread"` page carry **the same events**,
  once as character codas and once as a staged scene, and Act IV's own function line says
  it "positions the epilogue". So Act IV is the epilogue written as an act, corroborating
  §25 from the primary source — and **zero of the 22 exports contain an "ACT IV"** at all.
  What is genuinely unresolved:
  - **Timeskip** — Notion says 6–12 months, the export says "THREE DAYS AFTER",
    `B09_ENDGAME` §11 adds 1–2 years and says not to lock it.
  - **Does the rename complete here?** Notion says *MT becomes LT* and calls Kade's post
    the first `LT` entry; the export has him write the first post-Mending **`MT`** message
    with `LT` only hinted by a handshake invitation. **Rule this with the held
    Post-Mending era file and the three-referent `LT` problem, not separately** — it
    decides whether `LT` exists as a channel at the end of Book 9.

  Ledger §27.3.
- **Do the ND decision ledgers need a supersession field?** Open. `ND-032` is classified
  `SUPERSEDED` and protects the Kade→Elias sequence; a later document from the same
  session reverses it to Kade→Rex on eight sources plus an author ruling, and ND-032
  carries no mark. The ND labels describe how current authority treats a *source*, not how
  a later pass treats an earlier *finding*, so corrections accumulate in new files while
  the superseded entries keep reading as current. Ledger §26.12.
- **E19 and beyond.** E19 is named but never built. Do not generate, draft, or outline
  it. The prohibition stands until James lifts it.

Findings are observational. When two sources conflict, write down what each one says
and ask; do not pick a winner. That rule binds this document too: where an earlier
version of this file overruled a repository artifact, §6 now records both readings
instead.

### 4.1 The controlled-vocabulary collision — RESOLVED 2026-09-18

The collision recorded here is settled by `recovery/CANON_DECISIONS_2026-09-18.md` §1
and §3. Kept for the resolution, because migration still has to apply it.

| Token | Was recorded as | Ruling |
| --- | --- | --- |
| `STRAIN` (17) | missing `res_states` member | **Not a state.** Mechanica §33 stands. Strain remains canon as a *signal* (`COLOR_SEMANTICS.md`, Mechanica §51) and as the new `LOAD` axis, §1.1 and §1.4 |
| `EDGE` (1) | missing `res_states` member | **Not a state.** `SHARD-EDGE` is an oversimplification, not an endorsed form. Nuance moves to `Notes`, §1.2 |
| `BRUSH` (1) | missing `res_states` member | **Not a state.** `VT-BRUSH` refers to the VeilThread channel; the operative token is `VT`, §1.2 |
| `LORE` (5) | missing `modes` member | **Not a mode — a `supplement_type`**, §3.1 |
| `POL` (1) | missing `modes` member | **Not a mode — a `supplement_type`**, §3.1 |

The root cause was a missing axis, not a missing vocabulary. `LORE` and `POL` drifted
into `MODE` because there was no supplement-type column to hold them, and `STRAIN`
became a pseudo-state because nothing carried emotional load.

**ECID fields hold a single value** (§1.3). Arrow forms such as `CALM → STRAIN` are
redundant with the sequence: a field's value is inherently a transition from the
previous ECID. Store the state the episode ends in; movement is recoverable by reading
the previous episode.

**The migration mapping for all 25 recovered values is in §1.5 of the decisions
document.** Apply it exactly, and **preserve the original string in `Notes` on every
packet** — the mapping must stay auditable and reversible.

One reopening condition, stated in §1.1: the line-by-line memory chat review may revise
Mechanica, at which point `STRAIN` reopens.

---

## 5. Source tiers

One scheme only. `recovery/RECOVERY_LEDGER_2026.md` defines it:

| Tier | Meaning |
| --- | --- |
| A | Explicit locked source canon |
| B | Explicitly approved development outputs |
| C | Existing GitHub canon |
| D | Other sources — Notion, assistant-generated drafts, anything else recovered |
| E | Memory |

Ruled 2026-09-18 (`recovery/CANON_DECISIONS_2026-09-18.md` §5.1). Tier D widened from
"assistant-generated but unapproved" to cover all other sources, Notion included.
Notion-only facts stay `RECOVERED PRIOR CANON` until re-approved (§5.4).

A second, conflicting lettering exists in
`recovery/checkpoints/RECOVERY_STATE_CHECKPOINT_2026-09-15.md` (lines 16–18), where D
is "earlier Notion", E is "assistant-generated", and F is "memory". That file is the
only place it survives, and it is on the unmerged proposal branch.
**That scheme is retired and converts wherever found.** When converting it, rewrite to the
table above, note the conversion in the commit message, and record it in the ledger —
commit messages alone are too easy to lose.

---

## 6. Known state, as of 2026-09-17

> Verify with `git` before trusting this section; it dates quickly.

> **SUPERSEDED 2026-09-19 — the merge is done.** `main` was fast-forwarded
> `253fdf4 → 9e2f345` on James's instruction (authority: decisions §6.1). All 47 changes
> were additions; nothing on `main` was modified or deleted. The proposal branch ref is
> retained. **Work-queue item 1 is closed.** Ledger §32.
>
> Everything listed below is now **on `main`**. The list is kept as the record of what the
> merge brought over.

**The recovery work was not on `main`. It was on the branch
`proposal/concord-2026-reconciliation`, unmerged until 2026-09-19.**

That branch held, and `main` did not:

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

~~Check out that branch before concluding anything is missing.~~ No longer necessary —
`main` carries all of it as of 2026-09-19.

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

**Act I recovery status — RULED 2026-09-18.**

`recovery/CANON_DECISIONS_2026-09-18.md` §5.5 settles it:

- **Full beat text for E00–E18 exists**, in the unabridged source conversations.
- **E00–E15 are unexported and unmigrated.** The repository holds packets for E16–E18
  only, in `Story Development - Episode expansion process__part01/02.html`.

So "recovered complete" in `BOOK1_EPISODE_RECOVERY_STATE_2026-09-15.md` and in
`RECOVERY_LEDGER_2026.md` §5 referred to material that **exists but is not exported**.
The earlier reading recorded here — that it meant the title list — is superseded. The
distinction that matters for planning is *exported*, not *exists*: the beat text is
real, and work-queue item 7 targets `Archive Veil Book 1` because that is where it
lives.

The file-level evidence is unchanged and still correct: no packet body for E00–E15
appears in any export on either branch. That was a fact about the exports, not about
whether the material exists.

**E19 unlocks after the line-by-line chat review, organization and distillation**
(§6.5) — not after E01–E15 migration alone. Until then it is named only, never built.
Prohibited — see §4.

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

> **Read §8.0 first.** The numbered queue below is recovery-ordered. James redirected
> priorities on 2026-09-19 to the build pipeline, and §8.0 is how the two relate.

### 8.0 Build priorities — the pipeline this all serves

Ruled 2026-09-19: *extract the best versions of rules, context, characters, environments
and narrative → organize them → build a saga timeline with arcs and milestones → cascade
to trilogy, book, act, episode.*

Assessment at `proposals/concord-2026/NARRATIVE_BUILD_PRIORITIES_2026-09-19.md`;
ledger §28. The three findings that change how the queue below should be read:

- ~~The cascade has containers at every level except its root.~~ **Root created
  2026-09-20**: `rules/saga_context_S1.json`, alongside the trilogy contexts. Nine fields
  filled from ruled or recorded material — the 27-act structure, the trilogy split, the
  Jazz Framework axes, the POV baton, five global invariants, the 36-milestone grid, and
  the Mending era boundary. **Seven left `TODO`, each stating why**, including
  `saga_timeline` itself: the milestone *set* exists, the *arc structure over it* does
  not. Ledger §44.

  Still true below it: `book_context`'s `entry_state` / `exit_state_locks` /
  `locations_in_play` / `continuity_hooks` / `pov_targets` **are** the book-level timeline
  and are `TODO` in all nine books. They are the author's to fill.

  **They were never the 27 violations.** Corrected 2026-09-20; the earlier version of this
  bullet said they were. `book_context/` held **90** `TODO` strings across ten fields and
  the validator counted **27** of them — exactly the three `escalation_permissions`
  scalars per book. The five timeline fields above, and `title`, are unchecked:
  `CHK_VOCAB` fires only on keys listed in `JSON_KEY_VOCAB` (`tools/validate_canon.py`),
  and those six are not among them. Ledger §52.

  **The 27 are now filled and canon-scope is 0** — ruled 2026-09-20: *"min max works for
  me"* and *"the 27 violations should be derived from narrative and milestones, not
  dictated by author."* The book layer moved to the act's `{min, max}` shape and every
  value is a rollup of the three acts beneath it. Ledger §53.

  **The book layer is now derived, 2026-09-20.** `TODO` placeholders fall **63 → 20**.
  `continuity_hooks` and `exit_state_locks` come from the milestone grid's 33 cross-book
  dependencies (§59); `entry_state` for B02–B09 is the preceding book's exit (§60);
  `locations_in_play` carries the provisional type layer (§61); `pov_targets.rotation` is
  derived from the baton pass as an **initial proposal** (§62).

  **What stays authored: 20 strings.** `title` 9, `pov_targets.weights` 9, and B01's
  `entry_state` 2 — B01 opens the saga, so nothing precedes it to derive from. The
  projected figure was 19; it is 20 because an `entry_state` block holds two strings, the
  same miscount that made this bullet's residue read 54 before §53. Ledger §59 §4.

  **Two gaps are flagged, not filled.** Per-character entry state needs a character-arc
  layer that does not exist (§60 §2), and a per-book location roster needs a source that
  does not exist (§61 §2). Both fields say so in themselves rather than in a note beside
  them. **A clean validation report is still not a populated book layer.**
- **The first grid is populated.** `grids/milestones_payoffs.csv` holds **36 rows, all
  `proposed`** (ledger §41), checked by six `CHK_GRID_*` checks.

  **Pressure is thread-scoped, 2026-09-20** — ruled *"World pressure should not effect
  romance."* `pressure_before`/`pressure_after` became
  `thread_pressure_before`/`thread_pressure_after`, and a **`thread`** column was added
  with a vocabulary reconciled from the two lists on file (§64). Each row's pressure
  measures **its own thread**, which is what §43 found the column already doing
  inconsistently — five rows open *below* the previous row's close, impossible on one
  world scale.

  **The 36 values are still `proposed` and their provenance is mixed**: they were scored
  before the column existed, so some are world readings and some thread readings. The
  rename states intent; it does not certify the values. **17 of 36 threads are derived;
  19 are `UNSCORED`**, which is a vocabulary member, not an empty cell —
  `CHK_GRID_THREAD` makes an empty thread a violation.

  **The scale is deliberately flexible** (`milestone_grid.pressure_scale`): five levels by
  default, **calibrated per trilogy**, levels extensible, no fixed ceiling. Only T2 is
  compressed. **T3 descends** — it opens at its maximum and ends at its minimum — so any
  anchoring must define 1 as a trilogy's *minimum* and 5 as its *maximum*, never as
  "opening" and "peak".

  **Two grids, two quantities** (`grid_purposes`): this grid holds narrative pressure per
  thread; `grids/reader_pressure.csv` holds reader-facing intensity per cohort. Score a
  quantity in exactly one of them.

  **The `channel` column stays as it is.** 13 rows carry `MT`/`VT`/`LT`, 23 are empty.
  Backfilling `NONE` is **deferred** — ruled 2026-09-20 that narrative and milestones must
  develop first and will change it. §64 §6.

  The five `target_act: EP` rows validate as ordinary rows since Ruling 6; their notices
  are gone.
- **Three layers are missing from the repository — but not from the project.** Corrected
  2026-09-19 after a source review (ledger §29,
  `proposals/concord-2026/LOCATIONS_COMBAT_ANTAGONISTS_PRIMER_REVIEW_2026-09-19.md`):
  - **Locations** — a full CANON system exists in Notion,
    `HYBRID RESONANCE GEOGRAPHY SYSTEM` (Veil shards → Neon Zones → Loom Corridors →
    Echo Nodes), plus New Orleans and Reykjavík city bibles. It **already separates
    narrative locations from character interaction** (§V vs §VIII). Recovery, not design.
    **Blocked on the new `Corridor` token collision** — see §4.
  - **Combat** — a full CANON system exists in Notion (Conflict Engine v1.0, Combat Skill
    Trees, Opponent Archetypes, two Bentos, a Conflict Ladder). The `Phase 1A` export
    settles its shape: combat is **a mode of UARS expression, not a separate axis**, and
    Mechanica §57 already implements the scene-type half. **No new schema needed.**
  - **Antagonist arcs** — the template and the curves both already exist. Five antagonists
    carry full protagonist treatment and three carry a fifth `Backstory` file no
    protagonist has; the `Concord/` and `filaments/` faction directories are the group
    template, with `EraFunction` as the pressure-curve field. Ruled 2026-09-19: primary
    antagonists get protagonist treatment, groups get a pressure-curve model.

  Still genuinely unstructured: character arcs, POV allocation, chronology, motif binding.
  **And Seraphine — the lead — has no `EBCI` file**, the only main character without one.
- **Recovery passes 1–3 are done** (2026-09-19, ledger §30). All three layers are recovered
  into `recovery/LOCATIONS_RECOVERY_`, `COMBAT_CONFLICT_RECOVERY_` and
  `ANTAGONIST_ARCHITECTURE_RECOVERY_2026-09-19.md`. **Nothing is migrated**, and two
  blockers stop the locations layer: the **three-way location taxonomy conflict** (which
  also blocks deriving an `ENV` vocabulary) and the **four-way `Corridor` collision**. A
  third finding stands apart: an **Environmental × Antagonist × Resonance three-pass
  integration was designed and abandoned**, and its three output bibles exist nowhere —
  it is the most concrete "organize" step the sources themselves propose.
- **Only two questions truly gate the cascade**: item 1 below, and *which Veil draft is
  canon*. Most of the rest blocks one artifact, not the pipeline.

**Bookkeeping, in proportion.** The authority-lettering and classification-label questions
(ledger §26.4, §26.5) can wait indefinitely. The supersession question is real but
misframed: step 1 says *extract the best versions*, which presupposes we can tell which is
best, and ND-032 proved we currently cannot. The useful question is **what rule decides
which of two conflicting recovered versions wins** — ND-045 proposes a good one, and
ratifying it is the one bookkeeping decision that pays for itself.

**Updated 2026-09-18/19 against `recovery/CANON_DECISIONS_2026-09-18.md`.**

The §4.1 vocabulary collision is ruled, and so is the envelope question — **per-act
bands, applied 2026-09-19** (ledger §18). Items 4, 5 and 5a are **no longer blocked on
the envelope**. What remains: item 1 is ruled (merge, §6.1) but not performed on
`main`, and the Post-Mending era file is held pending the `LT` question.

1. ~~Decide the fate of `proposal/concord-2026-reconciliation`.~~ **DONE 2026-09-19 —
   merged.** Fast-forwarded `253fdf4 → 9e2f345`; 47 additions, 0 modifications, 0
   deletions; branch ref retained. Ledger §32. **This unblocks items 4, 5 and 5a on the
   item-1 count only** — item 4 is still gated by which Veil draft is canon, and 5a by
   the `EP`-slot question. The four content conflicts
   `recovery/PROPOSAL_BRANCH_MERGE_PREP_2026-09-19.md` predicted are now imported and are
   `main`'s to resolve.
2. Correct the Act I overstatement once James rules on §6, plus any one-digit SIDs, the
   duplicate tier scheme, and the empty `ChatGPT - Story Development.html` source file
   (708 bytes, shell only), per §3, §5 and §6
3. Close the missing-source gap in the ledgers, per §6
4. Migrate the Veil Consolidated Beat Bible into `book_context_B01/B02/B03.json` and the
   nine Veil act overlays, following `proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md`
   — **blocked on item 1 only.** The envelope rule is settled: act-level bands are in
   place, so `escalation_permissions` can now be derived. Note the map's instruction
   predates bands and describes book-level ceilings; ledger §18 records the open
   question of whether book contexts derive from their three acts or drop the field
5. Migrate the E16–E18 packets into the canon structure — **blocked on item 1 only.**
   The §1.5 mapping is ready, the validator's self-test confirms every target pair in
   it validates, and all three packets fall inside their act bands (`B01.A1`/`B01.A2`),
   verified 2026-09-19. The `W3` breach that blocked this was `S1.T1.B03.A3.E14`, which
   is item 5a's material and now carries a sanctioned exception
5a. Migrate the Book 3 Act III structural shells — `S1.T1.B3.A3.E01`–`E18`, plus the
   four-episode Veil→Neon epilogue, from the `Saga structural archive` export. This is
   the Book 3 analogue of item 5 and sits downstream of item 4, which sets the act
   envelope these episodes must fit inside. **Blocked on items 1 and 4, on decisions
   item 1 only.** All three earlier blockers are settled: `HEAT` and `FX` are optional
   at shell granularity (ruled 2026-09-19, `ECID_fields_optional`), and §2.2 rules that
   epilogues take the next sequential episode number, so the four Veil→Neon epilogue
   shells renumber into the Book 3 sequence. See `recovery/RECOVERY_LEDGER_2026.md` §15
6. Run the ChatGPT console export in list mode; produce the full workspace inventory.
   **Raised in value 2026-09-19:** until this runs, "not exported" and "does not exist"
   cannot be told apart. The Silence-and-Hope search (§22) is a concrete case where that
   distinction was assumed rather than established — the 21 exports are the archive
   layer, not the development layer, as
   `proposals/concord-2026/EXPORT_INVENTORY_AND_MISSING_SOURCE_MAP.md` §3 already
   records. **Two concrete targets found 2026-09-19** (§23): `Spine Architect chat`,
   named as the owner of saga-wide continuity storage, and `Saga Visual Bible
   Framework`. Neither is among the 21 exports. Sanitization stripped every
   conversation ID, so the exports cannot be mined for more
7. Extract remaining Tier 1 conversations, `Archive Veil Book 1` first — this is where
   the E00–E15 packets are expected to be. **Confirmed still necessary 2026-09-19:** the
   Notion `BOOK 1 — VEIL I (Final Beat Bible)` was read and does **not** hold them. It
   carries 15 act-level macro beats, not episode packets, with zero title overlap.
   Decisions §9's hypothesis is disconfirmed for Book 1. Ledger §21. **The three
   `ACT * SUMMARY — VEIL I` pages have now been read too (2026-09-19) and hold no packets
   either** — 7, 8 and 9 *clusters*, with Act I stating "No fixed episode count at this
   stage" and Act II "Episode counts will naturally emerge from cluster expansion during
   drafting". The Notion Book 1 layer is confirmed macro-only four times over, so
   `Archive Veil Book 1` is the only remaining candidate and further Notion searching for
   Book 1 episode material is low-value. Ledger §27.5
8. Migrate E01–E15 packets
9. Resolve the `canon/` vs `source_canon/` authority conflict (§1.1) and the Mechanica
   provenance question
9b. **Recover Silence and Hope — Tier-1 gap.** `canon/characters/` holds 62 files across
   14 characters and **neither Silence nor Hope appears in any of them**, nor in
   `source_canon/`. Two metaphysical entities who are each half of the Old Veil, whose
   existence defines `VT`, and whose break drives the endgame, have no canon file.
   **Notion is the only located source**: it holds both `08.10 • Silence — Metaphysical`
   and `08.11 • Hope — Metaphysical`. The 21 exports were searched 2026-09-19 and hold
   essentially nothing — 3 entity references, all the retired prologue title
   `Silence & Hope`; the other 10 `Silence` hits are Lucien's arc vocabulary, a
   different concept. Recommended as a Tier-1 recovery item; **awaiting confirmation**
   (ruling §7 question 2). Ledger §20 and §22
9a. **Deferred until recovery and distillation complete** (ruled 2026-09-19): author the
   ~40 `Asks`/`Flags`/`Protects` fields in `canon/editorial_lenses.md`. Not recoverable
   — decisions §5.6 confirms they were invented repo-side and are not in Notion. Do not
   fill them before then, and never by inference from the board members' published work
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

Flagged, not yet ruled on. Do not silently fix these while doing other work.

**Each is now scoped in full — files, occurrence counts and proposed fixes — in
`recovery/RECOVERY_LEDGER_2026.md` §16.** Read the relevant entry before touching any
file it names. No fix has been applied; two of the five need a ruling before one can be.

- **Faction name drift — `Technarc` is canonical, and it keeps coming back.** Ruled
  2026-09-19, decisions §6.4. Ledger §16.1 records the original pass.

  **This defect has now been corrected FOUR times** (`a83f78d`, `6ba4de9`, `5475b4c`,
  2026-09-20 §63) and re-entered three times. The count in this bullet was wrong before
  2026-09-20: it claimed *"0 `Technarch` outside `CLAUDE.md` and `recovery/`"*, and the
  real figure was **80** — 68 in `proposals/`, 12 in `canon/`.

  **Two distinct re-entry routes, both now understood:**
  1. **The proposal-branch fast-forward** (§32) landed *after* the correction passes and
     re-imported 68 uncorrected occurrences. A merge does not inherit a sweep.
  2. **The character migration** (§45–§51) copied the manifest's heading
     `5. TECHNARCH / REX ECOSYSTEM` verbatim into `manifest_section`, putting 12 into
     **canon scope** — the worst of the three re-entries, and self-inflicted.

  **Expect it again.** Any merge from a branch cut before a naming ruling, and any
  migration that copies a heading verbatim, reintroduces it. **The validator cannot catch
  this** — it is a spelling question, not a format violation. Check with
  `grep -ro 'Technarch' canon/ rules/ grids/` after any merge or bulk migration.

  **Current state, 2026-09-20:** `canon/` **0**, `rules/` **0**, `grids/` **1**,
  `proposals/` **6**. Every remaining occurrence is a **quotation of a source** and is
  annotated as such — `Technarch Directorate lineage`, `Technarch Hardliners`, the
  `Silver Static around Technarch towers` source-reads note, and the annotations
  themselves, which name the retired spelling in order to explain it. Ledger §63.
- ~~**Trilogy envelopes contradict the escalation model.**~~ **RESOLVED 2026-09-20 —
  the trilogy layer is now derived too, and the contradiction dissolved rather than being
  adjudicated.** The trilogy scalars were **skeleton defaults**, not author-set ceilings:
  all three files carried identical `W3`/`U5` beside an unfilled `TODO` reading *"Populate
  trilogy-specific ceilings and exceptions"*. So there were never two authored layers
  disagreeing — one was filled and one still held its placeholder. `environment_envelope`
  now carries bands rolled up from the nine books, the 13 breach notices cleared **by
  construction**, and `fx` is no longer checked as a ceiling because
  `default_vfx_ceiling` is a **default**. Ledger §57. The reopening text below is kept as
  the record of what was found, including what it got wrong:

  **Reopened 2026-09-20, then closed the same day.** The
  2026-09-19 entry below marked this resolved. It was not: the per-act bands were *added*
  and the trilogy scalars were never reconciled to them. Deriving the book layer put both
  in one cascade and exposed **13 axis-breaches across six of the nine books**. All three
  trilogies carry the same `weather_max: W3` / `corridor_max: U5`, while T2's and T3's
  acts want `U6`/`W4`. T1 is consistent; T2 and T3 are not. Ledger §53 §2. Deriving the
  trilogy ceilings the way the books were derived is the consistent reading of the
  2026-09-20 ruling, and T1's own `default_vfx_ceiling_note` is precedent for the ceiling
  being the error — but that is a **wider act than the ruling authorized, so it is an open
  author question**, reported by the validator as notices. What follows is the 2026-09-19
  record, still accurate about the act layer:

  **Per-act bands, 2026-09-19.** All 27 act overlays now carry `escalation_permissions` with
  `corridor`/`weather`/`fx` min-max bands, an `exceptions` list, and a `basis` field
  marking each block `observed` or `inferred`. Veil's FX ceiling rose to `FX2` — the
  recovered E16 packet was right and the ceiling was wrong. `S1.T1.B03.A3.E14`'s `W4`
  is a sanctioned exception. `CHK_BANDS` validates band coherence without
  second-guessing the values. Ledger §18; source at
  `proposals/concord-2026/ENVELOPE_INTERIM_VALUES_V2_2026-09-19.md`. **24 of the 27
  bands are inferred placeholders** — corrected 2026-09-20 from 18; only `B01.A1`,
  `B01.A2` and `B03.A3` carry `basis: observed`. The Post-Mending file is held — see §4.
- ~~**`Veil-Touch` vs `VeilThread`**~~ **Resolved 2026-09-19 — VeilThread.** All four
  `rules/` occurrences corrected, two of them in Mechanica. The three character cards
  needed no change: they had preserved the original while the rules files drifted.
  Ledger §16.6 and §20.
- **Five of the seven grid CSVs are header-only**, so `CHK_BREADCRUMBS` and
  `CHK_EMO_CIRCUIT` in `rules/validation_checks.json` still cannot run against any data.
  Corrected 2026-09-20 from "all six", which is wrong twice over — there are seven grids
  now, and two carry data: `milestones_payoffs.csv` (36 rows, ledger §41) and
  `locations_registry.csv` (31 places, new — ledger §61). The five empty are
  `breadcrumbs`, `episode_beats`, `reaction_modifiers`, `reader_pressure` and
  `supplement_deployment`.
- **All 27 act overlays are byte-identical** apart from their ID fields, as are all 9
  book contexts, capping `fun`/`slice_of_life`/`wonder` at `LOW` including the Book 9
  climax. **Confirmed unintended** by decisions §6.3: skeleton state, not design. They
  populate through items 4 and 5a; no separate fix is needed.
- ~~**No validation tooling exists.**~~ **Addressed 2026-09-19.** `tools/validate_canon.py`
  now enforces the mechanical layer — SID format including the two-digit book rule, ECID
  field names, and controlled-vocabulary membership for all six dimensions — reading every
  rule from `rules/canon_rules.json` rather than hardcoding it. Run it before any
  migration commit:

  ```sh
  python3 tools/validate_canon.py            # exits non-zero on any violation
  python3 tools/test_validate_canon.py       # 127 self-tests
  ```

  **Canon-scope is 0 and notices are 0 as of 2026-09-20** (all-scope 53), with **127
  self-tests**. Both former notice groups are closed: the 5 `EP` notices by Ruling 6
  (§56), the 13 containment notices by deriving the trilogy layer (§57). Notices are not
  violations and do not affect the exit code; **zero notices is now the meaningful state**,
  because every derived layer agrees with the one above it.

  Three checks guard that: `CHK_ENVELOPE` requires every book context to carry its band
  block, so a deleted or reverted envelope reads as a violation rather than a clean run
  (§54); `CHK_CONTAINMENT` reports a band exceeding its container (§57); and
  `CHK_DECLARED` makes Ruling 5's soft ceiling enforceable — an **undeclared** breach is a
  violation, a **declared** one a notice (§58).

  All-scope rose 35 → 53, entirely from `recovery/`, `proposals/` and this file quoting
  **one-digit book** forms. Those are not new defects: until the act slot became an
  alternation, `S1.T1.B3.EP.E01` did not match the SID finder at all and its bad book
  component went unseen. §3's scope warning already describes the condition. Ledger §56 §2.

  Baseline as of 2026-09-19: 27 violations in the substrate — the three
  `escalation_permissions` scalars in each of the nine book-context skeletons, and nothing
  else. The skeletons' other `TODO` fields are not checked; see §8.0.
  See `reports/README.md`. It does not
  catch the other four defects above — the faction drift is a spelling question and the
  envelope contradiction is a semantic one, and neither is a format violation.
