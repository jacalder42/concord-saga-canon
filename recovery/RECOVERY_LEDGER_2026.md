# Concord Saga Recovery Ledger 2026

Status: RECOVERY / NON-CANONICAL META
Purpose: Record what has been recovered, where it came from, and how authoritative it appears to be before any canon rewrite or normalization.

## Recovery principles

1. Do not overwrite current canon during recovery.
2. Preserve recovered authored beat content as-is before normalization or improvement.
3. Treat explicit FINAL / LOCKED / SINGLE SOURCE OF TRUTH material as highest-authority source unless a demonstrably later user decision supersedes it.
4. Treat approved episode-construction outputs as accepted development canon when the workflow shows archive/confirm/proceed behavior.
5. Treat GitHub TODO/scaffold files as infrastructure, not as contradictory canon.
6. Treat assistant proposals that were never clearly approved as non-canon recovery reference only.
7. Treat memory summaries as navigation aids, not source authority.
8. Record conflicts rather than silently reconciling them.

## Authority tiers

### Tier A — Explicit locked source canon
User-supplied or repository material explicitly marked FINAL, LOCKED, SINGLE SOURCE OF TRUTH, or equivalent.

### Tier B — Explicitly approved development outputs
Material produced in an approval / archive / proceed workflow and not later superseded.

### Tier C — Existing GitHub canon
Developed current repository content. A TODO placeholder does not override richer recovered material that was never migrated.

### Tier D — Assistant-generated but unapproved material
Useful for archaeology only; never silently promoted.

### Tier E — Memory summaries
Useful for locating likely material; never authoritative by themselves.

---

# 1. Saga-level structure

## Saga Continuity Spine v3
Status: PARTIALLY RECOVERED BY COMPONENT / EXACT STANDALONE ARTIFACT NOT FOUND IN CURRENT TWO-CHAT CORPUS

Phase 1A explicitly identifies Saga Continuity Spine v3 as safely preserved in project memory and names these components:
- protagonist baton: Baz -> Tahl -> Kade -> Seraphine -> LT
- trilogy escalation logic
- Book 9 endgame constraints

The same audit separately identifies:
- POV Baton Pass (Saga-level)
- trilogy leads and POV distribution rules
- Loom Books 7-9 Endgame Canon Cards

Interpretation: the conceptual spine is recoverable, but the exact standalone v3 source text has not yet been located in the two saved conversations. Do not fabricate a verbatim `Saga Continuity Spine v3` document from the component summary.

Action: later search additional Story Development chats/files for the original standalone artifact. In the meantime, use the Final Canon nine-book Beat Bible plus developed GitHub character/endgame canon as the stronger narrative evidence.

## Global rules and invariants
Status: PRESENT IN GITHUB
Current repository includes:
- no resurrection
- antagonists human or human-made only
- MT / VT / LT separation
- Resonance Potential equation: RP = Will x Emotion x Intent
- UARS soft-cap information
- controlled vocabulary for corridors, weather, resonance states, modes, heat, FX

Mechanica audit note: a dedicated recovery audit now exists at `recovery/MECHANICA_MIGRATION_AUDIT_2026.md`.

---

# 2. Trilogy and nine-book narrative architecture

## Trilogy Beats / Consolidated Beat Bible
Status: FOUND / FINAL CANON
Source: user-provided Trilogy Beats document recovered from the Phase 1A workflow and reproduced in Episode Expansion conversation.
Scope:
- Veil Books 1-3
- Neon Books 4-6
- Loom Books 7-9
- act-level beat sequences for all nine books

Book titles / recovered labels:
- B01 — Veil: The First Thread
- B02 — Veil: The Second Breath
- B03 — Veil: The Fracture Point
- B04 — Neon: First Fracture
- B05 — Neon: Fracture Patterns
- B06 — Neon: The Breaking (Santa Fe)
- B07 — Loom: The Quiet Front
- B08 — Loom: The Swamp of Alignment
- B09 — Loom: The Mending

Authority note: Episode Expansion conversation states the Veil Trilogy Beat Bibles were fully received, aligned cleanly against stored canon, and showed no drift before Book 1 episode construction began.

Action: preserve as archival canon unchanged before any 2026 editorial review.

---

# 3. Episode Expansion Engine

Status: FOUND / OPERATIONAL SPECIFICATION RECOVERED

Recovered instructions define the episode-construction layer as follows:
- target roughly 1.3-1.8k prose words per episode
- each book roughly 60-80 episodes total
- episode header with SID
- working title and function
- ECID block: POV, ENV, U-Level, Weather, Mode, Heat, FX, Resonance State, Audience
- Pressure Map: environmental, antagonist, internal
- Episode Jazz: Melody, Harmony, Rhythm, Performance, Intent
- 6-12 internal beats
- each beat includes BID, function/purpose, tone/pace, POV guardrails, symbolic motifs, ActionState + UARS cost, VFX ceiling + resonance behavior, relationship rung where applicable, and visible change
- exit condition with aftertaste + continuity hook
- 30/30/30/10 POV distribution across the book
- all resonance expression constrained by established physics-based mechanics

Required canon named in the recovered workflow:
- Veil System v3
- Mechanica v4
- Symbol & Motif System v2
- Voice Systems Bible
- Romance/Emotion System Canon
- Environment & Resonance Topology Bible
- Tech & Comms v2
- Antagonist Architecture Bible
- Character Appearance/Physicality
- Saga Continuity Spine v3
- Trilogy Structural Canons for Books 1-9
- Beat Bibles for Veil / Neon / Loom

Action: preserve this as the historical Episode Expansion Engine. Review for 2026 simplification only after recovery is complete.

---

# 4. Content ID system

Status: PRESENT IN GITHUB + RECOVERED IN WORKFLOW REFERENCES

Current GitHub interpretation:
- SID format: S1.T{1-3}.B{01-09}.A{1-3}.E{01-99}
- ECID fields: POV, ENV, CORRIDOR, WEATHER, MODE, HEAT, FX, RES
- BID format: {SID}-B{BeatNumber}

Recovered Book 1 episode material uses this pattern directly, for example:
- S1.T1.B1.A1.E01
- S1.T1.B1.A1.E01-B01

Phase 1A separately confirms that the `CONCORD CONTENT ID SYSTEM (SID / ECID / BID)` and compressed Episode + Scene Workflow Stack were considered safely retained as rules/constraints, while exact reusable operational templates were not necessarily retained.

Current assessment: no evidence in the two saved chats proves that SID/ECID/BID semantics were later renamed. Preserve existing meanings unless a later primary artifact demonstrates supersession.

**Superseded 2026-09-18 for the BID form.** `recovery/CANON_DECISIONS_2026-09-18.md`
§2.3 rules beat IDs to `{SID}-BT{BeatNumber}`. The `{SID}-B{BeatNumber}` form recorded
above is the recovered historical form and converts on migration. See §14.

---

# 5. Book 1 recovery status

## Book 1 Act I
Status: FULLY EPISODE-EXPANDED THROUGH E16

Recovered structure includes:
- E00 Prologue — The Conversation in the Sky
- E01 — The Sick Child
- E02 — Too Late
- E03 — The First Echo
- E04 — A Line Out of Place
- E05 — The Misalignment
- E06 — Crowd on Edge
- E07 — Instability in the Square
- E08 — Whispers of the Filament
- E09 — Rootkeeper's Glance
- E10 — Seraphine Strains
- E11 — Lucien Unravels
- E12 — The Dual Collapse
- E13 — A Pulse Over Jackson Square
- E14 — Lines Breaking Apart
- E15 — Baz, We Need You
- E16 — Everything Curves Southwest

E16 is explicitly labeled the ACT I CLOSE in the Episode Expansion conversation, followed by the statement that Book 1 Act I is fully complete.

Important version note:
- an earlier exported Book1 Act1 Beats document ends at E15 and describes E15 as the Act I finale
- the later Episode Expansion conversation extends Act I with E16 and explicitly closes the act there

Current recommendation: treat E16 as the later accepted Act I close; retain the earlier E15-only artifact unchanged in source archive for provenance.

## Book 1 Act II
Status: PARTIAL EPISODE EXPANSION / STOPPING POINT NOW VERIFIED

Recovered:
- E17 — Baz arrives / Act II opening — completed
- E18 — Context Sharpens — completed

The saved Episode Expansion conversation ends its recoverable construction sequence by instructing that E18 be archived and announcing the next episode as:
- E19 — Act II: Spike in the Neighborhood (Part I)

Targeted searches for `END EPISODE 19`, `Episode 19 archived`, `Episode 20`, and the E19 beat block returned no completed E19 artifact. The strongest available evidence therefore supports:

**Historical stopping point: E18 completed; E19 named but not constructed in this conversation.**

This is now stronger than a provisional assumption, though a separate Book 1 Beat Backup chat could still contain material not present in the two exported chats.

Action: do not resume E19 until the Book 1 Beat Backup chat is checked if it can be recovered. If that backup contains only E00-E18, E19 is the clean resumption point.

---

# 6. Book 2-9 episode-expansion status

Status: MACRO BEATS FOUND / EPISODE-LEVEL EXPANSION NOT VERIFIED

All nine books have act-level macro beats in the consolidated Trilogy Beats artifact.
No current recovered evidence proves full episode expansion for Books 2-9.

Action: search old Episode Expansion / backup conversations before assuming these levels were never built.

---

# 7. Mechanica / Resonance migration

Status: SUBSTANTIAL MIGRATION CONFIRMED

Phase 1A contains a component-level inventory of authoritative Mechanica/Resonance material. GitHub contains `rules/Mechanica-v4.md`, labeled:
- `Mechanica v4 (Memory Edition)`
- `Status: Authoritative Canon`
- `Source: Project Memory (inflated)`
- `Phase: 1A Migration`

The current file strongly matches major Phase 1A requirements including:
- authority/supersession
- resonance as emotional physics
- MT/VT/LT separation and no digital resonance transmission
- Veil/Neon/Loom/Post-Mending escalation
- hard constraints
- RP equation
- ~20% nonlinear boost threshold
- UARS and ActionStates
- boost taxonomy/costs/stacking/failure modes
- environmental conductivity/material behavior
- crowd physics and tech interference
- U1-U7 corridors
- W0-W4 resonance weather
- resonance states and shard progression
- containment/stabilization
- MT/VT/LT mechanics
- ascension/manufactured-meta constraints

Not yet proven complete relative to the Phase 1A checklist:
- explicit consequence ladder
- recovery/aftercare/reset rules
- exact event-trigger ladder
- explicit danger-window rules
- dedicated aftermath behavior rules
- exact VFX ceiling / symbol-action permission tables

See `recovery/MECHANICA_MIGRATION_AUDIT_2026.md` for the detailed non-canon audit.

Interpretation: Mechanica should be audited/provenanced, not redesigned.

---

# 8. Operational artifacts at risk

Status: IDENTIFIED AS PARTIAL / LOGIC-ONLY IN PHASE 1A

Phase 1A explicitly flagged the following as operational danger-zone artifacts whose logic was remembered but exact working versions might not be preserved:
- Veil episode template
- Episode -> Beat -> Scene pipeline
- Beat Architecture prompt
- Narrative Structure prompt
- Saga Beat Expansion Pipeline
- Trilogy Act-Level Beat Backup

Related preserved concepts listed in that audit include:
- CONCORD CONTENT ID SYSTEM (SID / ECID / BID)
- Episode + Scene Workflow Stack (compressed rules)
- beat-level requirements
- Fun Layer / F beats
- Mobius Audit System
- Breadcrumb pass concept
- Symbolic Action Engine (compressed)

Action: recover exact artifact text where available before inventing replacements.

---

# 9. Historical migration directive

Status: FOUND / SHOULD BE HONORED

Phase 1A explicitly instructed that before new system writing, the following should be archived as-is:
- Trilogy / Book beats for all nine books
- Book 1 Act 1 act-level beats

With:
- no edits
- no normalization
- no improvements
- just protection

Action: preserve recovered originals in a source-archive layer before normalization or 2026 revision.

---

# 10. Current repository-state interpretation

The repository is strongest in:
- rules / invariants
- character canon
- Mechanica / resonance concepts
- factions / supporting canon
- schema and templates

The repository is incomplete in:
- fully human-readable saga story spine
- trilogy narrative summaries at the top-level canon files
- book narrative spines
- populated act overlays
- populated episode beat grids
- migrated Book 1 episode expansions

Interpretation: the project stalled during canon migration / artifact persistence, not because the narrative architecture was undeveloped.

---

# 11. Immediate next steps

1. Preserve the original Trilogy Beats and Book1 Act1 Beats content in a source-archive location without edits.
2. Recover/check the separate Book 1 Beat Backup chat if available; verify whether it ends at E18.
3. Search additional Story Development chats/files for the exact standalone Saga Continuity Spine v3 rather than reconstructing it from memory summary.
4. Continue provenance recovery for the six not-yet-proven Mechanica components identified in the Mechanica audit.
5. Recover exact operational workflow artifacts where possible.
6. Only after recovery, create proposed current-state narrative files (Saga / Trilogy / Book / Episode) in a proposal layer.
7. Have a second model/reviewer inspect proposed migrations against existing canon before promotion.

---

# 12. Do-not-do list during recovery

- Do not rewrite the nine-book beat architecture from scratch.
- Do not normalize recovered beat wording before archiving originals.
- Do not fill missing episodes from memory.
- Do not treat TODO repository scaffolds as stronger than recovered final canon.
- Do not collapse MT / VT / LT boundaries.
- Do not silently reconcile conflicts.
- Do not resume E19 until recovery checks the separate backup chat or establishes it is unavailable.

---

# 13. ECID vocabulary collision

Status: CONFLICT RECORDED / UNRESOLVED / BLOCKS MIGRATION

The recovered episode packets fill ECID fields with tokens the controlled vocabulary in
`rules/canon_rules.json` does not permit: `STRAIN` (17 field values), `LORE` (5), `POL`
(1), `SHARD-EDGE` (1), `VT-BRUSH` (1). Migrating a packet means either writing those
tokens into canon or altering them on the way in, and both are canon acts.

`STRAIN` is the substantive one. It is named as a condition in tier-1 canon
(`canon/characters/SeraphineAppearance.md`, `### Under Strain`) and in the symbol system
(`rules/symbols/COLOR_SEMANTICS.md`, `### YELLOW — Strain / Overload`, "risk: shard
precursors"), but `rules/Mechanica-v4.md` §33 does not list it among the resonance
states. Both readings are recorded; neither is resolved here.

Evidence, counts, provenance and options: `recovery/ECID_VOCABULARY_COLLISION_2026.md`.

Blocks: migration of the Veil beat bible into book contexts and act overlays, and
migration of the E16–E18 packets. Four rulings are needed from the author before either
proceeds; they are listed in §7 of that memo.

---

# 14. Beat ID prefix — RULED 2026-09-18

Status: **RESOLVED.** `BT` adopted. See `recovery/CANON_DECISIONS_2026-09-18.md` §2.3.

The ruling: beat IDs are `{SID}-BT{BeatNumber}`. `rules/canon_rules.json` now carries
that form, applied cleanly without the two non-schema keys the earlier unapproved edit
introduced. The history below is preserved because it records why the change was
reverted once before being made properly.

---

## Original entry (superseded by the ruling above)

Status: PROPOSAL / UNAPPROVED / REVERTED FROM THE REPOSITORY

## What the repository says

`rules/canon_rules.json` defines `"BID_format": "{SID}-B{BeatNumber}"`, giving beat IDs
of the form `S1.T1.B1.A1.E13-B01`. §4 of this ledger records the same form, and the
recovered Book 1 material uses it.

## The problem

The form reuses `B` for two different things: the book number (`B1`) and the beat
number (`-B01`). A parser reading `S1.T1.B1.A1.E13-B01` has to know the position to
know which `B` means what.

## The proposal, and its status

A `BT` prefix — `S1.T1.B01.A1.E13-BT01` — was suggested in a draft working agreement
as the fix. **It was never approved by the author.** On 2026-09-18 that suggestion was
applied to `rules/canon_rules.json` in commit `e395470`, which also introduced two keys
(`BID_format_retired`, `BID_format_note`) that are not part of the file's schema.

That edit has been reverted. `rules/canon_rules.json` is byte-identical to `main`
again, and `CLAUDE.md` §3 now instructs sessions to write beat IDs in the existing
`-B{n}` form until a ruling exists.

## Why this is cheap to decide now

**No beat IDs exist anywhere in the repository.** A repository-wide search for the
pattern returns two hits, both illustrative examples inside prose — `CLAUDE.md` §3 and
§4 of this ledger — and neither is a live identifier. Nothing would need rewriting.

That changes the moment the first episode packet is migrated. The recovered packets
carry beat IDs in the old form (for example `S1.T1.B1.A1.E06-B2` and `-B4` in the
`Narrative Structure` export), so migration will start writing them into the repository.
Deciding before migration costs nothing; deciding after means a second rewrite pass on
top of the one-digit-book conversion already required by `CLAUDE.md` §3.

## Ruling needed — answered

Does the beat prefix stay `B` or become `BT`? **`BT`**, per §2.3 of the decisions
document. `BID_format` and `CLAUDE.md` §3 are updated. §4 of this ledger records the
old form as recovered-material context and is annotated accordingly. Recovered beat IDs
convert during migration.

---

# 15. Book 3 Act III structural shells — unqueued material

Status: RECOVERED / UNMIGRATED / NO QUEUE ITEM UNTIL NOW

## What exists

`Story Development - Saga structural archive` (both parts, proposal branch) holds 22
structural episode blocks that no work-queue item covered:

- **18 shells**, `S1.T1.B3.A3.E01` through `E18` — Book 3, Act III, "The Slip"
- **4 shells**, `S1.T1.B3.EP.E01` through `E04` — the Veil → Neon epilogue

The assistant turn following them records that they were stored "exactly as provided,
with no alteration, no compression", which places them as an archival paste rather than
generated material. See §14 of `recovery/ECID_VOCABULARY_COLLISION_2026.md` on why turn
role alone does not settle authorship.

## These are shells, not packets — the distinction matters

Each block carries 13 fields: `Title`, `Function`, `POV`, `ENV`, `U-Level`, `Weather`,
`Mode`, `Resonance State`, `Intent`, `Continuity In`, `Continuity Out`, `Anchor`,
`Notes`.

The Book 1 E16–E18 material in queue item 5 is a different and heavier artifact: full
packets carrying `Heat`, `FX`, `Audience`, a Pressure Map, Episode Jazz, and 6–12
internal beats with BIDs. Migrating a shell and migrating a packet are not the same
operation and should not share a procedure.

## Three blockers, two of them new

**1. Vocabulary (already recorded).** These shells carry 14 `STRAIN`, 4 `LORE`, 1 `POL`
and 1 `VT-BRUSH` — 20 of the 25 out-of-vocabulary ECID field values in the whole corpus.
Covered by §13 and by the four rulings in `ECID_VOCABULARY_COLLISION_2026.md` §7.

**2. Missing required ECID fields.** `rules/canon_rules.json` lists `ECID_fields` as
`POV, ENV, CORRIDOR, WEATHER, MODE, HEAT, FX, RES`. The shells supply no `Heat` and no
`FX` — zero occurrences across all 22 blocks. Migration therefore either leaves two
required fields empty, invents values, or the schema has to mark them optional at shell
granularity. **Ruling needed.**

**3. The epilogue has no valid act token.** The SID format is
`S1.T{1-3}.B{01-09}.A{1-3}.E{01-99}`. The four epilogue shells use `S1.T1.B3.EP.E01`
form — `EP` where an act must go. An epilogue is not act 1, 2 or 3, and the format has
no slot for it. This is the same class of gap as the `E00` prologue problem in
`CLAUDE.md` §3, and the two are best settled together: both ask whether the SID format
covers material outside the three-act spine. **Ruling needed.**

## Where it sits relative to the Veil migration

Book 3 is a Veil book, so this material is inside the Veil scope, not beside it:

- **Queue item 4** populates the nine Veil act overlays from the Beat Bible at act
  level. One of those nine is `act_overlays/act_overlay_S1_T1_B03_A3.json` — the act
  these shells sit inside.
- **Queue item 5a** (new) populates episode-level structure for that same act.

Item 4 sets the envelope; 5a fills it. Running 5a first would write episode rows with
no act-level ceiling to check them against — and this material contains a known breach:
`S1.T1.B3.A3.E14` carries `Weather: W4 (brief)` while
`rules/trilogy_context_T1_veil.json` caps Veil at `weather_max: W3`. That episode is
also the trilogy's only declared VT contact (`Anchor: FIRST AND ONLY VT BRUSH IN VEIL
TRILOGY`), so it is not a candidate for quiet downgrade to `W3`. The envelope defect
itself is recorded in `CLAUDE.md` §9.1 and expanded in §16 of this ledger.

## Ruling needed

1. Do shells migrate with `HEAT`/`FX` empty, or is the schema amended to make them
   optional at shell granularity?
2. How are epilogue units identified, given `A{1-3}` has no slot for them — and does
   the same answer cover the `E00` prologue?

---

# 16. Known defects register

Status: DOCUMENTED / NOT FIXED / FIXES PROPOSED ONLY

The five defects summarised in `CLAUDE.md` §9.1, with exact scope: which files, how
many occurrences, and what a fix would change. **No fix in this section has been
applied.** Defect 1 is a canon question and is the author's alone. Each entry should be
read before any work that touches the same files.

---

## 16.1 Faction name drift — `Technarc` vs `Technarch`

**This is canon, not spelling. Do not "fix" it.**

### Scope

64 occurrences of `Technarc`, 9 of `Technarch`, excluding `CLAUDE.md` and `recovery/`,
which quote both forms while documenting them.

The faction's own file, `canon/factions/Technarc.md`, titles it
**THE TECHNARC DIRECTORATE** — no `h` — and uses that form throughout.

All 9 variant occurrences:

| File | Line | Context |
| --- | --- | --- |
| `canon/characters/RexID.md` | 42 | "**Technarch pressure point:** asked to certify a system…" |
| `canon/characters/RexID.md` | 60 | "**Neon:** Technarch pressure escalates…" |
| `canon/characters/RexID.md` | 67 | "**Employer naming variance:** Technarch / Technarch Directorate…" |
| `canon/characters/VirelliID.md` | 117 | "Technarch hardliners and early anti-emotion movements reuse his logic" |
| `canon/factions/Dominions.md` | 98 | "Technarch hardliners and early anti-emotion movements reuse Dominion logic" |
| `canon/trilogy_veil.md` | 10 | "TODO: Dominions institutional pressure; early Technarch patterns." |
| `canon/trilogy_neon.md` | 10 | "Technarch hardliners, Choirless emergence, manufactured meta failures." |
| `rules/symbols/GEOMETRY_MOTIFS.md` | 42 | "- Technarch systems" |

### Why this is not a typo sweep

`canon/characters/RexID.md` line 67 sits under the heading
**"XI. Canon Conflict Ledger (Preserved Record)"** and reads:

> **Employer naming variance:** Technarch / Technarch Directorate treated as the same
> institutional pressure source

The variance is therefore **already recorded as a known and tolerated one** in tier-1
character canon, alongside three other deliberately preserved variances (legacy origin
package, geographic arc, engineering field phrasing). A find-and-replace would silently
overwrite a canon ledger entry that exists to preserve exactly this.

There is a second reading. That same line writes `Technarch / Technarch Directorate`
with the `h` on both sides, while the faction file writes `Technarc Directorate`
without. So the ledger entry may itself contain the drift it documents, in which case
it records a variance between two spellings but names only one of them. **Both readings
are recorded; neither wins.**

### Proposed fixes — pick one, none applied

**A. `Technarc` is canonical; the 9 variants are drift.** Correct all 9, and rewrite
`RexID.md` line 67 to name both spellings accurately. Changes 8 files. Risk: if
`Technarch` was ever an intentional in-world variant — a colloquial or hostile form,
say — this erases it.

**B. Both forms are canonical**, as `RexID.md` line 67 can be read to say. Change
nothing in the 8 files; add a naming note to `canon/factions/Technarc.md` recording
that both are in use and what each signifies. Changes 1 file.

**C. `Technarch` is canonical** and the faction file is the outlier. Changes 1 file
plus 64 occurrences. Least likely, listed for completeness.

### Ruling needed

Which spelling is canonical, and does `RexID.md` line 67 mean the variance is
tolerated or that it needs correcting?

---

## 16.2 Trilogy envelopes contradict the escalation model

### Scope

Three files, one field each, plus a second field that is also uniform:

| File | `default_vfx_ceiling` | `weather_max` | `corridor_max` | `allowed_heat_range` |
| --- | --- | --- | --- | --- |
| `rules/trilogy_context_T1_veil.json` | `FX1` | `W3` | `U5` | `H0`–`H4` |
| `rules/trilogy_context_T2_neon.json` | `FX2` | `W3` | `U5` | `H0`–`H4` |
| `rules/trilogy_context_T3_loom.json` | `FX3` | `W3` | `U5` | `H0`–`H4` |

Only the FX ceiling escalates. Weather, corridor and heat are identical across all
three trilogies.

### What it contradicts

`rules/Mechanica-v4.md` §7.3 describes the Loom trilogy as:

> - Systemic collapse
> - Resonance storms dominate
> - Corridor failures widespread
> - Shards shape geography

`Mechanica-v4.md` §25 defines `U6` as "Shard-Laced — fractures present, severe
instability, catastrophic failure likely", and §30 defines `W4` as `Landfall`. Those
are the mechanical terms for what §7.3 describes, and the Loom envelope forbids both.

### Consequence

`U6`, `U7` and `W4` are in the controlled vocabulary at
`rules/canon_rules.json` and are **unreachable in every trilogy**. Three of seven
corridor tiers and one of five weather states can never legally appear.

This also blocks work-queue item 4:
`proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md` instructs that
`escalation_permissions` be "cross-derived from Mechanica v4 + trilogy envelope rules",
and those two sources do not currently agree. And the recovered material already
breaches it — `S1.T1.B3.A3.E14` carries `Weather: W4 (brief)` inside Veil (§15).

### Proposed fixes — none applied

**A. Raise the Loom and Neon ceilings** so escalation is expressed in all three
dimensions, not just FX. Changes 2 files, 4 values. This is the reading `Mechanica-v4.md`
§7.3 supports, but the specific ceilings are a canon judgement — whether Neon reaches
`U6`, whether Veil's `W4` breach at E14 is a sanctioned exception or an error.

**B. Keep the ceilings and treat U6/U7/W4 as out-of-envelope by design**, reachable
only through an explicit per-episode exception mechanism that does not yet exist.
Changes 0 files but requires a new exception field in the schema and a rule for it.

**C. Narrow the controlled vocabulary** to what the envelopes permit. Rejected on its
face — it would delete `U6`, `U7` and `W4` from Mechanica, which §7.3 depends on.

### Ruling needed

Do the Loom and Neon envelopes rise, or does an exception mechanism cover
`S1.T1.B3.A3.E14` and anything like it?

---

## 16.3 All six grids are header-only

### Scope

| File | Data rows | Columns |
| --- | --- | --- |
| `grids/breadcrumbs.csv` | 0 | 9 |
| `grids/episode_beats.csv` | 0 | 17 |
| `grids/milestones_payoffs.csv` | 0 | 16 |
| `grids/reaction_modifiers.csv` | 0 | 9 |
| `grids/reader_pressure.csv` | 0 | 8 |
| `grids/supplement_deployment.csv` | 0 | 9 |

### Consequence

Two of the five checks in `rules/validation_checks.json` cannot run:
`CHK_BREADCRUMBS` ("setups map to payoffs; no orphan hints") has no breadcrumbs to
check, and `CHK_EMO_CIRCUIT` has no pressure data. `pressure_thresholds.notes` in the
same file says "Tune per reader cohort in reader_pressure.csv", which has no cohorts.

The headers themselves are sound — `episode_beats.csv` carries all eight ECID fields
plus `SID` and `BID`, and `tools/validate_canon.py` confirms the ECID block is
complete.

### Proposed fix — none applied

This is not a defect to fix directly. The grids populate as a **consequence** of
work-queue items 4, 5 and 5a: `episode_beats.csv` receives rows when packets migrate.
The others (`breadcrumbs`, `milestones_payoffs`, `reader_pressure`) hold editorial
telemetry that has no recovered source yet identified.

What is worth deciding now: whether `episode_beats.csv` is the migration target for
recovered packets at all, or whether packets land in `act_overlays/` with the grid
derived afterwards. `MIGRATION_MAP` does not say.

---

## 16.4 All act overlays and book contexts are identical templates

### Scope

- **27 of 27** act overlays reduce to a single distinct file shape once `act_id`,
  `book_id` and `trilogy_id` are normalised away.
- **9 of 9** book contexts likewise, normalising `book_id`, `trilogy_id` and `title`.
- **1 distinct** `soft_modulation` setting across all 27 overlays:
  `fun`, `slice_of_life` and `wonder` all `allowed: true`, `max_intensity: LOW`.

That last value is identical in `act_overlay_S1_T1_B01_A1.json`, the saga's opening
act, and `act_overlay_S1_T3_B09_A3.json`, its climax.

### Consequence

The 27 `TODO` placeholders in `escalation_permissions` across the nine book contexts
are the **entire substrate violation count** in
`reports/VALIDATION_BASELINE_2026-09-19.md`. Nothing else in the substrate fails.

### Proposed fix — none applied

`MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md` already reaches the same conclusion
independently — it calls the uniform `LOW` values "template defaults rather than
recovered act-specific canon" and instructs that `escalation_permissions` stay `TODO`
until systems reconciliation completes. That instruction is correct and should be
followed rather than replaced.

So: no fix. These files populate through work-queue items 4 and 5a, and item 4 is
blocked on §16.2.

---

## 16.5 No validation tooling — addressed 2026-09-19

Recorded here for completeness; this one is closed.

`tools/validate_canon.py` now enforces SID format including the two-digit book rule,
ECID field names, and controlled-vocabulary membership across all six dimensions,
reading every rule from `rules/canon_rules.json` rather than hardcoding it.
`tools/test_validate_canon.py` covers it with 27 tests. Baseline reports are under
`reports/`.

It closes the mechanical half only. The five checks named in
`rules/validation_checks.json` — `CHK_HUMANITY`, `CHK_BREADCRUMBS`, `CHK_CHANNELS`,
`CHK_ANTAG`, `CHK_EMO_CIRCUIT` — are editorial judgements about story content and still
need a reader. It also cannot catch §16.1 (a spelling question) or §16.2 (a semantic
one); both use valid tokens throughout.


END RECOVERY LEDGER
