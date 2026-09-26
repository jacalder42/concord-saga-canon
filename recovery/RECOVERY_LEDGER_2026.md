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

### Tier D — Other sources
Material from sources outside the locked/approved/GitHub layers — Notion, assistant-generated
drafts, and anything else recovered. Useful for archaeology; never silently promoted.
Notion-only facts stay `RECOVERED PRIOR CANON` until re-approved (decisions §5.4).

### Tier E — Memory
Memory summaries and project-memory recall. Useful for locating likely material; never
authoritative by themselves.

> **Ruled 2026-09-18** (`recovery/CANON_DECISIONS_2026-09-18.md` §5.1). The scheme is
> A locked source canon · B approved development outputs · C existing GitHub canon ·
> **D other sources** · **E memory**. Tier D widens from "assistant-generated but
> unapproved" to cover all other sources, Notion included. The competing checkpoint
> lettering (D earlier Notion / E assistant-generated / F memory) is **retired and
> converted wherever found** — it survives only in
> `recovery/checkpoints/RECOVERY_STATE_CHECKPOINT_2026-09-15.md` lines 16–18, which is
> on the unmerged proposal branch and converts when that branch lands.

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
Status: **CORRECTED 2026-09-18** — full beat text for E00–E18 EXISTS in the unabridged
source conversations. E00–E15 are UNEXPORTED and UNMIGRATED. The repository holds
packets for E16–E18 only.

> `recovery/CANON_DECISIONS_2026-09-18.md` §5.5 rules what "recovered complete" meant
> in this ledger and in `BOOK1_EPISODE_RECOVERY_STATE`: the material exists, but it is
> not exported. The earlier reading recorded in `CLAUDE.md` §6 — that "recovered
> complete" referred to the title list — is superseded. The distinction that matters
> for planning is **exported**, not **exists**: work-queue item 7 targets
> `Archive Veil Book 1` because that is where the unexported beat text lives.
>
> The superseded status line read: `FULLY EPISODE-EXPANDED THROUGH E16`.

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

**SUPERSEDED 2026-09-22:** This recommendation is retained only as a record of the earlier recovery state. Cross-check against the same-day Trilogy Act-Level Beat Backup and later structural reconciliation establishes the B01 E16 `Everything Curves Southwest` placement as cross-book contamination from B03 Act I. Current B01 v4.1a preserves only subtle unnamed directional breadcrumbs at E4 and E11; the explicit phrase remains B03 material. Retain the old E16 source packet unchanged as provenance, not governing canon.

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

**2. Missing required ECID fields — RULED 2026-09-19: optional at shell granularity.**

The shells supply no `Heat` and no `FX` — zero occurrences across all 22 blocks — while
`ECID_fields` listed both as required. James ruled the third option: the schema marks
them optional rather than migration leaving them empty or inventing values.

Applied as `systems.id_system.ECID_fields_optional: ["HEAT", "FX"]`. The validator now
reports a record omitting them as a **notice**, not a violation, so shells migrate
without failing the build while the omission stays visible in the report.

**The cost, recorded so it is not a surprise.** The checker cannot tell a shell grid
from a full-packet grid — nothing in the schema marks granularity — so a *full packet*
that omitted `HEAT`/`FX` would also pass with only a notice. The softening is scoped to
those two fields and no others: a missing `RES`, `MODE` or `CORRIDOR` is still a
violation, and a test asserts it. If granularity ever needs enforcing, the fix is a
granularity column or a filename convention the checker can read.

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

## Ruling needed — both answered

1. **Answered 2026-09-19: optional.** The schema marks `HEAT` and `FX` optional at
   shell granularity rather than migration leaving them empty or inventing values.
   See blocker 2 above for what was applied and what it costs.
2. **Answered 2026-09-18.** §2.2 rules that the Prologue is `E00` and **epilogues take
   the next sequential episode number**. So `S1.T1.B3.EP.E01`–`E04` renumber into the
   Book 3 sequence rather than needing a new act token, and the SID format needs no
   `EP` slot. The `E00` prologue question is settled by the same ruling, via the
   widened `E{00-99}` range.

---

# 16. Known defects register

Status: DOCUMENTED / NOT FIXED / FIXES PROPOSED ONLY

The five defects summarised in `CLAUDE.md` §9.1, with exact scope: which files, how
many occurrences, and what a fix would change. **No fix in this section has been
applied.** Defect 1 is a canon question and is the author's alone. Each entry should be
read before any work that touches the same files.

---

## 16.1 Faction name drift — RULED AND CORRECTED 2026-09-18/19

Status: **RESOLVED.** `Technarc` is correct. All 9 variants corrected 2026-09-19 per
`recovery/CANON_DECISIONS_2026-09-18.md` §6.4.

### What was applied

`Technarch` → `Technarc`, 9 occurrences across 6 files, exactly the list §6.4 names:

| File | Occurrences |
| --- | --- |
| `canon/characters/RexID.md` | 3 |
| `canon/characters/VirelliID.md` | 1 |
| `canon/trilogy_veil.md` | 1 |
| `canon/trilogy_neon.md` | 1 |
| `canon/factions/Dominions.md` | 1 |
| `rules/symbols/GEOMETRY_MOTIFS.md` | 1 |

Repository-wide count afterwards: 73 `Technarc`, 0 `Technarch`, excluding `CLAUDE.md`
and `recovery/`, which quote the retired spelling as evidence and are left alone
deliberately.

### Second pass, 2026-09-19 — the analysis layer

After the proposal branch merged into the working branch, a further **24** occurrences
came into reach. James ruled: correct them, leave the exports.

| Area | Before | After |
| --- | --- | --- |
| `proposals/concord-2026/` (7 files) | 23 | 0 |
| `recovery/checkpoints/` (1 file) | 1 | 0 |
| `recovery/source_exports/html_sanitized/` (6 files) | 19 | **19 — untouched** |

The exports are not corrected and must not be. They are the sanitized source
conversations — the only copy that exists anywhere, per `CLAUDE.md` §7 — and decisions
§6.1 forbids pruning or altering them in place. A spelling sweep across them would be
exactly that alteration.

So `grep Technarch` will never return zero repository-wide. It now survives in exactly
two deliberate places: the 19 in the exports, and four meta-documents that quote the
retired spelling while recording the ruling against it.

### The one line worth checking

The concern recorded below was `canon/characters/RexID.md` line 67, inside
**"XI. Canon Conflict Ledger (Preserved Record)"**, which read:

> **Employer naming variance:** Technarch / Technarch Directorate treated as the same
> institutional pressure source

It now reads:

> **Employer naming variance:** Technarc / Technarc Directorate treated as the same
> institutional pressure source

**The correction improves this line rather than damaging it.** Before, it named a
variance between two identical spellings, which was incoherent — the entry recorded a
drift it had itself absorbed. After, it reads as short-form (`Technarc`) against
full-form (`Technarc Directorate`), which is a real and meaningful variance and matches
the faction file's own title, **THE TECHNARC DIRECTORATE**.

So the second reading recorded below turned out to be the right one: that ledger entry
did carry the drift it documented. The other three preserved variances in that section
— legacy origin package, geographic arc, engineering field phrasing — are untouched.

---

## Original entry (superseded by the ruling above)

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

### Ruling needed — answered

Which spelling is canonical? **`Technarc`**, per §6.4. And `RexID.md` line 67 was
carrying the drift rather than sanctioning it, so correcting it made the entry
coherent. Option A was taken.

---

## 16.2 Trilogy envelopes contradict the escalation model

> **Ruled 2026-09-18 (§6.2): the identical envelopes are UNINTENDED.** Values should be
> fluid and matched to narrative momentum. **The replacement rule is not yet decided**
> — decisions §8 item 1 offers three shapes: advisory guidance with no enforced ceiling,
> per-act ceilings, or a ceiling tied to a momentum marker. Whatever replaces it must
> admit Veil packet `S1.T1.B3.A3.E14`, which already carries `Weather: W4`.
>
> Of the three options analysed below, **C is now excluded** — narrowing the vocabulary
> would contradict §6.2's finding that the ceilings, not the vocabulary, are wrong.
> This is the blocker on work-queue items 4, 5 and 5a.
>
> **Stated in full at `recovery/ENVELOPE_QUESTION_2026-09-19.md`** (2026-09-19), which
> supersedes the options analysis below. Two findings there change the shape of the
> question: `U7` is Post-Mending rather than an escalation tier, so its unreachability
> is correct and the real gap is a missing Post-Mending envelope; and `allowed_heat_range`
> is flat for a good reason, being the romance ladder rather than an environmental axis.

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

> **Ruled 2026-09-18 (§6.3): not intended — skeleton state, not design.** This confirms
> the reading below and the migration map's independent conclusion. No separate fix;
> they populate through work-queue items 4 and 5a.

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

## 16.6 `Veil-Touch` vs `VeilThread` — RESOLVED 2026-09-19: VeilThread

Status: **RESOLVED.** `recovery/CHANNEL_NAMES_RULING_2026-09-19.md`. All four `rules/`
occurrences corrected; the three character cards needed no change. **My framing of this
defect was wrong in one respect — see §20.** The cards were not the drift; they
preserved the original.

---

### Original entry (framing partly superseded)

Four occurrences of `Veil-Touch` across three authoritative `rules/` files against three
of `VeilThread` in three tier-1 character cards, with the decisions document using the
minority form. Full scope, evidence and the ruling needed are in §19.

Unlike §16.1's `Technarc`, these are two different words rather than two spellings, and
`VeilThread` collides with `LT`'s own name (*Luminous Thread*). No fix applied.

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


---

# 17. SID book component — RESOLVED 2026-09-19

Status: **CONFIRMED.** `B{01-09}` is correct. James ruled 2026-09-19 that the
`B{00-09}` in decisions §2.1 was a transcription slip: there is no book zero.

`rules/canon_rules.json` already carries `S1.T{1-3}.B{01-09}.A{1-3}.E{00-99}`, applied
2026-09-19, so no change was needed — the flagged reading was the right one. The
validator enforces the two-digit book rule from that pattern, and
`tools/test_validate_canon.py` asserts `B00` is out of range while `B{01-09}` stands.

The analysis that produced the flag is kept below.

---

## Original entry (the discrepancy, now resolved)

Status: DISCREPANCY RECORDED / ONE READING APPLIED / TRIVIAL TO CHANGE

`recovery/CANON_DECISIONS_2026-09-18.md` §2.1 writes the SID format as:

> Format `S1.T{1-3}.B{00-09}.A{1-3}.E{00-99}` — **two-digit book numbers**

The book component reads `B{00-09}`, admitting a book zero. Three things point the
other way:

1. The same sentence says "two-digit book numbers", which is what the widening from
   `B{1-9}` to `B{01-09}` achieved; it says nothing about admitting `B00`.
2. Every book in the repository is `B01` through `B09` — nine books, nine
   `book_context_B0*.json` files, 27 act overlays. There is no book zero and none is
   named anywhere in the saga architecture.
3. The instruction accompanying the ruling specified widening **the episode range** to
   `E{00-99}`, and named no change to the book component.

The most likely reading is a transcription slip: the `00` from the episode widening
carried onto the book component in the same sentence.

**Applied:** `S1.T{1-3}.B{01-09}.A{1-3}.E{00-99}`. The episode widening is made
exactly as ruled; the book component is left at `B{01-09}`.

**If `B00` was intended** — a book zero, a prequel volume, or a deliberate reservation
of the slot — it is a one-line change to `rules/canon_rules.json` plus a line in
`CLAUDE.md` §3, and the validator picks it up automatically because it derives its
rules from that file. Nothing else depends on it today.

**Answered 2026-09-19: it was not intended.** `B{01-09}` stands.

This was flagged rather than silently chosen because a SID format change is an
identifier ruling, and §4 of `CLAUDE.md` reserves those.

---

# 18. Banded envelopes — applied, with the Post-Mending file HELD

Status: PARTIALLY APPLIED / ONE CANON CONTRADICTION FLAGGED, NOT RESOLVED

Source: `proposals/concord-2026/ENVELOPE_INTERIM_VALUES_V2_2026-09-19.md`, committed
verbatim before anything was applied from it.

## Two rulings, both applied

1. **`FX2` in Book 1 Act I is correct** — "start with a bang". So
   `trilogy_context_T1_veil.json`'s `default_vfx_ceiling: FX1` was the error, not the
   recovered packet. Raised to `FX2`, with the reason recorded in the file. Recovered
   packet `S1.T1.B01.A1.E16` stands unamended.
2. **Bands replace ceilings**, on every axis in every act. Applied to all 27 act
   overlays as `escalation_permissions` with `corridor`/`weather`/`fx` min-max pairs,
   an `exceptions` list, and a `basis` field reading `observed` or `inferred` so no
   interpolated value can later be mistaken for a ruled one. `S1.T1.B03.A3.E14`'s `W4`
   is the first and only exception entry.

`tools/validate_canon.py` gained `CHK_BANDS`, which checks band **coherence** only —
bounds are vocabulary members, `min` does not exceed `max`, exception axes and values
are valid, exception SIDs parse. Band *values* are author judgement and are never
second-guessed; a test asserts that. All 27 bands pass.

## HELD: the Post-Mending era file forbids the era's own signature state

§6 of the source document specifies `rules/era_context_post_mending.json` with:

> `res_states_permitted`: `CALM` · `BLOOM` · `NODE`

**`LT` is missing, and it should not be.** `rules/Mechanica-v4.md` §33 lists `LT` among
the resonance states and defines it as *"Post-Mending prismatic filtration ·
Ascendant-only perception · Gentle, non-coercive presence"*.
`rules/Channels/LT_RULES_POST_MENDING.md` is headed **"Applies To: Post-Mending World
Only"** and defines `LT` as the post-Mending metaphysical channel formed when the Veil
becomes breathable. And `canon/characters/SeraphineIdentity.md` has the saga lead
become the Luminous Thread post-Mending — the saga's ending.

So a Post-Mending envelope permitting only `CALM`, `BLOOM` and `NODE` would forbid the
one state the era exists to contain, and would make the ending illegal under its own
rules.

**Both readings recorded, neither resolved, per `CLAUDE.md` §4:**

- *The document's list is right as written.* `LT` is a **channel**, and channels are
  not governed by an era's `res_states` — `VT` and `LT` sit in `res_states` in
  Mechanica §33 but describe channel interaction rather than field condition, so an
  era envelope might legitimately not enumerate them.
- *The list is incomplete.* Mechanica §33 makes `LT` a resonance state without
  qualification, and the era file's own axis is `res_states_permitted`. Omitting it
  excludes it.

The exclusion is the reason the file is held rather than written: creating it as
specified would encode a rule against the ending. **The file does not exist yet, and
`U7` and `NODE` still have no home** — the gap §4.1 of
`recovery/ENVELOPE_QUESTION_2026-09-19.md` identified remains open.

The same question applies to `VT`, which the document also omits.

## Three accuracy notes on the source document

None changes a band; all three are recorded so the reasoning stays auditable.

**1. The `B3.A3` floor count is across 22 episodes, not 18.** §1 says *"`B3.A3` sits at
`U1` for eleven of eighteen episodes"*. Counted from the shells: within `B3.A3`'s own
18 episodes, `U1` appears **7** times flat plus one `U1→U2`. The count of 11 is reached
only by including the four Veil→Neon epilogue shells, which are `B3.EP`, not `B3.A3`.
The band `U1`–`U5` is unaffected and correct either way.

**2. The epilogue shells have no band, and need none.** §2's table covers `B01.A1`
through `B03.A3` with no row for the Veil→Neon epilogue, so on the document's own terms
four recovered episodes are unbanded. Decisions §2.2 closes this: epilogues take the
next sequential episode number, so those four renumber into `B03.A3` as `E19`–`E22` and
fall under its band. Their values — `U1`, `U2→U3`, `U1`, `U1`; `W0`, `W1–W2`, `W0`,
`W0` — are all inside `U1`–`U5` / `W0`–`W3`. So §7's claim holds, by a route §7 does
not state.

**3. §7's "22 recovered episodes" excludes the three packets §2 cites as observed.**
The 22 are the structural shells (18 `B3.A3` + 4 `B3.EP`). `E16`, `E17` and `E18` are
separately recovered full packets and are the `[observed]` basis for `B01.A1` and
`B01.A2`. Checked independently: `E16` (`U3→U4`, `W1`, `FX2`), `E17` (`U2→U3`, `W1`,
`FX0→FX1`) and `E18` (`U2→U3`, `W1`, `FX1`) all fall inside their bands. The
verification is sound across all 25; the figure should read 25.

Also worth noting: the `B3.A3` shells carry **no `FX` field at all**, so the `FX1`–`FX2`
band on that act is inferred rather than observed, despite the row being marked
`[observed]` overall. The corridor and weather parts of that row are observed; the FX
part is not.

## Still open from §8 of the source document

1. `allowed_heat_range` removal from the envelope files — recommended there, not ruled.
2. What the nine book contexts hold now that bands live at act level: derived from
   their three acts, or removed. Their 27 `TODO` placeholders are still the entire
   substrate violation count.
3. `B08.A2`'s deliberate floor dip — the one place the source lowered a floor against
   the trilogy's direction.
4. The `B09.A3` era split. The act overlay carries the **pre-Mending portion only**,
   marked `unresolved` in the file, because the post-Mending half needs the era file
   that is held above.
5. The 18 Neon and Loom acts remain inferred placeholders, marked `basis: inferred` in
   every file.

---

# 19. Channels-and-states proposal — verified, nothing applied

Status: PROPOSAL VERIFIED / NOT APPLIED / FOUR RULINGS REQUESTED / ONE NEW DEFECT FOUND

Source: `proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md`, committed
verbatim. Its §7 asks four questions, all of which are author rulings under `CLAUDE.md`
§4, so **none of §3, §4 or §6 has been applied.**

## What checks out

The central argument holds, and the evidence is stronger than the document claims.

**`VT` and `LT` in `res_states` are not a category error.** `rules/Channels/VT_RULES.md`
line 11 defines `VT` as *"direct metaphysical boundary contact"* — an event, not a
medium. `Mechanica-v4.md` §33 gives `VT` as "Metaphysical boundary interaction" and
`LT` as "Post-Mending prismatic filtration". Both describe field conditions.

**The `MT`-absence argument is sound.** `res_states` holds `CALM · BLOOM · SHARD ·
RUPTURE · NODE · VT · LT`. `MT` is not there. Had the three channels been filed into
the state list by mistake, `MT` would have come with them. Its absence is evidence the
two that *are* there were put there deliberately.

**§4 item 4's `VT_RULES.md` §9 citation is accurate**, including "VT does not evolve
into LT" — that line sits just below the bullet list at line 143, not inside it. The
quotation omits one bullet, *"operates within filtered resonance"*, which is arguably
the most relevant of the three to a post-Mending envelope and should be carried over if
§4 item 4 is adopted.

## One citation that does not resolve — PARTLY CORRECTED, see §23

> **Corrected 2026-09-19 (§23).** The quoted string is still absent from the corpus,
> but the *rule* it carried is sourced: `Saga Beat Expansion Pipeline` records
> "VT cannot appear before Book 3 · LT cannot appear before Post-Mending", and bounds
> VT at both ends. The finding below is right about the citation and wrong to imply the
> claim was unsupported.


**§4 item 1 cites an "escalation curve" for `"VT: sealed until Tahl breach"`.** That
string appears nowhere in `rules/`, `canon/`, or any of the 21 sanitized exports. The
file it names is not in the repository either.

The underlying claim may well be right — `S1.T1.B3.A3.E14` is anchored
*"FIRST AND ONLY VT BRUSH IN VEIL TRILOGY"*, which implies nothing before it — but that
is an inference from the packet, not the citation given. **Ruling question 3 asks about
`VT` era gating, so this should be settled there rather than by treating the quoted
line as sourced.** If the escalation curve is a Notion document, it is in the not-yet-
recovered list at decisions §9.

## NEW DEFECT: `Veil-Touch` vs `VeilThread`

Found while verifying §1, flagged by nothing before now. This is the `Technarc` pattern
again, and the decisions document is on the wrong side of it.

| Form | Occurrences | Files |
| --- | --- | --- |
| **`Veil-Touch`** | 4 | `rules/Channels/VT_RULES.md`, `rules/Channels/CHANNELS_OVERVIEW.md`, `rules/Mechanica-v4.md` (×2) |
| **`VeilThread`** | 3 | `canon/characters/KadeEBCI.md`, `canon/characters/LacunaEBCI.md`, `canon/characters/TahlEBCI.md` |

Every authoritative rules file says **Veil-Touch**. Three tier-1 character cards say
**VeilThread**. They are different words, not spellings of one word — "touch" and
"thread" mean different things, and `LT` is already *Luminous **Thread***, so
`VeilThread` additionally collides with `LT`'s own name.

**`recovery/CANON_DECISIONS_2026-09-18.md` §1.2 uses `VeilThread`:**

> `VT-BRUSH` refers to the VeilThread channel; the operative token is `VT`.

So the binding decisions document uses the minority form, which came from the character
cards rather than from the channel rules. The ruling it makes — that the operative token
is `VT` — is unaffected either way.

This is recorded, not resolved, per `CLAUDE.md` §4. **Ruling needed: is `VT`
Veil-Touch or VeilThread?** If `Veil-Touch`, three character cards need correcting and
the decisions document needs a note; if `VeilThread`, four rules files do, including
Mechanica. The evidence favours `Veil-Touch` — it is in the authoritative channel rules
and in Mechanica, which §5.2 makes authoritative — but that is an observation, not a
ruling.

Cross-referenced into §16 as defect 16.6.

## §6's `MT` gloss drift is real

`rules/canon_rules.json` → `invariants.channels.MT` reads `mortal_media_channel`.
`rules/Channels/MT_RULES.md`, Authoritative Canon, defines `MT` as **Mortal
Technology**, *"the human-built information and communication layer"* — phones, AR
overlays, holochat. "Media" narrows it to publication, which is the wrong sense and
also the sense that collides with the `MT` supplement vehicle (*The Missing Thread*).

Not corrected: it is ruling question 4. The correction is one string.

## Why nothing was applied

All four questions in §7 are canon decisions. The grouping in §3 defines what kind of
thing each token is; the rules in §4 would become enforced constraints; §6 rewrites a
definition. `CLAUDE.md` §4 reserves all of it.

Two further reasons to wait:

1. **§4 item 4 would settle the held Post-Mending envelope** (§18) by permitting
   `CALM · BLOOM · NODE · VT · LT`. That is the reading this ledger argued for, but it
   arrives as a proposal, not a ruling, so the file stays held.
2. **§3's grouping and the `Veil-Touch` question touch the same block.** If both are
   ruled, they should land in one edit rather than two.

---

# 20. Channel names ruled — VeilThread applied, MT held

Status: PARTIALLY APPLIED / MECHANICA AMENDED / TWO QUESTIONS OPEN

Source: `recovery/CHANNEL_NAMES_RULING_2026-09-19.md`, committed verbatim first.

> MissingThread, VeilThread and LuminousThread are correct. MT is the public mortal
> channel (early Tahl). VT is the private channel between Silence and Hope that Tahl
> discovers. LT is the post-Mending channel.

## MECHANICA AMENDED — recorded under §5.2

`rules/Mechanica-v4.md` is authoritative under decisions §5.2 until the line-by-line
memory review. This ruling amends it, so the change is recorded here rather than made
silently:

| Line | Was | Now |
| --- | --- | --- |
| 723 | `- VT (Veil-Touch)` | `- VT (VeilThread)` |
| 1137 | `**VT:** Veil-Touch metaphysical channel` | `**VT:** VeilThread metaphysical channel` |

Nothing else in Mechanica changed. The amendment is a name, not a mechanic: `VT`'s
behaviour, its §33 state entry and its channel-separation law are untouched.

Also applied: `rules/Channels/VT_RULES.md:11` and
`rules/Channels/CHANNELS_OVERVIEW.md:14`. `VT_RULES.md` gains a note recording that
"direct metaphysical boundary contact" is **not** superseded — it is what the channel is
from the mortal side, which is exactly why `RES: VT` records the field registering
contact with a channel never meant to admit a mortal.

`rules/canon_rules.json` `invariants.channels` now carries all three ruled names and
definitions, with a `_naming_note` pointing at the open `MT` question.

## The ruling's justification checks out

`rules/Channels/CHANNELS_OVERVIEW.md` — the file that introduced both renamings —
declares `Source: Project Memory (inflated)`. `MT_RULES.md`, `VT_RULES.md` and
`LT_RULES_POST_MENDING.md` all declare `Source: Project Memory` with no inflation flag.
Verified. That single file is the only inflated one in the channel set, and it is the
one that drifted.

## TWO CORRECTIONS TO MY OWN EARLIER FINDINGS

Recorded plainly because both were stated with more confidence than they deserved.

**1. The three character cards were not drift.** §16.6 and §19 framed
`KadeEBCI.md`, `LacunaEBCI.md` and `TahlEBCI.md` as the minority form, and said "the
evidence favours `Veil-Touch` — it is in the authoritative channel rules and in
Mechanica". That reasoning counted files rather than tracing provenance. The cards had
**preserved the original** while the rules files drifted around them, and Notion carries
the Thread naming consistently across five independent pages. Majority in the
repository was the wrong test when the drift was introduced by a file that flags its own
source as inflated.

The same is true of `recovery/CANON_DECISIONS_2026-09-18.md` §1.2, which I described as
being "on the wrong side" of the drift. It was on the right side.

**2. The `mortal_media_channel` gloss was closer to right than the file it
contradicted.** §19 recorded it as a paraphrase that "narrows" `MT_RULES.md`'s
definition. In fact the gloss pointed at a public channel while the rules file had
expanded into infrastructure. The finding is withdrawn.

## The `MT` collision dissolves

`canon_rules.json` and `canon/supplements/SUPPLEMENT_VEHICLES.md` both carried a note
reconciling "MT the channel" with "MT the supplement vehicle". Under the ruling those
are **one object** — the MissingThread, the public mortal channel Tahl launches. The
note is removed rather than reworded.

`VT`'s multiplicity is real and stands: channel, resonance state, and supplement
vehicle, three vocabularies sharing one token.

## HELD: how `MT` reconciles

`MT_RULES.md` §1 defines `MT` as "the human-built information and communication
layer" — phones, AR overlays, holochat, broadcast media, data networks. That is
infrastructure. The ruling makes `MT` a publication Tahl launches. Renaming the file
would leave a document called MissingThread describing phone networks.

Three options are in the ruling §2 (A: channel vs substrate; B: `MT` as the mortal tier
with the MissingThread as flagship; C: split, adding a fourth token). **B is
recommended there and is not applied** — it is a canon act. `Mortal Technology` stays in
place across all six occurrences until it is ruled.

## NEW: the compound spellings do not match the repository

The ruling writes all three names closed up. The repository does not, and only one of
the three had a closed form to restore:

| Name | Closed form in repo | Spaced form in repo |
| --- | --- | --- |
| `VeilThread` | 3 (Kade, Lacuna, Tahl EBCI cards) | 0 — the drift was `Veil-Touch`, a different word |
| `MissingThread` | 1 (`canon/characters/TahlID.md`) | 6 (`SUPPLEMENT_VEHICLES.md`, `canon_rules.json`, decisions, ledger) |
| `LuminousThread` | **0** | **19** (`SeraphineIdentity.md`, `SeraphineAppearance.md`, `seraphine_vael_pov.md`, `LT_RULES_POST_MENDING.md`, `CHANNELS_OVERVIEW.md`, `Mechanica-v4.md`, `seraphine_full.md`) |

`VeilThread` was unambiguous and is applied. The other two are not:

- **Read strictly**, the ruling mandates closed compounds and 25 further occurrences
  change, including tier-1 Seraphine canon — she becomes *the Luminous Thread*
  post-Mending, which is the saga's ending.
- **Read as naming the channel rather than its spacing**, nothing further changes. The
  ruling's own change-scope §6 supports this: it lists the `Veil-Touch` and
  `Mortal Technology` edits and **does not mention `Luminous Thread` at all**.

Both readings recorded, neither applied. `LuminousThread` has zero repository support,
so unlike `VeilThread` this would be a new spelling rather than a restoration.

## NEW GAP: Silence and Hope have no canon files

Verified independently. `canon/characters/` holds **62 files across 14 characters**.
Neither Silence nor Hope appears in any of them, nor anywhere in `source_canon/`, and
no file is named for either. The phrase "Old Veil" appears nowhere in the repository
outside the sanitized exports.

Two metaphysical entities who are each half of the Old Veil, whose existence defines
`VT`, and whose break drives the endgame have no canon file. Notion has at least
`08.10 • Silence — Metaphysical`.

Added to the work queue as item 9b, **marked awaiting confirmation** — ruling §7
question 2 asks whether to queue it, so the item records the recommendation rather than
assuming the answer.

## Open

1. **How `MT` reconciles** — ruling §2, options A/B/C. Blocks the `MT` half of the
   rename and any retitling of `MT_RULES.md`.
2. **Whether `LuminousThread` and `MissingThread` close up**, per the table above.
3. **Silence and Hope recovery** — confirm queue item 9b.
4. Ruling §7 question 3 asks whether amending Mechanica needs more than a ledger entry.
   This entry is that record. If §5.2 wants something stronger — a version bump, or a
   note in Mechanica's own authority statement — say so and it is a small edit.

---

# 21. Notion Book 1 Final Beat Bible — read 2026-09-19. It is NOT the E00-E15 material.

Status: HYPOTHESIS DISCONFIRMED FOR BOOK 1 / WORK-QUEUE ITEM 7 UNCHANGED

Source: Notion `BOOK 1 — VEIL I (Final Beat Bible)`, last edited 2025-11-23, read
2026-09-19. Tier D, RECOVERED PRIOR CANON (decisions §5.4).

## The question it was read to answer

Decisions §9 lists the per-book Final Beat Bibles as not yet searched, and says the
last of them "may hold the E00–E15 material the chat exports are missing". Work-queue
item 7 depends on the answer: it targets the ChatGPT conversation `Archive Veil Book 1`
because that was believed to be the only home of those packets.

## The answer: no

The Book 1 Final Beat Bible holds **15 macro beats, five per act**, across three acts:

- Act I "THE HUM BEFORE THE CRACK" — `E1`–`E5`
- Act II "THE PRESSURE RISES" — `E6`–`E10`
- Act III "THE FIRST SHARD" — `E11`–`E15`

That is act-level structure for a whole book. The recovered ChatGPT material has
**seventeen episodes in Act I alone** (`E00`–`E16`), at 1.3–1.8k words each, with full
ECID blocks, Pressure Maps and 6–12 internal beats per episode.

These are two different granularities. The Notion page matches what §2 of this ledger
calls the Consolidated Beat Bible layer — "act-level beat sequences for all nine
books" — not the Episode Expansion Engine layer of §3 (60–80 episodes per book).

**Title overlap between the two sets is zero.** Notion's `E1` is "Seraphine: The
Lantern Glows Wrong"; the recovered `E01` is "The Sick Child". No Notion beat title
appears anywhere in the repository.

**So the E00–E15 packets are not in Notion's Book 1 Final Beat Bible.** Work-queue item
7 stands as written, and `CLAUDE.md` §7's source constraint remains load-bearing exactly
where it was.

Not checked: the eight other Final Beat Bibles, the three `ACT * SUMMARY — VEIL I`
pages, or the separate `Book 1 Prologue` page. The Act summaries are the most likely
remaining Notion home for episode-level Book 1 material and have not been read.

## Independent corroboration — and why it counts

**ChatGPT could not reference Notion.** So the Notion beat bible and the ChatGPT episode
expansion are independent lines of development. Where they agree, that is corroboration
rather than copying; where they differ, it is a genuine fork.

**They agree on the Act II opening.** Notion `E9` is "Baz Arrives in NOLA", the first
beat of Act II. The recovered ChatGPT packet `S1.T1.B1.A2.E17` is "Baz Arrives in NOLA",
the formal opening of Act II. Same title, same structural function, arrived at
independently. Only the numbering differs, which is exactly what the two granularities
predict.

**They agree that MT is the MissingThread.** The page lists `MT (early)` among Book 1's
Supplement Vehicles *and* gives `E7 — Tahl: Origin of MT — Tahl launches the early
version of Missing Thread`. One object, used as a supplement vehicle and launched by
Tahl — independent corroboration of the 2026-09-19 channel ruling and of the `MT`
collision dissolving (§20).

Bearing on the open `MT` reconciliation (ruling §2, options A/B/C): this page treats
`MT` purely as the publication Tahl launches. It carries nothing resembling
`MT_RULES.md`'s infrastructure definition. That is evidence, not a ruling.

**They are consistent on VT's era gating.** Book 1's Act III function is to "hint at
VT" — no contact occurs. The only VT contact in Veil is `S1.T1.B3.A3.E14`, anchored
"FIRST AND ONLY VT BRUSH IN VEIL TRILOGY". This is consistent with the "sealed until
Tahl's breach" claim that §19 flagged as citing an unsourced escalation curve. Still
not the cited source, but the pattern now has two independent witnesses.

## Conflicts and notes, none resolved

**A third prologue title.** Notion has a separate page `Book 1 Prologue — "Conversation
in the Stars"`. Decisions §2.2 rules the prologue is `E00`, titled **"The Conversation
in the Sky"**, superseding "Silence & Hope" from the Veil Master Beat Bible. So three
names exist: the ruled *Sky*, the superseded *Silence & Hope*, and Notion's *Stars*.
*Stars* and *Sky* differ by one word and are plainly the same artifact. The ruling
stands under §5.4; recorded so the variant is not mistaken for a fourth prologue.

**Notion carries `Technarch`.** The page reads "Dominions + Technarch shadows" and
"Technarch flags him". Decisions §6.4 ruled `Technarc` canonical and the repository is
corrected. This is consistent with Notion being older, and changes nothing — recorded
because anyone migrating from these pages will import the retired form.

**Episode numbering is continuous across the book**, `E1` through `E15`, not restarting
per act. That agrees with decisions §2.1's continuous rule. The form is one-digit and
carries no SID prefix, so migration converts it.

**`Jules` has no canon file.** The page has "Jules' lattice sketch overlaps faintly with
Tahl's notes" in `E5`. `Jules` appears nowhere in `canon/` or `source_canon/`. A smaller
instance of the §20 Silence-and-Hope gap; recorded, not queued.

## What this does not change

Nothing in the work queue moves. Item 7 keeps its target and its rationale. The finding
is a negative result, and worth the same care as a positive one: the hypothesis in
decisions §9 is now disconfirmed for Book 1 rather than open.

---

# 22. Silence and Hope in the exports — searched 2026-09-19, almost nothing there

Status: SEARCHED / NEGATIVE RESULT / ROOT CAUSE IDENTIFIED

Expectation checked: that the exported ChatGPT chats hold substantial Silence and Hope
material. They do not. The reason is structural and is already documented in the
repository's own inventory.

## The counts

Across all 21 sanitized exports:

| Token | Occurrences | Files |
| --- | --- | --- |
| `Silence` | 13 | 6 |
| `Hope` | 3 | 2 |
| `Old Veil` | 1 | 1 |
| `Silence and Hope` / `Silence & Hope` / `Silence + Hope` | 0 | 0 |

## Only three of the thirteen are the entity

**"Silence" in the exports overwhelmingly means Lucien's arc, not the metaphysical
entity.** Ten of the thirteen are arc vocabulary:

`Silence-echo crises` · `Silence-precursor spirals` · `Silence-with-Intent line` ·
`Silence-without-Intent arc` · `Silence-geometry threshold` · `Silence-echo tremors` ·
`Silence-echo patterns` · `Silence-geometry crisis` · `Tahl arc climax → Silence's spark`

Every one describes Lucien's dissociation and structural fracture, or Tahl's arc
endpoint. None describes the half of the Old Veil.

The remaining three, and **all three `Hope` occurrences**, are the same beat title in
two documents:

> `Prologue — Silence & Hope` (`Episode expansion process__part01`)
> `Prologue — Silence & Hope (canon)` (`Trilogy Act-Level Beat Backup`, twice)

That is the prologue title decisions §2.2 **supersedes** with "The Conversation in the
Sky". So the only entity-level trace of Silence and Hope in the entire export corpus is
a title that has since been retired.

The single `Old Veil` occurrence is a systems check — "Old Veil → Shards → Rupture" in
`Saga Beat Expansion Pipeline` — not a description of the entities.

## `Silence` is a token collision inside the project's own vocabulary

This is the finding worth carrying forward. `Silence` names two different things:

- **Silence**, the metaphysical construct, half of the Old Veil
- **the Silence arc** — Lucien's dissociation line, with its own compound vocabulary
  (`Silence-with-Intent`, `Silence-without-Intent`, `Silence-echo`, `Silence-geometry`)

Same class of collision as `MT` and `VT`, and worse for search: anyone grepping the
corpus for the entity gets ten arc hits for every three entity hits. That asymmetry is
very likely why the material feels like it should be there. It is not a reason to
rename anything — both usages are established — but it should be recorded before
someone concludes the entity material was lost.

## Root cause: these are the wrong chats, and the repo already said so

`proposals/concord-2026/EXPORT_INVENTORY_AND_MISSING_SOURCE_MAP.md` §3 states it
directly:

> The available structural exports are primarily **backup / archive / audit outputs**,
> not necessarily the chats where the late decisions were originally negotiated. …
> continued semantic searching inside the same backup files is unlikely to recover the
> missing *decision dialogue* if the originating chat itself was never exported.

Its evidence: `Trilogy Act-Level Beat Backup` asks for source beats to be pasted and
says it will not reconstruct; `Saga structural archive` defines itself as pure
structural storage that adds nothing; `Phase 1A Migration Plan` states authored assets
may exist only inside long chats.

And §4B of the same document, listing the highest-value missing chats, anticipates this
exact gap — it expects a missing chat to contain "the user's remembered Tahl/Silence
epilogue discussion".

**So the Silence and Hope material is very probably in the ChatGPT workspace, in chats
that were never exported.** The 21 exports are the archive layer, not the development
layer. Metaphysics and worldbuilding were developed elsewhere.

## What this changes

**Work-queue item 6 rises in value.** "Run the ChatGPT console export in list mode;
produce the full workspace inventory" is the gate on knowing what is recoverable at
all. Until it runs, the difference between *not exported* and *does not exist* cannot
be told apart — and this search is a concrete case where that distinction was assumed
rather than established.

**Item 9b's route is confirmed as Notion, not the exports.** Notion holds both
`08.10 • Silence — Metaphysical` and `08.11 • Hope — Metaphysical` (§20). The exports
hold neither. For this item Notion is the only located source, which is the reverse of
the usual precedence in decisions §5.4 — worth stating plainly so the Tier D marking is
not mistaken for the material being weak. It is not weak; it is the only copy found.

**Nothing in §20 is withdrawn.** That entry recorded the absence from `canon/` and
`source_canon/`, which stands. It did not claim the exports had been searched for the
entities; this entry closes that gap.

---

# 23. Tahl / Lucien / Caro / Mending in the exports — a divergence, not an absence

Status: SEARCHED / SUBSTANTIVE FORK FOUND / ONE EARLIER FINDING CORRECTED

Followed up §22 on the expectation that Silence-and-Hope material sits in the export
discussions of Tahl, Lucien, Caro and the Mending. Those discussions are **dense** —
`Tahl` 96, `Lucien` 107, `Seraphine` 99, `Baz` 62, `Mending` 36, `Caro` 15 — but they
carry no Silence-and-Hope entity content.

The reason is not that the exports are thin. It is that **they tell a different story
about the Mending.**

## The exports say the Mending is human

`Saga Beat Expansion Pipeline` runs an audit and records:

> **Ascendant Trio (Seraphine, Lucien, Caro):** No beats explicitly "crown" them; the
> Mending is framed as **coordinated human Intent & resonance skill**. After the
> Mending, language focuses on prismatic calm, not godhood. ✅ Pass — ascension is
> implicit in function, not called out as the point of the story.

Notion `05.02 • Metaphysics & Ascension Bible` says something different:

> 1.1 Silence & Hope (Old Metaphysicals) … **Silence + Hope give their metaphysical
> bodies**

**These may be compatible** — the trio supplies human Intent while the old
metaphysicals supply the substance. But the export passage is an *audit of the Mending*
that checks who does what and concludes it is coordinated human skill. An audit of that
event would be expected to name Silence and Hope if they were giving their bodies in
it. It does not mention them at all.

So this is a **fork between two independent lines**, not a gap in one. Recorded, not
resolved — decisions §5.4 gives GitHub and later recovered Beat Bible material
precedence over conflicting Notion, which would favour the human framing; but §22
establishes the exports are the archive layer, and an audit summary is not the same as
an originating decision. **Both readings stand until James rules.**

This is the substantive question behind work-queue item 9b: recovering Silence and Hope
from Notion means importing a metaphysical account of the Mending that the exported
material does not corroborate and arguably contradicts.

## CORRECTION to §19: the VT era-gating rule IS sourced

§19 recorded that the channels proposal cited an escalation curve reading
`"VT: sealed until Tahl breach"`, and that the string appears in no rules file, no canon
file, and none of the exports — concluding the citation "does not resolve".

**The quoted string is still not in the corpus, but the rule is.**
`Saga Beat Expansion Pipeline` carries it twice:

> **2. Resonance Logic Audit** — VT cannot appear before Book 3 · LT cannot appear
> before Post-Mending · Shards escalate properly across Neon

and, in the channel audit:

> VT: brush at Veil 3 end; full slip + Intent spark in Neon 6 Act II; no surviving VT
> contact afterwards. MT: Tahl's entire Neon arc + Kade's rise in Neon 6 / Loom; always
> mortal media. LT: Only hinted post-Mending (Book 9 Epilogue handshake).

So the substance of ruling question 3's era gating is sourced, in an export, and is
more precise than the proposal's paraphrase: `VT` is gated to **Book 3 onward**, not
merely "after Tahl's breach", and has **no surviving contact after Neon 6 Act II**.
That last clause is new information — it bounds `VT` at both ends.

§19's finding is corrected: the citation was to a document that does not exist under
that name, but the claim it carried is supported.

## Bearing on the open `MT` question

The same audit line reads: **"MT: … always mortal media."**

That is a third characterisation beside `MT_RULES.md`'s infrastructure definition and
the ruling's publication definition, and it sits closer to the publication reading —
"mortal media" is what the MissingThread is, not what a phone network is. It also
vindicates the `mortal_media_channel` gloss further than §20 already did.

Evidence for ruling §2's options A/B/C. Not a ruling.

## Two chats named in the exports that were never exported

Mined from the conversation text, since sanitization stripped the sidebar and every
conversation ID (zero UUIDs survive in the 21 files — the four IDs in
`EXPORT_INVENTORY_AND_MISSING_SOURCE_MAP.md` §2 must have been taken before
sanitization):

- **`Spine Architect chat`** — named in `Character Vault Chat` as the owner of
  "Saga-wide continuity storage", which the Character Vault explicitly does not handle.
  Not among the 21. A continuity-storage chat is a strong candidate for metaphysics.
- **`Saga Visual Bible Framework`** — named in `Character involvement pacing` as an
  existing chat title, in a list of bibles "not currently part of the Model Set".
- `Book 1 Beat Backup Chat` — already known and already absent; confirmed again here as
  the archive destination for E16, E17 and E18.

These are concrete targets for work-queue item 6 rather than a blind inventory.

## What this does not change

§22's conclusion stands: the Silence-and-Hope entity material is not in the exports.
This entry explains what *is* in the places it was expected to be, and finds that the
exported line describes the Mending without them.

---

# 24. The 2026-09-19 timeline / Veil / Notion bundles — verified, two defects caught

Status: COMMITTED VERBATIM / MILESTONE LOAD HELD / ONE DEFECT / ONE RETRACTED FINDING

Sources, all committed unaltered first: `recovery/SAGA_TIMELINE_2026-09-19.md`,
`recovery/VEIL_STRUCTURE_2026-09-19.md`, `recovery/NOTION_RECOVERY_2026-09-19.md`, and
the 36-row milestone load at
`proposals/concord-2026/milestones_payoffs_PROPOSED_LOAD_2026-09-19.csv`.

## DEFECT 1 — the milestone CSV would have destroyed three ruled columns

The uploaded load carries **16 columns**. `grids/milestones_payoffs.csv` carries **19**.
Missing: **`supplement_function`, `supplement_vehicle`, `supplement_form`.**

Those three were added on 2026-09-19 — the first two per decisions §3 (type, function
and vehicle are three independent axes), the third per the same-day ruling that form and
vehicle are separate values. The load was built against the pre-ruling header.

Loading it as-is would have silently dropped all three from the grid.

**Corrected load written to
`proposals/concord-2026/milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv`** — all 36
rows realigned to the 19-column header, the three new columns present and empty. Nothing
else altered. **Still in `proposals/`, not loaded**, because every row reads
`status: proposed` and the timeline document's §8 asks whether to load rather than
stating that it loads.

## ~~DEFECT 2~~ — WITHDRAWN. Commit `a4324a9` exists.

**This finding was wrong and is retracted in full.**

I recorded that `a4324a9`, cited in `VEIL_STRUCTURE` and `NOTION_RECOVERY` as locking
*Bastien "Baz" Arnaud* over Notion's *Baz Foix*, was "not a valid object name" and in no
branch of this repository.

It is a real commit. `a4324a9d3f6f5a45bbce4ea78ecdf924a481afd1`, authored by jacalder42
on 2026-09-19, adding ten lines to
`proposals/concord-2026/B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md`. It was pushed by
a **parallel session working the same branch**, and had not reached this clone when I
ran the check.

**The error was mine, not the document's.** `git cat-file` answered correctly about a
clone that was behind. I treated a local absence as a repository absence, and stated it
with more confidence than a single un-fetched lookup supports. The rule that follows:
**fetch before concluding anything is missing from git**, exactly as `CLAUDE.md` §6
already says for the proposal branch — I applied that discipline to branch contents and
not to commit hashes.

The naming note in both bundles is therefore **correct and correctly cited**. `Arnaud`
is current canon; `Foix` is the superseded Notion-side name.

One real observation survives: **two commits carry the identical message**
"Lock Bastien Baz Arnaud as current canon identity" — `a4324a9` and `6508833`. A
duplicate, not a defect, but worth knowing when tracing that ruling.

**The §19/§23 pattern claim is also withdrawn.** I generalised from two cases to
"citations from the Cowork side do not resolve". One of the two was my own fetch error.
The other — the `"VT: sealed until Tahl breach"` escalation-curve reference — was a
quoted string that did not exist while the rule it carried did, and Notion `01.02` has
since been found to carry that exact sense. Neither supports a pattern. There is no
systematic citation problem in these bundles.

## Integrity checks re-run independently, and they pass

`SAGA_TIMELINE` §4 claims the load has no dangling `required_setups`, no setup occurring
later than the milestone requiring it, and only ruled `supplement_type` values. Verified
against the file rather than taken on trust:

- 36 rows, every `required_setups` reference resolves
- no milestone requires a setup later in story order
- every `supplement_type` value is in the ruled or provisional vocabulary

Those claims stand.

## CONFLICT — `target_act: EP` contradicts the current ruling

Five rows — `M10`, `M11` (Book 3), `M23` (Book 6), `M35`, `M36` (Book 9) — use `EP` in
`target_act`.

`CLAUDE.md` §3 currently reads: *"Epilogues take the next sequential episode number."*
That is decisions §2.2, ruled 2026-09-18.

`VEIL_STRUCTURE` part 4 records a later ruling — *"Act 4 is more of a multi-episode
epilogue (~3-4)"* — and its §3 proposes **superseding** that with `EP` in the act slot,
offering three options:

- **A.** `EP` and `PR` both in the act slot; supersedes both D6 (`E00`) and D8
- **B.** `EP` only; prologue stays `E00` inside Act I
- **C.** Keep D8; the epilogue is the tail of Act III

**A is recommended there and none is ruled.** So the five `EP` rows presume an outcome.
They are correct under A or B and wrong under C. Left as written in the proposed load,
flagged here, and **the load cannot go into the grid until this is settled** — the
validator's SID format allows `A{1-3}` only, so `EP` is not expressible today.

## Book 9 has four acts — RULED 2026-09-19, see §25

`NOTION_RECOVERY` part 4 §1: the Book 9 Final Beat Bible runs **ACT I–ACT IV**, with Act
IV "Afterlight" at E16–E21. `S1.T3.B09.A4.E16` is not expressible under
`A{1-3}`, and the 27-Act Macro Structure says nine books times three acts.

Either the saga is 28 acts, or Act IV is the epilogue written as an act — which is what
the `EP` question above would settle. **The two questions are one question**, and should
be ruled together.

> **Half of it is now ruled.** James, 2026-09-19: *"Book 9 has 3 acts, the epilogue is
> several episodes long which could have implied a 4th act."* The saga is 27 acts; Act
> IV is the epilogue. The `EP` slot question above is **not** settled by it. §25.

## What the bundles unblock, and what they do not

| Held item | Status |
| --- | --- |
| `VT` era gating citation (§19, §23) | **Fully sourced.** `01.02` Trilogy Architecture: "VT sealed until Tahl brushes it". §23 found the rule in the exports; this finds it in Notion too, independently |
| Post-Mending envelope contents | **Sourced** — `06 • Post-Mending World Bible` gives no shards, Echo Nodes, "breaths not storms" supporting `W0`–`W1`, and `VT` persisting |
| `MT becomes LT` vs channel separation | **Resolved as a rename**, not a conversion, so `MT ≠ VT ≠ LT` holds |
| Silence and Hope | **Recovered** in full — structural half and emotional half, both dissolving at the Mending into Lucien and Caro |
| Who performs the Mending (§23) | **Resolved.** `B09.A3.E14`: the trio act *and* "Silence dissolves into Lucien. Hope dissolves into Caro." Both lines were right; the export audit was describing the human half |
| Post-Mending era file | **Still held** — `LT` now has *three* referents (Seraphine's ascended identity, the resonance state, Kade's renamed network), which is a new question, not the old one |

## The Veil two-draft problem remains the largest open item

`VEIL_STRUCTURE` part 1 records it and does not resolve it: Notion and the exports
disagree about whether Baz dies in Book 3, whether Tahl and Caro appear in Books 1–2,
whether the Caro–Elisabet romance exists in Veil, and whether Veil points at Santa Fe.
**Migrating any Veil act overlay writes one of two stories into canon.**

The rulings in part 2 cut across both drafts and are recorded as binding there, but they
settle character and causality, not act structure.

## Not applied

Nothing from these bundles is applied to the substrate. The milestone load is corrected
and staged in `proposals/`; every ruling that needs a schema change — `EP` in the act
slot, `A{1-4}`, the `pov_named_on_page` flag proposed at `VEIL_STRUCTURE` part 3 §4 —
waits on the rulings above.

===============================================================

# 25. Book 9 act count — RULED 2026-09-19: three acts

**Ruled by:** James, 2026-09-19 — *"Book 9 has 3 acts, the epilogue is several episodes
long which could have implied a 4th act."*

**Status:** RULED / NOTHING IN THE SUBSTRATE NEEDED CHANGING / THE `EP` SLOT REMAINS OPEN

---

## 1. What it settles

`NOTION_RECOVERY` part 4 §1 reported the Book 9 Final Beat Bible running **ACT I–ACT
IV**, Act IV "Afterlight" at E16–E21, and §24 recorded the fork: either the saga is a
28-act structure, or Act IV is the epilogue written as an act.

It is the second. Three consequences, all of them confirmations rather than changes:

| Artifact | Effect |
| --- | --- |
| `SID_format` in `rules/canon_rules.json` | **Unchanged.** `A{1-3}` stands; no `A4` |
| The 27-Act Macro Structure | **Stands.** Nine books × three acts |
| The 27 act overlays | **Correct as they are.** No 28th overlay is owed |
| `escalation_permissions` on `B09.A3` | **Its `unresolved` note narrows** — see §3 |

This also confirms, independently, the reading already recorded at
`recovery/VEIL_STRUCTURE_2026-09-19.md` part 4 §2: *"Book 9 has three acts and an
epilogue, not four acts. The Final Beat Bible's 'ACT IV — Afterlight' is the epilogue
written as an act."* That document reached it from the earlier ruling *"Act 4 is more of
a multi-episode epilogue (~3-4)"*; this ruling states it directly.

## 2. What it does NOT settle

**Where the epilogue goes.** The ruling says the epilogue is not an act. It does not say
whether the epilogue is a unit of its own in the act slot or the tail of Act III. Both
readings satisfy "Book 9 has 3 acts", so the three-way choice at
`recovery/VEIL_STRUCTURE_2026-09-19.md` part 4 §3 is untouched:

- **A.** `EP` and `PR` both in the act slot — `S1.T3.B09.EP.E01`, `S1.T1.B01.PR.E01`.
  Supersedes decisions D6 (`E00` prologue) and D8 (epilogues take the next sequential
  episode number). Recommended there.
- **B.** `EP` only; the prologue stays `E00` inside Act I. Keeps D6, asymmetric.
- **C.** Keep D8; the epilogue is the tail of Act III. The epilogue is then not a
  separate unit at all.

Under A or B the SID pattern becomes `S1.T{1-3}.B{01-09}.(A{1-3}|EP).E{00-99}`; under C
it is unchanged and `CLAUDE.md` §3 already reads correctly.

**So the milestone load is still blocked.** The five `target_act: EP` rows — `M10`,
`M11`, `M23`, `M35`, `M36` in
`proposals/concord-2026/milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv` — are
correct under A or B and wrong under C. `EP` is not expressible under the current
`SID_format`, so the load cannot enter `grids/` until A, B or C is ruled. That was the
blocker before this ruling and it is the blocker after it.

**And the two follow-ups in that document are still open:** whether Book 9's epilogue is
three or four episodes and which grouping (part 4 §4), and whether epilogue episodes
restart at `E01` within the unit or continue the book's numbering (part 4 §5 item 3).
The first is an authoring decision; the second only arises under A or B.

## 3. The `B09.A3` band note narrows

`act_overlays/act_overlay_S1_T3_B09_A3.json` carries an `unresolved` note on its
`escalation_permissions` recording that the band covers the pre-Mending portion only,
because the era boundary was believed to fall mid-act.

`NOTION_RECOVERY` part 4 §2 had already located that boundary at E14/E15 with Act IV
wholly post-Mending. With Act IV now ruled to be the epilogue, the boundary falls at the
**end of `B09.A3`** — a unit boundary under A or B, still mid-act under C, since C puts
the epilogue inside Act III.

**Not amended.** The note is only fully resolvable once the `EP` question is, and
amending it now would encode a reading of that question. Recorded here instead.

## 4. Nothing applied

No file changed under this ruling beyond this ledger entry and the `CLAUDE.md` §4 item
it narrows. The substrate was already correct for a three-act Book 9; what the ruling
does is close off the 28-act branch, so no future migration writes an `A4`.

END OF ENTRY 25

===============================================================

===============================================================

# 26. Review of the parallel narrative-recovery session — 2026-09-19

**Scope:** the 26 commits from `0332711` to `b139678`, which produced ten new documents
and about 2,800 lines of narrative recovery from the sanitized exports and Notion.

**Status:** REVIEWED / NOTHING APPLIED / NINE FINDINGS RECORDED

---

## 1. What the session produced

| Document | Lines | Home |
| --- | --- | --- |
| `NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT_2026-09-19.md` | ND-001..ND-033 | `proposals/` |
| `NARRATIVE_DECISION_LEDGER_PASS2_CHARACTERS_RELATIONSHIPS_ANTAGONISTS_2026-09-19.md` | ND-020..ND-038 | `proposals/` |
| `NARRATIVE_DECISION_LEDGER_PASS3_NOTION_CANON_RECOVERY_2026-09-19.md` | ND-039..ND-045 | `proposals/` |
| `B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md` | 24 numbered sections | `proposals/` |
| `ROMANCE_RELATIONSHIP_RECONCILIATION_2026-09-19.md` | 15 sections | `proposals/` |
| `NEON_B04_B06_SOURCE_RECONCILIATION_2026-09-19.md` | — | `proposals/` |
| `VEIL_MT_THREADNAUT_BREADCRUMB_GRID_2026-09-19.md` | MT-01..MT-14 + EP-A..EP-G | `proposals/` |
| `BAZ_WAREHOUSE_INCIDENT_RECOVERY_2026-09-19.md` | 291 | `recovery/` |
| `BAZ_DEATH_TIMING_RULING_2026-09-19.md` | 36 | `recovery/` |
| `TRIP_VELVET_VEIN_RECOVERY_2026-09-19.md` | 272 | `recovery/` |
| `LACUNA_RECOVERY_SOURCE_AUDIT_2026-09-19.md` | 291 | `recovery/` |
| `REX_TAN_RECOVERY_SOURCE_AUDIT_2026-09-19.md` | 264 | `recovery/` |

ND-001 through ND-045 are continuous with no gaps. Every Tier-1 file the audits cite
was checked and exists (`TripID`, `TripEBCI`, `trip_pov`, `RexID`, `LacunaID`).

## 2. The discipline held — this is the headline

**The session touched no substrate file.** Verified with `git log` per path: `grids/`,
`act_overlays/`, `book_context/`, `canon/` and `rules/` have zero commits from it. The
only substrate commit in the range is `1effb59`, which is this session's VeilThread
application.

Every document carries a status line, and they are honest ones — `PROPOSAL / RECOVERY —
NONCANONICAL UNTIL AUTHOR PROMOTION`, `do not treat unresolved items as new canon`,
`These are hypotheses only. Do not promote one without a recovered source or new author
ruling.` Author locks are labelled as such and separated from reconstruction candidates:
`B03_B04_HANDOFF` §14 explicitly says an author proposal *"remains an excellent
reconstruction candidate, but needs a direct source or explicit author lock before being
treated as recovered historical canon."* The MT breadcrumb grid contains beat functions
and prohibitions, never scene text, so `CLAUDE.md` §1's no-prose rule holds.

That is the working agreement doing its job. The findings below are about bookkeeping and
collisions, not about a session that overstepped.

## 3. Finding 1 — none of it is in this ledger

Every ledger commit in the range is this session's. Searching the ledger for
`BAZ_DEATH_TIMING`, `BAZ_WAREHOUSE`, `LACUNA`, `REX_TAN`, `TRIP_VELVET`,
`NARRATIVE_DECISION_LEDGER`, `ROMANCE_RELATIONSHIP`, `NEON_B04_B06`, `THREADNAUT` and
`PUNCTURE` returns zero hits. The one `B03_B04_HANDOFF` hit is §24's retraction citing it.

So **four author locks exist only inside proposal documents**:

1. Baz dies at the end of B03; the cast learns at the start of B04
   (`BAZ_DEATH_TIMING_RULING_2026-09-19.md`)
2. Bastien "Baz" Arnaud is the current canon identity name
   (`B03_B04_HANDOFF` §"AUTHOR LOCK — Baz identity name")
3. Tahl is not a primary character in B01–B03 and may not be named before the B03
   epilogue (`B03_B04_HANDOFF` §"Governing current author rulings" item 5)
4. The VT contact escalation ladder (`B03_B04_HANDOFF` §24)

`CLAUDE.md` §9 says a change to canon state that leaves the ledger stale is half-finished
work. This entry is the ledger catching up; it does not apply any of the four.

## 4. Finding 2 — a THIRD A–E authority lettering is now in use

`CLAUDE.md` §5 says **one scheme only**, and already records one retired competitor in
`recovery/checkpoints/RECOVERY_STATE_CHECKPOINT_2026-09-15.md`. A third has appeared at
`NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT_2026-09-19.md` §1 and is stamped on 16 ND items
(`**Authority:** B` ×14, `B/C` ×1, `A/C only where user selection is clear` ×1).

| Letter | `CLAUDE.md` §5 tier | SOURCE_AUDIT §1 authority |
| --- | --- | --- |
| A | Explicit locked source canon | Explicit author locks in the source conversation |
| B | Explicitly approved development outputs | **Purpose-built backup/archive chats** populated by the user |
| C | Existing GitHub canon | **Approved development outputs** |
| D | Other sources — Notion, drafts, anything recovered | **Later recovery/reconciliation summaries** |
| E | Memory | Memory summaries / recollection |

A and E roughly align. **B, C and D each mean something different in the two schemes**, so
a reader carrying one scheme into the other misreads every stamp — `Authority: B` reads as
"approved development output" under §5 and as "archive chat" under the audit.

**Not converted, and conversion is not mechanical.** The audit's B ("purpose-built
archive chats the user explicitly defined as canonical storage, excluded exploration from,
and pasted retained material into") has no §5 equivalent: under §5 those exports are
tier D, which is exactly the distinction the audit was built to preserve. Converting would
destroy information. Recorded as a question for James (§9 below) rather than resolved here,
per `CLAUDE.md` §4.

## 5. Finding 3 — the classification vocabulary drifted, the same way `MODE` did

SOURCE_AUDIT §2 declares six labels: `PRESENT`, `COMPRESSED`, `MISSING`, `CONFLICT`,
`SUPERSEDED`, `UNCERTAIN`.

Across the three ledger passes there are **58 `Classification:` stamps using 37 distinct
values**, of which **3** are exactly one of the declared six. The rest are compounds and
inventions: `PRESENT / CONFLICT WATCH`, `PRESENT, but under-protected`,
`SOURCE RECOVERED / HIGH VALUE`, `CONFLICT RESOLVED BY CURRENT TIER-1`,
`PROCESS DECISION`, `MISSING SOURCE / PROVENANCE GAP`, and thirty more. Several differ
only by trailing whitespace.

This is the `LORE`/`POL`-into-`MODE` failure again (§13, decisions §4.1): a vocabulary
with no room for a needed distinction grows compounds instead of a new axis. The
compounds are pairing a *state* (`PRESENT`, `MISSING`) with a *disposition*
(`CONFLICT WATCH`, `DO NOT PROMOTE`, `HIGH VALUE`). That reads as two axes, not one —
but naming them is an author call, not a cleanup.

## 6. Finding 4 — the VT ladder is locked, and three artifacts now contradict it

`B03_B04_HANDOFF` §24 records an author lock:

> **B01 NOTICE → B02 BRUSH → B03 PUNCTURE → B04–B05 EDGE / RECURRENCE → B06 SLIP → LOOM ECHO**

**It has no home in the schema.** `rules/canon_rules.json` has no VT-contact axis, no such
`controlled_vocab` list, and `grids/episode_beats.csv` has no column for it. This is the
`STRAIN`/`LOAD` shape exactly (§13, decisions §1.4): a real distinction with no field to
carry it. Note also that decisions §1.2 disposed of `BRUSH` and `EDGE` as *"not states —
the operative token is `VT`"*; that ruling was about `res_states` and stands, but both
tokens are now formal event classes on a different axis, so the disposal no longer
disposes of them.

**Three existing artifacts describe the B03 event in terms the ladder retires:**

| Artifact | Says | Under the ladder |
| --- | --- | --- |
| `act_overlays/act_overlay_S1_T1_B03_A3.json`, exception `reason` | "First and only VT brush in the Veil trilogy" at `S1.T1.B03.A3.E14` | that event is a **PUNCTURE**; the brush is in B02 |
| ND-004, "The Veil trilogy contains exactly one VT brush" | recommends preserving the trilogy-wide exclusion rule | the exclusion still holds for *brushes*, but B02 now carries one, so "first" moves |
| `milestones_payoffs_PROPOSED_LOAD_v2` row `M09` | "The chronicler's VT **slip**" at `B03.A3.E14` | the ladder explicitly says *"Do not call the B03 epilogue a slip"*; `SLIP` is reserved for B06 |

There is also a **placement** tension: the ladder puts the PUNCTURE in the B03 epilogue,
while the recovered packet anchors the event at `A3.E14`, mid-Act-III.

**Nothing changed.** The overlay `reason` is substrate and quotes its source verbatim, and
the ladder proposal itself instructs: *"If author locks this ladder, update Channel/VT and
Mechanica only after the broader recovery phase. Do not modify Tier-1 rules during forensic
reconstruction."* Held on that instruction.

## 7. Finding 5 — three records disagree about who performs the Mending

| Record | State |
| --- | --- |
| `CLAUDE.md` §4 | **Open.** "the export passage is an audit of that event and does not name them" |
| This ledger §24 | **Resolved.** `B09.A3.E14` carries the trio act *and* "Silence dissolves into Lucien. Hope dissolves into Caro"; both lines were right |
| ND-013 | **CONFLICT WATCH.** "This remains an unresolved fork and must not be silently merged into the structural event" |

ND-013's authority is `B/C` and it predates the Notion bundle that produced §24's reading,
so the likely history is that §24 supersedes it. **But that is an inference, not a record**,
and §24's "resolved" was written by this session without ND-013 in view. All three states
are left standing and flagged. At minimum `CLAUDE.md` §4 and ND-013 need to be reconciled
with §24, and if §24 overreached it needs withdrawing — that is question 1 in §9.

## 8. Finding 6 — there are two different Book 9 epilogues, and §25 only saw one

§25 recorded the Book 9 three-act ruling and left open "whether Book 9's epilogue is three
or four episodes", citing `VEIL_STRUCTURE` part 4 §4, which compresses the Notion Final
Beat Bible's six Act IV beats (E16 Seraphine · E17 Lucien · E18 Caro · E19 Elisabet ·
E20 Kade posts the first LT message · E21 Tahl's Echo).

**ND-015 gives a different epilogue from a different source** — the Loom Final Canon
backup, authority B:

1. Elisabet/Rex ↔ Kade/Lacuna holochat
2. Kade writes the first post-Mending **MT** message
3. Lacuna presses "post"
4. stars "twinkling in conversation"
5. **LT** handshake invitation using Tahl's triangle

Five beats, not six. Only the Kade-posts beat clearly overlaps, and even there the two
sources disagree on whether the first post is MT or LT — which touches the `MT becomes LT`
rename recorded at §24. The Notion version's three ascension codas and Tahl's farewell are
absent; the holochat, Lacuna pressing post, and the triangle handshake are absent from
Notion.

So the epilogue-length question is **not** "three or four" — it is an exports-versus-Notion
fork of the same shape as the Veil two-draft problem, and it must be resolved before the
length is chosen. §25 is amended by this entry rather than rewritten, since its own text is
accurate about what it had read.

## 9. Finding 7 — `CLAUDE.md` §4's Veil two-draft item is stale

§4 lists four sub-questions under "Which Veil draft is canon". Three now have author
rulings recorded in the new documents:

| §4 sub-question | State after this session |
| --- | --- |
| whether Baz dies in Book 3 | **Ruled** — end of B03, cast learns at start of B04 |
| whether Tahl and Caro appear in Books 1–2 | **Ruled for Tahl** — not a primary character in B01–B03, not named before the B03 epilogue. Caro not addressed |
| whether the Caro–Elisabet romance exists in Veil | **High-confidence recovered, not ruled** — "Veil seeds attraction", `ROMANCE_RELATIONSHIP` §2, marked NON-CANONICAL |
| whether Veil points at Santa Fe | **Untouched** |

`CLAUDE.md` still tells the next session all four are wide open. It is corrected in the
same commit as this entry, marking each sub-question with its actual state and keeping the
item open on the two that remain.

## 10. Smaller findings

**`Technarch` re-entered — corrected.** The retired spelling came back in six
`proposals/` documents (including both milestone load CSVs) and in two Claude-authored
`recovery/` audits. `Technarc` is canonical (decisions §6.4, ledger §16.1) and faction
naming is canon, so this is a ruled correction rather than a decision. Applied in a
separate commit:

| File | Corrected | Preserved |
| --- | --- | --- |
| `REX_TAN_RECOVERY_SOURCE_AUDIT_2026-09-19.md` | 16 | **4** |
| `BAZ_WAREHOUSE_INCIDENT_RECOVERY_2026-09-19.md` | 4 | 0 |
| `B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md` | 1 | 0 |
| `NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT_2026-09-19.md` | 1 | 0 |
| `NARRATIVE_DECISION_LEDGER_PASS3_NOTION_CANON_RECOVERY_2026-09-19.md` | 1 | 0 |
| `VEIL_MT_THREADNAUT_BREADCRUMB_GRID_2026-09-19.md` | 1 | 0 |
| `milestones_payoffs_PROPOSED_LOAD_2026-09-19.csv` (row `M30`) | 1 | 0 |
| `milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv` (row `M30`) | 1 | 0 |

The four preserved are genuine quotations of older material and are evidence: the
`"Rational Thread / Technarch defector / post-Mending leader"` package label, the
`"loyal Technarch engineer slowly defects"` phrasing, the B1 character list's
`"Technarch-adjacent; logistics-focused, skeptical but decent"`, and the line glossing
what `"Technarch-adjacent"` means. A fifth line in that file carried curly quotes around
`"loyalty"` rather than around the faction name, so it was the document's own prose and
was corrected.

PASS3's hedged `Technarc/Technarch containment` collapsed to `Technarc containment`.

The repository now reads **200 `Technarc`** and **zero `Technarch`** outside `CLAUDE.md`,
this ledger, `CANON_DECISIONS_2026-09-18.md`, `PROPOSAL_BRANCH_MERGE_PREP_2026-09-19.md`,
the four Rex quotations, and the three author-uploaded 2026-09-19 bundles
(`SAGA_TIMELINE`, `VEIL_STRUCTURE`, `NOTION_RECOVERY`) — which are originals under §1.0
and are not edited in place. `proposals/`, `canon/`, `rules/` and `grids/` are clean.

**`Threadnaut` has 84 references and no canon file.** It appears 68 times in `proposals/`
and 16 in `recovery/`, and **zero times** in `canon/`, `rules/` or `grids/`. It is now
load-bearing: the B03 epilogue reveal architecture and a whole 21-beat breadcrumb grid
depend on it. This is the same shape as work-queue item 9b (Silence and Hope): a
structurally essential entity with no Tier-1 file. Proposed as a queue item, not added
unilaterally — question 3 in §11.

**The MT breadcrumb grid asserts an open question as a governing lock.** Its §"Governing
locks" reads *"MT is mortal technology/media. No device accesses or transmits VT."*
`CLAUDE.md` §4 lists how `MT` reconciles with the infrastructure layer as **open**
(options A/B/C, `CHANNEL_NAMES_RULING` §2), and `Mortal Technology` as a name is
explicitly *not yet* retired pending it. The grid is marked NONCANONICAL so nothing is
breached — but promoting that grid would settle the MT question by side effect. Flagged
so the promotion is a decision rather than a consequence.

**`BAZ_WAREHOUSE_INCIDENT_RECOVERY_2026-09-19.md` is titled "Baz Foix".** The file was
created at `16fa7cc`, before the Arnaud identity lock landed at `6508833`/`a4324a9`, and
was never retitled. `canon/` reads Bastien "Baz" Arnaud throughout with zero `Foix`; all
21 surviving `Foix` occurrences are in `recovery/` and `proposals/` discussing the older
name, which is the right place for them. Left as found and recorded here, because the
document's own §"Superseded older staging" is where the correction belongs and a retitle
would make the file's history harder to read.

**`reports/README.md` is stale.** It records the `--all` baseline as 52 violations across
224 files with 18 `CHK_SID_FORMAT` in four files. The current figures are **61 across 243
files, 34 `CHK_SID_FORMAT` in 12 files**. The substrate figure is unchanged at 27, all
`TODO` placeholders. Every one of the 34 was checked: **all are intentional quotations** of
recovered one-digit SIDs, including the two `S1.T3.B09.A4.E16` occurrences, which are now
quotations of a form §25 ruled out. The milestone CSVs' hits are in the free-text `notes`
column citing recovered packets; their structured `target_book` columns correctly read
`B03`/`B08`/`B09`. No new real defect. The README is refreshed in the same commit.

## 11. What this adds to the author queue

1. **Does ledger §24 supersede ND-013 on who performs the Mending?** Three records
   currently disagree (§7). If §24 is right, `CLAUDE.md` §4 drops the item and ND-013 is
   annotated superseded; if not, §24 is withdrawn.
2. **Which Book 9 epilogue is canon** — the Loom Final Canon backup's five beats or the
   Notion Final Beat Bible's six (§8)? The three-or-four-episode question from §25 cannot
   be answered before this one.
3. **Is `Threadnaut` a Tier-1 recovery item**, alongside Silence and Hope (queue 9b)?
4. **Which authority lettering governs the narrative decision ledgers** (§4)? The two
   schemes are not inter-convertible without losing the archive-chat distinction.
5. **Do the classification labels need a second axis** — state plus disposition (§5)?

None of the five is decided here.

## 12. Addendum — `B09_ENDGAME_MENDING_ECHO_RECOVERY_2026-09-19.md`

The parallel session pushed an eleventh document while this review was being committed.
It changes two findings above and adds a tenth.

### It makes a third Book 9 epilogue rendering, not a second

Finding 6 (§8) recorded two. There are three, from three sources:

| Source | Beats | Shape |
| --- | --- | --- |
| Notion Book 9 Final Beat Bible, "ACT IV — Afterlight" | 6 (E16–E21) | three ascension codas · Elisabet · Kade posts first LT · Tahl's Echo |
| Loom Final Canon backup (ND-015) | 5 | holochat · Kade posts first **MT** · Lacuna presses post · stars twinkling · LT handshake |
| "Older detailed" Notion epilogue (§9 of the new document) | 11 | riverfront · repaired Tahl equipment · first LT post · Elisabet joins · Caro kisses Elisabet · Seraphine/Lucien approach · Luminous Parade · triangle flicker · Tahl farewell · stars · Book 1 prologue echo |

And a **fourth open variable**: the timeskip. The new document gives "6–12 months after
Mending", notes a later act backup compressing it to "three days after", and lists
"three days vs 6–12 months vs 1–2 years" as an unresolved detail. Its own instruction is
*"Do not lock exact epilogue timeskip yet."*

So §25's three-or-four-episode question is further from settled than §8 said, not closer.
Author question 2 in §11 stands and widens: three renderings and three timeskips.

### It supports §24's `LT`-has-three-referents note, and holds the same way

§10 of the new document lists exactly the conflation this ledger flagged at §24 —
Seraphine as "Luminous Thread", `LT` as renamed `MT`, and `LT` as the post-Mending
network — and rules for recovery purposes only that **Luminous Thread is post-Mending
only** and is not the name of the Mending mechanism. Its unresolved-details list keeps
"Final LT taxonomy: channel / metaphysical mesh / cultural archive / Seraphine role" open.
That is consistent with the Post-Mending era file staying **HELD** (§18), and it does not
release it.

On the Mending itself, §12 reads *"Seraphine/Lucien/Caro are the active Mending triad"*
and says nothing about Silence and Hope. That is a fourth record on the question in
finding 5 (§7) and it neither confirms nor contradicts §24's reading — it is silent on the
metaphysical half. Question 1 in §11 is unchanged.

### Finding 10 — the ND ledger has no supersession mechanism, and ND-032 is now wrong

The new document §3 and §4 **reverse ND-032**. ND-032 is classified `SUPERSEDED` and reads:

> Older antagonist bible: Kade nearly kills Rex … Later Final Loom structure: Kade nearly
> kills **Elias**; **Rex intervenes** … The later sequence is protected.

The new document marshals eight independent sources — the Kade and Rex character sheets,
the Rex and Tahl skill trees, the Master Saga Summary, the Antagonist Architecture bible,
the Kade→Tahl heat ladder and the Loom Trilogy Canon Bible — concludes *"The repeated
historical spine is Kade → Rex, not Kade → Elias"*, reclassifies the later act-level
backup as a compression/transposition error, and records a current author ruling:
**Elias manipulates Kade → Kade attacks Rex → Tahl Echo forces recalibration.**

The reversal looks well-evidenced and is the session correcting itself, which is the
process working. **The defect is that ND-032 carries no mark.** A reader working the
decision ledger in order reaches ND-032, sees `Classification: SUPERSEDED` with the
Kade→Elias sequence "protected", and has no way to know a later document overturned it.
Nothing in the ND format records supersession *of an ND item* — the labels describe how
current authority treats a **source**, not how a later pass treats an earlier finding.

This sharpens finding 1. It is not only that the ledger missed this work; it is that the
narrative decision ledgers have no way to retire their own entries, so corrections
accumulate in new files while the superseded entries keep reading as current. That is the
same failure mode the tier-scheme duplication caused (§5 of `CLAUDE.md`), and it will get
worse with every pass.

**Not fixed here.** Annotating ND-032 means editing another session's analysis to assert
which of two readings won, and although the evidence and the author ruling both point one
way, the fix that matters is structural — an ND supersession convention — not a single
annotation. Added as question 6:

6. **Do the ND ledgers need a supersession field**, so a later pass can retire an earlier
   ND item in place instead of contradicting it in a new file? ND-032 is the first case
   and will not be the last.

END OF ADDENDUM

END OF ENTRY 26

===============================================================

===============================================================

# 27. Open questions taken to the sources — 2026-09-19

**Ruling applied:** James, 2026-09-19 — *"ND-032 is correct, Kade nearly kills Rex."*
**Then:** *"Review other questions against your own review of Notion and export chats."*

**Status:** ONE RULING APPLIED / THREE QUESTIONS ANSWERED FROM SOURCE / THREE STILL
AUTHOR-ONLY / SIX NEW FINDINGS

Method: all 22 sanitized exports searched directly, plus seven Notion pages fetched —
`BOOK 9 — LOOM III (Final Beat Bible)`, `Book 9 Epilogue — "Luminous Thread"`, the three
`ACT * SUMMARY — VEIL I` pages, and the two pages carrying `Threadnaut`.

**Note on §1 of `CLAUDE.md`.** The Notion epilogue page is a staged scene containing
dialogue. None of it is transcribed here. Beats are recorded by function only.

---

## 1. RULED — ND-032: Kade nearly kills Rex

The ruling reverses ND-032's verdict. `NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT` ND-032 is
titled *"Kade's old 'nearly kills Rex' version is superseded"* and ends *"The later
sequence is protected"*, protecting Kade→Elias. **That verdict is now wrong.**

The Kade→Rex spine stands, as `B09_ENDGAME_MENDING_ECHO_RECOVERY_2026-09-19.md` §3–§4
argued from eight independent sources.

**Source of the error located.** The Kade→Elias line comes from one place, and this
review found it — `Trilogy Act-Level Beat Backup__part02`, B09 ACT III beat 2:

> Kade nearly kills Elias; Rex intervenes; Kade snaps

That is a single act-level beat line in a compression pass. Against it stand the Kade and
Rex character sheets, the Rex and Tahl skill trees, the Master Saga Summary, the
Antagonist Architecture bible, the Kade→Tahl heat ladder and the Loom Trilogy Canon
Bible. The forensic reading — a transposition error during act-level summarisation — is
confirmed by the evidence ratio, and now by the ruling.

**Governing sequence:** Elias manipulates Kade → Kade attacks Rex → nearly kills him →
Tahl's Echo forces recalibration → Kade rejects Brightbreak → turns to protecting the
Mending.

ND-032 is **not** edited here — see §7, question 6. The ND format still has no way to
retire an entry, so editing it in place would hide the structural problem this case
exposes rather than fix it.

## 2. ANSWERED — who performs the Mending, and why every record so far was too narrow

`BOOK 9 — LOOM III (Final Beat Bible)`, **E14 "The Mending (Breathable Veil Formation)"**,
marked *"This is the cosmological core of the saga."* The beat assigns **five distinct
human functions**, not three:

| Participant | Function at E14 |
| --- | --- |
| Seraphine | opens herself; prismatic resonance flows |
| Lucien | shapes structure around her, stabilising the flow |
| Caro | modulates the emotional burden, filtering the world's pain |
| **Elisabet** | grounds all three — *"the human heart of the mending"* |
| **Kade** | holds humanity steady through MT |

And then, in the same beat: **Silence dissolves into Lucien. Hope dissolves into Caro.**
Their last act is to **form the membrane with Seraphine**.

**So the fork was never a fork.** One primary source carries both halves in one beat. This
**confirms §24's reading** and **satisfies ND-013's caution** — nothing had to be merged,
because the source never separated them.

**But both records are still too narrow.** ND-013 says the Mending is "structurally
assigned to Seraphine + Lucien + Caro" and §24 says "the trio act"; the source gives
Elisabet and Kade explicit, named functions in the event. The Act III function line shows
where the trio framing comes from and what it actually means:

> Execute the mending of the Veil, the dissolution of Silence & Hope, and ascension of the
> new triad.

**The triad is who *ascends*, not exhaustively who *performs*.** The export's
`Trilogy Act-Level Beat Backup` line *"Seraphine, Lucien, Caro complete the Mending"* is
an act-level compression of a five-function event — the same compression class as the
Kade/Elias error in §1, from the same export.

**Recommended, not applied:** §24's row and ND-013 both need correcting to the five-function
form, and `CLAUDE.md` §4 can drop the item. That is three artifacts, so it is proposed
rather than done — question 1 in §7.

## 3. ANSWERED — the Book 9 epilogue: two of the three renderings are the same content twice

Notion structures Book 9 as **ACT I · ACT II · ACT III · ACT IV · plus a separate epilogue
page**. The export structures it as **ACT I · ACT II · ACT III · EPILOGUE**.

**ACT IV's own function line gives it away:**

> **Act Function:** Resolve character arcs and **position the epilogue**.

And the book overview's narrative-function list ends: *"Create space for an epilogue
(LT / post-mending world)."* So in Notion, Act IV is not the epilogue — it points at one.
Yet the separate `Book 9 Epilogue — "Luminous Thread"` page carries **the same events**:

| Notion ACT IV (E16–E21), as codas | Notion epilogue page, as staged scene |
| --- | --- |
| E16 Seraphine · E17 Lucien · E18 Caro | beats 4–5, Caro arrives, Lucien and Seraphine approach |
| E19 Elisabet | beat 3, Elisabet joins Kade |
| E20 Kade posts the first LT message; MT becomes LT | beats 2 and 7, Kade writes and reads the first LT entry |
| E21 Tahl's Echo's final gesture, then fades | beat 8, a final VT flicker, seen only by the ascended trio |

**Act IV is the epilogue written as an act.** That is exactly the ruling of §25, and it is
now corroborated from the primary source rather than inferred: the redundancy is visible
inside Notion itself, which is why Act IV reads as a fourth act that does not behave like
one.

**Zero occurrences of "ACT IV" in all 22 sanitized exports.** The export layer is
unanimously three-act. `ACT IV` is Notion-only, and the ruling matches the export layer.

**Two genuine conflicts survive, and they are not about length:**

1. **The timeskip.** Notion's epilogue page states **6–12 months after the mending**, with
   reasons (infrastructure returns, resonance normalises, Kade grows into his voice). The
   export heads its unit **EPILOGUE — THREE DAYS AFTER**. `B09_ENDGAME` §11 adds a third
   candidate, 1–2 years, and says not to lock it.
2. **Whether the rename completes here.** Notion Act IV E20 says *MT becomes LT* and the
   epilogue page labels Kade's post the first **LT** entry, "LT (formerly MT)". The export
   epilogue has Kade write the first post-Mending **MT** message, with a separate final
   beat for the **LT handshake invitation** — i.e. LT is only *hinted*, which is what
   `B09_ENDGAME` §10 reports the later continuity audit saying.

Conflict 2 is the live one: it decides whether `LT` exists as a channel at the end of Book
9 or is only gestured at, which bears directly on the **Post-Mending era file still HELD**
over its `res_states` list (§18) and on the three-referent `LT` problem (§24). It should be
ruled with those, not separately.

**Beat counts, for the record:** Notion Act IV 6 · Notion epilogue page 9 · export epilogue
5. The export's five are numbered **EP 01–EP 05** inside a unit named `EPILOGUE`.

## 4. ANSWERED — `Threadnaut` has exactly two sources, and neither is an export

| Layer | Occurrences |
| --- | --- |
| All 22 sanitized exports | **0** |
| `canon/`, `rules/`, `grids/` | **0** |
| Notion | **2 pages** |
| `proposals/` + `recovery/` | 84 |

The two Notion sources:

- `ACT I SUMMARY — VEIL I`, cluster 3 of 7, titled **"Tahl, Threadnaut"**
- `BOOK 4 — NEON I (Final Beat Bible)`: *"Filaments begin calling him 'Threadnaut.'"*

So 84 repository references rest on two Notion lines plus author recollection. **The two
lines disagree with each other** in exactly the way `B03_B04_HANDOFF` §11 predicted: the
B04 bible bestows the name *after* Tahl becomes public, while the Act I summary already
uses it as a Book 1 cluster title. The handoff document flagged this as a terminology
conflict and said not to collapse it silently. That was right, and the conflict is real.

**The Act I support is weaker than it looks**, because that page is part of a Veil draft
that is superseded on other grounds — see §6.

`Threadnaut` remains a candidate Tier-1 gap, now with its source base measured rather than
assumed. Question 3 in §7.

## 5. NEW — work-queue item 7: all three `ACT * SUMMARY — VEIL I` pages read, none holds packets

`CLAUDE.md` §8 item 7 recorded these three as *"unread and the likeliest remaining Notion
home for Book 1 episode-level material."* All three are now read. **None holds episode
packets, and two say so explicitly:**

| Page | Structure | Statement |
| --- | --- | --- |
| `ACT I SUMMARY — VEIL I` | 7 clusters | *"No fixed episode count at this stage; episodes will emerge naturally from drafting."* |
| `ACT II SUMMARY — VEIL I` | 8 clusters | *"Episode counts will naturally emerge from cluster expansion during drafting."* |
| `ACT III SUMMARY — VEIL I` | 9 scene clusters | no episode numbering of any kind |

With §21 (the Book 1 Final Beat Bible holds 15 act-level macro beats, not packets), the
Notion Book 1 layer is now **confirmed macro-only four times over**. The hypothesis that
Notion holds the E00–E15 packets is disconfirmed for Book 1 in full.

**`Archive Veil Book 1` in the ChatGPT workspace is the only remaining candidate**, which
raises the value of work-queue items 6 and 7 again and lowers the value of further Notion
searching for Book 1 episode material.

One useful corroboration: Act I's supplement list — MT #1, Chronicle sidebar, MT #2,
Velvet Vein #1, Chronicle leak, MT #3, Filament Drop #1 — matches the "Historical density
evidence" in `VEIL_MT_THREADNAUT_BREADCRUMB_GRID` exactly. That grid's density claim is
sourced.

## 6. NEW — there is a THIRD Veil draft, and it kills Baz in Book 1

`ACT III SUMMARY — VEIL I` is Book 1. Its cluster list includes:

> 8. **The Warehouse Incident (Baz's Death)**

and its establishing list includes *"Baz's death shattering Lucien and reshaping Neon
arc"* — all in **Book 1**.

This contradicts, inside the same Notion workspace:

- `BOOK 1 — VEIL I (Final Beat Bible)`: the Baz bond forms, *"setting up Book 3 tragedy"*
- `BOOK 3 — VEIL III (Final Beat Bible)`: *"Act Function: Execute the Rupture, **kill Baz**, break the cast, launch Neon"*
- the author's 2026-09-19 ruling: Baz dies at the **end of B03**

**Provenance favours the Final Beat Bible, narrowly but cleanly.** Notion's own
last-edited stamps, same day:

| Page | Last edited |
| --- | --- |
| `ACT I SUMMARY — VEIL I` | 2025-11-23 20:18 |
| `ACT II SUMMARY — VEIL I` | 2025-11-23 20:21 |
| `ACT III SUMMARY — VEIL I` | 2025-11-23 20:24 |
| `BOOK 1 — VEIL I (Final Beat Bible)` | 2025-11-23 **22:17** |

The Final Beat Bible is roughly two hours later than the act summaries and disagrees with
them, so the summaries read as a superseded restructuring experiment. The author's ruling
agrees with the later artifact.

**This widens "Which Veil draft is canon" from two drafts to three**, and the third is the
one that is already mostly ruled against. The three act summaries also stage Tahl heavily
in Book 1 — cluster 3 "Tahl, Threadnaut", cluster 5 "Tahl's First Threshold", *"Tahl's
irreversible commitment to the Pattern"* — against the lock that Tahl is not a named
primary before the B03 epilogue.

Recorded, not resolved. The evidence points one way and the ruling agrees with it, but
declaring a Notion page superseded is an author call.

## 7. NEW — the exports asked the prologue question and never answered it

`Episode expansion process__part01` contains the question this repository is still
arguing, asked of the author during Book 1 construction:

> Should the Prologue be treated as: A) Episode 0 (outside the Act structure), or
> B) Episode 1 within Act I? Canon supports both approaches.

**No answer follows.** The next turn jumps to Episode 16. Decisions §2.2 later settled it
as `E00`.

More useful is what the export layer *does*, which is **asymmetric**:

- the **prologue** sits as **beat 1 inside ACT I** — "Prologue — Silence & Hope (canon)",
  then "2. Seraphine fails to save the swamp child"
- the **epilogue** is a **unit outside the acts**, with its own numbering restarting at
  `EP 01` — both for Book 3 (`EPILOGUE — VEIL → NEON BRIDGE`, EP 01–04) and Book 9
  (`EPILOGUE — THREE DAYS AFTER`, EP 01–05)

**That is option B** of `VEIL_STRUCTURE` part 4 §3 — `EP` in the act slot, prologue stays
inside Act I — not the recommended option A. `VEIL_STRUCTURE` argued for A on symmetry
grounds; **the recovered material is not symmetric, and never was.** It also answers part 4
§5 item 3 as a matter of observed practice: epilogue episodes **restart at `EP 01`**.

This is evidence, not a ruling. The choice between honouring the recovered asymmetry and
imposing symmetry remains the author's.

## 8. Smaller findings

**The B03 "slip" wording is quoted, not careless.** `Episode expansion process__part01`
heads Book 1's third act `ACT III — THE SLIP` and gives beat 7 as
*"THE SLIP — Tahl's first VT brush"* at EP 14–15. So milestone `M09`'s "VT slip" wording
and the overlay exception's "VT brush" wording both quote the same source line, **which
itself calls one event by both names**. That conflation is precisely what the locked
NOTICE/BRUSH/PUNCTURE/SLIP ladder exists to resolve, and it strengthens §26.6: the three
artifacts are not sloppy, they faithfully reproduce a source that had not yet drawn the
distinction.

**Notion is the `Technarch` drift source.** The Book 9 bible reads *"Overthrow Dominion
and Technarch remnants"* and *"Technarch: Collapsed"*. The parallel session was reading
Notion, so the spelling travelled with the content. The correction at §26.10 stands, and
this explains how it re-entered — it will re-enter again on every Notion pass unless the
mapping is applied at read time.

**Per-act episode restarts confirmed pervasive in the act backup.** Every act in the
`Trilogy Act-Level Beat Backup` runs its own `EP 01–EP 23/24`. `CLAUDE.md` §3's scope
warning that this is a migration pass rather than a find-and-replace is correct and if
anything understated.

## 9. What is still author-only

Questions 4, 5 and 6 from §26.11 **cannot be settled from sources** — they are decisions
about this repository's own record-keeping, and no beat bible has an opinion on them:

4. Which authority lettering governs the narrative decision ledgers (§26.4)
5. Whether the classification labels need a second axis (§26.5)
6. Whether the ND ledgers need a supersession field (§26.12) — **now urgent**, because
   ND-032 is a confirmed-wrong entry with no way to mark it

The revised queue:

1. **Correct the Mending record in three places** to the five-function form (§2) —
   §24's row, ND-013, and `CLAUDE.md` §4. Recommended; not applied.
2. **The Book 9 epilogue timeskip** — three days, 6–12 months, or 1–2 years (§3).
3. **Does the MT→LT rename complete in the Book 9 epilogue** (§3)? Rule with the held
   Post-Mending era file and the three-referent `LT` problem, not separately.
4. **Is `Threadnaut` a Tier-1 recovery item** (§4), and which of its two conflicting
   naming sources governs?
5. **Are the three `ACT * SUMMARY — VEIL I` pages superseded** (§6)? Evidence and ruling
   both say yes; the declaration is the author's.
6. **Prologue/epilogue symmetry** (§7): honour the recovered asymmetry (option B) or
   impose symmetry (option A)?
7. Questions 4–6 above, unchanged.

END OF ENTRY 27

===============================================================

===============================================================

# 28. Priorities reassessed against the build pipeline — 2026-09-19

**Direction:** James, 2026-09-19 — *"many of these comments and questions focus on
bookkeeping versus narrative structure. We need to assess and organize our priorities."*
The pipeline: extract the best versions of rules, context, characters, environments and
narrative → organize them → build a saga timeline with arcs and milestones → cascade to
trilogy, book, act, episode.

**Status:** ASSESSMENT WRITTEN / NOTHING BUILT / THREE NEW LAYERS NEED AUTHOR DIRECTION

Full assessment at `proposals/concord-2026/NARRATIVE_BUILD_PRIORITIES_2026-09-19.md`.
Recorded here in brief so the ledger carries the structural findings.

---

## 1. The cascade has containers at every level except its root

| Level | Container | State |
| --- | --- | --- |
| **Saga** | **none** — `canon/saga_overview.md` is 22 lines of orientation | **MISSING** |
| Trilogy | `rules/trilogy_context_T1/T2/T3.json` | envelopes set; each still carries its own `TODO` |
| Book | `book_context_B01..B09.json` | 9 skeletons, every field `TODO` |
| Act | 27 act overlays | bands set 2026-09-19; `act_thesis`, `deltas`, success criteria, forbidden shortcuts all `TODO` |
| Episode | `grids/episode_beats.csv` | header-only, 0 rows |

**The saga timeline has nowhere to live.** That is the highest-value structural gap and
the cheapest to close, because the content is scattered rather than missing.

**The book container already anticipates the cascade.** `entry_state`, `exit_state_locks`,
`locations_in_play`, `continuity_hooks` and `pov_targets` *are* the book-level timeline,
and all five are `TODO` in all nine books. The schema was built for this and never filled.

## 2. The five extraction categories

| Category | Resolution | Note |
| --- | --- | --- |
| Rules | **High** | 25 files plus `canon_rules.json`. Nearly done; needs consolidation, not recovery |
| Context | **Containers only** | Blocked on narrative, not schema |
| Characters | **High for 14** | 62 files in a consistent four-file pattern plus 15 POV files — the only *finished* layer in the repo, and the obvious template for the rest. Absent: **Silence**, **Hope**, **Threadnaut** |
| Environments | **ABSENT** | See §3 |
| Narrative | **Recovered, unorganized** | 0 rows in all six grids |

## 3. Dimensions not yet considered — three named, four more found

**Locations — no layer exists.** No `canon/locations/`. Eight canon files mention
"location" at all; 6 New Orleans, 3 Santa Fe, 1 Honey Island; zero in `rules/` and
`grids/`. Three consequences already biting: `ENV` is an ECID field with **no vocabulary**
(`reports/README.md` records it), `locations_in_play` is `TODO` in all nine books, and
**the narrative-location versus character-location distinction James raised is not
currently expressible** — the first is a place with function and constraints, the second
is a character *state* belonging on an arc timeline, and no field separates them. The saga
is geographically dense in the recovered material, so this is recovery, not invention.

**Combat — no system.** 3 canon mentions, 1 in `rules/`, 0 in `grids/`, 0 hits for
"fight" — against recovered Loom material full of siege lines, Dominion's final push,
Virelli's attempt on Seraphine, and the just-ruled Kade-attacks-Rex sequence. The open
question is what *kind* of system the saga needs, and it has never been put.

**Antagonist arcs — material without structure.** `canon/factions/` has 10 files and
`episode_beats.csv` has an `antagonist_pressure` column, with nothing connecting them.
ND-020–ND-029 are the richest existing material and are prose with no grid to carry them.

**Four more found:** character arcs have no structured layer (66 files mention "arc" as
prose; `character_state_deltas` is an empty array in all 27 overlays); `pov_targets` is
`TODO` in all nine books; there is **no chronology artifact anywhere**, with three
timeskips open; and `motif_1`/`motif_2` have no vocabulary binding them to
`rules/symbols/`.

## 4. The open questions re-sorted — and one bookkeeping question that is really a step-1 question

**Blocking the cascade:** the proposal-branch merge (work-queue item 1); **which Veil draft
is canon**, now three drafts (§27.6); `EP` in the act slot, which gates the milestone load
that is step 3's raw material; and whether the `MT`→`LT` rename completes in the B09
epilogue. The first two are the real gates.

**Deferrable:** the B09 timeskip, the Threadnaut naming conflict, whether the three
`ACT * SUMMARY — VEIL I` pages are superseded, prologue/epilogue symmetry.

**On §26.4, §26.5 and §26.12 — two can wait indefinitely; the third is misframed.** Step 1
says *extract the best versions*, which presupposes we can tell which version is best.
**ND-032 is the proof that we currently cannot**: a decision-ledger entry marked
`SUPERSEDED` that protected the wrong sequence, with no way to mark it once a later pass
disproved it. James caught it; an extraction pass run earlier would have pulled
Kade→Elias into canon as a sourced decision.

So the question worth asking is not "do the ledgers need a supersession field" but **what
is the rule for deciding which of two conflicting recovered versions wins.** ND-045
already proposes a good one — later explicit author decisions beat earlier "Final Canon"
labels; exact pasted backups beat assistant summaries; unique Notion detail with no later
contradiction survives as candidate; conflicts are marked superseded or unresolved, never
merged. **Ratifying ND-045 as the extraction rule is the one bookkeeping decision that
pays for itself**, and the lettering and label questions can then be dropped.

## 5. What was recommended to stop

Further Notion searching for Book 1 episode packets. §27.5 closed it with four
confirmations. `Archive Veil Book 1` in the ChatGPT workspace is the only remaining
candidate — work-queue items 6 and 7.

## 6. Three shape questions before anything is built

1. **Locations:** one layer with a type field, or two — narrative locations and
   character-location states?
2. **Combat:** resolved through existing resonance mechanics, or its own axis the way
   `LOAD` was?
3. **Antagonist arcs:** the same arc treatment as protagonists, or a pressure-curve model
   tied to `antagonist_pressure`?

END OF ENTRY 28

===============================================================

===============================================================

# 29. Locations, combat and antagonists — primer review — 2026-09-19

**Direction:** James, 2026-09-19 — locations and combat *"should have a lot of primer
material in notion, chat exports, and maybe early git materials. Those should be reviewed
prior to acting or consolidating."* On antagonists: *"primary antagonists are treated
similar to protagonists (i believe this system already exists or was begun) and antagonist
groups can operate at a pressure curve model."*

**Status:** REVIEWED / NOTHING CONSOLIDATED / §28's ASSESSMENT PARTLY SUPERSEDED

Full review at `proposals/concord-2026/LOCATIONS_COMBAT_ANTAGONISTS_PRIMER_REVIEW_2026-09-19.md`.

---

## 1. The correction to §28

§28 recorded locations, combat and antagonist arcs as three layers that "do not exist" and
needed author direction on **shape**. **That was true of the repository and false of the
project.** All three are already-designed systems that never migrated to GitHub.

| Layer | §28 said | Actual |
| --- | --- | --- |
| Locations | absent, needs a shape decision | **Full CANON system in Notion.** Recovery plus one collision ruling |
| Combat | absent, needs a shape decision | **Full CANON system in Notion.** Migrates into existing UARS/scene-type structure; no new schema |
| Antagonist arcs | material without structure | **Template and curves both already exist** in the repo and the exports |

**None of the three needs a design proposal.** The shape questions §28 §6 posed are
answered by sources, not by decisions.

## 2. Locations — `HYBRID RESONANCE GEOGRAPHY SYSTEM — CANON` (Notion, 2025-11-27)

Nine sections, built on the project's own spine: *"Resonance geography = emotional
topography + civic stress + metaphysical pressure."* It **evolves per trilogy** — Veil
shards → Neon Zones → Loom Corridors → post-Mending Echo Nodes — with five Neon Zone
types, four Loom Corridor classes and a city-by-city map for New Orleans, Vienna,
Singapore, Reykjavík and Marrakesh. Two further city bibles exist: `NEW ORLEANS CITY BIBLE
(FINAL CANON)` (2025-12-01, neighborhood granularity) and `REYKJAVÍK — QUIET RESONANCE ZONE
(Deep-Pass v1)`.

**It already makes the distinction James raised.** §V is the narrative-location layer
(places with resonance properties); §VIII "Character Interaction Rules" is the character
layer (Seraphine senses distortion first, Rex calculates corridor-edge routes, Kade
destabilizes Amber Drift). One place layer plus a character-interaction layer referencing
it — recorded, not decided.

**It corroborates the Warehouse Incident independently.** The New Orleans map reads
*"Violet Bloom: Warehouse District (Baz's death site)"*, and Violet Bloom is defined as
near-shard rupture conditions — which is what `BAZ_WAREHOUSE_INCIDENT_RECOVERY` concluded
from unrelated evidence.

**NEW COLLISION — the `Corridor` token.** `canon_rules.json` uses `CORRIDOR` as an ECID
field with vocabulary `U1`–`U7`, and Mechanica §24–25 defines Corridor Tiers as
resonance-intensity bands. The geography system uses **Corridor** for named Loom travel
routes in four classes. Same word, two objects — the `VT` situation again. **Do not merge
and do not rename either before a ruling.** This blocks the locations migration.

## 3. Combat — a full system in Notion; the repo has one section

The substrate has exactly two things: Mechanica §57 `SCENE-TYPE APPLICATION`, which
includes an **Action / Conflict** type (rising cost curves, environmental damage, visible
failure risk), and an unticked checkbox at
`rules/resonance/EMOTIONAL_MODES_AND_INSTABILITY.md:207` —
`[ ] Optional: add civic vs combat emotional profiles`.

Notion holds six relevant pages, most in a `Resonance Mastery Mechanics` folder:
`CONCORD SAGA — CONFLICT ENGINE (v1.0)`, `COMBAT SKILL TREES (INTEGRATED)` Part I,
`OPPONENT ARCHETYPES & CHARACTER RESPONSES` (a *Resonant Combat System Module*),
`RES0NANT COMBAT BENTO v1`, `HUMOR & CONFLICT BENTO` (which carries a **Conflict Ladder**),
and `Character Engine Canon - Compact Bento` (§VIII *Combat / Action Translation*, "Character
Engine Bento v3 — Unified Action–Resonance System").

**The shape question is answered by the `Phase 1A Migration Plan` export**, which places
combat inside section 2, *UARS action economy and cost model*: *"Combat vs non-combat (how
UARS expresses differently in action scenes vs civic scenes vs intimacy)"*, alongside
*"Action permissions by corridor/weather"*. So **combat is a mode of UARS expression, not
a separate axis** — the opposite of the `LOAD` case. It needs no new schema, only
migration.

## 4. Antagonists — confirmed, and ahead of the protagonists

James's recollection is right and understated. **Saeko, Ito and Han Wei carry five files
each** — `ID`, `EBCI`, `Appearance`, `Render` **plus `Backstory`**, which no protagonist
has. Elias and Virelli carry the standard four. All five have POV files. Every protagonist
carries exactly four.

**The gap is on the protagonist side, and it is the lead.** Seraphine has three files and
**no `EBCI`** — `SeraphineAppearance`, `SeraphineIdentity`, `SeraphineRender`. She is the
only main character without an EBCI and the only one breaking the `*ID.md` convention,
while `source_canon/characters/seraphine_full.md` sits at 830 lines stamped `FINAL CANON`
behind the unresolved §1.1 authority conflict.

**The group template already exists and is unevenly applied.** Concord has a directory of
5 files (EraFunction · Limits · Mandate · Relationships · Structure) and Filaments 6
(adding Aesthetics · CanonLocks · Origin). Technarc, Dominions, Choirless, Brightbreak and
Manufactured Metas are **single files**. `EraFunction` is the pressure-curve field in
everything but name, so James's proposal is an existing convention to extend, not a new
model.

**The curves are already written.** `_ Narrative Structure _` carries a saga-level
antagonist evolution — *"Veil: secretive, institutional antagonism. Neon: splinter groups,
weaponized tech, fear populism. Loom: global panic and collapse-level human conflict"* —
and the `Saga Beat Expansion Pipeline` audit carries per-faction curves, e.g. *"Choirless:
Whispered ideology in Neon 4 → traction in Neon 5 → violence in Neon 6 → full militant
splinter in Loom."* Extraction into the faction files and binding to `episode_beats.csv`'s
existing `antagonist_pressure` column is the work.

## 5. Early git materials — nothing was lost

Checked all refs with `--diff-filter=A` and `--diff-filter=D`. **No location, geography,
environment, combat or action file has ever existed in this repository**, and only two
files have ever been deleted (a superseded unsplit export HTML and a stray `.pyc`). The
repo began with character and faction files and the systems layer arrived later and
partially. Nothing to recover from history.

## 6. INCIDENTAL — the Project Model Set names 14 advisory groups, none migrated

`Character involvement pacing__part02` holds the **Project Model Set**, *"a clean,
authoritative list … ONLY what is actually saved"* — five items. The repository has item 1
and part of item 2.

**Item 3, Advisory Groups (Core, Canon), saved 2025-11-16:** Art Direction Council ·
Continuity Wardens · Humanity Pass Council · Paratext Architecture Board · Breadcrumb /
Foreshadowing Weavers · **Action Realism Board** (*grounded conflict, violence realism,
physical logic*) · **Environmental Texture Board** (*ensures each location maintains
distinct sensory/cultural identity*) · Serial Release Calibration Team.

**Item 4, Provisional:** Visual Effects / Cinematic Imagery Panel · Resonant Tech
Calibration Review · Emotional Authenticity Advisory · Mystery/Conspiracy Calibration
Circle · Narrative Soundtrack Council · **Geography & Location Logic Panel**.

**All fourteen are absent from the substrate.** `canon/editorial_lenses.md` captured item 1
only. Directly relevant here: **locations and combat each already have a governance body in
canon**, and locations have a second pending. Item 5 also preserves an explicitly open
question: *"Filaments Call Sign 'K' Question — not yet resolved."*

## 7. INCIDENTAL — two December memory exports postdate everything else

`25.12.06 Memory List` (2025-12-06) and `Memory Set 25-1212` (2025-12-13, in a separate
`Concord Saga 25-1212 Export` folder) are later than every other artifact surveyed in this
project, which runs 2025-11-23 to 2025-12-01. They name ActionState routing
(Baseline→Rupture→Proto-Ascendant), UARS, corridor ecology, environmental modifiers,
resonance weather, the RP equation and the >20% boost rule.

Under ND-045 — later explicit material outranks earlier "Final Canon" labels — **these
are the best available index of the project's end-state canon**, and should be read before
any consolidation pass. Neither is among the 21 sanitized exports.

## 8. What this adds to the author queue

1. **The `Corridor` token collision** (§2) — blocks the locations migration.
2. **Are the 8 canon advisory groups still canon**, and do the 6 provisional ones ratify
   (§6)? Two of them govern exactly the subjects under review.
3. **Seraphine's missing `EBCI` and nonstandard `Identity` filename** (§4) — oversight or
   deliberate? Entangled with the `source_canon/` conflict.
4. **Should the December memory exports be the canon-state index** for extraction (§7)?
5. **The `Filaments Call Sign "K"` question** (§6), recorded as explicitly unresolved.

END OF ENTRY 29

===============================================================

===============================================================

# 30. Recovery passes 1–3 performed — locations, combat, antagonists — 2026-09-19

**Direction:** James, 2026-09-19 — *"proceed with recover passes, and review updated
repo."*

**Status:** THREE PASSES COMPLETE / NOTHING MIGRATED / ONE TIER-1 DEFECT FIXED

| Pass | Document | Sources |
| --- | --- | --- |
| 1 | `recovery/LOCATIONS_RECOVERY_2026-09-19.md` | 3 Notion pages |
| 2 | `recovery/COMBAT_CONFLICT_RECOVERY_2026-09-19.md` | 2 Notion pages |
| 3 | `recovery/ANTAGONIST_ARCHITECTURE_RECOVERY_2026-09-19.md` | 2 sanitized exports |

§29's central claim holds: **all three layers were already designed and simply never
migrated.** None needed a shape decision. Details live in the three documents; what
follows is what the ledger must carry.

---

## 1. Blockers found, none resolved

**Three location taxonomies, none matching** (pass 1 §2). The geography system uses five
Neon Zone types; the New Orleans bible uses `Blue Pulse Corridor` / `Red Lantern
Faultline` / `Violet Spiral`; Reykjavík uses the shard progression as a spatial tier. The
two New Orleans maps also disagree per-neighbourhood — Tremé and Marigny are **Blue
Pulse** in the system and **Red Lantern Faultline** in the city bible; only the Warehouse
District agrees, and only on colour. The city bible is four days later and stamped
`FINAL CANON`. **`ENV` vocabulary cannot be derived until this is ruled**, because the two
sources would produce different vocabularies.

**The `Corridor` collision is four-way, not two** (pass 1 §3): the ECID `CORRIDOR` axis
`U1`–`U7`; Loom Corridors as named travel routes; `"Blue Pulse Corridor"` as a *bloom
zone*; and ordinary streets (`Laugavegur Corridor`, `RIVER CORRIDOR`). Sense 3 is the
worst, applying the word to the thing sense 2 explicitly contrasts with — *zones are
chaotic pockets, corridors are safe routes*. ~~**Blocks the locations migration.**~~
**RULED 2026-09-19, Ruling 2 — see §33 and §34. The safety framing is superseded and this
objection is withdrawn; the distinction is geometric.**

**Two protagonist surnames disagreed with Tier-1 canon** (pass 2 §3) — **RULED 2026-09-19,
see §31: `canon/` is final.** Notion's combat skill
trees read **Caro Gauthier** and **Kade Rios**; `canon/` reads **Carolina "Caro" Alvarez**
and **Kade Harper**, five files each. `Gauthier` and `Rios` appear zero times in `canon/`.
The other five core names agree across both. This belongs with the parallel session's
`CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md`, which does not currently cover either.

## 2. What the passes settled without a decision

**Locations — the narrative/character split is in the source.** `HYBRID RESONANCE
GEOGRAPHY SYSTEM` §V is the place layer; §VIII "Character Interaction Rules" is the
character layer (Kade *destabilizes* Amber Drift zones; Rex calculates corridor-edge
routes; Elisabet's clarity-breath smooths a Drift Zone). One place layer plus a
character-interaction layer referencing it — exactly the distinction James raised,
already drawn.

**Combat — confirmed from the other direction.** The skill trees' six tiers **are** UARS
categories: Tier 3 is *Resonance Boost*, Tier 5 is *Failure Mode*. §29 read the `Phase 1A`
export as putting combat inside the UARS action economy; the skill-tree structure confirms
it. **No new schema is needed.** Combat also defaults to de-escalation — Elisabet and
Lacuna both neutralise nonviolently, and only Rex carries *"weapon proficiency high"*.

**Antagonists — both halves of the ruling already exist.** The individual half is done in
`canon/` (five antagonists at or above protagonist file parity). The group half is in the
exports as a **named "Antagonist Pressure Audit"**, with per-faction curves already
written and audited. The Choirless entry is the model case: *whispered ideology Neon 4 →
traction Neon 5 → violence Neon 6 → full militant splinter in Loom*, doctrine attached.
The saga-level curve is stated as **Institutions → Splinters → Extremists → Collapse
panic**, and two of the architecture's five immutable rules are already invariants in
`canon_rules.json`.

## 3. NEW — a three-pass integration pipeline was designed and abandoned

`_ Narrative Structure _` closes its antagonist compression with a next-steps plan sitting
exactly at the intersection of all three layers recovered here:

| Pass | Would produce |
| --- | --- |
| Environmental × Antagonist | **"Antagonist Geography Bible"** |
| Resonance × Antagonist | **"Resonance–Antagonist Interaction Bible"** |
| Full tri-weave | **"Civic Resonance Conflict Atlas"** |

**None of the three exists** — not in Notion, the exports, or the repository. The
conversation offered A/B/C, recommended Pass 1, and moved to an unrelated topic without an
answer. Same shape as the abandoned prologue question (§27.7).

Its worked examples — Virelli onto Vienna, Saeko's marches onto fractured Uptown,
Technarc Hardliners anchoring Singapore → AR instability → containment cordons — are
consistent with the geography system recovered in pass 1. **The two documents were written
to fit together and never joined up.** This is the most concrete "organize" step (James's
step 2) that the sources themselves propose.

## 4. NEW — Silence and Hope are characterized mechanically for the first time

The `CONFLICT ENGINE (v1.0)` vulnerability-trigger list ends with two entries that matter
for work-queue item 9b:

- **Silence** — paradox loops, emotional noise
- **Hope** — emotional overload, compassion fractures

and mode `M5` Cosmological names *"Silence paradox loops, Hope overload, VT instability"*.

§22 recorded the 21 exports as holding essentially nothing on them. This is thin — two
lines — but it is the first located source that gives them **mechanical** properties
rather than naming them. Notion `08.10` and `08.11` remain the primary 9b targets.

## 5. FIXED — 69 ChatGPT citation artifacts in three Tier-1 files

Found while cross-checking the protagonist surnames. `TahlID.md` (27), `LacunaID.md` (21)
and `KadeID.md` (21) carried stray `:contentReference[oaicite:NN]{index=NN}` markers —
migration residue never cleaned. The first line of `KadeID.md` read
`- **Name:** Kade Harper :contentReference[oaicite:27]{index=27}`.

**Verified lossless before removal:** 68 of 69 sat at end of line, and the single mid-line
case was two consecutive markers at a line end. Nothing but whitespace followed any of
them. `canon/`, `rules/` and `grids/` now read **zero**.

This is tool residue, not canon, so removing it was not a canon decision. It was **not**
one of the §9.1 known defects — it had not previously been noticed. Validator unchanged at
27 substrate violations.

## 6. Repository review — the parallel session

Fourteen commits since `973a7a0`, a secondary/tertiary **character and casting** pass:
audit passes 1–3, then editorial casting resolutions for NOLA civic, Filament, Saeko
orbit / civilian radicalization, Reykjavík, Vienna, Singapore, global place anchors and
media supplements, plus a Choirless/Koro Ito forensic recovery, a trilogy cast recurrence
check, and `CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md`.

The manifest is disciplined — `CONSOLIDATED EDITORIAL PROPOSAL — DO NOT MIGRATE TIER-1
CANON YET`, an explicit approval gate, a six-step migration procedure and a KEEP / RENAME /
MERGE / DEMOTE legend. It uses the SOURCE_AUDIT authority lettering, so the §26.4
collision persists; already flagged, not re-raised.

**Two overlaps with this session's passes need cross-checking before either promotes:**

1. The Reykjavík city bible introduces a castable tertiary character (the Harbor Shack #7
   fisherman) and `EDITORIAL_CASTING_RESOLUTION_REYKJAVIK_2026-09-19.md` casts that city.
2. The antagonist architecture's **Proto-Extremist Filament Leader — unnamed youth who
   seeds splinter militancy** is an uncast role, and both the Filament and civilian
   radicalization casting resolutions are live on that territory.

Neither is a conflict yet. Both become one if the two lines cast the same slot differently.

## 7. Prose rule observed

Four recovered pages contain prose, dialogue or generation tags: the New Orleans bible's
Sudowrite location keys, Reykjavík's "Signature Elisabet Moment" and a quoted Kade `MT`
line, and the Book 9 epilogue page read in §27. **None was transcribed.** Structure,
function and mechanics are recorded; the prose stays in Notion, and each document says so.

## 8. Added to the author queue

1. **Which location taxonomy governs** (§1) — blocks `ENV`.
2. **The four-way `Corridor` collision** (§1) — blocks the locations migration.
3. ~~Caro's and Kade's surnames~~ — **ruled 2026-09-19** (§31).
4. **Run the three-pass integration, and in what order** (§3)?
5. **Extend the faction directory pattern to the five antagonist factions?** This is the
   concrete form of the group pressure-curve ruling.
6. **Do Vienna, Singapore and Marrakesh have city bibles**, or need authoring? Only
   Reykjavík carries a `Deep-Pass v1` suffix, which implies a programme.
7. **Does the Conflict Engine's two-axis model stand** (Tier 0–5 plus C0–C5), and is its
   `Tier` the same 1–5 scale as `reader_pressure.csv`'s `intensity_1_5` and the milestone
   load's `pressure_before`/`pressure_after`? Possibly three unrelated 1–5 scales.

END OF ENTRY 30

===============================================================

===============================================================

# 31. Character names ruled final — reference alignment pass — 2026-09-19

**Ruled:** James, 2026-09-19 — *"names in repo canon/character can be considered final and
other references can be adjusted to match."*

**Status:** RULING APPLIED / 23 REFERENCES CORRECTED / QUOTATIONS PRESERVED / ONE NEW
DIVERGENCE FOUND AND FIXED

---

## 1. The authoritative list, from `canon/characters/`

| Character | Canonical name | Source file |
| --- | --- | --- |
| Baz | **Bastien "Baz" Arnaud** | `BazID.md` |
| Caro | **Carolina "Caro" Alvarez** | `CaroID.md` |
| Elias | **Elias Ward** | `EliasID.md` |
| Elisabet | **Elisabet Arnardóttir** | `ElisabetID.md` |
| Han Wei | **Director Han Wei** | `HanWeiID.md` |
| Ito | **Ito Masayuki** | `ItoID.md` |
| Kade | **Kade Harper** | `KadeID.md` |
| Lacuna | **Lacuna** (primary usage) | `LacunaID.md` |
| Lucien | **Lucien Kael** | `LucienID.md` |
| Rex | **Rex Tan** | `RexID.md` |
| Saeko | **Saeko Morita** | `SaekoID.md` |
| Seraphine | **Seraphine Vael** (birth name Seraphine Broussard) | `SeraphineIdentity.md` |
| Tahl | **Tahl Morgan** | `TahlID.md` |
| Trip | **Trip** (professional name; legal name intentionally undisclosed) | `TripID.md` |
| Virelli | **High Inquisitor Marcellus Virelli** | `VirelliID.md` |

## 2. A third divergence, found by this pass

§30 recorded two surname conflicts. A systematic sweep of every first-name/surname pair
across the repository found a **third**, and it is the most consequential because a
parallel-session document had already ruled the other way:

| Divergent form | Canonical | Where it came from |
| --- | --- | --- |
| `Caro Gauthier` | **Carolina "Caro" Alvarez** | Notion combat skill trees |
| `Kade Rios` | **Kade Harper** | Notion combat skill trees |
| **`Koro Ito`** | **Ito Masayuki** | the 2025-12-12 memory export |

`proposals/concord-2026/CHOIRLESS_KORO_ITO_FORENSIC_RECOVERY_2026-09-19.md` §I.A had
concluded: *"This resolves the previously incomplete 'Ito' reference: the historical name
is **Koro Ito**."* That conclusion was reached from the memory export without checking
`canon/characters/ItoID.md`, which is headed **ITO MASAYUKI**. The ruling settles it the
other way. The line is **not deleted** — it now carries a supersession note in place,
which is the first time a finding in this project has been retired in place rather than
contradicted in a later file (compare the ND-032 problem, §26.12).

Note the two forms differ in **given name**, not just order: Masayuki against Koro. This
is not a surname-first/given-first rendering difference.

**One apparent divergence was a false alarm.** `Seraphine Broussard` appears in
`SeraphineIdentity.md` as her **Birth Name**, with `Seraphine Vael` as the canonical name.
Both are canon; nothing to correct.

## 3. What was corrected, and what was deliberately left

**Corrected — 23 references in the documents' own voice:**

| File | Change |
| --- | --- |
| `CHOIRLESS_KORO_ITO_FORENSIC_RECOVERY_2026-09-19.md` | 7 doc-voice `Koro Ito` → `Ito Masayuki`; §I.A conclusion annotated as superseded |
| `CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md` | 3 |
| `EDITORIAL_CASTING_RESOLUTION_GLOBAL_PLACE_ANCHORS_2026-09-19.md` | 2 `Koro Ito`, 1 `Kade Rios` |
| `EDITORIAL_CASTING_RESOLUTION_VIENNA_2026-09-19.md` | 2 |
| `TRILOGY_CAST_CHECK_2026-09-19.md` | 1 |
| `ANTAGONIST_ARCHITECTURE_RECOVERY_2026-09-19.md` | canon-file table row corrected; the export quotation annotated |

**Preserved — quotations, because they are the evidence:**

- `CHOIRLESS_KORO_ITO...` lines 13 and 76 quote the 2025-12-12 memory export verbatim.
- `ANTAGONIST_ARCHITECTURE_RECOVERY` §2.3 quotes the export's key-individuals list; an
  inline note now records that `canon/` reads Ito Masayuki.
- The `COMBAT_CONFLICT_RECOVERY` §3 comparison table and the §30 passage keep both forms
  and are re-headed **RULED**, so the divergence stays auditable.

**Untouched by rule:**

- `recovery/source_exports/**` — originals, never edited in place (§1.0).
- `recovery/NOTION_RECOVERY_`, `SAGA_TIMELINE_`, `VEIL_STRUCTURE_2026-09-19.md` —
  author-uploaded bundles committed verbatim at `99e9927`. Between them they hold 4
  `Gauthier`/`Rios` references and 4 `Foix`. Same treatment as the `Technarc` pass.

## 4. `Baz Foix` — deliberately NOT swept

`Foix` appears 40 times across 11 files. **None was changed**, and that is a judgement
worth recording rather than a gap.

The Baz rename is **already author-locked** (`Bastien "Baz" Arnaud`, 2026-09-19), and the
surviving `Foix` references are documentation *of that rename* — identity-history
sections, supersession maps, and the parallel session's reconciliation manifest, which
exists precisely to track transfer/rename/merge decisions. `canon/` already reads Arnaud
throughout with zero `Foix`. Sweeping them would delete the record of the adjustment the
ruling describes, not complete it.

**One exception is flagged, not fixed:**
`recovery/BAZ_WAREHOUSE_INCIDENT_RECOVERY_2026-09-19.md` is **titled** *"Baz Foix —
Warehouse Incident Recovery"*, in the document's own voice, and was created at `16fa7cc`
before the identity lock landed. §26.10 already recorded this. Retitling it is a file
rename that would break the parallel session's references and obscure the document's own
history, so it is left for the author — but under this ruling it is now clearly wrong and
should be corrected when that session's manifest migrates.

## 5. Verification

- `Gauthier` and `Rios` now appear **only** in the two comparison tables and the three
  untouched author bundles.
- `Koro` now appears **only** in two verbatim quotations, one supersession note, one
  annotated quotation, and one ledger reference to a file name.
- `canon/`, `rules/` and `grids/` were **not modified** — they are the source of truth and
  already agreed.
- Validator unchanged at 27 substrate violations; 63 self-tests pass.

## 6. What this closes and what it opens

**Closes:** §30 question 3 (Caro's and Kade's surnames) and the `Ito` identity question,
which had been answered incorrectly.

**Opens nothing new**, but it makes one standing problem concrete: the
`CHOIRLESS_KORO_ITO` case is exactly the failure mode §26.12 describes. A proposal document
reached a naming conclusion from recovered sources **without checking `canon/`**, and
nothing in its format would have caught it. The rule that would have prevented it is
simple and worth stating: **`canon/characters/` is checked first on any identity question**,
which is now what the ruling says.

END OF ENTRY 31

===============================================================

===============================================================

# 32. Proposal branch fast-forwarded into `main` — 2026-09-19

**Authority:** `recovery/CANON_DECISIONS_2026-09-18.md` §6.1, executed on James's explicit
instruction 2026-09-19. **Work-queue item 1 is closed.**

**Status:** MERGED / FAST-FORWARD / NOTHING MODIFIED OR DELETED

---

## 1. What happened

```
main: 253fdf4 → 9e2f345   (fast-forward, 47 additions, 0 modifications, 0 deletions)
```

`origin/proposal/concord-2026-reconciliation` is **left in place as a ref**, now pointing
at the same commit as `main`.

## 2. Preconditions verified before touching anything

All four were checked and all four passed:

| Check | Expected | Actual |
| --- | --- | --- |
| `git rev-parse origin/main` | `253fdf42899366a8dd528ed913025737dac63706` | matched |
| `git rev-parse origin/proposal/concord-2026-reconciliation` | `9e2f3456ad0e4c17c93d4946b619934af3f12279` | matched |
| `git merge-base --is-ancestor origin/main origin/proposal/...` | exit 0 | **exit 0** |
| `git diff --name-status` between them | 47 lines, every one `A` | **47 lines, 47 `A`, 0 non-`A`** |

The diff shape is the important one: **every change is an addition.** No file on `main`
was modified, renamed or deleted by this merge, which is what
`recovery/PROPOSAL_BRANCH_MERGE_PREP_2026-09-19.md` predicted and what made the merge safe
to perform mechanically.

No conflicts were resolved, nothing was squashed, nothing was rebased, and no merge commit
was created — `--ff-only` at both the pull and the merge, and the push reported
`253fdf4..9e2f345` with no `+`, confirming no force.

## 3. Post-merge verification

| Check | Expected | Actual |
| --- | --- | --- |
| `git rev-parse origin/main` | `9e2f345…` | matched |
| `git log --oneline -1` | — | `9e2f345 Document sanitized export splitting and security handling` |
| `ls recovery/source_exports/html_sanitized/ \| wc -l` | 22 | **22** |
| `git merge-base --is-ancestor origin/main origin/claude/gifted-goodall-st4n7r` | exit 0 | **exit 0** |

**The working branch is unaffected.** `origin/main` is an ancestor of
`claude/gifted-goodall-st4n7r`, so there is no divergence and no rebase is needed; the
working branch sits 105 commits ahead of `main`. Validator on the working branch unchanged
at 27 substrate violations, 63 self-tests passing.

## 4. What this unblocks

`CLAUDE.md` §6's central warning — *"The recovery work is not on `main`"* — **no longer
holds.** `main` now carries the 21 sanitized exports plus their README, the
2026-09-15 checkpoints, and the `proposals/concord-2026/` analysis set.

Work-queue items that were **"blocked on item 1 only"** are now unblocked on that count:

- **Item 4** — migrate the Veil Consolidated Beat Bible into `book_context_B01/B02/B03`
  and the nine Veil act overlays. *Still gated by the open question of which Veil draft is
  canon (§27.6 records three drafts), so unblocked is not the same as ready.*
- **Item 5** — migrate the E16–E18 packets. The §1.5 mapping is ready and all three
  packets were verified inside their act bands on 2026-09-19.
- **Item 5a** — migrate the Book 3 Act III structural shells. Downstream of item 4, and
  still touching the open `EP`-slot question for its four epilogue shells.

Item 1's own preparation document, `recovery/PROPOSAL_BRANCH_MERGE_PREP_2026-09-19.md`,
also listed **four content conflicts the merge would import**. Those are now imported and
live on `main`. Importing them was the expected and accepted cost of the merge — they are
conflicts *between recovered documents*, not defects introduced by the merge — but they
are now `main`'s conflicts rather than a branch's, and the migration items above run into
them.

## 5. What did NOT change

- **No canon decision was made.** A fast-forward merge moves a pointer; it does not
  adjudicate anything the merged documents disagree about.
- **The proposal branch ref is retained**, per instruction.
- **`CLAUDE.md` §6 is now stale** in its "not on `main`" framing. Updated in the same
  commit as this entry; the section's file-level facts about what the branch held are
  preserved as the record of what was merged.

END OF ENTRY 32

===============================================================

===============================================================

# 33. Gate rulings applied — step 1: locations blockers closed — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md`, committed verbatim at `423984d`
before any work, per §7.

**Status:** §2 AND §3 OF `LOCATIONS_RECOVERY_2026-09-19.md` CLOSED / VALIDATOR 27 / 62,
UNCHANGED

---

## 1. Ruling 1 closed the taxonomy conflict by dissolving it

§30 recorded "three location taxonomies, none of them the same" as a blocker, and read it
as a contest between rival vocabularies. **Ruling 1 shows it was never that.** The three
are three different kinds of thing:

| Layer | Source | What it supplies |
| --- | --- | --- |
| **Type** | geography system | the **controlled vocabulary** of zone types and corridor classes. **`ENV` derives from here and only here** |
| **Name** | city bibles | **named places** — proper nouns for specific ground, each mapping onto a type |
| **Severity** | Reykjavík scheme | the **shard progression**, a scale layering over places. **Not a spatial taxonomy** |

The ruling's own line settles it: *"Red Lantern Faultline is a name, not a type."* The
New Orleans bible was never proposing a competing vocabulary; it was naming ground.

**The qualification is the operative part**, and it is broader than the contested
neighbourhoods: *"All specific type assignments are PRELIMINARY until vetted against
narrative and milestones"* — including *"the assignments both source documents already
carry."* So the geography system's own five-city map is provisional too, not just the
disputed entries. **Structure ruled, contents provisional.**

**Warehouse District resolves cleanly as a side effect.** `Violet Bloom` (type) and
`Violet Spiral` (name) were recorded as a near-miss disagreement; under the two-layer
shape they are one type and one name for the same ground. Still marked provisional.

**Scope, from the ruling:** the zone-type vocabulary appears in five files, all under
`recovery/` and `proposals/`; **the canon substrate contains none of it.** Nothing to
migrate, nothing to unpick — this is forward-looking structure only.

## 2. Ruling 2 closed the `Corridor` collision, and retired my own objection

The author's definition:

> **A corridor is a linear path or area between two known points. Context determines
> whether it is safe, dangerous, or otherwise.**

The four senses §30 recorded collapse to one definition, one scale and two instance
classes: `U1`–`U7` is **intensity measured on corridors**, Loom Corridors are **a named
class**, and Laugavegur / River Corridor are **ordinary instances, correct usage**.

**My "sense 3 is the worst" finding is withdrawn.** I argued a bloom zone could not be a
corridor because *zones are chaotic pockets, corridors are safe routes*. Safety is not
part of the definition, so the objection has no force. What decides "Blue Pulse Corridor"
is **geometry alone** — linear and connective, or a pocket without that geometry — and
that is a question about the referent, to be answered during the Ruling 1 vetting pass,
**not a naming decision now**.

**Consequential amendment:** the geography system's safe-route framing is superseded and
is amended wherever it appears — carried out as its own step.

**No renaming.** The ruling's scope note: bare `Corridor` appears in **13 places across
the canon substrate** — the EBCI header, Concord's Corridor Preservation, corridor
viability, corridor instability, corridor ecology `U1`–`U7`, corridor shifts — and **all
are correct under this definition.** None changed.

## 3. What this unblocks, and what it does not

**Cleared:** both locations blockers recorded at §30 §1. `ENV` derivation is no longer
gated on a taxonomy ruling.

**Not cleared, and deliberately so:** which type each named place maps onto. Tremé,
Marigny, the French Quarter and Bywater stay **unassigned** — not provisionally assigned —
per Ruling 1 and the instruction to leave contested ground out of the `ENV` derivation.

**Untouched:** whether Vienna, Singapore and Marrakesh have city bibles. Still open, still
gated on work-queue item 6.

## 4. One inconsistency in the rulings document, recorded not resolved

Ruling 3's standing carve-outs read: *"the author-locked controls are untouched: **Tahl
Morgan / MissingThread** and **Baz Foix** remain as locked."*

`canon/characters/BazID.md` reads **Bastien "Baz" Arnaud**, and `CLAUDE.md` §3 records
that `canon/characters/` is final. The most natural reading is that the *control* — the
Foix→Arnaud rename decision — is what stays locked, not that `Foix` is the canonical
name. That is consistent with §31, which deliberately left the `Foix` references in place
as documentation of the rename.

**Recorded, not acted on.** Nothing in this pass changes any Baz reference, and the
existing lock stands either way. Flagged so the reading is explicit rather than assumed.

## 5. Validator

`27 canon-scope / 62 all-scope` before and after. No change — this step edited one
`recovery/` document and added one ledger entry, neither of which carries validated
tokens.

END OF ENTRY 33

===============================================================

===============================================================

# 34. Gate rulings — step 2: the safe-route framing amended — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 2, *"Consequential amendment"*.

**Status:** AMENDED IN 3 PLACES / NOTHING RENAMED / SUBSTRATE UNTOUCHED / VALIDATOR 27 / 62

---

## 1. What the ruling requires

> The geography system's framing that **corridors are safe routes and zones are chaotic
> pockets** is superseded. Safety is contextual; the distinction is geometric. That line
> requires amendment wherever it appears.

## 2. Where it appears, and how each was handled

A repository-wide search for `safe route` / `safe routes` / `safe-ish` / `chaotic pocket`
found **8 occurrences outside `recovery/source_exports/`**. They are not all the same kind
of text, and they were not all treated the same way.

| Location | Kind | Action |
| --- | --- | --- |
| `LOCATIONS_RECOVERY` §1 era table — *"safe-ish paths through unsafe resonance"* | **verbatim source quotation** | **Annotated**, not rewritten — dagger note added |
| `LOCATIONS_RECOVERY` §1.6 — *"Zones = chaotic pockets · Corridors = safe routes"* | **verbatim source quotation**, headed *"as given"* | **Annotated**, heading marked superseded in part |
| Ledger §30 — the blocker record | this project's own finding | **Struck through**, pointed to §33/§34 |
| `LOCATIONS_RECOVERY` §3 | already struck through at §33 | no change needed |
| `LOCATIONS_RECOVERY` §3 amendment note | written at §33 to describe this step | no change needed |
| Ledger §33 | withdraws the objection in its own words | no change needed |
| `GATE_RULINGS_2026-09-19.md` ×2 | **the ruling itself** | **untouched** — it is the authority, committed verbatim |

**Quotations were annotated rather than rewritten.** Both surviving instances are the
geography system's own words, reproduced as evidence of what the source says. Editing them
would make the recovery document misreport its source in order to agree with a later
ruling, which is the opposite of what a recovery document is for. The same principle
governed the `Technarc` pass (§26.10) and the naming pass (§31).

## 3. What the annotations say

The corridor half of the gloss **no longer states the distinction**. A corridor is *"a
linear path or area between two known points"* — a **shape**, not a safety rating.

The clearest evidence that the old framing was already failing is inside the geography
system itself: **`Rupture Corridors`** are described there as *"extremely dangerous … lead
toward shard-cluster fail zones"*. Under *corridors are safe routes* that is a
contradiction in terms. Under the ruling it is unremarkable — a corridor in a dangerous
context. The four Loom Corridor classes were **never** a safety gradient; they are
`Humanitarian`, `Concord`, `Rupture` and `Ghostline`, which sort by **who built or uses
them and what they lead to**, not by how safe they are.

The reader-facing gloss is left standing as a simplification *for a reader*, with an
explicit note that it is **not the definition** and must not be used as a test of whether
something is a corridor.

## 4. Nothing renamed — verified

The ruling's scope note is explicit, and it was checked rather than assumed:

- Files changed by this step: **2**, both under `recovery/`.
- `canon/`, `rules/`, `grids/`, `book_context/` and `act_overlays/`: **0 files touched**.
- The substrate's `corridor` usages — the EBCI header, Concord's Corridor Preservation,
  corridor viability, corridor instability, corridor ecology `U1`–`U7`, corridor shifts —
  are **all correct under the ruled definition** and none was altered.

No mass rename. No prose rewriting. `Blue Pulse Corridor` was **not** touched: its fate
turns on the geometry test, which is a question about the referent and belongs to the
Ruling 1 vetting pass.

## 5. Validator

`27 canon-scope / 62 all-scope` before and after.

END OF ENTRY 34

===============================================================

===============================================================

# 35. Gate rulings — step 3: the two-layer location structure built — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 1.

**Status:** STRUCTURE BUILT / 31 PLACES RECORDED / CONTESTED GROUND UNASSIGNED /
VALIDATOR 27 / 62

**Artifacts:** `proposals/concord-2026/LOCATION_TWO_LAYER_STRUCTURE_2026-09-19.md` and
`proposals/concord-2026/location_places_PROVISIONAL_2026-09-19.csv`.

---

## 1. The shape

| | **Type layer** | **Name layer** |
| --- | --- | --- |
| Source | the geography system | the city bibles |
| Holds | the controlled vocabulary | proper nouns for specific ground |
| Membership | **ruled** | open |
| `ENV` derives from | **this layer only** | never |

The **shard progression** sits in neither. It is severity layering over places, and
Ruling 1 forbids treating it as a spatial taxonomy.

## 2. The type layer — ten members plus one holding token

Five Neon Zone types (`ZONE_BLUE_PULSE`, `ZONE_AMBER_DRIFT`, `ZONE_VIOLET_BLOOM`,
`ZONE_RED_FLARE`, `ZONE_SILVER_STATIC`), four Loom Corridor classes
(`CORR_HUMANITARIAN`, `CORR_CONCORD`, `CORR_RUPTURE`, `CORR_GHOSTLINE`), and `NODE_ECHO`.

Plus **`CORR_UNCLASSED`** — bookkeeping, not a class. **Nine of the eleven recovered Loom
corridors are named without a stated class**, and this token lets them be recorded without
inventing which of the four they belong to. That is a real gap in the sources, not a gap
in the structure.

**Token spellings are mechanical, not ruled.** The geography system supplies names; a CSV
field needs codes. Derived by fixed rule — group prefix plus the source's own colour or
class word — and no token carries meaning the source did not state. Changing them later
is a find-and-replace across two `proposals/` files and one `rules/` key.

## 3. The name layer — 31 places, four statuses

| Status | Count |
| --- | --- |
| `PROVISIONAL` | 17 |
| `UNASSIGNED_NO_TYPE_IN_SOURCE` | 8 |
| `CONTESTED_UNASSIGNED` | 5 |
| `PENDING_GEOMETRY_TEST` | 1 |

**Every non-`PROVISIONAL` row has an empty `mapped_type`**, asserted by a check rather
than by inspection. Contested ground is *unassigned*, never *provisionally assigned* —
which is the instruction, and the distinction that matters for step 4.

**Five contested, not four.** The ruling names Tremé, Marigny, the French Quarter and
Bywater. **`Red Lantern Faultline`** is added: it is the NOLA bible's name for
Tremé → Esplanade → Marigny, so it inherits their status. A name cannot be mapped while
the ground it covers is unmapped.

**`Blue Pulse Corridor` is held.** Its recovered extent — Convention Center → Riverwalk →
French Quarter — **reads as linear**, which would pass Ruling 2's geometry test, but it
terminates in contested ground and the ruling places the question in the vetting pass.
Recorded as pending. **Not answered.**

## 4. Two things the structure resolved on its own

**The Warehouse District.** §30 recorded it as the near-miss — "agrees in colour, differs
in term". Under two layers there is no disagreement: `ZONE_VIOLET_BLOOM` is the type,
"Violet Spiral" is the name, and the ground is the Warehouse District. One place.

**Bywater's second source evaporated.** §30 read it as a two-source disagreement between
`Amber Drift` and the NOLA bible's "Flickers → Ghostwaves". Under Ruling 1 the latter is
**shard progression, not a type**, so it was never a competing assignment. Bywater is
contested on the geography system's assignment alone — which is why the ruling names it
even though only one type was ever proposed for it.

## 5. Scope held

The ruling's scope note said the zone-type vocabulary lives in five files, all under
`recovery/` and `proposals/`, with **none in the canon substrate**. This step adds a sixth
and seventh, both under `proposals/`. **Nothing was written to `canon/`, `rules/`,
`grids/`, `book_context/` or `act_overlays/` by this step.**

## 6. Validator

`27 / 62` before and after.

END OF ENTRY 35

===============================================================

===============================================================

# 36. Gate rulings — step 4: `ENV` derived from the type layer — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 1 — *"`ENV` derives from that
layer and only that layer."*

**Status:** DERIVED AND ENFORCED / CONTESTED GROUND LEFT UNASSIGNED / VALIDATOR 27 / 62 /
71 SELF-TESTS PASSING

---

## 1. What was added

**`rules/canon_rules.json`** — two additions, the first substrate change in this queue:

- `controlled_vocab.env` — **11 tokens**: the five Neon Zone types, the four Loom Corridor
  classes, `NODE_ECHO`, and the `CORR_UNCLASSED` holding token.
- `location_system` — the type layer with each member's behaviour as the source gives it,
  the ruled corridor definition, and an explicit note that the shard progression
  contributes nothing.

**`tools/validate_canon.py`** — `ENV` joined `FIELD_VOCAB`, so it is now checked like any
other axis. `POV` remains free text.

**Six new self-tests**, pinning the four things that could drift: `ENV` is enforced; its
members are *exactly* the type layer; **named places are not members**
(`Violet Spiral`, `Red Lantern Faultline`, `Blue Pulse Corridor`, `Tremé`,
`French Quarter`); and the **shard progression contributes nothing**
(`FLICKER`, `GHOSTWAVE`, `FRACTURE`, `RUPTURE_THREAT`). Two more assert that no
non-`PROVISIONAL` row in the place registry carries a type.

## 2. Contested ground: unassigned, not provisionally assigned

The instruction was explicit, and it is now enforced by test rather than by care:
**Tremé, Marigny, the French Quarter and Bywater have no `ENV` value**, and neither does
`Red Lantern Faultline`, which spans them. A test walks the registry and fails if any
non-`PROVISIONAL` row acquires a type.

`Blue Pulse Corridor` likewise carries no type — held for the Ruling 2 geometry test.

## 3. The consequence this surfaced, which is the important part

**The validator's own fixtures were using free-text `ENV`.** Eleven rows read
`...,Seraphine,Square,U3,W1,...`, taken from the recovered E16 packet, whose `ENV` is
*"Streets leading away from the square (night)"*.

Under Ruling 1 **that is not an `ENV` value.** It is a scene setting; `ENV` is now a zone
or corridor **type**. The fixtures moved to `ZONE_BLUE_PULSE` and all 71 tests pass — but
the fixtures were only reflecting the source material.

**So: every recovered packet migrated from here on needs its `ENV` mapped to a type.**
That is migration work which did not exist before today. It affects work-queue item 5
(E16–E18), item 5a (the Book 3 Act III shells) and item 8 (E01–E15).

**Today it costs nothing** — `episode_beats.csv` is header-only, so enforcement adds zero
violations and the count is unchanged at 27 / 62. **At migration time it will cost
something**, and the count will rise unless the `ENV` mapping is done as part of the
migration rather than after it. Recorded in `reports/README.md` under known limitations so
whoever runs the migration meets it before the validator does.

This is worth stating plainly rather than burying: applying Ruling 1 made a previously
free field a controlled one, and the recovered material does not satisfy it. That is the
ruling working as intended — it is how a scene setting and a resonance type stopped being
the same field — but it is not free.

## 4. On the token spellings, again

Flagged at §35 and restated because it now lives in `canon_rules.json`: **membership is
ruled, spellings are mechanical.** `location_system._token_note` says so in the file
itself. Changing them is a find-and-replace across two `proposals/` files, one `rules/`
key and the test fixtures.

## 5. Validator

`27 canon-scope / 62 all-scope`, unchanged, with `ENV` now enforced. 71 self-tests pass
(up from 63). Both baseline reports regenerated.

END OF ENTRY 36

===============================================================

===============================================================

# 37. Gate rulings — step 5: character migration plan opened — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 3 — bundles A–I approved,
authorizing *"controlled canon migration planning and application per manifest §0"* and
explicitly **not** *"silent invention of unresolved material."*

**Status:** PLAN OPENED / NOTHING MIGRATED / NOTHING PROMOTED / VALIDATOR 27 / 62

**Artifact:** `proposals/concord-2026/CHARACTER_MIGRATION_PLAN_2026-09-19.md`

---

## 1. Manifest §0 step 1 is done, and it changes the risk profile

The obsolete-name search over §14's 36-name watchlist has been **run**, not just planned:

| Layer | Hits |
| --- | --- |
| **Canon substrate** | **4** |
| `proposals/` | ~280 |
| `recovery/` | 3 |
| `recovery/source_exports/` | 0 |

**35 of 36 names have zero substrate presence.** This is a `proposals/`-layer
reconciliation, not a canon rewrite. The migration is far less dangerous than the
manifest's size suggests — 600+ lines and ~80 entries, but almost none of it reaches
`canon/`.

## 2. The single substrate exception is already compliant

`PureTone` is the only watchlist name in the substrate: `SaekoID.md:122`,
`SaekoEBCI.md:34` and `:107`, `canon/factions/Choirless.md:125`.

The manifest rules it *"RETIRE AS SEPARATE MAJOR FACTION"* while preserving it as
*"earlier campaign/network/technology vocabulary."* **All four occurrences read
"PureTone logic"** — methodology, not faction. They are the surviving permitted sense.

So the one hit classifies **KEEP-AS-VOCABULARY, not RETIRE**, and **the watchlist requires
no substrate edit at all.** Worth stating because the opposite would have been the single
largest risk in this queue.

## 3. Batch order, with B and G last

Nine batches: **H** (trilogy load / migration *rules*) → A → C → D → E → F → I →
**B** → **G**.

**H runs first** by deliberate choice. It holds the migration rules themselves, so running
it first means every later batch is validated against them rather than retrofitted.

**B and G run last** per Ruling 3: approved in substance, but their place references
*"inherit Ruling 1's preliminary status."* They cannot start until the narrative vetting
pass settles the contested ground in `location_places_PROVISIONAL_2026-09-19.csv`.

**Bundle I migrates nothing.** It is approved *as a hold list*; its batch slot exists only
to record that it was considered and deliberately not moved.

**Every batch is gated** on the validator reporting at or below 27 / 62. A batch that
raises either number stops the queue.

## 4. Carve-outs enumerated rather than trusted to memory

Five **HOLD** items — manufactured-meta population, Arden Kess / LX-5, Lila Shore,
Nix & Rio, Ayo Mensah — are listed by name and bundle in the plan, excluded from every
batch.

**Terminal Witness** stays `RECOVER MORE / DO NOT PROMOTE`. Ruling 3: *"Protect the slot;
invent nothing."* Excluded from every batch, no facts supplied.

The **author-locked controls** (Tahl Morgan / MissingThread, and the Baz identity control)
are untouched. The plan carries forward §33 §4's recorded discrepancy — Ruling 3 writes
the control as *"Baz Foix"* while `canon/characters/BazID.md` reads
**Bastien "Baz" Arnaud** — with the reading that the **rename decision** is what stays
locked. **No Baz reference is changed by this plan**, so the discrepancy costs nothing
either way, but it is recorded in the plan itself rather than only here.

## 5. Ready state

**Batches 1–7 are ready to run.** Batches 8 and 9 wait on the Ruling 1 vetting pass — the
only remaining dependency, and a narrative one rather than a structural one.

## 6. Validator

`27 / 62`, unchanged. This step added one `proposals/` document and ran a read-only
search; nothing was migrated.

END OF ENTRY 37

===============================================================

===============================================================

# 38. Amendment 1 — Baz's surname ruled — 2026-09-19

**Ruled:** James, 2026-09-19 — *"Bastien "Baz" Arnaud is canon. The manifest's preference
for Basil "Baz" Foix is overruled; "Foix" is retired as a Baz surname."*

**Recorded at:** `recovery/GATE_RULINGS_2026-09-19.md`, **Amendment 1**.

**Status:** RULING RECORDED / CORRECTION PASSES FOLLOW AS SEPARATE COMMITS /
VALIDATOR 27 / 62

---

## 1. What it closes

The discrepancy first recorded at §33 §4 and carried into
`CHARACTER_MIGRATION_PLAN_2026-09-19.md` §4.3. Ruling 3's standing carve-out named the
locked control **"Baz Foix"**; `canon/characters/BazID.md` reads **Bastien "Baz" Arnaud**.

Both previous passes declined to resolve it. §31 left the `Foix` references standing as
documentation of the rename and said so explicitly; §33 recorded the inconsistency and
read it as *the rename decision* being what stayed locked rather than the name itself.
**That reading was the cautious one and it is now superseded by a direct ruling.** It is
kept in both documents rather than deleted, because it is what the intervening passes
acted on and the record should show why.

## 2. How the amendment was recorded, and why that shape

**Ruling 3's body is not rewritten.** It records what was ruled on 2026-09-19 and stands
as issued. Amendment 1 sits after it; the carve-out line carries a dagger pointing to it.

This is the same reasoning the earlier passes used for verbatim quotations — §26.10 for
`Technarc`, §31 for `Ito Masayuki`, §34 for the safe-route framing. **A record of what was
decided is not improved by editing it to match what was decided later.** The amendment
supersedes; it does not overwrite.

## 3. Scope, as the amendment states it

- Applies to **Baz only**: `Foix` is retired **as a Baz surname**.
- **`Janvier "Jan" Foix`** inherited the rejected surname and becomes
  **`Janvier "Jan" Arnaud`** — a consequential rename, flagged reversible, with his
  function preserved exactly.
- **The canon substrate is already correct** and is not touched: `canon/` reads
  `Bastien "Baz" Arnaud` throughout with **zero** `Foix`.
- **Quotations are annotated, not rewritten**, wherever a document quotes a source that
  said `Foix`.

## 4. What is unaffected

The rest of Ruling 3 stands: bundles A–I approved, the five HOLD carve-outs, Terminal
Witness as `RECOVER MORE / DO NOT PROMOTE`, and the **Tahl Morgan / MissingThread** lock.

## 5. Validator

`27 / 62`, unchanged. This commit records a ruling; it corrects nothing yet.

END OF ENTRY 38

===============================================================

===============================================================

# 39. Amendment 1 — proposal layer corrected — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` **Amendment 1**.

**Status:** 8 FILES CORRECTED / SUBSTRATE UNTOUCHED / PROVENANCE STATEMENTS PRESERVED /
VALIDATOR 27 / 62

---

## 1. The line drawn

`Foix` appeared in **14 files** (74 occurrences) — 13 before Amendment 1 was committed,
which itself added the fourteenth. The correction split them three ways:

| Kind | Action | Example |
| --- | --- | --- |
| **`Foix` used as Baz's *current* name**, in a document's own voice | **Corrected** | manifest §1 heading `### Baz Foix` → `### Bastien “Baz” Arnaud` |
| **Statements *about* the superseded name** | **Kept**, section annotated as ruled | *"The large November 2025 Notion canon uses Basil “Baz” Foix"* |
| **Originals and the authority** | **Untouched** | `GATE_RULINGS`, the author-uploaded bundles |

**The middle row is the one that matters.** Rewriting those would make the sentences
false, not current. *"Historical **Foix** references remain valid provenance"* becomes
nonsense as *"historical Arnaud references"*; a statement that Notion used `Foix` is a
**fact about Notion** and stays true no matter what is ruled here.

That is the instruction's quotation exception applied to reported speech as well as
quotation marks: **a recovery document must not be edited to make its source appear to
have said something it did not.** The same rule governed `Technarc` (§26.10),
`Ito Masayuki` (§31) and the safe-route framing (§34).

One of the corrected documents states the rule itself, which is why it was followed
rather than invented: `B03_B04_HANDOFF` §17 — *"historical **Foix** references remain
valid provenance and must not be rewritten inside archived source evidence."*

## 2. What was corrected

| File | Change |
| --- | --- |
| `CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md` §1 | Heading retitled; **alias line inverted** — `Bastien “Baz” Arnaud` is canon, `Basil “Baz” Foix` retired. It previously read the reverse |
| `EDITORIAL_CASTING_RESOLUTION_VIENNA_2026-09-19.md` | 4 doc-voice preferences corrected or struck, including *"protect Basil “Baz” Foix … unless a higher-authority current ruling says otherwise"* — **the ruling arrived** |
| `EDITORIAL_CASTING_RESOLUTION_GLOBAL_PLACE_ANCHORS_2026-09-19.md` | Baz entry in the cast list |
| `BAZ_WAREHOUSE_INCIDENT_RECOVERY_2026-09-19.md` | **Retitled.** Flagged at §26.10 and §31 and left alone twice; now correct, with a note recording the old title |
| `CHARACTER_MIGRATION_PLAN_2026-09-19.md` §4.3 | Discrepancy marked **RESOLVED** |
| `NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT_2026-09-19.md` §Baz | Section marked **RULED**; its *"direct author selection … has not yet been recovered"* now notes the ruling **arrived rather than was recovered** |
| `B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md` §17 | Section marked **RULED**; analysis and provenance rules stand |
| `CLAUDE.md` §3 | The *"deliberately not swept"* note replaced by the ruling |

## 3. Two documents that had it right and were overruled anyway

`NARRATIVE_DECISION_LEDGER_SOURCE_AUDIT` and `B03_B04_HANDOFF` both reached
**Bastien “Baz” Arnaud** as working authority from the evidence, and both said the direct
author statement had not been recovered. They were correct on the substance and correct to
hedge. **What they were waiting for never existed to be recovered — it was ruled.** Both
sections now say so.

The manifest went the other way, preferring `Basil “Baz” Foix` and marking
`Bastien “Baz” Arnaud` *"rejected unless higher-authority evidence emerges"*. That is the
line Amendment 1 overrules, and inverting it was the specific instruction.

## 4. Substrate untouched — verified, not assumed

`git diff --name-only` after the pass: **8 files, zero under `canon/`, `rules/`, `grids/`,
`book_context/`, `act_overlays/` or `source_canon/`.** The substrate already read
`Bastien "Baz" Arnaud` with zero `Foix` and needed nothing.

## 5. Left for the next commit

**`Janvier "Jan" Foix`** — manifest §4, bundle C. He inherited the rejected surname and is
renamed separately, so the consequential rename is its own auditable commit rather than
buried in this one.

## 6. Validator

`27 / 62`, unchanged.

END OF ENTRY 39

===============================================================

===============================================================

# 40. Amendment 1 — consequential rename: Janvier "Jan" Arnaud — 2026-09-19

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` **Amendment 1**, scope clause.

**Status:** RENAMED / **FLAGGED REVERSIBLE** / FUNCTION PRESERVED VERBATIM /
SUBSTRATE UNTOUCHED / VALIDATOR 27 / 62

---

## 1. Why he was affected at all

`Janvier "Jan" Foix` (manifest §4, bundle C) is **Baz's family**. He carried the surname
*because* Baz did. When `Foix` was retired as a Baz surname, Janvier inherited a name
that no longer exists in the cast — the rename is a consequence of the ruling, not a
separate judgement about him.

The alternative would have left a Foix relative of a man named Arnaud, which is worse than
either name alone.

## 2. Function preserved exactly — verified field by field

All four fields are **byte-identical** to the pre-rename entry:

| Field | Value |
| --- | --- |
| Status | `KEEP / NARROW RECURRING.` |
| Range | `lightly pre-B3 if useful; primary payoff Loom.` |
| Function | `Baz's family; grief that does not center Lucien.` |
| Ending | `OPEN.` |

**`Ending: OPEN` in particular is untouched.** Renaming a character is not an occasion to
close an open ending, and nothing here supplies detail the manifest did not have.

## 3. Reversibility, recorded in the entry itself

The manifest entry carries the note in place: *"Function unchanged; rename reversible —
if a later ruling restores `Foix`, only the surname moves."*

That is worth stating because Janvier's rename is **derivative**. It rests entirely on the
Baz ruling. If Amendment 1 were ever revisited, Janvier reverts mechanically — the given
name, the diminutive, the function, the range and the ending are all independent of the
surname.

## 4. Where he changed

| File | Change |
| --- | --- |
| `CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md` §4 | Entry retitled with the rename note; roster line |
| `EDITORIAL_CASTING_RESOLUTION_VIENNA_2026-09-19.md` | 4 — cast list, keep line, function line, and the "Foix family identity" argument |
| `EDITORIAL_CASTING_RESOLUTION_GLOBAL_PLACE_ANCHORS_2026-09-19.md` | roster line |
| `TRILOGY_CAST_CHECK_2026-09-19.md` | roster line |
| `SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS1_2026-09-19.md` | See §5 |

### 4.1 The Vienna "family identity" line needed thought, not replacement

It read: *"Janvier Foix further strengthens the **Foix family identity** in the recovered
cast architecture."*

A blind substitution would have produced a sentence asserting an Arnaud family identity in
*recovered* material, where no such thing appears — the recovered cast architecture really
does say Foix. It is struck through and restated instead: **the family identity holds and
is the reason for the rename; the surname is Arnaud.** The original stays visible.

## 5. A document that asked for exactly this, and got it

`SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS1` §Janvier read: *"surname relationship now
requires review after Baz Arnaud lock."*

**The audit called for the review; the ruling supplied it.** The line now records that it
was reviewed and resolved rather than leaving a standing request that has been answered.
This is the second such case in two commits — §39 recorded two documents waiting for a
direct author statement on Baz that arrived as a ruling rather than a recovery.

## 6. Verification

- Remaining `Janvier Foix` / `Jan Foix` strings outside `source_exports/`: **3**, all
  supersession notes recording the old name, plus the ruling and ledger text.
- `git diff --name-only`: **zero** files under `canon/`, `rules/`, `grids/`,
  `book_context/`, `act_overlays/`, `source_canon/`.
- Validator `27 / 62`.

END OF ENTRY 40

===============================================================

===============================================================

# 41. First grid populated — `milestones_payoffs.csv` is live — 2026-09-20

**Status:** 36 ROWS LOADED / ALL `proposed` / CANON-SCOPE 27, ALL-SCOPE 62→61

**The six grids have been header-only since the repository began.** This is the first one
with data in it, and it is the raw material for the saga timeline (§28, step 3).

---

## 1. What was loaded

`proposals/concord-2026/milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv` →
`grids/milestones_payoffs.csv`.

**v2, not v1.** v1 predates the three supplement axes and is missing
`supplement_function`, `supplement_vehicle` and `supplement_form`, so its rows would not
line up with the grid header. v2 carries all nineteen columns.

Verified after load: **36 data rows**, **36 unique non-empty `milestone_id`**, header
**byte-identical** to the schema, and the grid **byte-identical to its staging source**.

## 2. Every row stays `proposed` — deliberately

All 36 rows carry `status: proposed`. Nothing was promoted to `ruled`.

That is what the `status` column is for: **the grid can be live without being settled.**
Loading it makes the data reachable, checkable and diffable; it does not assert that any
milestone is final. Several rows depend on questions still open in §4 of `CLAUDE.md` —
notably the five `target_act: EP` rows, which remain unexpressible under `A{1-3}` until
the `EP`-slot question is ruled.

## 3. One cell corrected, on a ruling

**The load did not go in clean, and the queue stopped until it was ruled on.**

Row `M09`'s free-text `notes` read:

> `Recovered packet S1.T1.B3.A3.E14, anchored 'FIRST AND ONLY VT BRUSH IN VEIL TRILOGY'.`

`B3` is the one-digit form, corrected to `B03` under §3's two-digit rule. **James ruled:
fix the typo** (2026-09-20).

Three things make this a correction rather than a rewritten quotation:

1. It is **prose in a comment field**, not a structural identifier. That row's actual
   columns already read `T1` / `B03` / `A3` / `E14`.
2. It is **this repository's own shorthand referring to a packet**, not a reproduction of
   the packet's own header line.
3. **The original survives untouched** in `recovery/source_exports/`, which is never
   edited in place (§1.0). Nothing is lost.

Had it been a genuine quotation of a source's own text, the standing rule would have
applied instead — annotate, do not rewrite (§26.10, §31, §34, §39).

**Corrected in both places**, so the grid and its staging source do not drift: the live
grid and `milestones_payoffs_PROPOSED_LOAD_v2_2026-09-19.csv`. It was the **only** full
SID string in the entire 36-row load — all 19 columns of all 36 rows were checked.

## 4. A prediction I got wrong, corrected

`reports/README.md` recorded, when the `--all` baseline was regenerated at §26:

> The two milestone CSVs deserve a note … their hits are in the free-text `notes` column
> … **Loading them will not import a malformed SID.**

**The first half was right and the conclusion was wrong.** The validator scans file text,
not only structured fields, so loading did import a flagged string — canon-scope went
27→28 on the first attempt. The line is corrected in the same commit.

## 5. Validator

| Scope | Before | After |
| --- | --- | --- |
| canon | 27 | **27** |
| all | 62 | **62** |

**All-scope netted to zero, by two movements that cancelled.** Correcting the v2 staging
file removed one occurrence (62→61). Writing *this entry* put one back (61→62): §3
above quotes the pre-correction string once, as the evidence of what was fixed.

**It is quoted exactly once on purpose.** A second copy in this section took the count to
63 and had to come out — above the ceiling, which stops the queue. Hence the descriptive
reference here instead of a second quotation.

The v1 staging file `milestones_payoffs_PROPOSED_LOAD_2026-09-19.csv` **still carries the
typo and was deliberately not touched**: it is superseded, it is not the file that was
promoted, and it is the record of what v1 contained. It accounts for the surviving
occurrence outside this ledger.

Recorded because the intermediate reading was briefly 61 and the first draft of this entry
claimed that as the final state. It is not; 62 is. Documenting a one-digit SID costs one
all-scope violation, which is the same trade `reports/README.md` has recorded since §26 —
these files quote the wrong form in order to rule against it.

END OF ENTRY 41

===============================================================

===============================================================

# 42. The milestone grid is checked — 2026-09-20

**Status:** 5 CHECKS ADDED / 15 TESTS / ALL PASS ON THE GRID AS PROMOTED /
CANON-SCOPE 27, ALL-SCOPE 62

`grids/milestones_payoffs.csv` went live at §41. This makes it **checkable**, so the next
edit to it cannot quietly break it.

---

## 1. The five checks

| Check | Enforces |
| --- | --- |
| `CHK_GRID_SCHEMA` | Header matches `milestone_grid.columns` **exactly**. Column drift fails loudly and **stops the remaining checks**, which index by column name |
| `CHK_GRID_ID` | `milestone_id` unique and non-empty |
| `CHK_GRID_SETUPS` | Every `required_setups` entry resolves to a `milestone_id` **in this grid** |
| `CHK_GRID_TARGET` | `target_book` two-digit `B01`–`B09`; `target_trilogy` `T1`–`T3`; `target_act` `A1`–`A3` |
| `CHK_GRID_STATUS` | `status` drawn from `controlled_vocab.milestone_status`, new: `proposed` · `ruled` · `migrated` · `retired` |

**All five pass on the grid as promoted.** That is the point: they are a **ratchet against
future edits**, not a cleanup task, so any failure from here is a change someone made.

Each is asserted **twice** in the self-tests — the live grid passes it, and a known-bad
fixture fires it. A check that only ever passes proves nothing. 71 tests → **86**.

`rules/canon_rules.json` gains `milestone_grid` (the schema and the target vocabularies)
and `controlled_vocab.milestone_status`.

## 2. The one check that did NOT pass, and what was done about it

The instruction was that all six checks currently pass. **Five do. The act check does
not**, and the queue would have gone 27→32 if it had been written as a plain violation.

Five rows — `M10`, `M11`, `M23`, `M35`, `M36` — carry **`target_act: EP`**.

**`EP` is not an act.** James confirmed 2026-09-20: *"All books will have 3 acts"*, and
**27 acts is the cap** — verified in the substrate as 27 overlay files, three per book,
with `A{1-3}` in the SID format. So an `A1`–`A3` check is correct and must not be widened
to admit `EP`.

But **whether `EP` belongs in the act slot at all is an open author question**
(`CLAUDE.md` §4; ledger §24, §25, §27.7), and it is the *reason* those five rows exist in
this shape. Flagging them as violations would assert an answer.

**They are reported as notices instead**, using the channel the validator already has for
`ECID_fields_optional`. The report names all five with a pointer to the open question.

This is **not loosening the check**:

- `A4` is still a violation — tested.
- A one-digit `B1` is still a violation — tested.
- `EP` is still **reported**, by name, every run — tested.
- The moment the ruling says `EP` is not an act slot, the notice becomes a violation by
  deleting one branch. The moment it says `EP` **is** valid, it joins `target_act_values`.

**The checker reports; it does not decide.** That is the same posture as `CHK_BANDS`, which
validates band coherence without second-guessing the values (§18).

## 3. What the checks confirmed about the load

Running them is the first independent confirmation of the grid's internal consistency:

- **36 unique, non-empty** `milestone_id`.
- **Every `required_setups` reference resolves.** `SAGA_TIMELINE` §4 claimed this and §24
  verified it by hand; it is now machine-checked on every run.
- **Every `target_book` is two-digit.** The one-digit form that stopped the queue at §41
  was in a `notes` cell, never in a structured column.
- **Every row is still `proposed`.** A test asserts this specifically, so a future load
  cannot promote rows to `ruled` as a side effect.

## 4. Validator

| Scope | Before | After |
| --- | --- | --- |
| canon | 27 | **27** |
| all | 62 | **62** |
| self-tests | 71 | **86** |

Notices rose 0 → 5, which do not affect the exit code.

END OF ENTRY 42

===============================================================

===============================================================

# 43. OPEN QUESTION — the pressure columns are live and provisional — 2026-09-20

**Status:** OPEN — AUTHOR RULING NEEDED / **NOT A GATE** / NO VALUES ALTERED

**Raised by:** `recovery/SAGA_TIMELINE_2026-09-19.md` §2 and §3, written while the grid
was still staged. §41 loaded it, so **both columns are now in a live canon-scope grid**
and the question has moved from theoretical to load-bearing.

**Nothing in this entry changes the data.** `pressure_before` and `pressure_after` are
untouched, and **no `thread` column was added**. Recording the ambiguity is the job.

---

## 1. Finding one — the scale saturates with four books to go

`SAGA_TIMELINE` §2: the line pins at **5 from M19 (Book 5 Act III) to M32 (Book 9
Act III)** — fourteen consecutive milestones at the ceiling, before the Mending drops it
to 3 and the Lightfall to 1.

Measured against the live grid:

| | Count of 36 |
| --- | --- |
| Rows entering at `pressure_before: 5` | **16** |
| Rows leaving at `pressure_after: 5` | **18** (half the grid) |

The sixteen already at the ceiling before their own milestone fires:
`M10`, `M19`–`M33` inclusive.

> *"A scale that maxes out with four books to go cannot discriminate between the
> Colorstorm, Tahl's death, the exodus and the swamp convergence — and those are not
> equivalent."*

Two options are offered there, and **both are design decisions, not data fixes**: widen
the scale (1–7 or 1–10, with 5 reserved for "Neon's worst"), or rebase the middle (hold
Books 1–4 to 1–3). The timeline document deliberately left the 1–5 values in place
rather than invent a scale; **this entry does the same.**

## 2. Finding two — `pressure` is doing two different jobs

`SAGA_TIMELINE` §3: several rows show pressure *dropping* against the preceding row —
`M04`, `M07`, `M17` — **and none is an error.** They start or continue a *different
thread* at its own level. `M07` is the Caro–Elisabet formation, low-pressure by nature,
sitting between two high-pressure world events.

So the column is simultaneously recording **world pressure** and **the pressure of the
thread the milestone belongs to**, and those diverge constantly.

**27 of 36 rows have `pressure_after <= pressure_before`.** Under a single global reading
that looks like three quarters of the saga's milestones failing to raise the stakes.
Under the per-thread reading most of them are simply a different thread being measured.
**The number is only alarming under one of the two interpretations, which is the
ambiguity in one statistic.**

The recommendation on file is a `thread` column — `veil` · `mt` · `tahl` ·
`silence_hope` · `institutions` · `filaments` · `caro_elisabet` — with pressure read
*within* a thread. **Not added.** It is a schema change to a live grid and needs a ruling.

## 3. The empty `channel` column, and how it connects

**23 of 36 rows have an empty `channel`.** The 13 that are populated read `MT` ×6,
`VT` ×6, `LT` ×1.

This is **partly downstream of the same question.** `channel` answers *which thread does
this milestone belong to* for the three Threads specifically. A milestone on the
Caro–Elisabet thread or the institutions thread has no channel to name, so the cell is
blank — not because the information is missing, but because **the column can only express
thread membership for three of the seven threads §2 identifies.**

If a `thread` column is ruled in, most of those 23 blanks become expressible and
`channel` narrows to what it actually means: which of `MT`/`VT`/`LT` carries the
milestone. If it is not, the blanks stay blank and the thread information stays
unrecorded.

**Not all 23 are downstream of it.** Some milestones genuinely touch no channel. The two
cases are not currently distinguishable, which is itself part of the finding.

## 4. Why this is an open question and not a gate

The grid is **live and every row is `proposed`** (§41). That is exactly the state this
question needs: the values are loaded, checkable and diffable, without asserting they are
final.

- Nothing downstream consumes `pressure_*` yet — no grid reads it, no tool computes on it.
- The saga root (§44) references the milestone **set**, not its pressure values.
- `CHK_GRID_*` (§42) validates structure, and **deliberately does not judge pressure
  values** — the same posture as `CHK_BANDS`.

So the pipeline proceeds. **What must not happen is a later pass reading these numbers as
settled**, which is what this entry exists to prevent.

## 5. For the author

1. **Widen the pressure scale, or rebase the middle?** (§1) Sixteen rows enter at the
   ceiling; the last four books have nowhere to climb.
2. **Add a `thread` column?** (§2) It would make `pressure` unambiguous and, per
   `SAGA_TIMELINE` §3, make the melody and harmony passes mechanical.
3. **Does the empty `channel` on 23 rows mean "no channel" or "not yet recorded"?** (§3)
   Currently indistinguishable.

Until 1 and 2 are ruled, **the loaded `pressure_before` and `pressure_after` values are
provisional** — loaded so the grid is live, not because the scale is settled.

END OF ENTRY 43

===============================================================

===============================================================

# 44. The saga root exists — `rules/saga_context_S1.json` — 2026-09-20

**Status:** CREATED / 9 FIELDS FILLED FROM RULED MATERIAL / 7 LEFT TODO, EACH SAYING WHY /
CANON-SCOPE 27, ALL-SCOPE 62

§28 recorded the cascade's central structural gap: containers exist at trilogy, book, act
and episode level, and **nothing above them.** The chain ran
`book_context_B0X.json` → `act_overlay_S1_T*_B0*_A*.json` with no root, so the saga
timeline — step 3 of the build pipeline — had nowhere to live. **It now has one.**

Placed in `rules/` alongside `trilogy_context_T1_veil.json` and its siblings, which is
where the layer directly below it already lives.

---

## 1. What was filled, and from what

**Nine fields, every one from material already ruled or already recorded:**

| Field | Source |
| --- | --- |
| `structure` — 3 trilogies, 9 books, **3 acts each, 27 total** | Ruled §25, **confirmed by James 2026-09-20**. Verified in the substrate: 27 overlays, three per book, `A{1-3}` in the SID format |
| `trilogies` — `T1` Veil / `T2` Neon / `T3` Loom, with book ranges | `CLAUDE.md` §3; book ranges from the existing contexts |
| `structural_frame` — Jazz Framework v2, five axes | `canon/saga_overview.md` |
| `pov_baton_pass` — Seraphine Vael lead; Arnaud / Morgan / Harper | `canon/saga_overview.md`, with **canonical full names** per §31 and §39 |
| `global_invariants` — five | `saga_overview.md`, corroborated against `canon_rules.json` |
| `milestones` — grid, count 36, all `proposed` | §41 |
| `era_boundary` — the Mending at `S1.T3.B09.A3.E14`, Lightfall at `E15` | §27.2 |

The invariants list carries **five**, not the four in `saga_overview.md`: *manufactured
metas cannot ascend* is added because `canon_rules.json` already holds it as
`manufactured_metas.cannot_ascend`. That is a corroborated invariant, not a new one.

`pov_baton_pass` is **half-filled on purpose** — the baton itself is recorded, but
`weights` is TODO. `pov_targets` is TODO in all nine book contexts and no distribution
model has ever been authored.

## 2. What was left TODO, and why that is the correct outcome

**Seven fields, thirteen TODO markers**, each stating its own reason rather than sitting
blank:

| Field | Why it is TODO |
| --- | --- |
| `saga_timeline` | The milestone **set** exists; the **arc structure over it** does not. Character arcs, antagonist arcs and chronology are all unstructured (§28, §30) |
| `entry_state` | Needs an authorial statement. The nine book-context `entry_state` fields are the author's to fill |
| `exit_state_locks` | `BOOK 9 — END STATE` exists in Notion and is recorded at §27, but **promoting it is a canon decision** |
| `trilogy_summaries` | `saga_overview.md` carries TODO for all three; not recoverable |
| `post_mending_snapshot` | `saga_overview.md` carries TODO, **and** the Post-Mending era file is HELD over the `LT` question (§18) |
| `chronology` | **No timeline artifact exists anywhere in the substrate**, and three timeskips are open (§27.3, §30) |
| `pov_baton_pass.weights` | As §1 |

Several of these could have been filled with a plausible sentence. **None was.** The
instruction was explicit and matches §4 of `CLAUDE.md`: a TODO left is correct; a
sentence written to fill it is not. `exit_state_locks` is the sharpest case — the Book 9
end state is *recovered and recorded*, so the words exist, but promoting recovered Notion
material into a canon container is precisely the decision Claude does not make.

## 3. The nine book-context TODOs are untouched

`git status book_context/` is **empty**. Those 27 violations are the author's to fill and
remain the canon-scope baseline.

The saga root's own thirteen TODOs **add no violations**, because none sits under a key in
`JSON_KEY_VOCAB` — the book contexts' TODOs are flagged for being in
`escalation_permissions.max_corridor_tier` and siblings, which are vocabulary-checked
fields. The root carries no envelope fields at all: **envelopes belong to the trilogy and
act layers, which already have them.**

## 4. What the root does not do

- **It does not populate the cascade.** It gives the cascade a top, which is a different
  and smaller thing.
- **It asserts no new canon.** Every filled field points at where it came from.
- **It does not resolve anything open.** Where a field touches an open question — the
  Post-Mending envelope, the pressure scale, the timeskips — it **names the question and
  its ledger entry** rather than answering it.

## 5. Validator

| Scope | Before | After |
| --- | --- | --- |
| canon | 27 | **27** |
| all | 62 | **62** |
| files scanned | 190 / 267 | **191 / 268** |

86 self-tests pass.

END OF ENTRY 44

===============================================================

===============================================================

# 45. Character migration batch 1 — bundle H, trilogy load control — 2026-09-20

**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Ruling 3, bundle **H** approved.
Plan: `proposals/concord-2026/CHARACTER_MIGRATION_PLAN_2026-09-19.md` §2, batch 1 of 9.

**Status:** MIGRATED / 3 FILES / CANON-SCOPE 27, ALL-SCOPE 62 / 86 TESTS

**First batch of the character migration to reach the substrate.** Everything before this
was planning.

---

## 1. Why H ran first

Not alphabetical. Bundle H is the **trilogy load and migration rules themselves**, so
running it first means batches 2–7 are measured against rules that are already in place
rather than retrofitted to them afterwards. The plan fixed this order at §2.

## 2. What moved, and where

Manifest §11 holds three per-trilogy cast-load rules. Their correct home is the **trilogy
layer**, which already exists: `rules/trilogy_context_T1_veil.json` and its two siblings.
Each gains a `cast_load` block carrying its own `_source` line.

| Trilogy | Foreground | Key constraint |
| --- | --- | --- |
| **T1 Veil** | recurring neighborhood/civic faces; institutional antagonists mostly peripheral | do not seed the full future Filament roster; **B03 prioritizes the Baz death, the fracture and the Tahl reveal** over new introductions |
| **T2 Neon** | the **earned expansion window**; established civic faces reused as their jobs change under pressure | **B06 introduces almost no major new supporting characters** — cash established relationships instead |
| **T3 Loom** | geographically huge, emotionally recognizable; **default to returning faces** rather than replacement shelter leaders, reporters or couriers | earlier institutions become collapse consequences rather than equal final-villain towers; the Chronicle is dead as an institution; **do not give everyone an epilogue card** |

**Nothing was reworded into new meaning.** The manifest's prose is carried across as
written, split into `foreground` / `institutional_antagonists` / `constraints` so a later
pass can check against it mechanically rather than by reading.

## 3. Two things this does immediately

**It gives the later batches a measuring stick.** T2's *"B06 introduces almost no major
new supporting characters"* and T3's *"default to returning faces"* are exactly the tests
batches 2–7 need when deciding whether a recovered secondary character survives. Without
H first, each of those decisions would have been made on judgement and reconciled later.

**It corroborates work already done.** T1's constraint that B03 prioritizes the Baz death
and the Tahl reveal over new introductions agrees independently with the B03→B04 handoff
reconciliation and with the author lock that Tahl is not a named primary before the B03
epilogue (§26.9). Two separate passes arriving at the same shape.

## 4. What was preserved

Each trilogy context keeps its own `TODO` (*"Populate trilogy-specific ceilings and
exceptions"*) — **unfilled and moved to last**, because it is a different question and
still the author's. `cast_load` sits before it.

No envelope field was touched. `tone_envelope`, `era_envelope`, `environment_envelope` and
`hard_constraints` are unchanged, so the banded-envelope work of §18 is unaffected.

## 5. Validator

`27 / 62` before and after; 86 self-tests pass. `cast_load` introduces no
vocabulary-checked key, so it adds nothing to either count.

## 6. Next

Batch 2 is **bundle A** — Filament / community, manifest §2, 13 entries. Batches 2–7 are
ungated; batches 8 (**B**) and 9 (**G**) wait on the Ruling 1 vetting pass.

END OF ENTRY 45

===============================================================

===============================================================

# 46. Character migration batch 2 — bundle A — 2026-09-20

**Authority:** Ruling 3, bundle **A** approved. Plan §2, batch 2 of 9.

**Status:** MIGRATED / 12 CAST ROWS + 8 RETIRED ALIASES / CANON-SCOPE 27, ALL-SCOPE 62

**This batch creates the artifact the rest of the migration lands in.**

---

## 1. Two new canon files, and why two

| File | Holds |
| --- | --- |
| `canon/cast_registry.csv` | **Surviving** secondary and tertiary cast — status, category, range, function, relationships, guardrail, historical material absorbed, migration note, ending |
| `canon/cast_retired_aliases.csv` | **Retired and merged** identities, each with its disposition and target |

They are separate because they answer different questions. The registry answers *who is
in the cast*; the alias file answers *what happened to the name you found in an old
document* — which is manifest §0 step 6 and the §14 watchlist disposition, and is the
thing a future reader hitting `Mira Tremeaux` in a recovered file actually needs.

## 2. Why a registry and not Tier-1 character cards

The obvious target would have been `canon/characters/`, which carries the four-file
pattern (`ID` · `EBCI` · `Appearance` · `Render`). **That would have required inventing
appearance, emotional-behavioural interfaces and render references that do not exist in
any source**, for twelve characters.

Ruling 3 authorizes *"controlled canon migration planning and application"* and
explicitly **not** *"silent invention of unresolved material."* So the migration carries
across exactly the fields the manifest holds, and no more. If any of these twelve is later
promoted to full Tier-1 treatment, that is an authoring decision with its own gate.

## 3. Parsed, not transcribed

The rows were **generated by parsing the manifest**, not retyped. Twelve entries with
seven-plus fields each is roughly a hundred values, and hand-copying them is exactly the
kind of pass that introduces a `Koro Ito` (§31). The parser reads `### ` headings and
`Field: value` lines, so the registry says what the manifest says.

## 4. What is in it

Twelve surviving entries, `A01`–`A12`: **Mara / M** (KEEP / PROMOTE) · **Arianna
Duplantier** · **Jae "Sparrow" Nguyen** · **Samir "Pivot" Choksi** · **Nara Epps** ·
**Ray "Stitch" Duong** · **Liyun Park** · **Corrine Dalcourt** (RENAME) · **Ren Bellande**
(REBUILD / RENAME / MERGE) · **Ishaan Virk** · **Blue String Kids** (KEEP AS COLLECTIVE) ·
**Rootkeeper** (DEMOTE / KEEP LOCAL).

Every row carries a `function` and an `ending`; none is blank — checked, not assumed.
**Ten of the twelve endings are `OPEN`**, and they stay `OPEN`. Migration moves a record;
it does not close a question.

Eight retired aliases: `Mira Tremeaux` (RETIRE, functions split), `Malik Price` and
`Domenico "Dome" Reyes` (MERGE Ren), `Ringo Marcel` (rebuilt as Ren Bellande),
`Lila Carter/Sparrow` (MERGE Jae), `Jas Holcomb` (MERGE Nara), and
`Miss Tilda "Lantern" Baptiste` and `Mère Céleste Boudreaux` (MERGE selected material to
Arianna).

**All eight are on the §14 watchlist**, and §37 established that watchlist has **zero
substrate presence** except a compliant `PureTone`. So retiring them costs no substrate
edit — the alias file records the disposition for anyone reading older material.

## 5. One guardrail carried across verbatim

Ren Bellande's entry carries a `Guardrail` field the other eleven do not:
*"not evil, not secretly controlled, not Choirless."* It is preserved as its own column
rather than folded into `function`, because it is a **constraint on future writing**, not
a description. His ending is also the one that is not simply `OPEN`:
*"OPEN BUT PAYOFF REQUIRED in Loom."*

## 6. Validator

`27 / 62` before and after; 86 tests pass. Files scanned 191 → **193**.

## 7. Next

Batch 3 is **bundle C** — Dominion / Vienna, manifest §4, 6 entries.

**The migrator needs one change before batch 4:** bundles D, F and I carry **HOLD** items,
and “HOLD stays held” means they must not land in a registry that reads as promoted cast.
They route to a separate held file.

END OF ENTRY 46

===============================================================

===============================================================

# 47. Character migration batch 3 — bundle C — 2026-09-20

**Authority:** Ruling 3, bundle **C** approved. Plan §2, batch 3 of 9.

**Status:** MIGRATED / 5 CAST ROWS + 6 RETIRED ALIASES / CANON-SCOPE 27, ALL-SCOPE 62

---

## 1. What moved

`C01` **Marcellus Virelli** (KEEP / PRIMARY DOMINION FACE) · `C02` **Caldas Ren** ·
`C03` **Marius Holt** · `C04` **Helena Kael** (KEEP / NARROW) ·
`C05` **Janvier "Jan" Arnaud** (KEEP / NARROW RECURRING).

Six retired: `Severin Virelli`, `Arel Tovin`, `Sigrun Dahl`, `Sabir Vollen`,
`Nadia Verenz`, `Eryk Sorensen` — all *"RETIRE/MERGE/DEMOTE according to scene"*, and all
six on the §14 watchlist with zero substrate presence.

## 2. The rename held, without being re-applied

`C05` came across as **Janvier "Jan" Arnaud**, not `Foix`. The parser reads the manifest
as it now stands, and §40 corrected it there. **Nothing in this batch re-applied the
rename** — it was already right at the source, which is what a migration should find.

That is the first independent confirmation that the Amendment 1 pass (§38–§40) actually
landed: a downstream tool reading the manifest cold produced the canonical name.

## 3. Two endings that say what is NOT locked

`C01` and `C02` carry endings that **explicitly unlock** prior material:

- Virelli — *"OPEN; old off-page B9 death NOT LOCKED."*
- Caldas Ren — *"OPEN; old storm death NOT LOCKED."*

These are the opposite of the usual migration risk. Rather than a recovered fact being
promoted by accident, the manifest is **actively releasing** two deaths that older
material had recorded, and the registry carries that release rather than the death.
Migrating the field as written is what preserves it.

## 4. A parser gap found and closed

Bundle A's retired identities are a **bullet list**; bundle C's are a **single prose
line** — *"Severin Virelli, Arel Tovin, …: RETIRE/MERGE/DEMOTE according to scene."*

The first run of batch 3 reported **0 retired aliases** and would have silently dropped
all six. Caught by reading the section rather than trusting the count, the parser now
handles both shapes, and the run was redone from a clean checkout.

**Worth recording as a method note:** a parser that silently finds nothing looks exactly
like a section that contains nothing. The check that caught it was comparing the output
against the source, not inspecting the output alone.

## 5. Validator

`27 / 62`; registry 12 → **17** rows, retired 8 → **14**. All ids and aliases unique.

## 6. Next

Batch 4 is **bundle D** — Technarc / Singapore, manifest §5, and the **first batch with
HOLD items**: `Manufactured-meta population` and `Arden Kess / LX-5`. The migrator now
routes them to `canon/cast_held.csv`, marked **not promoted**, rather than into the
registry.

END OF ENTRY 47

===============================================================

===============================================================

# 48. Character migration batch 4 — bundle D, and two schema corrections — 2026-09-20

**Authority:** Ruling 3, bundle **D** approved. Plan §2, batch 4 of 9.

**Status:** MIGRATED / 7 CAST + 3 RETIRED + **2 HELD** / CANON-SCOPE 27, ALL-SCOPE 62

---

## 1. The HOLD carve-out is now structural, not a promise

Bundle D is the first batch carrying **HOLD** items, and they do **not** enter the
registry. A third file, `canon/cast_held.csv`, takes them:

| Name | Status |
| --- | --- |
| Manufactured-meta population | `HOLD FOR MECHANICA + MANUFACTURED-META SPECIFIC REVIEW` |
| Arden Kess / LX-5 | `HOLD` |

Each row carries the reason verbatim: *"HOLD carve-out stands under Ruling 3; NOT promoted
by this migration."*

A check asserts **no HOLD name appears in the registry.** §37 enumerated the five HOLDs so
they could not be missed; this makes missing them *mechanically impossible* for the
remaining batches, which is a stronger guarantee than a list someone has to remember.

## 2. Correction — three registry rows are already Tier-1 characters

Batch 4's first run put **Rex Tan** in a secondary-cast registry. His own manifest entry
says *"migration outside scope except relationship references."*

Checking back, batch 3 had already done the same to **Marcellus Virelli**, and D01 to
**Director Han Wei**. All three have full four-file Tier-1 treatment in
`canon/characters/`.

**They are not removed — their rows carry real decisions** (Virelli's *"old off-page B9
death NOT LOCKED"* is exactly the kind of thing that must not be lost). Instead the
registry gains a **`tier1_canon`** column naming their existing files, so the record is
kept without implying they are newly-added secondary cast.

The registry was regenerated for A, C and D together from a clean checkout. A and C rows
are otherwise unchanged.

## 3. Correction — the Tier-1 detector was wrong the first time

The first implementation matched on a six-character filename prefix and found **only Han
Wei**, missing Rex and Virelli — the two cases that prompted the column.

Rewritten to derive the stem set from the filenames themselves
(`RexID.md` → `Rex`, `VirelliEBCI.md` → `Virelli`) and match whole words. Now flags
exactly three, with **no false positives** — checked specifically against the near-misses:
`Helena Kael` (Lucien's file stem is `Lucien`, not `Kael`), `Ren Bellande` and
`Ishaan Virk` (against `Virelli`).

**A detector that finds one of three looks like a detector that works.** What caught it
was naming the expected hits in advance and comparing, not reading the output.

## 4. What moved

`D01` **Director Han Wei** (Tier-1) · `D02` **Rex Tan** (Tier-1; migration out of scope) ·
`D03` **Dr. Shun Watanabe** (RENAME PROPOSAL) · `D04` **Dr. Kasumi Arendt** ·
`D05` **Gianna Locke** · `D06` **Harlow** (KEEP; Rook MERGE/RETIRE) ·
`D07` **Tamsin "Bluewire" Kho** (DEMOTE).

Three retired: `Rook`, `Yara Kint`, and `Pierre Morozov and generic duplicate analysts`.

The last is **left as one entry, not split.** The source names one person and an unnamed
class in a single disposition; splitting it would invent a roster of analysts that does
not exist.

## 5. Validator

`27 / 62`; 86 tests. Registry **24** rows (A 12, C 5, D 7), retired **17**, held **2**.

## 6. Next

Batch 5 is **bundle E** — ideological / Choirless, manifest §6, 5 entries. This is where
**Ito Masayuki** sits, so it is a direct test of whether the §31 naming correction holds
at the source the way the Baz rename did in batch 3.

END OF ENTRY 48

===============================================================

===============================================================

# 49. Character migration batch 5 — bundle E — 2026-09-20

**Authority:** Ruling 3, bundle **E** approved. Plan §2, batch 5 of 9.

**Status:** MIGRATED / 3 CAST + 4 RETIRED / CANON-SCOPE 27, ALL-SCOPE 62

---

## 1. The naming correction held at source — second confirmation

`E03` came across as **Ito Masayuki**, not `Koro Ito`.

§31 corrected that in the manifest after a proposal document had concluded the wrong way
from a memory export without checking `ItoID.md`. **Batch 5 did not re-apply anything** —
the parser read the manifest cold and produced the canonical name, exactly as batch 3 did
for `Janvier "Jan" Arnaud`.

Two independent confirmations now that the naming passes landed where it mattered: at the
source a downstream tool reads, not just in a ledger entry describing them.

`E01` **Saeko Morita** and `E03` **Ito Masayuki** both flagged `tier1_canon` — five files
each, the `*Backstory.md` antagonists of §29 §4.

## 2. Two more parser gaps, both silent

Bundle E exposed two entries the migrator would have dropped without a word.

**`PureTone` was being written into the cast registry.** Its status is *"RETIRE AS
SEPARATE MAJOR FACTION"* — it is a **retirement, and not a person**. Any entry whose
status begins `RETIRE` now routes to the alias file. This matters beyond tidiness:
§37 established `PureTone` is the **one watchlist name with substrate presence**, and all
four occurrences read *"PureTone logic"*, the surviving technology sense. Filing it as
cast would have contradicted the disposition that makes those four occurrences correct.

**The `Quiet Doctrine / duplicate anti-resonance roster` entry produced nothing.** The
prose-retire handler added in batch 3 was keyed to headings starting with *"Retire"*, and
this one does not. `Marcus Kell`, `Priya Sen` and `Jonah Grieves` would have vanished.
The handler now triggers on the **shape** of the entry — no status, no bullets, a
`Names: disposition` line — rather than on heading wording.

**That is the third silent-drop this migration has produced** (§47's bullet-versus-prose
lists, §48's Tier-1 detector, and this). All three had the same signature: **plausible
output, quietly short.** The only thing that caught any of them was checking the source
section against the row count rather than reading the rows.

## 3. What moved

Registry: `E01` **Saeko Morita** (KEEP, Tier-1) · `E02` **Tessa Vane** (RENAME/REBUILD) ·
`E03` **Ito Masayuki** (KEEP / PRIMARY HUMAN FACE OF CHOIRLESS, Tier-1).

Retired: `PureTone` · `Marcus Kell` · `Priya Sen` ·
`Jonah Grieves and equivalent parallel-faction identities` — the last left whole for the
same reason as §48's analysts: the source names a person and an unnamed class in one
disposition.

## 4. Verification

A check now asserts **no name appears in both the registry and the alias file.** Passing.

Registry **27** (A 12, C 5, D 7, E 3) · retired **21** · held **2** · all ids unique.
`27 / 62`.

## 5. Next

Batch 6 is **bundle F** — media / public voices, manifest §7, with one HOLD
(`Lila Shore`). Batch 7 is **bundle I**, which **migrates nothing**.

END OF ENTRY 49

===============================================================

===============================================================

# 50. Character migration batch 6 — bundle F, and a coverage ratchet — 2026-09-20

**Authority:** Ruling 3, bundle **F** approved. Plan §2, batch 6 of 9.

**Status:** MIGRATED / 11 CAST + 6 RETIRED + 1 HELD / CANON-SCOPE 27, ALL-SCOPE 62

---

## 1. Bundle F broke the parser twice more — in opposite directions

**The MT chorus was being retired.** `Core MT chorus — KEEP HANDLES` is a bullet list, and
the bullet handler written in batch 3 assumed bullets meant retirement, because bundle A's
bullets were `Retired Filament identities`. So `Ribbon_9`, `GlassHarbor`,
`NthDaySurvivor` and `tinfoilmage` — four handles the manifest says **KEEP** — were being
filed as retired.

**This was worse than a drop.** The earlier three gaps lost rows; this one **inverted
their meaning**, and the output looked complete. Bullets now route on the heading keyword:
`RETIRE`/`MERGE` → alias file, anything else → registry.

**`Media identities retired as recurring` produced nothing.** It uses `Name → disposition`
with an arrow; the prose handler only understood `Names: disposition` with a colon. Five
more names — `Jenna Alvar`, `Carmine Goodwin`, `Lina Harrow`, `Wyatt LaGrange`,
`Rachel Dupont / Marja Li` — would have vanished.

## 2. So the check became mechanical

Five parser failures across four batches, all with the same signature: **plausible output,
quietly wrong.** Each was caught by reading the manifest section and comparing — which
works until the reader is tired.

The migrator now asserts **every `### ` heading in a section produces at least one row**
somewhere — registry, alias file or held — and exits non-zero naming the unaccounted
headings otherwise.

**Verified by deliberately reintroducing the arrow-form bug:**

```
exit: 1
UNACCOUNTED HEADINGS in section 7: ['Media identities retired as recurring']
```

It fires, and it names the heading. This is the ratchet the earlier four gaps needed and
did not have.

## 3. What moved

**Cast (11):** `F01` Naomi Clairborne (PRIMARY CHRONICLE FACE) · `F02` Zane Rowley ·
`F03` Silas Moreau · `F04` Patrice Valois · `F05` Signalman East ·
**`F06`–`F09` the MT chorus** — Ribbon_9, GlassHarbor, NthDaySurvivor, tinfoilmage ·
`F10` BriteLine (KEEP FINITE) · `F11` ghost_frequency (DEMOTE / CHORUS COLOR).

The chorus rows carry the entry's `Identity rule` as their **guardrail**: *"do not reveal
legal identities by default."* That is a constraint on future writing, so it is preserved
as a field rather than folded into function — the same treatment as Ren Bellande's
guardrail in §46.

**Retired (6):** `BlackHarbor` plus the five media identities.

**Held (1):** `Lila Shore` — `HOLD/NARROW`. The third HOLD to route correctly without
intervention.

## 4. Regeneration was additive

A–E were regenerated alongside F and came back **byte-identical**: the diff is
**18 insertions, 0 deletions**. The parser changes affect only shapes those bundles do not
use, which is the result the fixes should produce.

## 5. Verification

Registry **38** · retired **27** · held **3** · all ids unique · no name in both registry
and alias file · no HOLD in the registry. `27 / 62`, 86 tests.

## 6. Next

Batch 7 is **bundle I** — and it **migrates nothing**. Approved *as a hold list*; its slot
exists to record that it was considered and deliberately not moved.

END OF ENTRY 50

===============================================================

===============================================================

# 51. Character migration batch 7 — bundle I, which migrates nothing — 2026-09-20

Batch 7 of the character migration plan. Bundle I was approved by Ruling 3
**as a hold list** — *"nothing in it is promoted."* This entry records that it was
processed, not that anything moved into cast.

## 1. What the bundle covers

Two manifest sections:

- **§9 GLOBAL UTILITY / HOLD POPULATION** — 9 entries
- **§10 TERMINAL WITNESS — UNRESOLVED RECOVERY ITEM** — 1 entry

## 2. Where the rows went, and why none reached the registry

`canon/cast_registry.csv` is **unchanged by this batch. 38 rows before, 38 after.**

The migrator carries a bundle-I override that routes every non-retirement row to
`canon/cast_held.csv` rather than the registry:

```python
if bundle == "I":
    held = rows
    rows = []
```

This matters for the four `DEMOTE / LOCAL` entries, which are the only rows where the
routing is a judgement rather than a transcription. A `DEMOTE` row in the registry would
assert saga-recurring secondary-cast status; the ruling withholds exactly that. Demotion
to local use is **not** promotion to the registry, so they are held.

Retirements still land in `canon/cast_retired_aliases.csv`: recording a retirement is the
opposite of promoting a name.

**Retired (3)** — `Etienne Malhotra` · `Dr. Lila Renton` · `Jae Park`, each
`RETIRE/MERGE` into an existing function.

**Held (7)** — `Nix & Rio` and `Ayo Mensah` (HOLD), `Nayana Iyer`, `Hadia Noureen`,
`Samuel "Sam" Broussard` and `Marienne St. Clair` (DEMOTE / LOCAL), and
`TERMINAL WITNESS`.

## 3. The sixth silent drop — a section with no entry headings

§10 first reported **`0 cast rows, 0 retired aliases`** and looked finished.

It was not. §10 has **no `### ` entry heading at all** — its `Field: value` lines sit
directly under the `## 10.` heading, because the section describes one unresolved item
rather than a roster. The parser splits sections on `\n### `, so it found zero entries.

Worse, the **coverage ratchet added in §50 could not see it.** That check asserts every
`### ` heading produces at least one row. A section with no headings has nothing to
account for, so it passed — the ratchet was silent precisely where it was needed. This is
the sixth instance of the migration's recurring failure signature, *plausible output,
quietly wrong*, and the first where an existing guard was structurally blind to it.

Two fixes:

1. **Headless sections parse as a single entry**, named from the section heading with the
   number and trailing dash-clause stripped — `TERMINAL WITNESS`.
2. **A universal ratchet**: a section that produces no rows *at all* now aborts.

   ```python
   if not rows and not retired:
       raise SystemExit("section %s produced NO rows at all" % num)
   ```

   No manifest section is empty of people, so zero output is never a correct result. This
   guard does not depend on the section's shape, which is what made the §50 ratchet
   miss here.

Verified by reintroducing the bug on a copy of the migrator: exit 1,
`section 10 produced NO rows at all`.

## 4. Terminal Witness is preserved whole

The author instruction is *"Terminal Witness stays RECOVER MORE."* Its held row carries
that verbatim as `status`, and its `reason` states the author instruction rather than the
bundle-I carve-out boilerplate — the two are different grounds for holding and should not
read as the same one.

The held schema has no `historical` column, so the row's `note` was widened to join the
recovered function, the historical name, the evidence status and the proposed
consolidation. Nothing in §10 is dropped: the historical name **"Mara Nichols"**, the
Tier E evidence status, and the `Ramon Espina` consolidation condition all survive in the
row.

`Approval: [ ] pending recovery` is unchanged, in the manifest and in effect.

## 5. Verification

Registry **38** (A 12, C 5, D 7, E 3, F 11) · retired **30** · held **10** (D 2, F 1,
I 7) · all cast ids unique · no name in both registry and alias file · no HOLD status in
the registry. `27 / 62`, 86 tests.

## 6. Next

**Batches 1–7 are complete.** Batches **8 (bundle B)** and **9 (bundle G)** remain gated
on the Ruling 1 narrative vetting pass and are not startable from the manifest alone.

END OF ENTRY 51

===============================================================

===============================================================

# 52. Two counting errors in CLAUDE.md, corrected — 2026-09-20

Found while verifying the **Book Escalation Ceilings — Derivation Draft** against the
substrate. Both are factual misstatements in the working agreement, not canon questions,
so they are corrected rather than flagged. Neither changes a rule; both change what a
future session would believe about the repository's state.

## 1. The 27 violations were attributed to the wrong fields

**Was** — CLAUDE.md §8.0: *"`book_context`'s `entry_state` / `exit_state_locks` /
`locations_in_play` / `continuity_hooks` / `pov_targets` **are** the book-level timeline
and are `TODO` in all nine books. Those 27 violations are the canon-scope baseline."*

**Is** — those five fields are indeed `TODO` in all nine books, and **none of them is
counted.** `book_context/` holds **90** `TODO` strings across ten fields. The validator
reports **27**, and they are exactly:

    escalation_permissions.max_corridor_tier    9
    escalation_permissions.max_weather          9
    escalation_permissions.max_fx               9

Verified by reading the report directly: all 27 are `CHK_VOCAB`, three per book context,
naming those three keys.

**Why.** `CHK_VOCAB`'s placeholder branch fires only on keys present in `JSON_KEY_VOCAB`
(`tools/validate_canon.py`), which maps the three escalation scalars and four envelope
keys. `entry_state`, `exit_state_locks`, `locations_in_play`, `continuity_hooks`,
`pov_targets` and `title` are not in that map, so their `TODO`s are invisible to the
validator — 63 strings, uncounted.

**Consequence, and why it matters now.** The derivation draft's closing line — *"committing
the ceilings alone takes canon-scope violations from 27 to 0"* — is arithmetically
correct. Under the old CLAUDE.md wording it read as *the book-level timeline is complete*,
which it would not be. The corrected bullet states the count and the residue together:
**a clean report is not a populated book layer.**

> **Residue corrected 2026-09-20, §53.** This entry first said 54 uncounted strings. It is
> **63**: the six field *names* carry seven TODO *strings* per book, because `entry_state`
> holds two (`world`, `key_character_states`). 27 + 63 = 90, which is the total above.

## 2. "18 of the 27 bands are inferred" — the real split is 24 / 3

**Was** — CLAUDE.md §9.1: *"18 of the 27 bands are inferred placeholders."*
`reports/README.md` carried the same error with its complement: *"the checker treats them
exactly like the 9 marked `observed`."*

**Is** — **24 inferred, 3 observed.** The three observed acts are **`B01.A1`, `B01.A2`
and `B03.A3`**.

Verified twice, from independent sources that agree:

- The 27 overlay files' own `basis` fields: `{'observed': 3, 'inferred': 24}`.
- `ENVELOPE_INTERIM_VALUES_V2_2026-09-19.md`, the source: 3 `[observed]` table rows
  (a 4th marker is the legend line) and 25 `[inferred]`, of which one is the **held
  post-Mending era file at line 157, not one of the 27 acts** — leaving 24.

Both corrected sites now name the three observed acts rather than only a count, so the
claim is checkable without recomputing it.

## 3. Also sharpened

CLAUDE.md §9.1's validator baseline said *"27 violations, all of them `TODO` placeholders
in the nine book-context skeletons"* — true as written, but it invites the same inference
as §1. It now names the three escalation scalars and says the skeletons' other `TODO`
fields are unchecked.

## 4. Not changed

`RECOVERY_LEDGER_2026.md` §44 ¶3 says *"Those 27 violations are the author's to fill"*
under the heading **The nine book-context TODOs are untouched**. That sentence is about
ownership, not composition, and is still true. Left alone.

The derivation draft itself is **not committed** — it is a draft for review, and its §3
schema recommendation and §4.1 conflict are the author's calls.

## 5. Verification

`27 / 62`, 86 tests. No substrate file touched: the corrections are confined to
`CLAUDE.md` and `reports/README.md`.

END OF ENTRY 52

===============================================================

===============================================================

# 53. The book envelopes, derived — and a live trilogy contradiction — 2026-09-20

Two author rulings, 2026-09-20:

1. **`{min, max}` is approved** for the book layer — *"min max works for me."*
2. **The 27 violations are derived, not authored** — *"I also believe the 27 violations
   should be derived from narrative and milestones, not dictated by author."*

Ruling 2 settles what the derivation draft left open in its §6: the ceilings are a
rollup, so filling them is not the author's job. This entry applies both.

## 1. What was written

All nine `book_context_B0X.json` move from three scalars to the act shape:

    "escalation_permissions": {
      "corridor": {"min": "U1", "max": "U5"},
      "weather":  {"min": "W0", "max": "W3"},
      "fx":       {"min": "FX1", "max": "FX2"},
      "exceptions": [...],
      "basis": "derived",
      "derivation": "...", "act_basis": {...}, "source": "..."
    }

| Book | corridor | weather | fx | observed acts | exc |
| --- | --- | --- | --- | --- | --- |
| B01 | U1–U5 | W0–W2 | FX0–FX2 | A1, A2 | 0 |
| B02 | U1–U5 | W0–W3 | FX0–FX2 | — | 0 |
| B03 | U1–U5 | W0–W3 | FX1–FX2 | A3 | 1 |
| B04 | U2–U5 | W1–W3 | FX1–FX3 | — | 0 |
| B05 | U2–U6 | W1–W4 | FX2–FX3 | — | 0 |
| B06 | U3–U6 | W2–W4 | FX2–FX3 | — | 0 |
| B07 | U3–U6 | W2–W4 | FX2–FX3 | — | 0 |
| B08 | U3–U6 | W2–W4 | FX2–FX3 | — | 0 |
| B09 | U5–U6 | W3–W4 | FX3–FX3 | — | 0 |

Every value is the min of its three acts' mins or the max of their maxes. **No judgement
was applied to any number.** The table was computed independently from the 27 overlays
and reproduces the derivation draft's table row for row.

`basis` is **`derived`**, not `observed`/`inferred`, because the rollup's standing comes
from the operation, not from evidence. Which acts under it were observed is recorded
separately in `act_basis` — only **three acts in the saga** are `observed`
(`B01.A1`, `B01.A2`, `B03.A3`), so seven of the nine books rest entirely on inference.

B03's `W4` exception carries forward with a `from_act` pointer. B09 carries
`unresolved_era`: its band is the **pre-Mending portion only**, because `B09.A3` spans the
Mending. Milestone **M34's own note places the boundary at `S1.T3.B09.A3.E15`** — so the
gap is locatable, not vague. `U7` (Quiet Veil) appears in no act band in the saga.

## 2. The trilogy layer contradicts the act layer, on 13 axes

**This is the finding, and it is not resolved here.**

CLAUDE.md §9.1 recorded *"Trilogy envelopes contradict the escalation model"* as
**resolved 2026-09-19 — per-act bands**. It is not resolved. The per-act bands were
*added*; the trilogy scalars were never reconciled to them. Filling the book layer put
the two in the same cascade and made the conflict visible:

| Trilogy | container | books beneath it want |
| --- | --- | --- |
| T1 Veil | `U5` / `W3` / `FX2` | `U5` / `W3` / `FX2` — **consistent** |
| T2 Neon | `U5` / `W3` / `FX2` | `U6` / `W4` / `FX3` — breaches all three |
| T3 Loom | `U5` / `W3` / `FX3` | `U6` / `W4` / `FX3` — breaches corridor and weather |

**Six of nine books breach their container**: B04 (fx), B05–B08 (all three / two), B09
(corridor, weather). Thirteen axis-breaches in total. All three trilogies carry the same
`weather_max: W3` / `corridor_max: U5`, which is itself the signature of values set once
for the saga rather than per trilogy.

Each of the six books records the breach in an `unresolved` field on its envelope. Nothing
was changed in `rules/trilogy_context_*.json`.

> **Corrected 2026-09-20, §57.** This section reasoned about the trilogy scalars as though
> they were *values someone chose*. They were not. All three trilogy files carried
> identical `W3`/`U5` beside an unfilled `TODO` reading *"Populate trilogy-specific
> ceilings and exceptions"* — **skeleton defaults, never populated.** Read that way there
> was never a contradiction between two authored layers, only one layer that had been
> filled and one that had not. This section's *"wider act than the ruling authorized"*
> caution was therefore more cautious than the facts required. Same class of
> misattribution as the two CLAUDE.md errors in §52. Section 4 of this entry also counted
> `fx` among the breached axes; there is no trilogy `fx_max`.

**Why this is the author's call and not a rollup.** Ruling 2 says envelopes are derived,
which would make the trilogy ceilings the max of their three books — `U6`/`W4`/`FX3` for
both T2 and T3. That is the consistent reading, and there is precedent: T1's
`default_vfx_ceiling_note` records this exact situation being decided once before, when a
recovered packet contradicted the ceiling and **the ceiling was ruled the error**. But the
ruling named the 27 book violations, and rewriting three trilogy containers is a wider
act than it authorized. Recorded, not performed.

## 3. Cross-check against the milestone grid

Ruling 2 says *narrative and milestones*, so the derived envelopes were checked against
the 36-row grid. Every milestone whose description implies rupture- or storm-level
conditions was tested against its act's weather ceiling.

**Exactly one conflict, the one the draft already found.** `M08` — the first Rupture, the
Warehouse Incident — sits at `B03.A3` under a `W3` ceiling, and Mechanica §30 defines
`W4` Landfall as the state where *"shards or rupture-level events likely"*. The one `W4`
exception in the saga is at `E14` and is granted for the **VT brush**, not the Rupture.

`M19`, `M24`, `M30` and `M34` all sit under `W4` ceilings; no conflict. `M01` and `M03`
match a keyword scan but are shard *events*, and Mechanica makes such events *likely under*
Landfall without requiring Landfall for them — the implication runs one way only. So the
conflict count stands at one, and **the Mechanica text does not force it**: "the Rupture
does not require Landfall conditions" is the better-supported reading of §30 as written.
Open, in CLAUDE.md §4. Not resolved here.

## 4. Correction to §52

§52 said the uncounted residue was **54** `TODO` strings. It is **63**. The six field
*names* carry seven TODO *strings* per book: `entry_state` holds two (`world`,
`key_character_states`). 27 + 63 = 90, the total §52 itself states. Corrected in §52 and
in CLAUDE.md §8.0.

Those 63 are untouched by this entry, exactly as the derivation draft's §6 says they must
be: they are descriptions of a narrative that does not exist yet.

## 5. Verification

Canon-scope **27 → 0**. All-scope **62 → 35**. 86 tests.

`check_bands` already runs on every JSON object, so the new blocks are shape-checked and
coherence-checked the moment they exist — min and max are vocabulary members, min does not
exceed max. It passes on all nine.

**The count reached 0 partly because two checks cannot yet see a missing block.** That is
closed in the next commit, not left standing; §54. The order is forced — adding the
required-block check first would have made the nine flat `TODO` skeletons fail it and
raised the baseline from 27 to 54, which the standing instruction forbids.

END OF ENTRY 53

===============================================================

===============================================================

# 54. Closing the false-clean gap, and reporting the trilogy breach — 2026-09-20

§53 filled the book envelopes and reached **canon-scope 0**. Part of that zero was
earned and part of it was the checks not looking. This entry makes the whole of it
earned, and puts the §53 §2 contradiction on the validator's own report.

## 1. `CHK_ENVELOPE` — an envelope must exist

`check_bands` opens with:

```python
if not isinstance(ep, dict) or "corridor" not in ep:
    return                      # book_context's flat TODO form, handled elsewhere
```

That early return was correct while the book layer was flat `TODO`s. After §53 it is a
hole: **delete `escalation_permissions` from a book context and the report reads zero
violations** — not because the envelope is right, but because nothing is looking at it.
This was flagged before the fill, so it is closed rather than discovered.

`CHK_ENVELOPE` requires every `book_context/` file to carry a band-shaped block with a
`basis`. Verified by deleting B05's block on the live repository: **1 violation**, where
the same deletion before this commit produced **0**. Restored immediately.

It also catches a **revert to the old scalar shape** — `max_corridor_tier` and friends no
longer satisfy the book layer, so the pre-2026-09-20 form cannot come back quietly.

## 2. `CHK_CONTAINMENT` — the trilogy breach, as notices

§53 §2 found the trilogy scalars contradicting the act bands on 13 axes. That finding
lived only in prose and in six `unresolved` fields, which means the next person to change
an act band would not be told.

`CHK_CONTAINMENT` compares each book's derived envelope against its trilogy container and
reports every breach. **As notices, never violations** — the same treatment the `EP`-slot
question gets in the milestone grid, and for the same reason: which layer gives way is an
open author question, not a format error. Notices do not affect the exit code.

The live report now carries **18 notices — 5 `EP` and 13 containment** — and the 13 match
the independent cross-check in §53 §2 exactly:

    B04  fx FX3 > T2 FX2
    B05  corridor U6 > U5, weather W4 > W3, fx FX3 > FX2
    B06  corridor U6 > U5, weather W4 > W3, fx FX3 > FX2
    B07  corridor U6 > U5, weather W4 > W3
    B08  corridor U6 > U5, weather W4 > W3
    B09  corridor U6 > U5, weather W4 > W3

## 3. A path bug found while writing the check

`TRILOGY_CONTEXTS` was first written with working-directory-relative paths. Run the
validator from anywhere but the repository root and the `open` fails, the handler returns,
and the containment check reports nothing — **the exact failure mode the check exists to
prevent**, reintroduced inside the fix for it.

Resolved against `REPO`, like every other path in the tool. Verified by running from
`/tmp`: 13 notices, same as from the root. The self-tests were run from `/tmp` too, the
lesson from §42's `LIVE_GRID` slip.

## 4. Tests

**86 → 100.** Fourteen new, in two classes.

`BookEnvelopeIsRequired` asserts the live nine pass, and that a missing block, a dropped
axis, a missing `basis` and a reverted scalar block each fire. One test states the
regression directly: it asserts `check_bands` **stays silent** on a missing block and that
`CHK_ENVELOPE` speaks — so if someone later "simplifies" the early return away, the test
that documents why it is there fails.

`TrilogyContainmentIsANoticeNotAViolation` pins both halves: the breach is seen, and it
does not reach the violation list. It also pins the live count at **13**, so a change to
an act band that silently widens or closes the contradiction shows up as a failing test
rather than as a quietly different report.

## 5. Verification

Canon-scope **0**, all-scope **35**, **100 tests**, 18 notices. Ratchet proven by
deliberate breakage on the live repository, not by fixture alone.

## 6. What is now open, for ruling

1. **The trilogy contradiction** (§53 §2). Deriving the trilogy ceilings from the books
   gives `U6`/`W4`/`FX3` for both T2 and T3. Consistent with the 2026-09-20 ruling and
   with T1's own precedent, but wider than that ruling authorized.
2. **M08's Rupture under a `W3` ceiling** (§53 §3). One conflict, and Mechanica's wording
   does not force it.
3. The `63` book-level `TODO` strings, unchanged and deliberately so.

END OF ENTRY 54

===============================================================

===============================================================

# 55. Five author rulings — 2026-09-20

`recovery/GATE_RULINGS_2026-09-20.md`, committed verbatim. Continues the four gates of
2026-09-19. Each closes a question `CLAUDE.md` records as open.

| # | Ruling | Closes |
| --- | --- | --- |
| R5 | Trilogy ceilings are **soft**; every breach must be **declared** | §9.1 trilogy contradiction, ledger §53 §2 |
| R6 | `PR` and `EP` sit **outside** the act model; 27 acts stands | §4 *"Does `EP` go in the act slot?"* |
| R7 | Pressure is calibrated **per trilogy** | §8.0 pressure provisionality, ledger §43 |
| R8 | Location assignments **derived now**, provisional **in the field** | §8.0 locations blocker, R1 qualification |
| R9 | POV rotation **derived** as an initial proposal; weights authored | §8.0 POV allocation |

## 1. The common move

Four of the five replace *leave it empty until ruled* with **derive it and mark it
provisional**. That is a change of default, and it is the reason this queue exists: the
material to derive from was already in the repository, and the containers were empty
because emptiness had been read as the safe choice.

It is not always the safe choice. An empty field cannot be checked, cannot be cited, and
cannot be corrected — it only looks conservative. A derived field marked provisional
carries its own uncertainty and can be regenerated when its source changes.

**What did not move**: `title`, `pov_targets` weights, and B01's `entry_state`. Those
require authorial statement and no derivation can supply them.

## 2. R5 reframes the §53 §2 finding rather than deciding it

§53 §2 asked which layer was wrong, the act bands or the trilogy scalars. R5's answer is
that a band which may deliberately be crossed is not contradicted by crossing it — what
matters is whether the crossing is **declared**. Undeclared is a violation; declared is a
notice.

This does not by itself legitimize the 13 breaches. It sets the rule under which the next
entry's derivation decides their fate.

## 3. R6 unblocks five milestone rows

The `EP`-slot question has blocked `M10`, `M11`, `M23`, `M35` and `M36` since the grid
loaded (§41, §42). R6 answers it by rejecting the framing: the slot is not an *act* slot
but a **structural-position** slot, of which `A1`–`A3` are three values and `PR`/`EP` are
two more. 27 acts remains the cap because a prologue is not an act.

This sits well with the source asymmetry in §27.7 — prologue inside ACT I, epilogues
outside the acts — without needing it resolved: both get a position.

## 4. Verification

No substrate file touched. Canon-scope **0**, all-scope **35**, 100 tests, **18 notices**
— unchanged, as a rulings-only commit should be.

END OF ENTRY 55

===============================================================

===============================================================

# 56. `PR` and `EP` enter the vocabulary — 2026-09-20

Ruling 6 applied. **Notices 18 → 13**: the five `EP` notices cleared, the 13 containment
notices remain. Canon-scope **0**. Tests **100 → 109**.

## 1. The pattern could not simply be edited

`SID_format` lives in `canon_rules.json` and the validator builds its matcher from that
string, so the obvious move was to widen `A{1-3}`. **It does not work.** `SidFormat`
split on `\{(\d+)-(\d+)\}` and emitted `literal + (\d+)` per component — every component
was numeric by construction, and `PR` and `EP` are not.

The parser now accepts a second component form alongside the numeric range:

    {01-09}              numeric range, width taken from `lo`
    {act:A1|A2|A3|PR|EP} alternation over literal tokens, optionally named

The new pattern is `S1.T{1-3}.B{01-09}.{act:A1|A2|A3|PR|EP}.E{00-99}`. The numeric form
is untouched, which is why the two-digit book rule still holds and why the existing suite
passed the refactor before the pattern changed.

The loose matcher for an alternation is deliberately **wider than the allowed set**
(`[A-Za-z]{1,3}\d{0,2}`), so `A0`, `A4` and `XX` are *found* and then fail validation
rather than going unseen. Verified: all three fail, `PR`/`EP` pass, `S1.T1.B1.EP.E01`
still fails on the book component, and act-prefix forms like `S1.T1.B01.A1` still parse.

## 2. A blind spot closed, and it moved the all-scope count

All-scope rose **35 → 50**. Every one of the 15 is a **one-digit book** in a quotation of
recovered material, in `CLAUDE.md`, `proposals/` or `recovery/`.

They are not new defects. They are SIDs the finder **could not see before**: with a purely
numeric act slot, `S1.T1.B3.EP.E01` did not match the finder at all, so its one-digit book
went unreported. The old suite asserted this as accepted behaviour, in a test named
`test_epilogue_act_token_is_not_matched_as_valid` whose own comment called it a
*"documented limitation"*.

That test is replaced by `test_the_old_ep_blind_spot_is_closed`, which asserts the
opposite and says why. **Canon-scope is unaffected** — the substrate carries no such form.
The rise is detection reaching material `CLAUDE.md` §3's scope warning already describes.

## 3. The dead carve-out removed

`check_milestone_grid` special-cased `EP` into a notice. With `EP` in
`target_act_values` that branch is unreachable, and leaving it would have parked a
superseded reading in the code. Removed, with a comment recording what it was.

`_act_note` is rewritten: `A1`-`A3` are the three acts, `PR` and `EP` are structural
positions outside the act model, 27 remains the cap. The previous note called `EP` "NOT a
valid act"; under Ruling 6 that framing was wrong, not merely outdated.

## 4. Recorded, not resolved — epilogue episode numbering

The five `EP` rows suggest epilogue numbering **continues the book's sequence** rather than
restarting at `E01`: `M23` cites `E20` in B06, `M35` `E20` and `M36` `E21` in B09. High
numbers, consistent with continuation.

**Where they live matters and the record should be exact**: `target_episode_or_range` is
**empty on all five** `EP` rows. The numbers appear in the `notes` column as *Notion
provenance citations* — "Notion B6 aftermath unit E20", "Notion B9 E20", "Notion B9 E21".
`M10` and `M11` (B03) carry no episode number at all.

So this is **evidence from the source layer, not a populated field**, and it bears on the
open question in `CLAUDE.md` §4 of whether epilogue episodes restart at `E01`. §3 of
`CLAUDE.md` rules that epilogues take the next sequential episode number, which agrees.
**Not resolved here.** If the continuation reading is wrong, it is an author question.

## 5. Verification

Canon-scope **0**. All-scope **50** (was 35; §2). Notices **13** (was 18). Tests **109**
(was 100), including: a prologue SID parses, an epilogue SID parses, `A0`/`A4`/`XX` fail,
act-prefix forms still parse, the whole live grid passes with its `EP` rows, and the five
`EP` rows are still present — so the cleared notices cannot have come from losing rows.

END OF ENTRY 56

===============================================================

===============================================================

# 57. The trilogy envelopes, derived — the contradiction dissolves — 2026-09-20

**Notices 13 → 0.** Canon-scope **0**. Tests **109 → 111**.

## 1. The finding that changes §53 §2

§53 §2 recorded 13 axis-breaches and framed them as a contradiction between the
narrative-derived act layer and the trilogy layer, calling the trilogy values *"older
author-set ceilings"*. **That was wrong, and it is the same class of error as §52's two.**

All three trilogy files carried identical `weather_max: W3` / `corridor_max: U5` beside:

    "TODO": "Populate trilogy-specific ceilings and exceptions."

**Skeleton defaults. Never populated.** No author set them; the identical values across
three tonally different trilogies were the tell, and §53 noticed the tell without drawing
the conclusion.

So there were never two authored layers disagreeing. There was one layer filled and one
layer still holding its placeholder — and the caution in §53 about "a wider act than the
ruling authorized" was more cautious than the facts required.

## 2. What was written

`environment_envelope` on all three trilogy files moves to the band shape, derived from
the nine books by the same rollup the books use on the acts:

| Trilogy | books | corridor | weather | exceptions |
| --- | --- | --- | --- | --- |
| T1 Veil | B01–B03 | U1–U5 | W0–W3 | 1 |
| T2 Neon | B04–B06 | U2–U6 | W1–W4 | 0 |
| T3 Loom | B07–B09 | U3–U6 | W2–W4 | 0 |

B03's `W4` VT-brush exception propagates up with both a `from_act` and a `from_book`
pointer, so it is traceable from the trilogy down to the episode.

Each carries `soft_ceiling` recording Ruling 5 in the file itself, and `supersedes`
recording exactly what the scalars were. The `TODO` is closed and says why.

**The 13 breach notices cleared by construction** — a book cannot exceed a container
computed from itself. That was the predicted outcome and it is the right kind of
verification: the number went to zero because the arithmetic made it impossible, not
because a check was loosened.

## 3. `fx` is a default, not a ceiling

There is no trilogy `fx_max`. The era envelope carries `default_vfx_ceiling` — the FX
level to assume when nothing says otherwise — and **exceeding a default is not a breach.**

`CHK_CONTAINMENT` was checking it as one, which produced 3 of the 13 notices (B04, B05,
B06) and put `fx` into six book `unresolved` notes as a breached axis. `container_band()`
now returns `None` for `fx` and the checker skips it, with the reason in the docstring and
a test asserting it.

The derived fx band is still recorded on each trilogy as
`fx_band_derived_from_books`, **for reference only**, next to a field naming the
distinction. Losing the number would have been the wrong fix.

## 4. The six book notes, corrected

The `unresolved` field on B04–B09 is replaced by `superseded_finding`, which records the
closure and **both things the old field got wrong**: the "author-set ceilings"
misattribution, and counting `fx` as a breached axis. The old field name was itself
misleading once the question closed.

## 5. Tests

**109 → 111.** `test_the_live_breach_count_is_thirteen` becomes
`test_the_live_breach_count_is_zero`, with the reason stated: both layers derive from the
same rollup, so any breach means a hand-edit. Two added:
`test_fx_is_never_a_breach`, and
`test_every_book_band_is_inside_its_derived_trilogy_band`, which asserts the rollup's
defining property directly for all nine books rather than inferring it from a zero count.

The fitting/breaching fixtures now read the live trilogy caps rather than hardcoding
`U5`/`W3`, so they track the data instead of pinning the superseded values.

## 6. Verification

Canon-scope **0**. All-scope **52**, unchanged by this commit — the earlier 50 predated
ledger §56, which quotes `S1.T1.B3.EP.E01` twice as evidence and so adds two one-digit-book
detections to its own file. Notices **0**. Tests **111**.

END OF ENTRY 57

===============================================================

===============================================================

# 58. `CHK_DECLARED` — what makes a soft ceiling still checkable — 2026-09-20

Ruling 5 says a trilogy ceiling is *"a tripwire, not a wall"*. Without a check, that
sentence removes enforcement and puts nothing in its place — a soft ceiling nobody
verifies is the same as no ceiling. `CHK_DECLARED` is the other half of the ruling: a band
**may** exceed its container; it may not exceed it **silently**.

- **Undeclared** breach → **violation**.
- **Declared** breach → **notice**, so the crossing stays visible without failing the run.

## 1. Both rungs of the cascade

| Rung | Child | Container | Axes |
| --- | --- | --- | --- |
| 1 | act overlay | its book | corridor, weather, fx |
| 2 | book context | its trilogy | corridor, weather |

`fx` is checked at rung 1 and **skipped at rung 2**: the trilogy carries
`default_vfx_ceiling`, a default rather than a ceiling, and exceeding a default is not a
breach (§57 §3).

## 2. What counts as declared

An exception covers a breach when it names **the same axis**, permits **at least as much
as the breaching band claims**, and its `sid` sits **inside the entity that breaches**.

The SID condition is the one that does real work. Without it, B03's genuine `W4` VT-brush
exception would license a `W4` band anywhere in the saga — an exception granted for one
episode would silently become a standing permission. With it, `_covers` rejects an
exception whose SID belongs to another book, and a test asserts exactly that.

A weaker exception does not cover a stronger claim: an exception permitting `U5` does not
license a band reaching `U6`. A stronger one does.

## 3. Proven by deliberate breakage, both directions

Silent on the live substrate, so the proof is constructed — the same method as
`CHK_ENVELOPE` in §54, and the reason this entry can claim the check works rather than
merely that it does not complain.

**Step 1** — raise `B01`'s corridor max `U5 → U6` against a T1 container of `U5`, with no
exception:

    | `CHK_DECLARED` | 1 | 1 |     canon-scope 1

**Step 2** — add the exception, changing nothing else:

    {"sid": "S1.T1.B01.A3.E12", "axis": "corridor", "value": "U6",
     "scope": "brief", "reason": "PROOF FIXTURE - not canon"}

    canon-scope 0, notices 2

Both results are what Ruling 5 specifies. `book_context_B01.json` was restored from the
index immediately; **the fixture is not in the repository.**

## 4. Tests

**111 → 118.** Seven, covering `_covers` in both directions — matching, weaker, stronger,
wrong axis, wrong book — plus two on the live substrate: that it carries no undeclared
breach, and that B03's real exception carries all five fields Ruling 5 names.

Run from `/tmp` as well as the repository root.

## 5. Verification

Canon-scope **0**. All-scope **53**. Notices **0**. Tests **118**.

Zero notices is now the meaningful state: every derived layer agrees with the one above
it, and the one real exception in the saga sits below every ceiling it touches.

END OF ENTRY 58

===============================================================

===============================================================

# 59. `continuity_hooks` and `exit_state_locks`, derived — 2026-09-20

Two of the five book-level timeline fields were never authorial in the first place. They
were already written down, in `grids/milestones_payoffs.csv`.

## 1. The grid is a dependency graph

`required_setups` encodes **54 edges**: 33 cross-book, 21 within-book, **zero dangling and
zero backward** — no milestone requires a setup from a later book. Verified before
deriving anything; a backward edge would have meant the grid, not the derivation, needed
attention.

**A cross-book dependency IS a continuity hook.** Nothing had to be invented, only read
in the other direction.

| Book | owes forward | collects | locks |
| --- | --- | --- | --- |
| B01 | 6 | 0 | 3 |
| B02 | 6 | 2 | 4 |
| B03 | 4 | 2 | 4 |
| B04 | 4 | 5 | 5 |
| B05 | 2 | 4 | 3 |
| B06 | 5 | 3 | 4 |
| B07 | 4 | 4 | 5 |
| B08 | 2 | 4 | 3 |
| B09 | 0 | 9 | 5 |
| | **33** | **33** | **36** |

Both hook columns sum to the cross-book edge count, and the locks column to the milestone
count. **B01 collects nothing and B09 owes nothing forward** — the shape the saga's ends
should have, and a check on the derivation that costs nothing to read.

B09 collecting **9** is the largest value in the table: the endgame is where the most
threads are paid off, which is what one would expect and is now stated in the data rather
than assumed.

## 2. IDs, not descriptions

Every entry cites **milestone IDs and structural coordinates only** — no copied
description text. Two reasons, and the second is the load-bearing one:

1. The grid holds the descriptions.
2. A copy is a second thing to drift. `exit_state_locks` describing the Warehouse Incident
   in its own words would be a paraphrase that could quietly stop matching `M08`.

`exit_state_locks` carries `_status: "proposed"`, inherited from the grid rows, so nothing
here reads as settled that the grid does not.

## 3. Regenerable

Both blocks open with `_basis: derived`, a `_derivation` naming the source, and
`_counts`. The derivation says *regenerate rather than hand-edit*: if the grid changes,
the block is stale, and the only correct response is to recompute it.

## 4. The remaining count, and a correction to the target

Real `TODO` placeholders in `book_context/` are now **45**, down from 63: `title` 9,
`pov_targets` 9, `locations_in_play` 9, `entry_state.world` 9,
`entry_state.key_character_states` 9.

**The stated end-state target of 19 is 20.** The queue reserves three things as authored —
`title` (9), `pov_targets` weights (9) and B01's `entry_state` (1 book). But an
`entry_state` block holds **two** strings, `world` and `key_character_states`, so B01
contributes 2, not 1: 9 + 9 + 2 = **20**.

This is the same miscount that made §52's residue read 54 instead of 63 — a field name
counted where a string should have been. Recorded here rather than resolved by reshaping
B01's block to produce a 19: the data should not be bent to match a number.

**A counting note.** A naive scan for the substring `TODO` reports 51, because six
`superseded_finding` fields *quote* the trilogy's old `TODO` text as evidence. The count
above matches only values that **start with** `TODO`, which is what a placeholder is.

## 5. Verification

Canon-scope **0**. All-scope **53**. Notices **0**. Tests **118**. Nothing in the grid was
modified — this entry only reads it.

END OF ENTRY 59

===============================================================

===============================================================

# 60. `entry_state` for B02–B09, derived — 2026-09-20

`B0N` entry is `B0N-1` exit. The chain:

    B02 <- B01  M01 M02 M03
    B03 <- B02  M04 M05 M06 M07
    B04 <- B03  M08 M09 M10 M11
    B05 <- B04  M12 M13 M14 M15 M16
    B06 <- B05  M17 M18 M19
    B07 <- B06  M20 M21 M22 M23
    B08 <- B07  M24 M25 M26 M27 M28
    B09 <- B08  M29 M30 M31

Each block **cites** the predecessor's `exit_state_locks` rather than restating them —
one source, not two. `B09`'s own five milestones (`M32`–`M36`) are locks, not an entry
state, because nothing follows.

## 1. B01 stays `TODO`, and says why in the field

B01 opens the saga. It has no predecessor, so there is nothing to derive from. Its
`entry_state` now carries `_basis: "authored - not derivable"` and a `_reason` stating
that, with `world` and `key_character_states` left `TODO`.

The reason belongs **in the file**. A future session reading a `TODO` beside eight derived
siblings would otherwise reasonably assume it had been missed.

## 2. One field is only partly derivable, and says so

`world` derives cleanly: the world as the previous book leaves it, cited by milestone.

**`key_character_states` does not.** The milestone grid records **events**, not
per-character condition. `M20` says Tahl dies; it does not say what state that leaves
Seraphine in. So the derived value cites what *is* known and then states plainly what is
not:

> Character-level state is not carried in the milestone grid … per-character detail needs
> either a character-arc layer (none exists yet — `CLAUDE.md` §8.0 lists character arcs as
> genuinely unstructured) or an author pass. **Not invented here.**

This is the honest shape. Writing a plausible sentence about each cast member's condition
at each book boundary would have filled the field and produced nine books of fiction that
nothing supports. **Flagged for the author**: if per-character entry state is wanted, it
needs the character-arc layer first, and that layer does not exist.

## 3. Count

Real `TODO` placeholders in `book_context/`: **45 → 29**. Remaining: `title` 9,
`pov_targets` 9, `locations_in_play` 9, and B01's `entry_state` 2.

## 4. Verification

Canon-scope **0**. All-scope **53**. Notices **0**. Tests **118**.

END OF ENTRY 60

===============================================================

===============================================================

# 61. Locations: the type layer derived, the book dimension absent — 2026-09-20

Ruling 8 applied. It splits cleanly into a part that was fully derivable and a part that
has **no source at all**, and the two must not be reported as one.

## 1. The contested five, assigned — and four of them were never contested

`grids/locations_registry.csv` is new: 31 places, canon-scope, carrying every
place-to-type assignment with its status **in the field**, as Ruling 8 requires.

The five contested rows are now assigned. **Applying Ruling 1 dissolved four of them
rather than deciding them:**

| Place | Was | Now | Why it was never a conflict |
| --- | --- | --- | --- |
| Tremé | contested | `ZONE_BLUE_PULSE` | Geography system gives the **type**; "Red Lantern Faultline" is a **name**. Different axes. |
| Marigny | contested | `ZONE_BLUE_PULSE` | Same. |
| Bywater | contested | `ZONE_AMBER_DRIFT` | Geography system gives the type; Flickers → Ghostwaves is **shard progression**, a severity scale Ruling 1 states is not a spatial taxonomy. |
| Red Lantern Faultline | contested | `CORR_UNCLASSED` | A **name**, by its own source note. Ruling 2 geometry test: Tremé → Esplanade → Marigny is linear and connective → corridor; class unstated. |
| French Quarter | contested | `ZONE_BLUE_PULSE` | **The one real inference.** See below. |

Plus `NOLA-16` Blue Pulse Corridor → `CORR_UNCLASSED`, on the geometry test already
written in its own source note.

**The French Quarter is marked differently and deliberately**:
`PROVISIONAL_INFERRED_FROM_NAME`, not `PROVISIONAL_DERIVED`. The geography system assigns
it nothing; the only statement is bible membership of the named *"Blue Pulse Corridor"*.
Taking a type from a name is the move **Ruling 1 explicitly warns against**, so the row
says so and names itself the first to revisit. Flattening it into the other four would
have hidden the weakest evidence in the table behind the strongest.

**Ruling 8 was not applied to the eight `UNASSIGNED_NO_TYPE_IN_SOURCE` rows.** R8
authorises deriving **contested** assignments — rows where two sources speak. For these,
none does. Deriving from nothing is invention, not derivation, and each row now says that
in place of a value.

## 2. The book dimension does not exist

`locations_in_play` is a **per-book** field. The two-layer structure has **no book
dimension**, and nothing else in the repository supplies one.

Measured rather than assumed: scanning all 36 milestone descriptions and notes against
all 31 place names finds a location named in **3 of 9 books**.

    B01  Bywater             exact_name        M01
    B07  Honey Island Swamp  alias_inference   M28
    B08  Honey Island Swamp  alias_inference   M31

Each book's field carries the registry pointer, the derivation, the counts, and those
entries — with `match` distinguishing an exact place-name hit from an alias inference
(*"the swamp"* → Honey Island Swamp; the registry holds exactly one swamp). The inference
is labelled rather than merged, because an exact name and a guess are not the same
evidence.

**Six books list nothing, and the field says what that means**: no milestone in the book
names a place — *not* that the book has no locations.

The alternative was listing all 31 places under every book. That would have produced a
full-looking field asserting that every place appears in every book, which is false.

**OPEN, flagged for the author**: a per-book location pass needs a source that does not
yet exist.

## 3. Count

Real `TODO` placeholders: **29 → 20**. `locations_in_play` is closed on all nine.

Remaining: `title` 9, `pov_targets` 9, B01 `entry_state` 2 — **20, not the 19 the queue
projected**, for the reason in §59 §4.

## 4. Verification

Canon-scope **0**. All-scope **53**. Notices **0**. Tests **118**. The proposals-layer
source file is unchanged; the registry is a derived copy, per §1.0.

END OF ENTRY 61

===============================================================

===============================================================

# 62. POV rotation derived; the queue closes — 2026-09-20

Ruling 9 applied, and the eight-commit queue ends here.

## 1. The rotation

Composed mechanically from `rules/saga_context_S1.json` `pov_baton_pass`: **saga lead plus
this book's trilogy lead.** Nothing else was read in.

    B01-B03  T1   Seraphine Vael + Bastien "Baz" Arnaud
    B04-B06  T2   Seraphine Vael + Tahl Morgan
    B07-B09  T3   Seraphine Vael + Kade Harper

Marked `_basis: "derived - INITIAL PROPOSAL, not ruled"`, as Ruling 9 specifies.

Six books carry a `_ruled_constraints_bearing_on_this` field citing rulings that touch the
proposal without changing it — Baz dying at the end of B03, Tahl's B01–B03 absence, `M20`
placing Tahl's death in B06.A3, `M23` passing `MT` to Kade. B06's notes that whether POV
continues through Tahl's Echo (`M22`, `M27`) is **not settled by the baton pass and is not
decided here**.

## 2. Weights stay authored, and the field says why

Ruling 9 leaves the weights to the author. The field states the reason rather than only
the fact: a count-based weighting would rest on the `channel` column, which is **empty on
23 of 36 grid rows**. A number derived from a third of a dataset would read as measurement
while being an artifact of what happens to have been filled in.

The deeper reason is in the field too: **a POV distribution is a statement about emphasis,
and no count supplies one.**

## 3. Where the book layer stands

`TODO` placeholders across `book_context/`: **63 → 20**.

| Field | Before | After | How |
| --- | --- | --- | --- |
| `escalation_permissions` | 27 | 0 | rolled up from acts, §53 |
| `continuity_hooks` | 9 | 0 | 33 cross-book dependencies, §59 |
| `exit_state_locks` | 9 | 0 | milestones landing in the book, §59 |
| `entry_state` | 18 | **2** | preceding book's exit, §60 — B01 has no predecessor |
| `locations_in_play` | 9 | 0 | provisional type layer, §61 |
| `pov_targets` | 9 | **9** | rotation derived; **weights authored** |
| `title` | 9 | **9** | authored |

**20, not the projected 19** — §59 §4.

## 4. What is derived is not the same as what is known

Three fields are populated *and* carry a stated gap. Recording them together matters more
than the count does:

- **`entry_state.key_character_states`** (B02–B09) cites the previous book's milestones
  and then says per-character condition is **not in the grid** — the grid holds events.
  Needs a character-arc layer that does not exist.
- **`locations_in_play`** carries the type layer and says the **book dimension has no
  source**. Six books list nothing, and the field states that this means no milestone
  names a place, not that the book has no locations.
- **`pov_targets.weights`**, above.

Each says so **in itself**, not in a note beside it. A reader who finds only the value
still finds the caveat — the same reason Ruling 8 put provisional status in the field.

## 5. Verification

Canon-scope **0**. Notices **0**. Tests **118**. All-scope **54**, every one a one-digit
book inside a quotation in `recovery/`, `proposals/` or `CLAUDE.md` — including the two
this ledger adds by quoting `S1.T1.B3.EP.E01` as evidence in §56.

END OF ENTRY 62

===============================================================

===============================================================

# 63. `Technarch` re-entered twice more — the fourth correction — 2026-09-20

Found while reviewing the open-items proposal, which itself wrote `Technarch` in its §2.
That prompted a check, and the check found **80 occurrences** of a spelling ruled retired
on 2026-09-19.

## 1. CLAUDE.md's count was wrong

§9.1 claimed *"0 `Technarch` outside `CLAUDE.md` and `recovery/`"*. Actual: **68 in
`proposals/`, 12 in `canon/`.**

## 2. Two re-entry routes, and the second is mine

**Route 1 — the merge.** `a83f78d`, `6ba4de9` and `5475b4c` corrected the spelling across
canon, rules and the analysis layer on 2026-09-19. The proposal-branch fast-forward (§32)
landed **after** all three and re-imported 68 uncorrected occurrences from a branch cut
before them. **A merge does not inherit a sweep**, and nothing warned that it had not.

**Route 2 — the character migration, and this one is worse.** Batches 1–7 (§45–§51)
copied the manifest heading `## 5. TECHNARCH / REX ECOSYSTEM` verbatim into the
`manifest_section` column of three new cast files, and one `Status:` line into a fourth
field. That put **12 occurrences into canon scope**: `cast_registry.csv` 7,
`cast_retired_aliases.csv` 3, `cast_held.csv` 2.

The manifest is dated **2026-09-20** — after the ruling — so it introduced the retired
form fresh, and the migration propagated it into `canon/`. Verbatim copying is normally
the safe choice; here it carried a known-bad token across a layer boundary.

## 3. What was corrected and what was kept

**Corrected: 68 in 12 `proposals/` files, 12 in 3 `canon/` files, 4 in the manifest.**

**Preserved: 4 quotations**, the same four the 2026-09-19 pass preserved — an
independent agreement worth noting, since the test was applied afresh rather than copied:

- `"Technarch Directorate lineage"` ×2, Singapore resolution
- `` `Technarch Hardliners` ``, primer review
- `Source reads "Silver Static around Technarch towers"`, the places CSV

The rule is unchanged from §16.1 and the `Foix` and `Ito` corrections: **correct a
document's own voice; never rewrite a quotation of a source.** The two prose quotations
are now annotated in place, so the retained spelling explains itself instead of reading
like a miss.

**`grids/locations_registry.csv` needed no change.** Its single occurrence was already
the correct pattern: the place is named `Technarc towers district`, and the note quotes
the source's spelling with the correction cited.

## 4. Why this will happen again

Four corrections, three re-entries. The mechanism is structural, not careless:

- A branch cut before a naming ruling carries the old spelling, and merging is not
  sweeping.
- A migration that copies headings verbatim carries whatever the heading says.

**The validator cannot catch it.** Spelling is not a format violation, and §9.1 has said
so since the tooling landed. §9.1 now carries a grep to run after any merge or bulk
migration, and states the expectation that it recurs rather than declaring victory a
fourth time.

## 5. Verification

`canon/` **0**, `rules/` **0**, `grids/` **1** (quotation), `proposals/` **6** — the four
quotations plus two inside the annotations, which name the retired spelling in order to
explain it. Canon-scope **0**, notices **0**, 118 tests.

END OF ENTRY 63

===============================================================

===============================================================

# 64. `thread` lands; pressure becomes thread-scoped — 2026-09-20

Five answers from the open-items review, applied together because they are one design.

## 1. The ruling that decides the shape

> *"World pressure should not effect romance."*

That settles what §43 §2 could only observe. The column was recording two quantities at
once, and the evidence was five rows opening **below** the previous row's close — `M04`,
`M07`, `M09`, `M17`, `M18`. `M07`, the Caro–Elisabet bond, opens at 3 when `M06` closed at
4. A single world scale cannot do that. Read against its own thread, it is ordinary.

So `pressure_before` / `pressure_after` become **`thread_pressure_before` /
`thread_pressure_after`**: each row's pressure measures **its own thread**.

**The rename states intent; it does not certify the 36 values.** They were scored before
the column existed, so their provenance is mixed — some world readings, some thread
readings. `_pressure_note` says so in the schema, and every row remains `proposed`. Rows
carrying a non-`world` thread need re-scoring. **Renaming without that caveat would have
been the exact error the proposal warned about in its own §1** — making the documentation
definite and the data false.

## 2. The thread vocabulary, reconciled

Two lists were on file. Ledger §43 §2: `veil · mt · tahl · silence_hope · institutions ·
filaments · caro_elisabet`. The open-items proposal §2: the POV baton leads plus the
faction lines. **Ruled: reconcile.** The union, with three changes:

1. **`veil` → `world`.** `veil` collides with T1's name, and the thread is the world's
   condition, not the trilogy's.
2. **`institutions` splits** into `dominion`, `technarc`, `choirless`. Grouping them
   cannot separate B08's Technarc collapse from its neighbours, and **resolution is the
   entire purpose of the column** — the B07/B08 pair is the case that motivated it.
3. **`seraphine`, `baz`, `kade` added.** §43's list omitted all three POV leads.

**`mt` is kept distinct from `tahl`**, deliberately. The channel's arc — anonymous, named,
passed to Kade, renamed `LT` — outlives the person carrying it, and `M23`/`M35` are
channel events, not Tahl events.

Twelve threads plus `UNSCORED`.

## 3. Assignment: 17 derived, 19 explicitly `UNSCORED`

A thread is assigned only where the row's own description names **exactly one**. Rows
naming several stay `UNSCORED` — they are the ambiguous cases the author must settle, and
guessing would bury the ambiguity:

    M11  tahl + baz          M12  mt + tahl        M15  kade + filaments
    M23  mt + kade           M35  mt + kade

**`UNSCORED` is a vocabulary member, not an empty cell.** `CHK_GRID_THREAD` makes an
*empty* thread a violation, precisely because an empty cell cannot be told apart from an
oversight — the same posture Ruling 8 took for provisional locations, and the same lesson
as §61's six empty location lists.

## 4. The scale is flexible, and T3 runs backwards

> *"the intent is to be flexible and allow escalation within a trilogy not be defined by
> an overly restrictive system. If needed increase the number of levels or redefine by
> each trilogy, etc."*

`milestone_grid.pressure_scale` records: default 5 levels, **per-trilogy calibration**,
**levels extensible**, no fixed ceiling. Widening the scale or rebasing a trilogy needs no
further ruling.

Two measured facts are recorded with it, because they constrain any future anchoring:

- **Only T2 is compressed.** It uses 4 and 5 across three books. T1 spans 1–5; T3 spans
  1–5 (distinct 1, 3, 4, 5). The case for rescaling is one trilogy strong.
- **T3 descends.** T1 and T2 rise; T3 **opens at its maximum** (B07 is `5→5` throughout)
  and **ends at its minimum** after the Mending. So an anchor must define 1 as the
  trilogy's **minimum** and 5 as its **maximum**, never as "opening" and "peak" — for T3
  the opening *is* the peak, and the opening-baseline form inverts the scale. The
  proposal's §1 used exactly that wording.

**On the B06/B07 flatness** (the open-items §1 claim, and the point the author found
unclear without context): under per-trilogy calibration B06 is T2's top and B07 is T3's
top, so **both still score 5**. The numbers do not separate; only their meaning does.
Separating B07 from B08 — both T3, both at the ceiling — was always the `thread` column's
job, not the anchor's. Recorded so the anchoring work is not expected to do it.

## 5. Two grids, two quantities

Ruled: keep both, and score a quantity in exactly one of them. `grid_purposes` in
`canon_rules.json` records the split.

`milestones_payoffs.csv` holds **narrative** pressure per thread. `reader_pressure.csv`
holds **reader-facing** intensity per cohort — its own columns already say so
(`reader_group`, `pressure_state`, `intensity_1_5`, `episode_range`), and both
`canon/editorial_lenses.md` and `rules/validation_checks.json` already point at it.

The 2026-09-19 draft framed these as alternatives. They are not: threading fixes *whose*
pressure a milestone records; the reader grid answers a question the milestone grid never
asks. A quiet scene can be the hardest to read.

## 6. The `channel` backfill is DEFERRED, not done

The proposal's §3 would have written `NONE` into 23 rows and closed the item.

**Ruled: not yet.** *"narrative plot and milestones need to be developed before this
matters, and they will change this."*

That is the right call and §43 §3 supports it: the two cases — a milestone that genuinely
touches no Thread, versus one whose thread the `channel` column cannot express — *"are not
currently distinguishable."* The `thread` column now expresses the second case, so the
question is better posed than it was, but 23 rows of `NONE` would still be 23 editorial
assertions dressed as a mechanical fill. **The proposal listed it as needing no author
input; it needs 23 such inputs.** Left open.

## 7. Verification

Canon-scope **0**. Notices **0**. Tests **127** (was 118), nine added: a valid thread
passes, `UNSCORED` passes, an **empty** thread fails and the message names `UNSCORED`, an
unknown thread fails, `veil` is gone and `world` present, `institutions` is gone and the
three factions present, every live row names a thread, the pressure columns are
thread-scoped, and the scale is not saga-absolute.

END OF ENTRY 64

===============================================================

===============================================================

# 65. Character migration batches 8 and 9 — B and G, the last two — 2026-09-20

**Ruled 2026-09-20: "B and G are approved."** The character migration is complete.

## 1. What the gate actually was

Ruling 3 of 2026-09-19 marked both **"Approved, conditional on Ruling 1 vetting"** and
added that their *place* references *"inherit Ruling 1's preliminary status."* The
migration plan §4.4 read that as a hard stop: *"Batches 8 and 9 cannot start before
that."*

Two readings were live — that the condition is the vetting itself, or that it is
satisfied by place references carrying preliminary status. **The author took the second.**
Ruling 8 of 2026-09-20 is what makes it workable: preliminary now means *derived and
marked*, not *absent*, and `grids/locations_registry.csv` exists to carry it.

## 2. Migrated

**Bundle B — NOLA civic / cultural** (manifest §3): **11 cast rows, 1 retired**
(`Auntie Mae Broussard`).

**Bundle G — place anchors** (manifest §8): **7 cast rows, 0 retired, 1 held.**

All 18 registry rows carry a `migration_note` recording that their place references are
**provisional**, citing the registry rather than copying values from it — so they
regenerate when vetting changes a type instead of going stale.

Two G rows are anti-promotions and worth naming, because they record a decision *not* to
create cast: `Santa Fe` — *"NO RECURRING PLACE ANCHOR PROMOTED"* — and `Coastal Japan` —
*"NO NEW REPRESENTATIVE CHARACTER REQUIRED."* Migrating them keeps the decision on the
record rather than leaving the absence to be rediscovered.

## 3. `Mara Niht` is not `Mara Nichols`, and the migrator nearly said it was

`Mara Niht` (bundle G) carries `KEEP NAME / RECOVER MORE`, so `is_held()` routed it to the
hold list — correct. But the reason text it received was **Terminal Witness's**, because
that branch keys on the string `RECOVER MORE`.

**They are different characters.** Manifest §15 lists them as recovery items **1 and 2**.
`SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS2` treats them apart and in opposite directions:

- **`Mara Nichols`** — *the name is retired*; working label `TERMINAL WITNESS`.
- **`Mara Niht`** — *"Author ruling fixes spelling/name: Mara Niht"*; the name is
  **protected**, and what is missing is the source body.

One name retired, one name protected, two letters apart. The row now carries its own
reason and a note stating the distinction first, plus the source lead, the reserved
function, the `DO NOT LOCK` list and the pending approval.

**Seventh instance of the migration's signature failure** — plausible output, quietly
wrong — and the first caused by a *reason string* rather than a dropped or misfiled row.
The coverage ratchet from §50 cannot see this class: the row was produced, counted and
filed correctly, and only its explanation was false.

## 4. Final state of the character migration

Registry **56** (A 12, B 11, C 5, D 7, E 3, F 11, G 7) · retired **31** · held **11**.

All cast ids unique · no name in both registry and alias file · no `HOLD` status in the
registry.

**All nine batches are complete.** Bundle I migrated nothing, by design (§51).

## 5. Verification

Canon-scope **0**. Notices **0**. Tests **127**.

END OF ENTRY 65

===============================================================

===============================================================

# 66. Mara Niht — a cross-project import, and her source is not here — 2026-09-20

Author ruling, given after §65 flagged the name collision:

> *"Mara Niht is another music project we have that was inspired by the Concord world and
> we have decided to integrate her with connections to Elisabet. Her music profile and
> writings were included as part of the large chatGPT chat backup/export."*

## 1. What this settles, and what it does not

**Settled.** She originates in a **separate music project**, inspired by the Concord world
rather than written for it. **Integration is decided.** She has **connections to
Elisabet**.

That last point upgrades one line of the manifest's `DO NOT LOCK` list. *"Exact
relationship to Elisabet"* stays unlocked, but the question changed: the relationship
**exists**, and only its nature is open. Her held row records the distinction rather than
deleting the entry.

**Still `DO NOT LOCK`**, unchanged: age, nationality, style, instrument, exact
relationship to Elisabet, Resonance status, first appearance, Harpa role.

**Corroboration worth recording**: `canon/characters/ElisabetID.md` gives **Elisabet
Arnardóttir**, an Icelandic name, and `SECONDARY_TERTIARY_CHARACTER_AUDIT_PASS2` says Mara
Niht *"links Elisabet's pre-saga Icelandic life to the living cultural world of the
saga."* The ruling and the recovered material point the same way.

## 2. She stays held — for the body, not for the decision

Her status becomes `KEEP NAME / INTEGRATION RULED / BODY PENDING RECOVERY`.

**Not promoted to the cast registry**, because every attribute is still `DO NOT LOCK`. A
registry row would assert a migrated cast member with no recovered content behind it.
**Promotion now waits on recovery, not on a further ruling** — the gate moved, and the
row says which gate it is.

## 3. Her source is NOT in this repository

The author says the material was in the large backup. **It is not among the 21 sanitized
exports here.** Searched 2026-09-20 across all of `recovery/source_exports/`:

    Mara          0 files       Velvet Vein   0 files
    Niht          0 hits        Harpa         0 files
    singer        0 files       songwrit      0 files      lyric   0 files

Zero, on every name variant and every term from her reserved function. The only
`Mara Niht` string in the repository is this ledger.

**This is the distinction work-queue item 6 exists to make.** `CLAUDE.md` §8 item 6: until
the workspace inventory runs, *"not exported" and "does not exist" cannot be told apart.*
Here it can now be stated precisely — **exported, but not into this repository** — because
the author has confirmed the material exists.

So `Develop Singer Style` joins `Spine Architect chat` and `Saga Visual Bible Framework`
(§23) as a **named, confirmed-to-exist recovery target**. It is the strongest of the
three: the other two are inferred from references inside the exports, while this one the
author has confirmed directly.

## 4. A prose guardrail, stated before it is needed

Her **writings** are presumably lyrics or poetry.

`CLAUDE.md` §1: *"No prose, scene text, or dialogue is stored here. If a task would put
narrative prose in this repo, stop and say so instead."*

**When the body is recovered, the writings themselves do not land in this repository** —
only structured references to them. Recording this now, while recovery is still ahead,
rather than at the moment someone is holding the text and looking for somewhere to put
it.

## 5. An open question the tier scheme does not cover

The tiers (§5) describe **Concord-internal authority**: locked source canon, approved
development output, existing GitHub canon, other recovered sources, memory.

**Mara Niht is none of these.** She is another project's material, authored outside the
saga, imported into it by decision. Her music profile has its own provenance and its own
prior authority, and "Tier D — other sources" flattens that into the same bucket as a
Notion page.

**Not resolved here.** It is a small question while she is the only case, and a real one
if more cross-project integration follows. Flagged rather than answered, per §4.

## 6. Verification

Canon-scope **0**. Notices **0**. Tests **127**. No source export was read into canon; the
search was read-only.

END OF ENTRY 66

===============================================================

===============================================================

# 67. Mara Niht recovered — and the source body cannot live here — 2026-09-21

The author supplied the material and ruled the role: *"She falls into a similar role as
Trip (just in a more limited scope)."*

Distillation at `recovery/MARA_NIHT_RECOVERY_2026-09-21.md`. This entry records the two
findings that matter beyond her own row.

## 1. The source contains no saga material at all

`Bubble Grunge Lyrics`, 429 turns, 108,378 words. Measured across the whole file:

    Mara 283 · Niht 175 · Iceland 72 · Reykjavík 5
    Elisabet 0 · Concord 0 · Velvet Vein 0 · Harpa 0 · Trip 0

**Every saga-side fact about her is authorial, not recovered.** The Elisabet connection,
the Velvet Vein bridge, the Harpa role, the Trip-analogous function — none is in the
source. §66 anticipated the shape of this but not its completeness.

The Iceland coding is substantial and genuinely corroborates the Elisabet decision —
`ElisabetID.md` gives **Elisabet Arnardóttir**, and PASS2 says Mara Niht *"links
Elisabet's pre-saga Icelandic life to the living cultural world of the saga."* **But
corroboration is not derivation.** The source shows why the decision reads well; it did
not supply it. Her row says so, so a later pass cannot mistake the ruling for a find.

## 2. The body is recovered and is NOT in this repository

**513 lyric blocks.** `CLAUDE.md` §1: *"No prose, scene text, or dialogue is stored here.
If a task would put narrative prose in this repo, stop and say so instead."*

So the stop happened. The 680 KB `.md` and 1.7 MB `.json` are not committed.

**§1 and §7 genuinely conflict here**, and this is the first material where both bite:
§7 calls recovered source irreplaceable and says to commit it before transforming, *"so
the raw form survives in history."* §1 forbids exactly this content. §1 instructs a stop,
so the stop wins — **but the §7 risk is unmet and real: the author's copies are the only
ones.** Three options are put to the author in the recovery document's §5; none is taken
here.

The `.json` carries a `workspace_account_id`, deliberately reproduced nowhere.

**One incidental find for work-queue item 6.** This export **retains its conversation
id**. §8 item 6 records that sanitization stripped every id from the 21 exports, *"so the
exports cannot be mined for more"* — this file demonstrates an export path that keeps
them.

## 3. A correction to the recovery record

The manifest names the source lead as `Develop Singer Style`. The material arrived as
`Bubble Grunge Lyrics`. Either the lead was wrong or `Develop Singer Style` is a
**different, still-unrecovered** conversation. **Not resolved.** Recorded so item 6 does
not close a target on a name that does not match.

> **RESOLVED 2026-09-21, §68 — the lead was wrong.** `Develop Singer Style` was supplied;
> its id matches the manifest exactly, and it is a **different music project** (Eli Stone,
> male baritone, literary-song catalog) with **0 hits for `Mara` or `Niht`**.

## 4. Promoted, with the analogy marked as an analogy

Both gates cleared — integration ruled 2026-09-20 (§66), body recovered 2026-09-21 — so
she moves from the hold list to the registry as **G08**. Registry **57**, held **10**.

Her `function` is **inferred by analogy and labelled as such**. The author ruled a
*resemblance* to Trip and a *narrower scope*; that is not a field-by-field copy, so Trip's
function line is quoted as the thing being resembled rather than transcribed into hers.

**`range` is the same shape**: the bound is ruled — narrower than Trip's *"saga-recurring
as place logic permits"* — while the exact extent is not.

**Non-resonance is inferred, not ruled.** Trip's guardrail reads *"non-resonant; not
Filament leadership"*, and the analogy suggests the same. Her row says **confirm before
use**. Resonance status is on the `DO NOT LOCK` list, and an analogy is not a ruling —
this is precisely the seam where an inference would otherwise harden into canon unnoticed.

The whole `DO NOT LOCK` list survives recovery intact. Two entries are now *informed*:
**style** (the source gives a genre and a voice, which is an artist's style, not the
saga's field) and **nationality** (Iceland coding is aesthetic — the source itself says
*"content palette (urban, not Iceland)"*).

## 5. Verification

Registry **57**, retired **31**, held **10**. Ids unique · no name in both registry and
alias file · no `HOLD` in the registry. Canon-scope **0**, notices **0**, tests **127**.

No lyric text entered the repository.

END OF ENTRY 67

===============================================================

===============================================================

# 68. The manifest pointed at the wrong conversation — 2026-09-21

`Develop Singer Style` was supplied, and it answers the question §67 §3 left open.

## 1. The id matches and the conversation is not hers

The manifest §8 gives Mara Niht's source lead as *"historical ChatGPT conversation
'Develop Singer Style,' conversation ID `6a982376-6858-83ea-95e3-b32e8897ec5f`."*

**The id matches exactly.** The conversation is a **different music project**:

- **Eli Stone**, a *male baritone* singer-songwriter; album *False Witness*.
- A catalog built from **classic-literature scenes** — Gatsby, Macbeth, Dorian Gray, Anna
  Karenina, the Odyssey, Moby-Dick — written so the songs do not obviously tie to their
  sources.
- **0 hits for `Mara`. 0 for `Niht`.**

So of the two readings offered on 2026-09-20 — the lead was wrong, or a different
conversation is still unrecovered — **the first is correct**, and the target is closed
rather than outstanding.

**Both conversations are now recovered and neither names the other.** `Bubble Grunge
Lyrics` (Jan, 429 turns, female-led bubble grunge) never says `Eli Stone`; `Develop Singer
Style` (Sept, 28 turns, male baritone) never says `Mara`. Mara Niht's **only** source is
`Bubble Grunge Lyrics`.

## 2. Why the misattribution is worth a ledger entry

It was **not** a vague pointer. It carried a full conversation id, which is the strongest
form of provenance this project has — and §8 item 6 records that the 21 sanitized exports
lost their ids entirely, so an id is precisely what a recovery pass would trust most.

**A precise citation was confidently wrong.** Recovering it looked like success: a named
conversation, an exact id, a real file. Only the term counts showed it was the wrong
project. Had the name matched loosely — two singer-development chats — it could have been
filed as hers without anyone checking whether she appears in it.

The manifest line is **annotated, not deleted**: the original lead stays as the record of
what was believed, with the correction beside it.

## 3. Eli Stone is recorded, not integrated

`recovery/ELI_STONE_PROJECT_2026-09-21.md`. **No ruling touches this project**, so there
is no cast row, no character file and no manifest entry — only a provenance record so the
same id is not chased twice.

**The open question is put to the author and not answered**: Mara Niht was integrated as a
cross-project import; **Eli Stone is a second project of the same kind.** Whether it is
also an integration candidate is a §4 decision. If it is, the cross-project tier question
(§66 §5) stops being a one-off and needs a rule.

**Its body is not stored either** — 28 lyric blocks, same §1 ground as Mara Niht's.

One incidental confirmation: the source floats **`Calder Vane`** as an artist name and
rejects it as too close to the author's own. `Calder` is the author, not a project — which
explains the *"Calder engine"* and *"Calder Voice"* labels in `Bubble Grunge Lyrics`.

## 4. Verification

Canon-scope **0**, notices **0**, tests **127**. No lyric text entered the repository. No
cast row was added or changed by this entry.

END OF ENTRY 68

===============================================================

===============================================================

# 69. Five more music conversations — one touches canon, and adds none — 2026-09-21

Index at `recovery/MUSIC_PROJECT_CORPUS_2026-09-21.md`, now covering all **seven**
music-project conversations supplied.

## 1. The result

Of the five new ones, **four contain no Concord content at all** — a band OS
(`Loose Change Parade`), an artist-concept chat, a yacht-rock song review, and an
**architectural walkthrough score for a middle school in North Little Rock**, which is
unrelated to the saga entirely.

The fifth, `Elias Ward Songwriting Prep`, opens with **four Tier-1 Elias canon blocks** —
POV, Identity v1.1, EBCI, Appearance. That looks like a Tier-1 recovery. **It is not.**

## 2. The blocks are the repository's own files, verified word-for-word

| Block | Repo file | Result |
| --- | --- | --- |
| POV | `canon/pov/elias_ward_pov.md` | ratio **1.000** |
| Identity v1.1 | `canon/characters/EliasID.md` | **0.999**, 0 of 66 segments missing |
| EBCI | `canon/characters/EliasEBCI.md` | **563 words to 563, zero word-level opcodes** |
| Appearance | `canon/characters/EliasAppearance.md` | ratio **1.000** |

The sub-1.000 figures are punctuation and bullet glyphs. Stripped of markdown, the EBCI
comparison returns **no differences at all**.

**A negative finding, and worth the check.** §68's lesson was *check that a recovered
source names the character it was recovered for*; this is its complement — **check that
recovered canon is not canon you already have.** A conversation that opens with four
Tier-1 blocks is exactly the shape that gets filed as a find. Nothing needed recovering,
and nothing was created.

It also establishes something useful in the other direction: the songwriting work was
**canon-grounded**, not drifting. The assistant held position until released, then worked
from the repository's own canon.

## 3. The author ruled the songs' status inside the conversation

> *"Music should be narrative adjacent, but not in world. They can stand-alone without the
> story."*

So Elias's songs are **not in-world artifacts and are not canon.** Nothing is migrated —
the material is derived *from* canon, and migrating it would invert the dependency.

**The contrast with Mara Niht is the point.** She was integrated as a *character* (§66);
Elias's songs are explicitly *not* integrated as *work*. Cross-project material can cross
in one direction without the other following, and these two cases now bracket the range.

## 4. Two flags

**`Elias Ward` was on a real artist-name candidate list.** `Artist Concept Development`
has it at #2 beside `Calder Rowe` and `Jonah Black`. **Not chosen** — one occurrence, no
development. Recorded so it is not revived later without anyone noticing it is a Concord
antagonist's name.

**A Concord system this repository does not have.** `Song Review and Evaluation` cites
*"your Romance System (S4–S6 energy)"*. The repository's romance ladder is `HEAT`,
`H0`–`H4`: five levels, `H`-prefixed. `S4`–`S6` implies **six or more levels and a
different prefix**, so it is not a rename of `HEAT`.

Either a separate system exists outside this repository, or the reference is loose. This
is the same shape as the Silence-and-Hope gap (work-queue item 9b): **something referred
to as canon from outside, with no file here.** Not resolved; flagged.

## 5. Also noted

`Artist Identity and Lyrics` builds its band OS on a **PCM profile of the author** — "The
Calder Base". It is a document about the author's creative process, **not a character**,
and is not canon. Recorded only so a later pass does not mistake it for a character sheet.

## 6. Verification

Canon-scope **0**, notices **0**, tests **127**. **No lyric text entered the repository**,
and **no canon file was changed** — this entry only compares and indexes.

END OF ENTRY 69

===============================================================

===============================================================

# 70. Ruling 10 — the prose rule is scoped; the export is not here yet — 2026-09-21

`recovery/GATE_RULINGS_2026-09-21.md`, adopted from `PROSE_RULE_RULING_2026-09-21.md`.
Four load-bearing claims were checked first; **three confirmed, one refined, one
unverifiable.**

## 1. What changed

Prose is forbidden in the **substrate** and permitted in **`sources/`** (verbatim,
append-only) and **`manuscript/`** (authored, never tool-rewritten). Both sit outside
validation in either scope.

The old rule used **absence** to stop prose being mistaken for canon. That held until the
sources themselves were prose, at which point §1 and §7 contradicted each other and three
recovery documents had to record the conflict as unresolved. The new rule states the
distinction — *location is not authority* — instead of enforcing it by exclusion.

`PROSE_DIRS` names the exclusion in the validator so it is a **decision rather than an
accident of what `SUBSTRATE_DIRS` omits**, and five tests hold it, including one that
plants a file in `sources/` and proves it is not scanned. Tests **127 → 132**.

## 2. Confirmed — §7 was wrong

§7 said Business workspaces have *"no data export … both routes were tested and closed"*
and that sources are *"one-way storage and not reliably re-retrievable."*

The supplied `.json` files carry **`exported: 2026-09-15T16:57:09.617Z`**, an account id
and the native conversation object. An export exists and has been run. §7 is rewritten,
with the old text kept in §7.1 — several documents reasoned from it, most consequentially
the recommendation to hold source bodies outside the repository, which is what produced
the conflict Ruling 10 closes.

## 3. Confirmed, and stronger than the proposal claimed

The proposal argued for committing both formats because *"the `.json` preserves turn
structure the markdown flattens."* Measured, it is worse than flattening:

| | `.md` | `.json` |
| --- | --- | --- |
| structure | linear headings | native message tree, **678 nodes** |
| user | 216 | 216 |
| assistant | 213 | 230 |
| **system** | **0** | **229** |
| tool | 0 | 2 |

**The markdown renders no system messages at all.** Committing only the `.md` would
discard 229 messages per conversation — precisely the material recording how each
conversation was configured. "Both formats" is not redundancy.

## 4. Refined — the archive is lossy, but one implication was wrong

The whole 21-file sanitized archive is **25,952 words**; one supplied conversation is
**108,378**. It is plainly a small fraction of its sources, and its README's *"not
summarized or intentionally edited"* cannot bear the weight of meaning complete.

**But the retention percentages could not be verified here, and the conclusion drawn from
them overreached.** `Saga structural archive` was tested against what `CLAUDE.md` §3 cites
it for: **all 18 episode shells `S1.T1.B3.A3.E01`–`E18` are present**, plus the four
epilogue shells.

So the archive **kept the structured artifacts** and lost conversational context around
them. That is why extraction from it worked, and it means prior conclusions are
**unaudited, not discredited** — a materially different claim from "five documents reasoned
from 20% copies." Re-running extraction against full sources is how to settle which.

The README is corrected and the directory re-designated a **lossy historical derivative**.
**Not deleted**, per the proposal and for the stated reason: conclusions rest on it, and
deleting it would make them unauditable.

## 5. Unverifiable here — and it blocks the next step

The proposal reasons from **72 conversations**. **This session holds 7.**

    /root/.claude/uploads/  ->  7 conversations (16 files)
    /mnt/user-data/         ->  empty
    sources/                ->  created, EMPTY

**Ruling 10 gives the material a home. The material is not in it.** No claim about the
72-conversation corpus is made or relied on anywhere above; every figure quoted comes from
files actually in hand.

So the task shift is **half-actionable**: the policy is in place, the directories exist,
the validator holds the line — and the assessment of the full exports cannot begin until
the export is supplied.

## 6. Verification

Canon-scope **0**. Notices **0**. Tests **132**. All-scope **60**, the rise entirely from
this entry and the new documents quoting one-digit SIDs as evidence, per §56 §2.

**No prose entered the substrate, and `sources/` is empty**, so nothing has yet been
stored under the new permission.

END OF ENTRY 70

===============================================================

===============================================================

# 71. Amendment 1 to Ruling 10 — strip workspace ids — 2026-09-23

Ruled 2026-09-21: *"strip workspace ids"*, answering the question put before any source
was committed. Recorded in `recovery/GATE_RULINGS_2026-09-21.md`, **Amendment 1**.

## 1. The carve-out, and why it does not hollow out Ruling 10

Ruling 10 stores sources *"verbatim, never edited."* This is the **one** permitted
deviation: `workspace_account_id` is replaced with the literal `REDACTED` before a file
ever enters `sources/`.

An archive with one **declared, uniform, mechanically verifiable** redaction is still an
archive. An archive with undeclared edits is not. Three conditions hold the distinction:
the redaction is named in the ruling, in `sources/README.md` and **in the file itself**
(the key is kept, only its value replaced, so a reader sees that redaction happened); it
is surgical; and `MANIFEST.csv` carries the SHA-256 of **both** the original and the
stored file.

## 2. Scope, measured before writing the tool

- `workspace_account_id` is a **single top-level key** per `.json`, **one distinct value**
  across all files.
- **The `.md` files do not contain it at all.** They are stored byte-identical.
- `real_author` holds only `tool:web` / `tool:web.run`; `owner` is null. Neither is
  personal; neither is touched.

## 3. `tools/ingest_sources.py`

> **Superseded 2026-09-24** by `tools/redact_export_ids.py` (byte-identical output) run from `tools/ingest_export.ps1`; see `sources/README.md`.

Copies, redacts, verifies and manifests in one pass. Standard library only, so it runs on
the author's machine.

**The substitution is text-level, not a re-serialisation.** Loading and re-dumping the
JSON would reformat every line — a far larger edit than the redaction it is meant to make,
and one that would destroy any claim to verbatim storage. The tool substitutes the value
in place and leaves every other byte alone.

It aborts rather than storing a file when the redaction would change anything else, when a
`.md` unexpectedly contains the key, or when an existing stored file differs
(`sources/` is append-only; `--force` is required to override).

## 4. Proven, not asserted

Run against the 7 conversations in hand:

- **All 7 `.md` files byte-identical** to their originals.
- Each `.json`: **exactly one** occurrence replaced, **28-byte** size delta.
- **The reversal test.** Substituting the original value back into the stored file yields
  a file **byte-identical to the original**, for both JSONs.

That last check is the whole proof, and it is `O(n)`: if putting the value back reproduces
the original exactly, the redaction changed that value and **provably nothing else**. A
`difflib` comparison was attempted first and is quadratic — it did not finish on a 1.7 MB
file. A `cmp -l` byte count was also tried and is **actively misleading here**: because the
redaction shortens the file by 28 bytes, every subsequent byte is offset and `cmp` reports
~1.5 million "differing bytes" for a one-value change.

## 5. Order matters, and getting it wrong is unrecoverable

**Redaction happens before the first commit, never after.** Committing raw files and
stripping them later does not remove the value — it stays in git history permanently, and
removing it then means rewriting published history, which §2 forbids. The tool exists so
the redacted form is what gets committed in the first place.

## 6. Still outstanding

**`sources/` holds only its README.** The 144 files are not committed. The ruling, the
carve-out and the tool are all in place; the material is not.

END OF ENTRY 71

===============================================================

===============================================================

# 72. Two ingest pipelines reconciled into one — 2026-09-24

Instructed 2026-09-24. The repository held **two ingest pipelines that could not both
stand**, and neither could complete an ingest on its own.

## 1. Why they could not both stand

| Pipeline | Had | Lacked |
| --- | --- | --- |
| `tools/ingest_sources.py` (§71, Amendment 1's tool) | the redaction, correctly — key kept, value `REDACTED` | exclusions, forbidden-content scan, public-repository gate; and it wrote its own `MANIFEST.csv` **in a different schema**, which would have overwritten the reviewed one |
| `tools/ingest_export.ps1` + `tools/verify_sources.py` | exclusions, hashing, forbidden-content scan | any redaction at all — they **aborted** on `workspace_account_id` rather than applying Amendment 1 |

So one tool could redact but would have committed the token-bearing `.json` and both
personal conversations; the other would refuse to commit anything at all. **Running either
alone produces a wrong result, and running both produces a manifest collision.**

`sources/README.md` had drifted with them: it permitted Amendment 1's redaction in one
section and stated *"Exclusion, never redaction"* two sections later. Both sentences were
true of one tool each, which is exactly how the contradiction survived review.

## 2. The reconciliation keeps the mechanism and discards neither safety layer

`tools/redact_export_ids.py` carries Amendment 1's substitution forward unchanged: the key
is kept, the value becomes the literal `REDACTED`, the edit is text-level rather than a
re-serialisation, and every other byte survives. It is keyed to `MANIFEST.csv`, which now
records **two** hashes per `.json` — `json_sha256_exported` and `json_sha256_committed` —
so every stored file traces byte-for-byte back to the original export. A file matching
neither hash is refused rather than guessed at, and a file already matching the committed
hash is left alone, so re-running is a no-op.

**Byte-identity checked: 68 of 68.** Its output equals `tools/ingest_sources.py`'s on every
committed `.json`, verified by running both tools and comparing hashes. That check and the
end-to-end `-NoPush` run were performed **against a clone of `main` at `5e78cf2`, not in
this session** — the export files are not here — and are recorded on that basis.

`tools/ingest_sources.py` is **retired by `git rm`**, not deleted as recovered material:
it was tooling, its redaction lives on byte-identical, and §71 and
`GATE_RULINGS_2026-09-21.md` both keep their descriptions of it with a supersession line
added beneath. The bodies are unchanged; they are records of what was decided.

**The ruling is unchanged. Only the tooling is consolidated.** Amendment 1 said strip the
workspace ids before the first commit; it still says that, and the same substitution still
performs it.

## 3. What else the supplied files correct

- **The README contradiction is gone.** Redaction is now stated once, as the single
  permitted deviation from verbatim storage, specified to the byte.
- **The export timestamp is a range, not a point.** `16:46:23Z` to `18:22:17Z` across the
  72 conversations. The old README quoted one conversation's stamp as if it were the
  export's.
- **The verifier now fails an unredacted file** rather than ignoring the key — the gap
  flagged 2026-09-23, where `FORBIDDEN` omitted `workspace_account_id` entirely and
  Amendment 1 was therefore unenforced. It also holds the identifier's **SHA-256 only**,
  never its value, and hash-matches every UUID in every committed file, so the value
  cannot re-enter through a `.md` either.

## 4. The repository is public, and publishing is the author's decision

Confirmed 2026-09-24 against the GitHub API: `private: false`, `visibility: public`. This
**reverses the state recorded 2026-09-21**, when the repository was private. The ingest
script detects visibility by attempting an anonymous read and **refuses to commit to a
public repository without `-AllowPublic`**, so publishing the export is an explicit act
each time rather than a default. The author has taken that decision.

## 5. Verification

Run in this session, on the tooling commit:

- Canon-scope **0**; validator clean before and after.
- Self-tests **132**, all passing.
- All six excluded filenames present in `.gitignore`, **exactly once each**.
- The identifier's value appears **nowhere** in the tree, including this entry.

## 6. The ingest followed the same day

**Superseded within hours.** This section read *"`sources/` still holds only its README"*;
the ingest ran on 2026-09-24 and it no longer does. **§73 records it**, including the
end-of-line defect that made the first attempt non-verbatim.

END OF ENTRY 72

===============================================================

===============================================================

# 73. The account export is committed — and the eol trap it walked into — 2026-09-24

**138 files under `sources/chatgpt_export_2026-09/`**, from 70 of the 72 exported
conversations, run from the author's machine with `tools/ingest_export.ps1 -AllowPublic`.
The pipeline behaved exactly as §72 describes: 144 copied, 6 excluded, 68 redacted, 139
paths staged and **nothing outside `sources/`**.

Commits `3eece5c` (the export), `963ce04` (`.gitattributes`), `de5722b` (the repair).

## 1. The first commit was not verbatim, and the check that should have caught it passed

`core.autocrlf` is **true** on the ingesting machine. **20 of the 70 committed `.md` files
carried mixed line endings**, and git converted their `CRLF` to `LF` on the way into the
blob. Every one is *smaller* than its `md_bytes` row by less than its line count —
`Lucien_canon_workflow` lost **93 bytes across 222 lines**, `Project_memory` **3,513**. The
`.json` files hold no raw `CR` bytes, so all **68 of 68** redactions were byte-exact; the
damage was confined to markdown.

**The failure mode is the finding, not the byte count.** The conversion happens between the
working tree and the blob, so the ingesting machine still held the original bytes:
`verify_sources.py` run *there* hashed the originals and printed `PASS`. Run against a fresh
checkout in the same hour it printed **20 hash mismatches**. The archive verified correctly
**only on the machine that made it** — the one place the check cannot tell you anything.

This is the second time in two days that a check passed by looking at the wrong copy; §71's
`cmp -l` reading was the first. **A verification that runs only where the artifact was
produced is not a verification.** MANIFEST.csv caught it the moment it was read anywhere
else, which is precisely what an audit surface is for.

## 2. The fix is a rule, not a repair

`.gitattributes` marks **`sources/** -text`**, disabling eol conversion in both directions
regardless of the committing platform's `core.autocrlf`. The 20 blobs were then re-committed
from the originals, guarded by running `verify_sources.py` on the author's machine **first**
— a `PASS` there proves the working copies are still untouched, and re-committing rewritten
files would have stored the wrong bytes twice over.

Two files rode along and are now pinned: `sources/README.md` and `MANIFEST.csv` flipped to
`CRLF` under the new rule, since `-text` stores whatever the working tree holds. Both are
**authored here, not received**, so they carry `text eol=lf` and cannot drift with the
committing platform. Their content was verified byte-identical across the flip.

## 3. Verified, on a checkout that is not the one that made it

- `verify_sources.py` — **PASS**, 138 present, 6 excluded, 0 unlisted, every hash matched.
- The identifier's value — **absent from the entire tree**, by `git grep`.
- `"workspace_account_id": "REDACTED"` — **68 files**, matching the 68 committed `.json`.
- Canon-scope **0**; self-tests **132**, all passing.

## 4. Three defects in `ingest_export.ps1`, recorded not fixed

1. **`-DryRun` leaves its copies in place**, so the real run that follows always aborts on a
   dirty tree. Hit on the first attempt. The fix is for the dry run to clean up after itself,
   or for the preflight to exempt untracked files under the destination — **not** to relax
   the clean-tree check.
2. **`Set-Content -Encoding UTF8` writes a BOM** in Windows PowerShell 5.1, so `3eece5c`'s
   subject line opens with an invisible `U+FEFF`. Not worth rewriting published history.
3. **`git push`'s ordinary stderr renders as a PowerShell error record.** The push had
   succeeded; the red text was noise. A caller who trusts the colour would have pushed twice.

## 5. What this unlocks

`CLAUDE.md` §8 item 6 — *"until this runs, 'not exported' and 'does not exist' cannot be told
apart"* — **is now runnable against real sources.** The two live targets, `Spine Architect
chat` and `Saga Visual Bible Framework`, can be searched for rather than reasoned about, and
every extraction claim resting on the 25,952-word sanitized derivative (§7.2) can be re-run
against the **7,363,532 words** now in hand.

**None of that is done.** The material is stored and auditable; it is not yet read.

END OF ENTRY 73

===============================================================

===============================================================

# 74. First survey of the export — two targets close empty, the Book 1 packets are found — 2026-09-24

The first search of the corpus committed in §73. Full findings at
`recovery/ACCOUNT_EXPORT_FIRST_SURVEY_2026-09-24.md`. **Nothing migrated, nothing ruled.**

## 1. Both live targets of §8 item 6 are resolved, and neither holds canon

- **`Spine Architect chat`** is `2025-12-09__Structural_spine_storage__693823f7` —
  **2 turns, 410 words.** The startup prompt appointing it owner of the nine-book
  structural spine, and the reply *"Ready. Paste the first structural segment…"*. **Nothing
  was ever pasted.** The queue's description of it was accurate about its charter and wrong
  about its contents; the claim traces to `Character Vault Chat` **routing** continuity
  storage there, which is not a record that anything arrived.
- **`Saga Visual Bible Framework`** — **2 turns, 1,070 words**, a Workflow/Pipeline/Schema
  stamped *"Ready for population after the Faction Bible is completed."* The framework, not
  the Visual Bible.

**This is exactly the distinction item 6 was raised to make** — *"until this runs, 'not
exported' and 'does not exist' cannot be told apart."* Both were exported; both are empty.
Item 6's remaining value is the inventory, not these two.

## 2. `Archive Veil Book 1` holds E00–E17

**18 distinct packets**, full ECID headers plus `PRESSURE MAP`, `EPISODE JAZZ`, `BEATS` and
`EXIT CONDITION`. The repository held **E16–E18 only**, so **E00–E15 are recovered** and
item 7's ten-month-old prediction — *"this is where the E00–E15 packets are expected to
be"* — is confirmed.

`EPISODE 3` is pasted twice and is **not a version conflict**: identical bodies, a
truncation query between them, then *"archived verbatim with no truncation."*

## 3. Five things the packets bear on, none of them resolved here

1. **The prologue's act slot is `A0`** — a fourth form, after `A1`+`E00`, Ruling 6's `PR`,
   and the export layer's beat-1-inside-ACT-I. It is the only one implying a zeroth act,
   which the three-act cap forbids, so it most likely reads as Ruling 6's position marker
   under another letter. **That inference is the author's.**
2. **The `B01.A1` band is breached on all three axes** — `U7` and `FX3` at E00, `W3` at E13
   and E14, against `U1–U4` / `W0–W2` / `FX0–FX2`. That band is one of only **three**
   marked `basis: observed`, and it was observed from E16–E18 **while sixteen episodes of
   the same act were unexported**. E14's own note calls **FX3** the *"Act-level limit"*.
   The FX ceiling has already moved once on exactly this evidence (§18, FX1 → FX2). Whether
   the prologue breaches `A1` at all depends on item 1, so **the two are put together.**
3. **§3's continuous-numbering ruling is corroborated at source** — `E16` is `A1`, `E17` is
   `A2`, no restart, in an artifact predating the ruling by ten months.
4. **§4.1's vocabulary findings are confirmed as input data** — arrow forms throughout,
   `Mode` carrying two to four values (`CIV`, `ACT`, `INT`, `SCI`, `HOR`, `HORP`, `LORE`),
   and a `-TINT`/`-LACED` resonance family larger than the three tokens §4.1 adjudicated.
   The §1.5 mapping applies unchanged; `HOR`/`HORP` and the multi-value shape are not
   covered by it.
5. **The first Silence-and-Hope material in any export** — the `E00` packet gives them a
   contrast pair (containment against warm modulation), calls them *"metaphysical roles,
   not beings"*, and has them choose not to intervene. **A beat outline, not a character
   file**, and Tier D. Item 9b's gap is no longer total; item 9b is not closed.

## 4. Corrected within the hour — §2 was a re-discovery, and the correction is the better finding

The survey was written **without accounting for the 2026-09-20 forensic audits in this same
directory.** `ACCOUNT_EXPORT_B01_ACT1/ACT2/ACT3_EPISODE_FORENSIC_AUDIT_2026-09-20.md` had
already recovered Book 1's packets — **E00–E42, all three acts** — from
`2025-12-08__Episode_expansion_process__6936cb32`. **§2 above claimed as a find what was
found four days earlier, more completely, from a different source.**

**Item 7's prediction was right about the material and wrong about its address.** It named
`Archive Veil Book 1`; the packets came from `Episode expansion process`. Item 7 and item 8
are satisfied in substance, and **`CLAUDE.md` §6's *"packets for E16–E18 only"* is stale** —
which §6 itself warns of.

**What survives is sharper than what was claimed.** `Archive Veil Book 1` has been cited as
a *target* in four places and **read by none of them**, so Book 1 Act I now has **two
independent witnesses, one day apart, that disagree**:

| | `Episode expansion process` 12-08 | `Archive Veil Book 1` 12-09 |
| --- | --- | --- |
| Titles | dramatic — *The Sick Child*, *Too Late* | structural — *THE CHILD IN THE SWAMP (Part I/II)* |
| Prologue | **The Conversation in the Sky** — the ruled title | **Silence & Hope** — the retired title |
| Act I ends | **E15**, Act II opens *Baz Arrives in NOLA* at E16 | **E16** (`S1.T1.B1.A1.E16`), Act II opens at E17 |

1. **The prologue title inverts this project's usual tiebreak.** §3's ruled title sits in
   the **earlier** artifact and the retired one in the **later**. §27.6 declared the
   `ACT * SUMMARY` pages superseded precisely on "later artifact wins". **Here the ruling
   and the recency heuristic point opposite ways** — the ruling stands, so the heuristic is
   what fails. First case showing it is not load-bearing alone, which bears directly on
   §26.12's open question about what rule decides between conflicting recovered versions.
2. **The act boundary differs by one episode, and the act slot is part of the SID.** The
   two sources give `E16` different identifiers. Narratively compatible — both close Act I
   on Baz being summoned and open Act II on his arrival — but a migration writes one of
   them into canon. **This is *which Veil draft is canon* at one episode's granularity.**

Also corrected: §3's claim that the `E00` packet is the first Silence-and-Hope material in
any export. It is the **second**; the 12-08 prologue is in the Act I audit. §22's *"the 21
exports hold essentially nothing"* was about the **sanitized derivative**, not the account
export.

**Unaffected by the correction:** the two empty item-6 targets (§1), and `A0`, which appears
nowhere in the repository outside this entry and the survey.

## 5. Verification

Canon-scope **0**; notices **0**; tests **132**; verifier **PASS** at 138. All-scope rises,
entirely from this entry and the survey quoting **one-digit book** SIDs and `A0` as
evidence — the condition §3's scope warning and §56 §2 both describe, not new defects.

END OF ENTRY 74

===============================================================

===============================================================

# 75. Editorial review of the 2026-09-20 → 24 work — 2026-09-24

Full review at `reports/EDITORIAL_REVIEW_OF_RECENT_WORK_2026-09-24.md`. Occasioned by §74
§4: a survey re-derived findings the 09-20 audits already held. That was a reading failure
**and a symptom** — a session that follows `CLAUDE.md` faithfully can still miss four days
and 180 commits, because the working agreement no longer describes the repository.

## 1. The body of work is sound, and its discipline is better than this ledger's

Eight phases in four days: 24 export audits and **E00–E42 episode audits for Books 1–3**;
the B01 beat bible from v1 to the integrated v4.1b; Mechanica/Resonance, Conflict and VFX
integrity audits each with a paired proposal; lived-world baselines; the B01 event-mechanics
chain ending in **author ruling D1–D7**; the saga anchor register; all 36 milestones
reviewed; and the Loom carry-forward passes.

**The habit worth copying:** both author rulings state their own *scope of acceptance*.
`B01_EVENT_OBSERVATION_AUTHOR_RULING` says outright it "does not claim the author reviewed
each prior source line." That is what stops an "Agreed" becoming approval of everything
upstream of it, and this ledger has no equivalent convention.

## 2. Verified mechanically, from a clean checkout

Every testable claim in `FULL_EXPORT_ALL_SYSTEMS_STATE_REVIEW_2026-09-23` holds: the stale
`Mortal Technology` labels, five header-only grids, four `source_canon/` subdirectories
holding only READMEs, TODO scaffolding in the trilogy cards. One correction of emphasis —
`VT_RULES.md` is **not** stale, it already carries its retirement note.

## 3. Three governance defects, none of which an audit can see about itself

1. **`Technarch` has re-entered a fifth time, by a new route.** §16.1 and §9.1 name two
   routes, merges and verbatim heading copies. This is neither: it is **sustained analytical
   writing adopting the sources' spelling**. `canon/` **0** and `rules/` **0**, so canon
   scope is clean — but `proposals/` is **17** against §9.1's recorded 6, and in `reports/`
   the retired spelling **outnumbers** the canonical one **23 to 13**. Only **2 of 29**
   occurrences in the 09-2x layer sit near a supersession marker, so these are not the
   annotated quotations §9.1 describes.

   **The prescribed mitigation has failed five times.** §9.1 also asserts the validator
   cannot catch this. **True of the current validator, false as a limit** — a retired-terms
   check is structurally identical to `CHK_VOCAB`.
2. **`reports/` has been repurposed and its README now contradicts its contents.** Both
   `CLAUDE.md` §1 and `reports/README.md` call it generated artifacts, *"do not hand-edit,
   regenerate."* **34 files; 2 are generated.** The other 32 are hand-authored editorial
   reports including the week's two most load-bearing documents. The two real generated
   files are **stale** — they record 27 canon-scope and 61 all-scope violations against a
   current **0**. This wants a ruling, not a cleanup: the repository otherwise keeps a clean
   four-way separation of evidence, argument, verdict and generated fact.
3. **`decisions/` is undocumented.** It holds the two author rulings — the highest-authority
   artifacts of the week — and appears in no table or index in `CLAUDE.md`. That is exactly
   the failure that occasioned this review.

## 4. `CLAUDE.md` is now the repository's least current document

§6 is stale on packets (E00–E42 recovered, not E16–E18). §8 item 6's three targets are
**all resolved**. Item 7 is satisfied, from a different conversation than it names. §8.0's
"three layers missing" is overtaken. §9.1's counts are wrong. §1's table calls `reports/`
generated and omits `decisions/`.

§6 carries its own *"verify with `git`"* warning and that warning worked. **§8's queue
carries none, and §8 is where the misdirection happened.**

**Recommended: one consolidation pass on the *state* sections only** — §1's table, §6, §8's
queue, §9.1's counts. §3's conventions and §4's open-author-question list are current,
carefully built, and should not be touched.

## 5. Two tooling items offered, not begun

`CHK_RETIRED_TERMS`, reading a `retired_terms` map from `canon_rules.json` — violation in
canon scope, notice elsewhere, with a quotation-suppression marker so annotated cases stay
legal and an explicit exemption for `MT_RULES.md`, which §4 **holds**.

And the **provisional exception manifest** that `B01_EVENT_OBSERVATION_AUTHOR_RULING` §4
requires and that does not exist: the E37/E36-with-S05 and E44/E43 inversions are a live
trap for any automated pass, and the ruling anticipated the trap without the artifact being
built.

## 6. One corroboration worth recording

`PRE_EBCI_SYSTEMS_AUDITS_REVIEW` recommends treating `FX2` as a **presentation default, not
a ceiling**. The validator already implements exactly that, independently and for its own
reason: `container_band()` returns `None` for `fx`, so `CHK_CONTAINMENT` never checks it as
a ceiling, because `default_vfx_ceiling` is a default (§57). Two lines of reasoning five
days apart, same conclusion, same axis — worth having when FX is next argued against the
recovered `E14` note calling **FX3** the "Act-level limit" (§74 §3).

END OF ENTRY 75

===============================================================

# 76. Governance consolidation pass — 2026-09-25

The first of the consolidation steps the author adopted on 2026-09-25, after a
repository-wide review and a parallel external one agreed: **consolidate and selectively
promote before any further archaeology or episode generation.** This entry acts on §75,
whose three governance defects and two offered tooling items had gone unaddressed through
twelve further commits. **Nothing ruled, nothing migrated, no canon content changed.**

## 1. `CHK_RETIRED_TERMS` — the manual grep becomes a check

`rules/canon_rules.json` gains a `retired_terms` block (six names, each with canonical form
and ruling; additions only). The validator reports a match as a **violation in canon
scope** and a **notice in all-scope**. Case-insensitive, whole-word; exceptions pinned to
file, term and line substring. **`Mortal Technology` is deliberately not listed** — held,
not retired (§20).

`reports/` and `decisions/` joined all-scope. They had been scanned in **neither** scope,
which is how `Technarch` in `reports/` went 23 → 30 after §75 counted it.

## 2. The first run found three misses from the §20 VeilThread pass

That pass grepped case-sensitively for `Veil-Touch`. Three headings set in capitals kept
the retired name, and §20 and CLAUDE.md have reported the rules layer clean since:

| File | Was | Now |
| --- | --- | --- |
| `rules/Mechanica-v4.md` §38 | `VT — VEIL-TOUCH` | `VT — VEILTHREAD` |
| `rules/Channels/VT_RULES.md` line 1 | `# VT — VEIL-TOUCH RULES` | `# VT — VEILTHREAD RULES` |
| `rules/Channels/CHANNELS_OVERVIEW.md` §4 | `VT — VEIL-TOUCH (WHAT IT IS)` | `VT — VEILTHREAD (WHAT IT IS)` |

Name changes under the existing ruling; no mechanic touched. Mechanica §37 `MT — MORTAL
TECHNOLOGY` is left as is.

## 3. Documents

- **`CLAUDE.md` rewritten**, 883 → 262 lines, rules only. Old version archived verbatim at
  `recovery/CLAUDE_MD_ARCHIVE_2026-09-21.md`; pre-2026-09-25 citations of "CLAUDE.md §N"
  refer to it.
- **`decisions/README.md`** — authority rule (a ruling overrides proposal/recovery/report
  interpretations within its stated scope, only there), the scope-of-acceptance convention
  made permanent, and an index including the six earlier rulings that stay in `recovery/`.
- **`reports/README.md`** — two kinds: generated `VALIDATION_BASELINE_*`, authored everything
  else. Nothing moved; links preserved.
- **`decisions/B01_SEQUENCE_EXCEPTIONS_PROVISIONAL.json`** — the manifest the 09-23 ruling
  item 4 requires. Both inversions, both orders, marked `HELD`. Chooses no order.
- **`README.md`** replaced; it still described a starter template.
- **`.github/workflows/validate.yml`** — the three checks on every push.

## 4. Recorded, not resolved

1. **E19 gate.** The prohibition (archive §4) was written against the 18-episode Act I
   numbering. B01 v4.1b has 48 episodes and review packets now reach E45. No ruling records
   whether the EBCI hold replaced the gate. **Author question.**
2. **`canon_rules.json` `_naming_note` says `Mortal Technology` is retired**; §20 and the
   channel ruling hold it open. Contradiction recorded in CLAUDE.md §4.1; the note is not
   edited.
3. **Branches.** `claude/gifted-goodall-st4n7r` (1 unique commit, an older
   `narrative-audit-framework-v1.md`) and `proposal/concord-2026-reconciliation` declared
   archival in CLAUDE.md §8. Neither deleted.
4. **Remaining sweep**, queued as CLAUDE.md §9 item 1: own-voice `Technarch` and one-digit
   `B1` labels in `proposals/` and `reports/`. Quotations stay. Now counted by the
   validator rather than remembered.

## 5. Verification

Canon scope **0**; self-tests **132 → 144**; verifier **PASS** at 138. All-scope notices
**351**, all `CHK_RETIRED_TERMS`, all outside the substrate.

END OF ENTRY 76

===============================================================

===============================================================

# 77. Own-voice retired names swept from proposals/ and reports/ — 2026-09-25

Completes the one item §76 left open in `CLAUDE.md` §9 item 1. `CHK_RETIRED_TERMS` notices
were used **as leads, not as a replacement list**: every occurrence was read in context and
classified before anything changed.

## 1. What changed

| | Count |
| --- | --- |
| `Technarch` → `Technarc`, own voice | **32** across 13 files |
| `S1.T1.B3.A3.E14` → `S1.T1.B03.A3.E14`, own-voice example | **1** |
| `B7-nn` / `B8-nn` → `B07-nn` / `B08-nn`, row handles | **22** in one file |
| Annotation instead of edit | **1** file |

The handles are in `reports/B07_B08_PLACE_EVENT_PRESENCE_LEDGER_PASS1_2026-09-23.md`, which
coined them itself while its own title reads `B07–B08`. **Nothing outside that file cites
them**, checked before renaming, so no cross-reference breaks.

## 2. What was deliberately preserved — 16 `Technarch` remain in scope

**Quotations of a source, verbatim.** Three spans were protected by name during the sweep:
the Dec 8 macro's *"Technarch response collapses; disinformation surges,"* the milestone
row wording *"Technarch collapses in B8,"* and — a different case — `bystander and
Technarch` in `MECHANICA_RESONANCE_SYSTEMS_INTEGRITY_AUDIT` §28, which **records the literal
strings that were searched**. Correcting that one would falsify a method record, not a
faction name.

**Already-annotated quotations** in `proposals/concord-2026/`: the `LOCATIONS_COMBAT_ANTAGONISTS_PRIMER_REVIEW`
and `EDITORIAL_CASTING_RESOLUTION_SINGAPORE` blocks that carry *"Retired spelling retained
above, deliberately,"* and the `location_places_PROVISIONAL` CSV row, whose cell already
reads `Technarc towers district` and quotes the source's `Technarch towers` beside it.

**`reports/EDITORIAL_REVIEW_OF_RECENT_WORK_2026-09-24.md`, 7 occurrences.** The retired
spelling **is that document's subject** — it is the record of the fifth re-entry this sweep
corrects. Rewriting it would delete the finding.

## 3. Annotated rather than rewritten

`proposals/concord-2026/RECOVERED_SAGA_SPINE_PROPOSAL.md` gives `S1.T1.B1.A1.E01` and
`S1.T1.B1.A1.E01-B01` as its SID and BID examples. Both are pre-ruling forms, and the
document's own closing line treats acronym expansion as **version history**. Correcting the
book digit alone would have produced `S1.T1.B01.A1.E01-B01` — a corrected SID wearing a
retired beat suffix, which is worse than either form. It carries a note naming both current
forms instead.

## 4. Left alone, and why

**`reports/VALIDATION_BASELINE_ALL_2026-09-19.md` — 37 of the 105 SID violations.** A
**generated** artifact whose content *is* the list of malformed SIDs it detected. Hand-editing
it would falsify a report; `reports/README.md` forbids it. It regenerates.

**`reports/README.md` — 3 hits.** It quotes the malformed forms while explaining them,
including the sentence noting the milestone CSVs' hits sit in a free-text `notes` column
citing a recovered packet.

**`recovery/` — 252 notices, untouched.** Out of this item's scope, and `recovery/` is never
edited in place.

**Other retired terms are out of scope and remain**: 38 `Foix`, 8 `Veil-Touch`, 8 `Koro Ito`,
1 `Kade Rios`, 1 `Caro Gauthier` in `proposals/` and `reports/`. §9 item 1 names `Technarch`
and one-digit `B1` only. **Recorded here as the next sweep's leads**, and the `Foix` figure
is the largest single block left.

**`S1.T3.B09.A4.E16`** appears in `reports/README.md` and the baseline as a **ruled-out**
act form (ledger §25: Book 9 has three acts). Not one-digit, not in scope, already explained
where it appears.

## 5. Before and after

| | Before | After |
| --- | --- | --- |
| All-scope notices | 365 | **333** |
| — `proposals/` | 65 | **53** |
| — `reports/` | 39 | **19** |
| — `recovery/` (out of scope) | 252 | 252 |
| All-scope `CHK_SID_FORMAT` violations | 105 in 18 files | **104 in 17 files** |
| Canon scope | 0 | **0** |
| Self-tests | 144 | **144** |
| Source verifier | PASS | **PASS** |

The 32-notice fall equals the 32 corrections exactly: 12 in `proposals/`, 20 in `reports/`.

**No canon mechanics, episode order or EBCI status was touched.** The E19/EBCI ruling is
deliberately **not** in this change.

END OF ENTRY 77

===============================================================

===============================================================

# 78. The remaining retired terms reviewed — and almost none of them were drift — 2026-09-25

§77 swept `Technarch` and one-digit `B1`. This pass applies the same method to everything
left in `proposals/` and `reports/`: **56 occurrences across five terms**, each read in
context before anything changed.

## 1. The result is the opposite of §77

**Zero text corrections were warranted.** One annotation was.

| Term | In scope | Own-voice drift | Disposition |
| --- | --- | --- | --- |
| `Foix` → Arnaud | 35 | **0** | provenance, rename records, annotated strikethroughs |
| `Veil-Touch` → VeilThread | 7 | **0** | quotations of the stale rule file, or "retired" statements |
| `Koro Ito` → Ito Masayuki | 5 | **0** | quoted memory export, annotated supersession |
| `Kade Rios`, `Caro Gauthier` | 0 | — | present only in the 09-24 editorial review |
| `Technarch` (residue) | 9 | **0** | the three protected quotations, five annotated, one CSV cell |

**This is a finding, not a null result.** §77 corrected 32 occurrences because sustained
analytical writing had adopted the sources' faction spelling. The character and channel
names show **no such drift at all**: the 2026-09-19/20 passes handled them correctly, and
every survivor is doing a job.

Representative: *"historical **Foix** references remain valid provenance and must not be
rewritten inside archived source evidence"*; *"**Superseded 2026-09-19:** James ruled that
the names in `canon/characters/` are final"*; *"`rules/Channels/CHANNELS_OVERVIEW.md` still
calls MT 'Mortal Technology' and VT 'Veil-Touch,' despite current channel rulings"*. Each
**names the retired form in order to retire it.** Correcting any of them would delete the
record that the rename happened.

**So `CHK_RETIRED_TERMS`' notice count is not a defect backlog.** After §77, the notices in
`proposals/` and `reports/` are almost entirely the audit trail working as designed. The
number will not go to zero and should not.

## 2. The one thing worth acting on

`proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md` proposes a `json` block
for `rules/canon_rules.json` carrying `"MT": "Mortal Technology …"`, `"VT": "Veil-Touch …"`
and `"LT": "Luminous Thread …"` — written the **same day** the channel ruling retired all
three labels.

The document is not wrong about anything: its quotation of `CHANNELS_OVERVIEW.md` is
accurate, that file does still carry the old labels, and the proposal's real subject is the
`res_states_kind` grouping, which the labels do not affect. But **applying the block as
written would put retired names into canon scope**, where `CHK_RETIRED_TERMS` makes them a
violation and CI fails.

**Annotated, not rewritten.** Rewriting would misreport what was proposed on 2026-09-19;
the note says the grouping stands, the labels do not, and names the current forms. Same
reasoning as §77 §3 for the recovered spine proposal.

## 3. Deliberately untouched

`Mortal Technology` — **9 occurrences in scope and not in `retired_terms` at all**, because
`CLAUDE.md` §3 and §4 **hold** it rather than retiring it: the MT-versus-infrastructure
question is open, and `rules/Channels/MT_RULES.md` must keep its name until it is ruled. The
check correctly says nothing about them.

`recovery/` — 252 notices, never edited in place. `decisions/` — 2 notices, author rulings.

`reports/EDITORIAL_REVIEW_OF_RECENT_WORK_2026-09-24.md` — 12 notices across five terms,
because §5 of that document **lists the retired terms as the specification for the check
that now reports them**. Rewriting it would delete the specification.

## 4. Verification, and a correction to §77's figures

| | HEAD after §77 | After §78 |
| --- | --- | --- |
| All-scope violations | 108 | **112** |
| All-scope notices | 346 | **357** |
| Canon scope | 0 | **0** |
| Self-tests | 144 | **144** |
| Source verifier | PASS | **PASS** |

**Both figures rise, and that is correct behaviour.** Nothing was corrected. The annotation
and this entry **name retired terms in order to discuss them**, and the paragraph below
**quotes four malformed SIDs in order to explain them** — so all-scope gains 11 notices and
4 violations from this entry alone. A pass that reviews malformed names and identifiers
necessarily adds both. **Judge the sweep by the classification, not by the counter**; the
counter that matters is canon scope, which is **0**.

**§77's reported figures were measured too early and understate the committed state.** It
reported 104 violations and 333 notices; the true post-commit figures are **108 and 346**.
The gap is **§77's own ledger entry**, which quotes `S1.T1.B3.A3.E14`, `S1.T1.B1.A1.E01`,
`S1.T1.B1.A1.E01-B01` and `S1.T3.B09.A4.E16` as the evidence for what it decided — exactly
**+4** malformed SIDs — and names five retired terms, **+13** notices. The measurement was
taken after the file edits and before the ledger was written.

**The §77 comparison it drew is still sound**, because both its before and after figures
excluded its own entry: the 32-notice fall from 365 to 333 is a like-for-like measure of the
corrections. What was wrong was calling 333 the committed state. **Measure after writing the
ledger, not before** — the ledger is inside all-scope.

**No canon mechanics, episode order or EBCI status touched. The E19/EBCI ruling is not in
this change.** `CLAUDE.md` §9 item 1 is now complete.

END OF ENTRY 78

===============================================================

===============================================================

# 79. The E19 rule is superseded by the EBCI hold — 2026-09-25

Ruled 2026-09-25, in the author's words: *"e19 rule is superceded by ebci"*. Recorded at
`decisions/B01_E19_EBCI_GATE_AUTHOR_RULING_2026-09-25.md`.

## 1. What it settles

The question `CLAUDE.md` §4.1 carried as *"not recorded anywhere"*. The archive's §4 rule —
*"E19 is named but never built. Do not generate, draft, or outline it. The prohibition
stands until James lifts it"* — was written against an **18-episode Act I**. B01 v4.1b is a
prologue plus **48 episodes**, so `E19` had stopped denoting the first unbuilt episode of
anything, and it was unclear whether the old rule still bound alongside the EBCI hold.

It does not. **One gate replaces two.**

## 2. Supersession is not release, and that is the whole point

**The set of episodes that may be generated today is unchanged: none.** Before the ruling a
session faced two prohibitions on building B01 episodes; it now faces one, **and that one is
still shut** — `B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md` §5, *"Continue to hold
event EBCI … do not begin the deferred expansion by implication,"* and `CLAUDE.md` §9 item 5,
**"Release B01 to EBCI — author gate."**

**"E19 is unblocked" is the misreading the ruling document exists to prevent.** `E19` has no
privileged status now. It is one of 48 episodes behind a single hold, rather than the first
episode behind two.

This is why the ruling was written as a *narrowing*, not a *lifting*: a four-word author
reply retiring a prohibition is exactly the shape that, recorded carelessly, becomes
accidental permission. The `decisions/` convention — accepted in column 1, **not** accepted
in column 2 — is what stops it, and column 2 here is long.

## 3. Scope

**B01 only.** The hold it defers to is B01-scoped. B02–B09 remain governed by §9 item 6,
*"No B02–B09 episode expansion yet,"* untouched. Also untouched: the two sequence inversions
in `B01_SEQUENCE_EXCEPTIONS_PROVISIONAL.json`, D1–D7 of the 09-23 ruling, and every other
open question in §4.1.

## 4. Migration

`CLAUDE.md` §4.1 loses the E19 row — the question is answered. §8 records the single-gate
state and says in its own text that supersession is not release. `decisions/README.md`
indexes the ruling. **The archive keeps its original prohibition verbatim**: `recovery/` is
never altered in place, and the superseded rule is the record of what was superseded.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138. All-scope figures
rise again from this entry quoting the retired rule, as §78 §4 describes.

**No episode content was generated, drafted or outlined.**

END OF ENTRY 79

===============================================================

===============================================================

# 80. Secondary and tertiary cast reconciliation, Pass 4 — 2026-09-25

`CLAUDE.md` §9 item 2. Proposal at
`proposals/SECONDARY_TERTIARY_CAST_RECONCILIATION_PASS4_2026-09-25.md`. **Nothing renamed,
nothing promoted, no episode function or B01 order touched, no EBCI.**

## 1. Four Pass 1–3 actions have closed since 2026-09-19

Mara Niht's source is recovered (§67); her B01 scene question is answered by v4.1b, which
maps *"v3 E08 | source E08; unnamed local → Mara/M"* and gives her a civilian Life Packet;
her Filament source is substantially recovered. Only *"recover former Mara Nichols"* is
still open.

**One conclusion is qualified rather than closed.** PASS2 §80's *"Mara Niht links Elisabet's
pre-saga Icelandic life to the living cultural world of the saga"* is **authorial design
intent, not recovered fact**: her source has **zero** occurrences of `Concord`, `Elisabet`,
`Velvet Vein` or `Harpa`, and its Iceland coding is explicitly aesthetic — *"content palette
(urban, not Iceland)"*. Corroboration, not derivation.

## 2. The two-Mara hazard is real, not yet live, and cheapest to settle now

The 2026-09-19 ruling protects both `Mara / M` and `Mara Niht`. **Pass 4 does not reopen
it.** What the ruling could not have addressed, because she had no recovered source then, is
that **both are New Orleans characters** — the Filament in the community web, the musician
*"visiting"* the Velvet Vein, which is a public venue a community organizer can walk into.

**It is not a live problem.** All 15 `Mara` mentions in v4.1b are A01; Mara Niht is absent
from B01 and her **first appearance is on the `DO NOT LOCK` list**. So it becomes real the
moment she is placed — which makes a decision taken now free and one taken later a scene
edit.

**Proposed: a register rule, not a rename.** The recovered material already separates them —
the Filament bible states call signs *"are anonymous single letters used inside Filament
channels and are not public branding,"* so she is **`Mara` in neighbourhood and civic
registers and `M` inside Filament channels**, while the musician is **`Mara Niht` in full,
never bare `Mara`**. No name changes, no beats touched.

## 3. The sharpest collision in the cast was never named

**`Ren`.** **A09 Ren Bellande** (Filament; helper → direct action → coercion) against
**C02 Caldas Ren** (Dominion; surveillance → intimidation). A given name against a surname,
**across opposing factions**, both `KEEP`, and **Passes 1–3 did not list it** — their
collision set named Mara, Halley, Harrow, Arnaud, Nguyen, Baptiste and Reyes.

Cheap to fix: A09's status is **already `REBUILD / RENAME / MERGE`** while C02 is plain
`KEEP`, so renaming A09's given name resolves it without touching the Dominion layer.

Every other token collision pairs a kept character against a **retired** alias and holds
while the retirement does. Two are worth writing down: **`Baptiste` is shared by two kept
characters** (Roland, Anaïs) with family intent nowhere stated, and **`Harlow` is a
single-word name one character from the retired `Harrow`**.

**A reference gap, not a duplicate:** the 09-24 carriers document uses a bare `Sparrow` as a
Loom carrier without a `cast_id`, while **A03 Jae "Sparrow" Nguyen** ranges `B1–late
Neon/Loom`. Probably the same person; unstated, it is how a duplicate support role gets
created.

## 4. Recurrence, and a limit on how far it can be stated

The place overlay's B1 foreground (Mara/M, Arianna, Sparrow lightly, Mme Rosette, Rootkeeper)
and the measured v4.1b footprint agree: **seven of 57 registry characters carry B01** — Mara/M
15 mentions, Trip 14, Broussard 7, Virelli 5, Rosette 3, Rootkeeper 2, Arianna 1, Naima 1.
B01 is deliberately thin, per the overlay's *"do not seed the entire later Filament ensemble
in B1."*

**But the registry cannot answer this saga-wide.** 26 of 57 rows have an **empty `range`**:
all 7 of bundle D, 7 of 8 in G, 6 of 11 in F, 3 of 5 in C, 2 of 3 in E — against **0 of 12 in
A**. Recurrence is answerable for the Filament and NOLA-civic layers and **not** for the
institutional, antagonist or media layers. Filling those is a mechanical follow-up.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

Six decisions are put to the author, and **none of them blocks §9 item 3 or item 4** — the
B01 event census and the whole-book rhythm pass can proceed with the cast as it stands.

END OF ENTRY 80

===============================================================

===============================================================

# 81. B01 event census Pass 2 — tier mapping and the measurements Pass 1 asked for — 2026-09-25

`CLAUDE.md` §9 item 3. Proposal at
`proposals/B01_EVENT_CENSUS_PASS2_TIER_MAPPING_AND_MEASUREMENTS_2026-09-25.md`. **No event
created, promoted, merged or counted as settled; no episode function, supplement or the
locked order touched; no EBCI.**

## 1. Two letter schemes were colliding

§9 item 3 says *"C events separated from D receipts"* — the **tier** grammar, where **C** is
a local event and **D** a receipt. Census Pass 1's ledger uses its own **C/Q/L**, where
**C** is a *candidate-bearing slot*, not an event, and **L** silently contains what the tier
grammar calls **D**.

**So `C` meant two different things across two live documents.** This repository has been
bitten by exactly this before — the retired `D=Notion / E=assistant / F=memory` lettering
against the A–E source tiers (§5). **Proposed: never write a bare letter** — `slot-C/Q/L`
for census rows, `tier-C/D` for events.

The restatement matters: the task is to find which changes inside the 48 slots are
**tier-C local events** and which are **tier-D receipts attached to them**, not to count
slots. **"22 events" is not a reading of this census**, and a bare number travels further
than its caveat.

## 2. Three of the five requested measurements are computable; two must not be

Pass 1's gate 3 asked for five. Computed by reparsing its 48-row ledger (22 slot-C, 6
slot-Q, 20 slot-L, verified):

- **(d) Longest run without a changed option: 4** — E41–E44 — and **never more than 2
  consecutive slots with neither slot-C nor slot-Q.** There is no dead stretch in the book.
- **(e) Consequence screen time: 83%** of the 28 candidate-bearing slots have receipt space
  within two episodes. The five without are E07, E15, E23, E47, E48 — and **E47/E48 are an
  artifact of the book ending**, not a finding. The real observation is three interior runs
  of three consecutive candidate slots: **E07–E09, E15–E17, E23–E25**. Observations for the
  rhythm pass, **not defects**: E15–E17 is the civic disturbance into the comparative reports
  into the call to Baz, deliberately dense.
- **(c) Kind mix: partial.** Only the four carded windows carry kind tags. Tagging the other
  44 is cheap and needs no causal decision — it classifies *what* changes, not *why* — so it
  is the one unblocked input.

**Not computable, and deliberately left so:** **(a) distinct causal changes** requires the
boundary adjudication now in progress, and arithmetic on slots is what the cards document
explicitly warns against; **(b) events with physical Resonance** is gated by **author ruling
D5**, so counting them would presume rulings not yet made.

## 3. The measurements survive the held order question

Pass 1 cautions *"plot a timeline only after the two unresolved order exceptions are
decided."* Recomputed under **both** numeric order and the file order ruling D7 describes
(E37 before E36, E44 before E43), all three measurements are **identical**.

**So the rhythm pass (item 4) can use them today.** What still needs D7 is any measure of
**prose position or density along the body**, which is what the caution is actually about.

## 4. The four windows are not advanced, and that is correct

Cards Pass 1 left one E40 candidate, two E45 candidates, and six shells needing decisions.
Every one turns on a source reading not yet done or a ruling explicitly held. **Advancing
them by editorial judgement would be inventing the answer** — the failure §4 exists to
prevent.

**One resolvable test is available now and needs neither source nor ruling:** `B1-45B`
against **E48**. Both are commitments to continued inquiry, and the census already flags E48
as *"separate continued inquiry only if an independently new commitment follows."* A
side-by-side read of the two v4.1b beats settles whether that is one commitment or two.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138. Measurements are
reproducible by reparsing census Pass 1 and recomputing under both orders.

END OF ENTRY 81

===============================================================

===============================================================

# 82. B01 census Pass 3 — the E45/E48 merge test, and it removes a candidate — 2026-09-25

`CLAUDE.md` §9 item 3, continuing §81. Proposal at
`proposals/B01_EVENT_CENSUS_PASS3_45B_E48_MERGE_TEST_AND_KIND_TAGS_2026-09-25.md`. **Nothing
promoted, created or counted as settled; no beat, episode function, supplement or the locked
order touched; no cause assigned; no EBCI.**

## 1. The one test that needed neither source recovery nor a held ruling

§81 identified `B1-45B` against `E48` as resolvable by reading the two v4.1b beats side by
side. It is.

**E45's structural aftermath is a decision.** The trio argues with three named positions —
Baz on what they are justified in saying, Seraphine on who gets abandoned when responsibility
becomes everywhere, Lucien on when refusing to extrapolate becomes its own error — and
*"they agree to widen inquiry, not certainty."*

**E48 does not re-decide it.** It has *"Baz argues investigation must widen"* and *"trio
chooses to continue,"* with *"global extent remains unconfirmed"* — **the same posture, not
an escalation.**

**`E45` keeps both candidates** — `B1-45A` and `B1-45B` remain two E45 candidates, `45B`
conditional as cards Pass 1 left it. What the test classifies is **E48's continued-inquiry
*wording*** as a **tier-D receipt of `B1-45B`**, not a second inquiry decision. **E48 keeps
its own candidate**, the quiet predicted pulse, *"close enough to expectation to falsify
'random'"* — a separate matter.

**A receipt lets a claim be tested; it is not evidence the claim is true.** **E48 does not
show the widened inquiry was acted on** — no destination, receiver, report or accepted cost
appears in its beats. It shows the E45 posture is still the trio's posture at the book's end.
**E48 is not a payoff of `B1-45B`**, and whether that obligation is ever carried is open —
part of what keeps `45B` conditional.

**The finding stays reversible.** It rests on E48 giving Baz an *argument* rather than the
trio a *new decision*. If a revision has E48 settle something E45 left open — a destination,
a receiver, an accepted cost — the test re-runs.

## 2. Candidate counts are unchanged — corrected

Cards Pass 1's net stands: **one E40 gathering candidate and two E45 candidates.** This test
changes **no candidate count**; it settles a classification one step away from the count.

**Corrected 2026-09-25, same day.** This entry and Pass 3 §1 first said the E45 pair became
*"one candidate plus one receipt"* and that the pass *"removes a candidate."* Both were
wrong, in two distinct ways: they **demoted `B1-45B`**, which stays as a conditional
candidate, and they **attached the receipt label to the wrong object** — the receipt is
**E48's wording**, not `B1-45B`. A third overreach rode along: describing the receipt as
showing the commitment *"survived"* the final event implies E48 evidences the inquiry being
acted on, which its beats do not support.

The pattern is familiar enough to name: **an argument that a document is admirably
subtracting rather than inflating is itself a pressure toward a tidy conclusion.** The
correction is recorded, not swept.

## 3. Kind tags across all 48 slots close measurement (c)

§81 found (c) computable only for the carded windows and noted that tagging *"classifies what
changes, not why"* — no causal decision, no held ruling. Done, as a proposal, so the author
decides by seeing the result rather than authorizing blind.

Among the **28** candidate slots: **evidential 10, relational 4, civic 4, institutional 3,
physical 3, perceptual 2, decisional 1, care 1.**

**3 of 28 candidate slots carry `physical` as their *primary* tag** — E33, E45, E48.

**Read narrowly.** Each slot takes **one primary tag**, for what principally changes there.
The figure is **not** a count of Resonance occurrences, **not** a count of episodes
containing something physical, and **not** an adjudicated event total — a `civic` or
`evidential` slot may well contain a physical manifestation, E15 being the obvious case.
What it supports is only that **the primary changes across B1's candidate slots are mostly
not physical**, consistent with the Book 1 public/local/no-combat/low-amplitude constraint.
Measurement (b) still cannot be answered while **D5** holds.

`evidential` at 10 of 28 is the largest kind, concentrated at E16, E20, E25, E27, E35, E39,
E47 — worth checking in item 4 for whether they escalate or restate, which Pass 1 already
asks of the E25/E27 and E39/E47 pairs.

**A counting note, recorded because it nearly shipped wrong.** The mix table was first
hand-tallied and was wrong by one on `evidential` — 10/9 against the true 11/10. It is now
a machine recount of the tag column. Small, but this ledger has twice before recorded a
figure measured the convenient way (§74 §4, §78 §4), and the pattern is the point.

## 4. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

Unchanged: E23, E38 and E40 need source work before another editorial pass adds value;
`B1-45A`'s causal contract stays gated by **D5**; measurement (a) stays uncomputed.

END OF ENTRY 82

===============================================================

===============================================================

# 83. B01 whole-book rhythm pass — the book needs nothing added — 2026-09-25

`CLAUDE.md` §9 item 4. Report at `reports/B01_WHOLE_BOOK_RHYTHM_PASS_2026-09-25.md`.
**No beat, episode function, supplement, order or classification changed; no event promoted
or counted; no cause assigned; no EBCI.**

**A reconciliation, not a fresh ECG.** Three rhythm reports already existed, all dated
2026-09-21, analysing **v4** — they predate v4.1b, ruling D1–D7 and the census. Re-running
them would duplicate good work.

## 1. The two numbering spaces, and the map

**The 09-21 reports are written in v3 episode numbers; the census, the cards and v4.1b are
not.** The deep matrix's middle-density warning about *"E16–E22"* is **v4.1b E20, E22, E23,
E24, E25, E27, E29**; its austere sequence *"E33→E36"* is **v4.1b E45→E48**.

**Applying an ECG finding to the same-numbered v4.1b slot gets the wrong episode every time
after E02**, and no document said so while both live in the same directory.

The map is recoverable from v4.1b's own headers (`## 45. THE REBOUND / v3 E33 | source E38`).
Extracted and **machine-verified: 36 pairs, zero mismatches**, with the 12 unmapped slots
exactly the Life/Reward layer. **Cite the v3 number when quoting a 09-21 report** — the
cheapest defect prevention available.

## 2. v4.1b implemented the ECG's headline recommendation, guardrail and all

Deep matrix Pass 2 called **positive anticipation** the book's *"missing category"* and
proposed seeding a Velvet Vein event, paying it later, under a *"critical guardrail: do not
automatically attack or destroy the event."*

v4.1b has the whole chain: **E06** seeds the room, **E28 (LR08)** *"create positive
anticipation"*, **E31 (LR09)** *"actually pay the promised pleasant night"* — and E31 carries
**"HARD GUARDRAIL — Do not attack the event."** The guardrail survived into the architecture
nearly verbatim.

Also closed: the three-layer ECG's **47 → 48** count correction propagated. And the
middle-density run it feared **no longer exists as a run** — LR06, LR07 and LR08 interleave
among those seven episodes.

## 3. What the census data adds

- **All 12 Life/Reward episodes are census slot-L.** Not one is candidate-bearing; the census
  reached that independently of the layer's design.
- **Eight *causal-spine* episodes are also slot-L** — E06, E10, E19, E22, E32, E38, E41,
  E46 — three marked PROTECTED or ABSOLUTELY PROTECTED. **So 20 of 48 episodes carry
  lived/negative-space work and only 12 are the LR layer.** Any compression treating "the LR
  episodes" as the book's slack would cut the wrong twelve.
- **Every dense run is immediately relieved.** The three runs of three consecutive candidate
  slots — E07–E09, E15–E17, E23–E25 — are each followed straight away by lived space (E10,
  LR05, LR07). **The book never sustains a fourth.** With the longest slot-L run at 2, the
  alternation is tight in both directions: no dense stretch, no dead stretch.
- **The austere sequence is design, not drift.** Pass 2's longest no-candidate run, E41–E44,
  is *after the breaking* → exhaustion humour → grounding fails → *something strange that
  doesn't hurt*, landing on the Rebound — exactly what the three-layer ECG described in v3
  numbering, verifiable in the current architecture.

## 4. Finding

**On its own terms, the book's rhythm needs no addition** — a book-internal judgment,
provisional on the saga and Veil trilogy passes (qualified in §84). Every ECG-identified gap
v4.1b could close is closed; reward, wonder, anticipation, humour and recovery all have dedicated slots with
guardrails. The one place worth a *reading* pass is the **evidential cluster** at E16, E20,
E25, E27, E35, E39, E47 — where escalation is most likely to flatten into restatement, and
where Pass 1's split/merge tests already point.

## 5. Deliberately not measured

**Romance, character load and location recurrence** need a per-episode presence-and-place
table that does not exist — the same gap §80 found in the cast registry, where 26 of 57 rows
have an empty `range`. Deep matrix Pass 2 reports these for v4 and those findings stand; this
pass does not restate them as if re-verified. **Threat** is not measured because it depends on
causal questions **D5** holds. **No prose-position measure** is attempted, because that needs
the order decision **D7** holds; everything above is order-invariant.

## 6. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138. The v3 map is
machine-verified against the bible; the rest is reproducible from census Pass 1 and Pass 3's
tag table.

END OF ENTRY 83

===============================================================

===============================================================

# 84. Work queue reordered: saga first, then Veil, then B01 EBCI — 2026-09-25

Author direction, verbatim: *"I think our next tasks are going to be saga wide milestones,
rhythm, balancing, etc then we will work on episodes for B2 and B3 to complete the trilogy,
then we will work on EBCI for B1 and develop packets for sudowrite etc."* Forwarded with it:
a ChatGPT review proposing the same order in more detail. **A work-order decision, not a
canon one**, so it is recorded in `CLAUDE.md` §9 and here rather than in `decisions/`.

## 1. The new order

**Saga structural pass (active) → lock saga architecture → B02/B03 episode architecture →
Veil trilogy audit → B01 EBCI (author gate) → Sudowrite packet.** Hierarchy: saga → trilogy
→ book → episode → EBCI → prose.

**Provenance of the steps.** Saga pass, B02/B03, B01 EBCI and Sudowrite are **the author's
words**. *Lock saga architecture* (step 2), *Veil trilogy audit* (step 4), *Sudowrite packet
as a smaller derived interface, never raw EBCI*, and *no `ebci/` directory yet* come from the
**forwarded review**; adopted here as sound process, and **the author may strike any of
them**.

## 2. What it changes

- **B02/B03 episode architecture is now queued**, replacing §9's former *"no B02–B09 episode
  expansion yet"* **for those two books only**. B04–B09 remain unexpanded. **Architecture is
  not EBCI**: the B01 hold stands and still gates only B01.
- **The B01 rhythm pass (§83) is qualified as book-internal.** The review's point is correct
  and the pass should have said it: a book can pace well on its own and still repeat the
  saga's escalation shape. *"Needs nothing added"* now reads *"needs nothing added for its
  own sake."* Qualified in the report, in §83 and in `CLAUDE.md` §8.
- **The saga pass starts as a reconciliation.** Event tiers and the unslotted pool, the
  M01–M36 review and adjudication, the anchor register, the place/antagonist transition map,
  the carry-forward checks and the B07/B08/Loom ledgers already exist. `CLAUDE.md` §9's
  reading map now lists them. Same lesson as §74 §4 and §83: read before generating.

## 3. Not adopted — the manifest set

The review also proposes a `manifests/` directory of eleven navigation files, including a
`CURRENT_STATE.md`. **Not built**, pending the author's choice; the reasoning is put to him
separately. In brief: `CURRENT_STATE.md` would duplicate `CLAUDE.md` §8, and this repository's
most expensive recurring failure has been **navigation documents going stale** — §8's queue
fell 180 commits behind, and the v3/v4.1b numbering split went unstated for four days.

## 4. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

END OF ENTRY 84

===============================================================

===============================================================

# 85. Saga structural pass 1 — resolution, the nine-book map, and B08 — 2026-09-25

`CLAUDE.md` §9 step 1. Proposal at
`proposals/SAGA_STRUCTURAL_PASS1_RESOLUTION_MAP_AND_B08_2026-09-25.md`. **No milestone, grid
value, book context, act overlay or episode changed; no event placed, promoted or retired;
no author question answered; no EBCI.**

Also recorded: **navigation manifests are deferred** until Veil EBCI is built, possibly later
— author, 2026-09-25, answering §84 §3. `CLAUDE.md` §9 says so.

## 1. The nine books do not exist at the same resolution

B01 has **14** episode/beat-level documents; B02 and B03 have **3** each; **B04–B09 have
none** — three to five milestone rows per book plus pool candidates. And the B04–B09 book
contexts are `_basis: derived` *"from grids/milestones_payoffs.csv"*, so they **cannot
corroborate the grid** — using them would count the same 36 rows twice.

**So any nine-book density comparison would find Veil dense and Neon/Loom sparse purely
because more of Veil has been written down.** Same class of error as §83's v3/v4.1b split.
The saga pass therefore works at the **one resolution all nine share — milestone rows plus
pool candidates**. Veil's episode detail waits for the trilogy audit, where it can be
compared with itself.

## 2. What the shared-resolution map shows

- **The three tier-A anchors sit in each trilogy's closing book** — B03 Warehouse, B06
  Santa Fe, B09 Mending — and **both trilogy handoffs are in `EP` positions.** The
  three-by-three skeleton is sound.
- **Promises are end-weighted within books:** five of nine — B03, B05, B06, B08, B09 — carry
  no Act 1 milestone. Shape, not defect; the grid lists promises, not plot.
- **Thread pressure is unusable as a rhythm signal after B04 Act 3.** Of the seventeen rows
  M16–M32, sixteen end at 5; eleven score 5→5 consecutively. The 09-23 review already said
  so. **A first draft of this finding said "seventeen consecutive" by conflating the span
  with the run; corrected by script before commit.** Fourth figure this session caught
  that way, and the check is now habit rather than luck.

## 3. B08 is squeezed, not empty

Eight pool candidates attach to B08. **Four collide with B07** (011, 012, 015, 016, flagged
duplicate or alternate), **one with B09** (020, the chamber), **one is warned against
repeating B07** (019), and **one is a proposal with no recovered incident** (018).

**Only POOL-017 — Choirless coercive quieting of a community — is B08-native, supported by the
author-pasted December macro, and free of any duplicate flag.** It is also the only one that
cannot steal B09's ending, since it concerns coercion rather than access to Honey Island.

**This reframes the instruction.** *"Strengthen B07–B08 without stealing B09's ending"* is at
least as much **disentangling B07 from B08** as finding new B08 material. B07 is the richest
book in the pool — eight candidates — partly because it stands on B08's ground. Proposed:
adjudicate the four collisions first (the pool's own step 3), and treat POOL-017 as the
leading B08 turn candidate **for the author's consideration only**.

## 4. Milestone decision #1 is narrower than the packet put it

The packet asked whether Tahl is first named in the **B3 epilogue or B4**, crediting B4 to *"an
earlier same-day explicit ruling"* and assigning Claude the source check. Done.

**The only verbatim author utterance** (`VEIL_STRUCTURE_2026-09-19.md`): *"Tahl isn't named
until Book 3 … his remorse in B4 is his protagonist arc beginning."* **The B03-epilogue rule
has no quoted source** — it is a paraphrase in the handoff's list, already recorded in §26.6
as a lock living only in a proposal.

They do not conflict. **B4 rests on reading "remorse in B4" as "named in B4"**; no author
sentence names B4 as the point of first naming. **The live question is "the B3 epilogue, or
earlier in Book 3?"** — B4 stays open only if the author meant *"until"* as a bare floor.

## 5. What the saga pass can judge now

Anchors, pool, milestone architecture and trilogy transitions — **yes**, pending the five
decisions. Causal dependencies, character and place recurrence, antagonist pressure and
Mechanica escalation — **partly**. Rhythm and density — **only coarsely**. Thread pressure,
and Life/Reward, wonder, fun, romance, heat and humour — **not yet**: they need rescoring or
episode-grain data that only B01 has. The pass says at which later step each becomes
judgeable rather than faking a nine-book reading from B01.

## 6. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

**Next, unblocked:** adjudicate the four B07/B08 pool collisions, and the packet's remaining
Claude-checkable items. **Blocked on the author:** the five milestone decisions, open since
2026-09-23.

END OF ENTRY 85

===============================================================

===============================================================

# 86. The five milestone-gate decisions answered — 2026-09-26

Ruling at `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`. **Three ruled, two
leans.** No grid row, episode, rule file or EBCI status changed.

The author, verbatim: *"1. B3 epilogue · 2. Tahl posted the coordinates of the event Baz was
investigating. Perhaps causing more people to go there and it taking too long for Baz to
evacuate the location. · 3. Soft lean toward yes as events · 4. i lean actual opening · 5. We
originally discussed LT being the final thing in the epilogue where Seraphine reaches out to
the survivors."*

## 1. What is ruled

- **Tahl is named in the B3 epilogue.** This closes the question §85 narrowed. It also gives
  one of §26.6's *"four locks living only in proposals"* its first author source: the
  handoff's unquoted paraphrase now has the author's words behind it.
- **Tahl posted the coordinates of the event Baz was investigating.** He exposed a location
  and made it public. That is the packet's option A, and it rules out option B: **Tahl's post
  does not cause the Rupture.** The crowd-and-slowed-evacuation chain carries the author's
  **"perhaps"** and is **not ruled**. It is the leading hypothesis the Warehouse causal card
  must test. Nothing says Tahl knew Baz was there, and *"Baz does not work directly with
  Tahl"* stands.
- **LT is the final beat of the Book 9 epilogue: Seraphine reaching out to the survivors.**

## 2. The LT answer took neither offered option, and it matches Mechanica

The packet offered two options: **A**, LT as a distinct public channel identity, and **B**, an
MT rebrand. The answer is neither. **`Mechanica-v4.md` §39 already says what the author
recalled:** *"LT … is perceivable only by ascendants … Civilians perceive only calm or
clarity."* Seraphine is one of the trio who ascend. So the ruling and the rule file agree.

**The disagreement is with M35**: *"MT is renamed LT; Kade's stewardship completes,"* noted as
*"A rename, not a channel conversion"* from Notion B9 E20. **That wording is superseded on
LT's identity.** LT is not MT renamed and it is not Kade's. What becomes of MT and of Kade's
stewardship after the Mending is a **separate, open question**, and so is what survivors
actually perceive. Mechanica says *calm or clarity*, not a readable message.

**Worth recording as a pattern:** the packet's options were built from the grid and Notion,
and neither carried the Mechanica constraint. The rule file held the answer all along. When
an option set is derived from one source layer, it can omit the reading another layer already
fixes.

## 3. Leans are recorded so they are not promoted

**Lean 3** keeps the Riot of Light, first public meta and NOLA Colorstorm **as events** in the
search. It does **not** revive the wording claims the review flagged: *"first global"* (M19)
and *"first public"* (M17) still need evidence.

**Lean 4** favours an **objective** storm opening at B08's end. The packet's minimum scene card
for a literal opening is still owed, and POOL-020's duplicate risk with B9 is unresolved.

## 4. Propagation

`CLAUDE.md` §4.1: the Book 9 epilogue row now records LT's ruled identity. The §26.6 row notes
that Tahl's naming has an author source. §8 records that the gate is answered and what comes
next. Saga pass 1 §6 is annotated as answered. `decisions/README.md` indexes the ruling.
**The live grid is untouched.** M35 keeps its wording until a proposed copy is reviewed.

**Next, per the packet's release criterion:** B3, B6 and B8 event cards, then a proposed grid
copy with original and revised wording side by side.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

END OF ENTRY 86

===============================================================

===============================================================

# 87. MT continues after the Mending; LT access conflicts with Mechanica §39 — 2026-09-26

Addendum to `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`. The author, verbatim:
*"MT after mending = MendedThread, MortalThreads, etc same initials, but embracing a new role
for it and for Kade"* and *"I think the protagonist survivors are able to use LT much like
Tahl and VT."*

## 1. MT survives, and M35 is now superseded twice over

**MT continues past the Mending** under a new MT-initialled name, with a new role for the
channel and for Kade. This answers the half of §27.3 that asked whether *"MT→LT completes"* in
the Book 9 epilogue: **it does not, because MT does not become LT.** *MendedThread* and
*MortalThreads* are examples, **not a choice**, and the new role is not specified.

M35 read *"MT is renamed LT; Kade's stewardship completes."* That is now superseded on LT's
identity (§86) and on MT's fate (here).

## 2. My §86 said the LT answer matched Mechanica. With the addendum, it does not

§86 recorded answer 5 as agreeing with `Mechanica-v4.md` §39: *"LT … is perceivable only by
ascendants … civilians perceive only calm or clarity."* **That was true of answer 5 on its
own.** The addendum says the **non-ascended** protagonist survivors can **use** LT, the way
Tahl used VT. **The two statements now conflict.** The agreement holds only for ordinary
civilians.

**Not resolved.** Mechanica is authoritative until its line-by-line review, and §4 of the
working agreement forbids picking a winner. The ruling puts three readings to the author:
**amend §39** so named survivors have access, as VT admits Tahl; **reception, not access**,
where §39 stands and survivors experience LT only through an ascendant reaching them; or
**widen "ascendant,"** which touches the trio question in §27.2. Reception fits the author's
words least well, since *"use LT much like Tahl and VT"* implies the survivor acts.

**The author's analogy carries structure worth keeping visible.** VT is the channel between
Silence and Hope that a mortal, Tahl, reached although it was not built for him. Read the same
way, LT is the channel the ascended trio occupy that the surviving protagonists can reach. The
symmetry is the author's. Whether §39 is amended to carry it is his call.

## 3. The pattern from §86, again, one day later

§86 noted that the packet's LT options omitted the Mechanica reading because they came from a
single source layer. **The same thing happened in reverse here:** I read the answer through
Mechanica and called it a match, and the author's next message showed that §39 is itself one
layer of the intent. **A match with the rule file is evidence, not confirmation**, while the
rule file is still awaiting its own review.

## 4. Propagation

`CLAUDE.md` §4.1: the Book 9 epilogue row records MT's continuation and supersedes M35. A new
row carries the §39 tension and its three readings. **Unchanged:** the grid, `Mechanica-v4.md`,
`MT_RULES.md` (still held on the infrastructure question), and the closed-vs-spaced naming
question. *MendedThread* is written closed in the author's message, which is evidence, not a
ruling.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138.

END OF ENTRY 87

===============================================================

===============================================================

# 88. B03 Warehouse causal event card, Pass 1 — 2026-09-26

Proposal at `proposals/B03_WAREHOUSE_CAUSAL_EVENT_CARD_PASS1_2026-09-26.md`. The first of the
three event cards the milestone packet places between the author's answers and a proposed grid
copy. **No episode, beat, grid row, rule or EBCI status changed; no Resonance mechanism
supplied.**

## 1. The chain, with every link's status

Fifteen links, from Baz investigating to the lasting scar. **Five are ruled outright; a sixth
follows from a ruling; two are the author's own hypotheses** (the crowd drawn by the post, and
the slowed evacuation). The physical core — Rupture, partial collapse, Baz freeing a child and
being crushed — is **recovered** from the November B3 bible. It is **not mechanized**, and D5
keeps it that way.

## 2. The author's answer fills the gap the leading reconstruction left

The 09-19 recovery's best candidate was **containment plus evidence retrieval**: authorities
seal rather than evacuate, and Technarc agents obstruct exit. Its stated weakness: *"exact delay
not recovered."* **It explained why people were not evacuated. It did not explain why so many
were there.**

**The author's hypothesis answers exactly that.** The post draws people in; the perimeter and
retrieval slow their exit; the Rupture outruns Han Wei's model. **Compatible and additive, not
competing**, and together they keep the 09-19 constraint that *"no individual needs to murder
him."* **Compatible is not decided**; the card adopts none of the three mechanisms.

The recovery's older idea, that Tahl's publication worked **through institutions**, is kept as
an alternative. The author's stated consequence runs **through the public**. The recovery's best
line survives and is sharper for it: *"MT was right about the danger, but being right changed
the board."*

## 3. The two rulings interlock

**The main structural finding.** The B03 reconciliation map has one Tahl publication, in the
epilogue, **after** the Warehouse. **Ruling #2 implies an earlier post**: to draw people to the
site, the coordinates must go up **before** the Rupture. **Ruling #1 makes that post anonymous**
when it appears. So an anonymous Act III post becomes the thing the epilogue reveals Tahl wrote,
and his B4 remorse follows from it. **Reveal and remorse become causally tight rather than
adjacent**, and that follows from the author's two answers, not from invention.

The B03 map therefore needs an **Act III posting beat**. How the reader meets it — on the page,
only through its effect, or only in the epilogue — is the author's staging choice.

## 4. Kept off the card, and left open

**Mechanism C** — Dominion extracting Lucien during the crisis — stays off. Its actors are
recovered but its Warehouse link is not, and it may conflict with the cast learning of Baz's
death in B04.

Four questions for the author, none blocking the B6 and B8 cards: how the Act III post is
staged; **whether Tahl knew Baz was there** (the ruling says the post was of *"the event Baz was
investigating,"* which need not mean Tahl knew — and whether he knew is what his remorse is
about); which antagonist intervenes; and whether containment and retrieval stand alongside the
crowd.

## 5. Verification

Canon scope **0**; self-tests **144**; source verifier **PASS** at 138. A first draft said "six
links are ruled"; five are ruled outright and link 3 follows from one. Corrected before commit.

END OF ENTRY 88

===============================================================

# 89. Mechanica §39 amended for Kade; B09 epilogue scene; Warehouse answers — 2026-09-26

**Status:** records two author rulings and the rule edits one of them instructs. No episode,
grid row or EBCI status changes.

## 1. What the author said

> Amend 39 to allow at least Kade access. There should be an epilogue scene worked out with
> Lacuna and Kade talking while looking at the night sky and closing with a prompt from LT
> reaching out. (Mobius with B1 prologue Conversation in the stars)

and, answering the Warehouse card's §6 (§88):

> 1. I am open to it being a visible supplemental text, or only seen via effect. I think the
>    aftermath is visible in the epilogue. Tahl seeing reports about unexpected bystanders
>    hampering efforts and a first responder perishing, or etc.
> 2. No, Tahl may well not even know Baz's name until much later.
> 3. Which ever fits the saga better, perhaps Dominion was expected to be present, but Technarc
>    were not…
> 4. Whatever serves the saga best

## 2. LT access — §87's conflict resolved for Kade

The author chose **reading 1 of §87 (amend §39)**. `decisions/LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md`.

- **`rules/Mechanica-v4.md` §39:** *"Is perceivable only by ascendants"* → *"Is accessible to
  ascendants and, by named exception, to Kade,"* with a dated note quoting the author and
  keeping the old wording.
- **Consequential edits** so the substrate does not contradict itself: Mechanica §33
  (*"Ascendant-only perception"*), `rules/Channels/CHANNELS_OVERVIEW.md` §5 and §6,
  `rules/Channels/LT_RULES_POST_MENDING.md` §2. Each now points at §39 and adds nothing.
- **Not changed:** §37 (*"MT cannot … access VT or LT"*). Kade's access is personal, not via MT.
- **Reading 3 (widen "ascendant") was never available.** `KadeID.md` says Kade *"does not
  ascend."* Recorded so a later pass does not re-propose it.
- **Open:** "at least" sets a floor, so other survivors' access is still open. It is also open
  what access consists of, and whether an LT **"prompt"** fits `LT_RULES_POST_MENDING.md`'s
  *"never presents as a voice, command, or instruction"* and *"LT never interacts directly with
  MT."* A prompt felt as presence fits; one shown on a screen does not.

## 3. The B09 epilogue scene

**Ruled:** Lacuna and Kade talk under the night sky; the scene closes on LT reaching out; it is a
Möbius with the B01 prologue. It fits answer 5 (§86) if the LT prompt is Seraphine's reach
received through Kade's access. That reading is natural but not stated, and it is not recorded as
ruled. The author wrote *"Conversation in the stars"*. That is treated as a paraphrase, and the
prologue's title, *The Conversation in the Sky*, is unchanged. The ruling offers three mirror
readings against the prologue's Möbius seed (*"distance, constraint and incomplete
communication"*), each marked as a reading. **No scene text is written.**

## 4. Warehouse answers

`decisions/B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md`; card §1 and §6 updated.

- **RULED: Tahl did not know Baz was there.** His remorse is for a consequence he did not
  foresee. Hedged: he may learn Baz's name much later than the cast learns of the death (B04).
- **Post staging narrowed** to a visible supplemental text or effect-only. Learning of it only
  in the epilogue is no longer among the options.
- **Epilogue aftermath (hedged):** Tahl reads reports of unexpected bystanders hampering
  efforts. This gives links 4 and 9 an on-page form without ruling them.
  **"A first responder perishing" is recorded two ways:** Baz reported unnamed (he is an
  investigator by role but acts as a rescuer), or a second death no source contains. Not chosen.
- **Answers 3–4 were delegated.** Working assumption, marked PROPOSAL and overridable: **both**
  mechanisms alongside the crowd. **Dominion is expected** (the perimeter, mechanism A).
  **Technarc is not expected** (the retrieval, mechanism B) and is the link-7 intervention. Its
  unsanctioned presence gives a concealment motive that feeds the 09-23 B05 function. C stays
  off. **"Expected by whom"** is open: the public, Baz or Tahl.

## 5. Delegation is recorded as delegation

The author twice asked for "whatever fits the saga." §4 of the working agreement still applies:
the answer is a **recommendation adopted as a working assumption**, with its reasons written
down, and it reverts cleanly if the author overrides it. It is not a ruling, and no other
document depends on it yet.

## 6. Verification

Canon scope **0** (the §39 edit is in canon scope); self-tests **144**; source verifier **PASS**
at 138. All-scope: 112 `CHK_SID_FORMAT`, unchanged, and 356 notices. The one new *"B1"* is
in the author's verbatim quote and is kept as evidence.

END OF ENTRY 89

===============================================================

# 90. Correction to §89: the §39 amendment missed Kade's Tier-1 card — 2026-09-26

**What was wrong.** §89 amended Mechanica §39 and three rule lines so that Kade has LT access,
and said the substrate no longer contradicted itself. It still did. `canon/characters/KadeEBCI.md`
said, under LT: *"Not accessible"*; *"Receives prismatic handshake only in epilogue (no agency)."*
The search for the old wording covered `rules/` and the word "ascendant"; the card says neither.
Found while building the B6 card, on reading Tahl's and Kade's EBCI channel blocks.

**What replaced it.** KadeEBCI's LT block now says Kade has access by named exception, cites
the ruling, and keeps the old wording. The **handshake line is kept**: it is the LT reach that
closes the ruled epilogue scene. *"(no agency)"* is retained until the author rules what access
consists of. The ruling's table of follow-on edits now lists this edit and says it was added in
a follow-up commit.

**What the card adds to the ruling.** Kade's card already had an **epilogue handshake**. The
Lacuna–Kade scene gives that handshake a setting and a witness. It is not a new invention.
`LacunaEBCI.md` gives Lacuna *"not accessible; post-Mending clarity hum only"* for LT. That is
unchanged, and it partly answers the ruling's question of what Lacuna perceives in the scene.
`TahlEBCI.md` (*"Inaccessible; Echo may interface lightly post-death only"*) is unchanged.

**Lesson.** When a rule is amended, search the substrate for the concept (here, per-character LT
blocks), not only for the old sentence.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 90

===============================================================

# 91. B6 Santa Fe and B8 storm-wall event cards, Pass 1 — 2026-09-26

**Status:** two PROPOSAL cards. No episode, grid row, rule or EBCI status changes. With the B3
card (§88), this completes the three cards the milestone packet requires before a proposed grid
copy. The author's answers to the questions below gate that copy.

## 1. B6 Santa Fe (`proposals/B06_SANTA_FE_CAUSAL_EVENT_CARD_PASS1_2026-09-26.md`)

A 17-link chain drawn from the author-pasted Neon master (both pastes agree) and the Tier-1
Tahl cards. Findings:

- **Tahl's death is prolonged VT contact at the rupture, per his own cards.** `TahlEBCI.md`:
  *"VT contact occurs late and is fatal"*; *"cannot survive prolonged VT exposure"*; VT access
  is *"triggered by cumulative pressure + proximity"*; `TahlID.md`: *"dies at Santa Fe rupture."*
  The milestone overlay had left *"exact injury and VT link"* open. The link is not open on the
  cards; only a material injury is. Retiring the NOLA transit-platform scene also removes a
  duplicate of Baz's crush death.
- **Why Tahl is at Santa Fe is unsourced.** READING: it inverts the Warehouse, a consequence at
  a distance in B03 and in person in B06.
- **The Santa Fe threat runs six steps over two books.** B5's close (*"collapse imminent"*) and
  B6 Act I's close (*"begins tearing"*) need distinct observable states. A mapping onto
  Mechanica §34's ladder is offered, not adopted.
- **Tier-1 conflict found:** `TahlEBCI.md` limits Echo appearances to *"penultimate chapter only
  (Book 9)"* with *"no agency, only guidance"*. Grid M22 (B6), M27 (B7, *"an agent again"*) and
  M36 (B9 EP) contradict it. The milestone review had not cited the card. Two readings recorded.
- **The Warehouse ruling's "much later" has a deadline:** Tahl dies in B6 Act II.
- M20's A3 → A2 correction: both author pastes agree on A2. Put to the author to confirm.

## 2. B8 storm wall (`proposals/B08_STORM_WALL_OPENING_EVENT_CARD_PASS1_2026-09-26.md`)

The packet's minimum scene card for a literal opening, following the author's 09-26 lean.
Findings:

- **Mechanica §31 constrains it.** *"Crowd density"* escalates weather, so the siege feeds the
  W4 storm. *"Sudden calm is suspicious,"* so an opening is by rule suspect. That favours a
  bounded, costly, short opening.
- **READING:** the opening arrives as Kade reaches his *"misinterpretation threshold"* (B8 A3.4),
  so Brightbreak could credit it to him. That would give POOL-018 its missing concrete incident
  and give B9's Brightbreak zenith a cause. **Not proposed:** that Kade causes it.
- **B8 A3 and B9 A1–A2 restage three beats:** the convoy splits three times, the siege forms
  twice, and the approach to the chamber happens twice. B9 opens with a *"retreat from NOLA"*
  after B8 has ended at the swamp. Three readings are recorded: seen-not-entered,
  forward-team-through, and move-the-opening. The last goes against the author's lean.
- The Dec 7 **assistant** draft had the wall *forming* at the B8 close. The Dec 8 author paste
  has it *opening*, and the author paste governs.

## 3. Found in passing: the Loom master's B9 epilogue

The same author-pasted file (~ll. 707–712; again at ~1438) carries a **B9 epilogue, "three days after"**: a
holochat check-in; Kade writes the first post-Mending MT message; Lacuna presses *"post/enter"*;
*"they look up at sky — stars 'twinkling in conversation'"*; *"Kade receives LT handshake request
(Tahl's triangle symbol)."* This bears directly on the 09-26 epilogue ruling: the timeskip, a
device-borne prompt, and whose reach it is (Tahl's symbol against answer 5's Seraphine). It is
**not analysed here.** It goes into the export search the author requested next, which records
it against the rulings.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 91

===============================================================

# 92. The B09 epilogue's source conversations recovered — 2026-09-26

**Status:** recovery. No ruling, substrate or episode change.
`recovery/B09_EPILOGUE_KADE_LACUNA_SOURCE_RECOVERY_2026-09-26.md`.

**Asked:** the author: *"check exports for previous conversations about B9 aftermath with Kade
and Lacuna, I know there was a lengthy discussion about the aftermath in general and that
conversation specifically."*

**Found:**

- **The specific conversation:** `2025-11-27__Narrative_Structure__69286516.md`, 2025-11-29/30.
  The author designed the epilogue turn by turn: Lacuna presses post; the stars *"twinkling like
  they're talking"*; a *"message request prompt"* showing only **Tahl's triangle**; a
  *"conversation in the stars"* breadcrumb for the Möbius. He locked it with *"Lock it and
  proceed"* (~88183) and accepted a days-after skeleton on 11-30 (~113672).
- **His recollection:** `2025-12-07__Beat_bible_recovery_process__69350113.md` l. 9755 matches
  the design point for point, and says *"we settled on the couple days later version."*
- **The general aftermath:** `2025-12-01__Worldbuilding__692dc2fb.md` ~96782–109420, the
  assistant-built POST-MENDING CANON v1 and PART V. The author steered: not utopian, *"connected
  via emotion,"* and the epilogue *"already beat locked."*
- **Earlier:** 11-15, the first epilogue proposal (LT as a notification, *"someone out there wants
  to talk"*) and the only author statement on Kade's post-Mending role (an **"Accord"**,
  hedged). 11-16: *"the stars are talking"* **is** Silence and Hope on VT, the prologue half of
  the Möbius.

**Corrections to the record:**

1. The 09-26 epilogue ruling **restates a locked 2025 design**; it is not a new invention.
2. `EXPORTED_CHAT_FORENSIC_PASS1.md` §6 and the 09-15 B9 endgame checkpoint say the epilogue's
   choreography *"remain[s] unrecovered."* **It is recovered** (Narrative Structure
   ~87561–88184, ~113472–113760). Those files are not edited; this entry is the correction.
3. **§27 §3's "6–12 months" timeskip came from an assistant-generated Notion page** the author
   answered only with *"Proceed."* Every author statement from 11-30 on says days.

**Three tensions with 09-26, put to the author and not resolved:** (a) the timeskip; (b) who
reaches out, Tahl's triangle (2025) or Seraphine (09-26), which the accepted 11-30 skeleton
reconciles (*"Tahl is the conduit on Kade's side; Seraphine/Lucien/Caro on the other"*); (c) the
prompt appears on **Kade's device** in every 2025 version, against `LT_RULES_POST_MENDING.md` §6.
That conflict is between the author's locked design and an assistant-built rule file.

**Method:** a background search agent located the passages. Every author quotation in the
recovery document was then checked against the `.md` export in this session, as were the
assistant citations it relies on. One agent claim needed a correction: the *"Lock it and
proceed"* turn is at ~88183, not 88181.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 92

===============================================================

# 93. Author answers on B06, B08 and the B09 epilogue; `LT_RULES` §6 exception — 2026-09-26

**Status:** records one author-answer document and the rule edit it instructs.
`decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` quotes the author verbatim and
sorts each answer into ruled, recalled, lean or accepted.

## Ruled

- **Tahl's Echo appears once in an identifiable capacity to the cast.** Other echo moments may
  or may not be his. This answers §91's TahlEBCI-versus-grid conflict in substance.
- **Tahl learns Baz's name from a news report, before he dies**, and learns why Baz mattered
  from the protagonists. This closes the name question left by the Warehouse ruling (§89).
- **Tahl's echo is the LT conduit** that makes LT *"more tangible than VT was."* It reconciles
  the locked 2025 triangle with the 09-26 "Seraphine reaches out" (§92): the trio reach; the echo
  carries it to Kade.
- **Kade's post-Mending role:** Elisabet, Rex and Kade stitch society back together, and Kade
  focuses on those involved with the rebellion. *Accord* or *Concord* for what grows out of it;
  the name is open. This answers the 09-26 addendum's *"new role … for Kade."*

## Accepted, recalled, lean

- **Accepted as intent:** the Santa Fe ladder mapping (§91): B5 close = Ghostwave-class;
  B6 A1 close = Fracture; B6 A2 = Rupture.
- **Accepted:** an exception in `LT_RULES` §6 for the epilogue handshake, enabled by Tahl's
  echo. **Applied.** The general rule stands, and §2, §4 and Mechanica §37 were read against it.
- **Recalled:** Neon pulls at least Tahl, maybe a core group, to the Southwest. The warnings come
  from VT. **Tahl's soul is caught / collected by Silence.** Mechanica §38 means a VT warning
  reaches the public only through a person; Tahl or the Filaments as relay is not chosen.
- **Adopted as working answer:** **Elias claims the B8 opening for Kade**, whether or not Kade
  caused it. The author leaves the cause open. The packet's and KadeID's guardrails would apply
  if it was Kade.
- **Leans:** M20 at the **very end of B06 A2**, with the start of A3 still possible and a
  decision expected during Neon episode mapping. **The packet's "A3 → A2" correction is
  therefore not confirmed.** The epilogue timeskip leans to **a few days**. Mending-site material
  goes in "Act III", the opening "perhaps at the very end of Act II".

## Direction

*"We need to spend a good bit of time developing Loom … it has been spreading thin."* Added to
CLAUDE.md §9 step 1.

## Open, put to the author

1. **Which book's "Act III / end of Act II"?** B09 is the better textual fit, and it would move
   the opening out of B08 (close to the B8 card's reading 3). B08 is the other reading.
   **Nothing is moved until answered.**
2. **Which Echo moment is Tahl's one identifiable appearance?** The B09 penultimate-chapter flare
   is the natural candidate (TahlEBCI; Loom master). The epilogue triangle and M36's farewell
   would then need to be something other than appearances.
3. **"More tangible than VT"** against `LT_RULES`' soft language and §4 (*"cannot transmit
   information"*). This bears on the held Post-Mending era file.
4. **An observation on the name:** *Concord* is already the protagonists' in-world group
   (`LacunaID.md`) and the saga's title.

## Where it was applied

- The B6 and B8 cards (§6 and §4 marked answered).
- The Warehouse and LT/epilogue rulings (dated follow-up notes).
- The decisions index; CLAUDE.md §4.1, §8 and §9.
- **The grid is untouched.** These answers go into the proposed grid copy, which is next.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 93

===============================================================

# 94. Follow-up: the B08 opening stays; factions learn the site only in B09 Act III; the flare is Tahl's one appearance — 2026-09-26

**Status:** records the author's answers to the two questions §93 left open. They are appended
as §4 of `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md`.

**The author:** *"the stone wall opening can be in b8 and it could even be fleeting. I was
thinking the antagonist factions should not know the swamp is the mending site until b9 act iii.
We can't have an entire book of them laying siege on the mending site."* · *"flare is known (by
Rex), triangle is implied."*

- **The B08 storm-wall opening may stay in B08, possibly fleeting.** §93's question 1 is answered
  for B08; moving the opening to B09 falls away.
- **The factions do not learn the swamp is the Mending site until B09 Act III.** This is the
  author's intent, and it is now a governing constraint on Loom development (CLAUDE.md §9 step 1).
  **Eight or more pasted beats conflict with it**:
  - B07: factions converging (A2.8, A3.8); Kade's MT pointing toward the swamp (A3.3); the
    Choirless intercepting (A3.6).
  - B08: Brightbreak shadowing Kade (A1.5); perimeter sightings (A1.7); siege lines (A3.1).
  - B09: a perimeter breach (A1.7); **all of B09 Act II, "The Siege of the Swamp."**
  
  They are listed in the ruling's §4.1 for rework; none is rewritten. The protagonists' own
  knowledge fits the constraint if it stays private.
- **Reading offered, not adopted:** the protagonists' candidate-site chain (NOLA → Santa Fe → Mound
  City → St. Louis → Serpent Mound; POOL-015) gives the factions somewhere else to look through
  B07–B08.
- **READING:** Elias claiming the opening for Kade can be the factions' misreading. They hear of a
  miracle, not a site. Where Elias is when he makes the claim is open.
- **Tahl's one identifiable Echo appearance is the B09 flare, and Rex knows it.** The epilogue
  triangle is implied. For the grid copy: M22 and M27 are not identifiable; **M36's identifiable
  farewell conflicts** and must become implied, merge into the flare, or retire.

This also resolves §93's question 2, and the B8 card's finding C leans to reading 1 (seen, not
entered).

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 94

===============================================================

# 95. Loom structural pass 1; the Dec 8 "masters" are assistant output — 2026-09-26

**Status:** PROPOSAL pass plus a provenance correction.
`proposals/LOOM_STRUCTURAL_PASS1_B07_B09_2026-09-26.md`. No grid, ruling or episode change.

**Asked:** the author, *"The milestones above again make me feel like Book 9 has been spread out
to fill Loom"*, then *"yes, start the Loom pass."*

## 1. Provenance correction (repo-wide)

The Dec 8 Veil, Neon and Loom "MASTER BEAT BIBLE" texts, pasted by the author into
`2025-12-08__Trilogy_Act-Level_Beat_Backup` (and two other Dec 8 chats), were **generated by the
assistant** in `2025-12-07__Beat_bible_recovery_process`: Veil at l. 31274, **Neon at l. 31452
after the USER prompt "Prepare neon"**, and **Loom at l. 31614 after "Prepare loom."**

Since at least 09-23 the repo has cited them as *author-pasted* and *"CURRENT high-value macro"*.
That includes the B06 separation report, the B07/B08 storm-wall test, the Loom ledgers, the
milestone packet, and today's B6 and B8 cards and rulings. **Content stands; weight drops** to
"an assistant reconstruction the author backed up." The Loom text contradicts the author on the
near-kill: it has Elias where he says Rex. Notes were added to the B6 and B8 cards. `recovery/` and
`reports/` files are not edited; this entry is the correction.

**Consequences:**

- The epilogue is unaffected; it stands on the author's own words (§92).
- **B6 timing:** the Act II placement of Tahl's death comes from the Neon backup. The author's
  own 2025 words lean later: *"end of Book 6"* (`NS` ~68443); *"I thought it was act III"*
  (`Saga_Beat_Expansion_Pipeline` ~6437). M20 stays open for Neon mapping.
- The book titles (*The Quiet Front*, *The Swamp of Alignment*) are assistant titles.

## 2. Found: the author's own per-book plan

`2025-11-27__Narrative_Structure__69286516.md` ll. 39256–39274, 2025-11-28, USER:

- **B07:** funeral → Lacuna settles Kade → Seraphine drawn toward becoming the Loom → Kade on
  MT → Elias met, Brightbreak formed → *"a catalyst event to fracture the brittle world"* → a plan
  to learn how to stabilize the Veil.
- **B08:** Lacuna and Kade argue about violence → *"a search for the tear in the veil"* → ends
  *"learning it may be back in Louisiana."*
- **B09:** escape, pursuit, *"feint in Nola while the crew heads to Honey Island"*; A3 *"the
  antagonists learn that Honey Island Swamp is the site"*; the last chapter or two are the
  Elias/Kade/Rex/Tahl scene, then the Mending.

**It already contains the 09-26 site-secret constraint.** The same conversation records the
author making the same complaint ten months earlier: *"how does that fill an entire book?"*
(~38122); *"the end game is getting spread back out"* (~59719). On 12-09 he proposed anchor
milestones *"to keep events from spreading out"* (`Episode_expansion_process` ~44555).

Also found: *"Tahl dies, Silence grieves and collects him"* (`Prompt_crafting_types` ~53372,
2025-11-13). This is the author source for today's recalled *"Silence collects Tahl's soul."* It
has been added to the 09-26 ruling.

## 3. Measured, by script

On the Dec 8 assistant Loom text, the share of swamp-approach beats is:

| Book | Approach beats | Share |
| --- | --- | --- |
| B07 | 12 of 26 | 46% |
| B08 | 14 of 24 | 58% |
| B09, Acts I–II | 11 of 16 | 69% |

**Eleven beats conflict** with the site secret. The chat figure "nearly two-thirds" for B08 was
high.

## 4. Proposal (not adopted)

The author's plan is proposed as Loom's spine. Its two empty slots are where B07 and B08 get
their own anchors:

- **B07 catalyst:** C1 NOLA breaks / C2 Kade's voice moves people / C3 a local systems failure.
- **B08 anchor:** A1 a thin-place event / A2 Kade's first complicity in violence / A3 the Choirless
  quieting.

The recommendation for discussion is C2+C1 and A1+A2. **Grid-copy consequences:**

- M31 is replaced by B08's close, *"the tear may be back in Louisiana."*
- M28 becomes a departure from NOLA, not toward the swamp.
- M27 becomes a VT-side beat.
- M29 retires.
- **Add** Elias's arrival, the Lacuna split, the NOLA feint, the antagonists learning the site,
  and **Kade's near-kill of Rex plus Tahl's flare, which is absent from the grid.**

## 5. Corrections made today

1. Ruling §4.3 cited *"Rex intervenes"* from the assistant line; corrected (Kade nearly kills Rex).
2. The B8 card's B9 arc lines are flagged as assistant-master.
3. Chat: B08 share 58%, not "nearly two-thirds."
4. Chat: B07's title as a signal of its own story is withdrawn; it is an assistant title.

**Method:** two read-only search agents; every author quotation used was checked against the
export in this session, and each agent's claim that the masters are assistant output was
confirmed at the prompt lines.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 95

===============================================================

# 96. Loom spine and anchors ruled — 2026-09-26

**Status:** records an author ruling. `decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`.
No grid, episode or rule change.

**The author**, answering the Loom pass §8: *"1 yes, 2 C1+C2, 3 A1+A2, 4 foreshadowing (argument?)
at end of B7, split at beginning of B8."*

- **Spine:** the author's 2025-11-28 plan (§95 §2), not the Dec 8 assistant master.
- **B07 anchor:** Kade's MT post, amplified by Elias, moves people, and New Orleans breaks. The
  crew departs, not toward the swamp. The causal order between post and break is not ruled.
- **B08 anchors:** a costly finding at a thin place (search strand) and Kade's first complicity in
  his splinter's violence (Kade's strand). **Which thin place is open.** The Choirless quieting
  stays available, neither chosen nor rejected.
- **Lacuna–Kade:** foreshadowed at B07's end (*"argument?"*, tentative), split at B08's start.

**Constraints the anchors must satisfy:** the site secret; different in kind from the B03 and B06
collapses; Kade redeemable, with the Rex near-kill not pre-empted; Elias without metaphysical
access; D5.

**Grid-copy consequences:**

- M28 becomes a departure from New Orleans.
- M31 is replaced by *"the tear may be back in Louisiana."*
- M29 retires.
- Rows to add:
  - Elias attaches to Kade.
  - The B07 anchor.
  - The Lacuna argument and split.
  - The two B08 anchors.
  - The NOLA feint.
  - The antagonists learn the site.
  - **The Rex near-kill and Tahl's flare.**

**Next:** event cards for the B07 anchor and the two B08 anchors, then the proposed grid copy
covering all nine books.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 96

===============================================================

# 97. Loom follow-up ruled; B07 and B08 anchor event cards — 2026-09-26

**Author:** *"Santa Fe, / Book 7 opens with funeral (lacuna prominent) / Serpent Mound / then
proceed with the event cards."* Recorded as a follow-up in
`decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`:

- B08's thin place is **Santa Fe**.
- B07 opens **at Tahl's funeral, with Lacuna prominent**. This matches the author's 2025-11-30
  statement that Lacuna *"is introduced as the leader of Tahl's second line"*
  (`Concord_Saga_review` ~1618).
- B09's escape is at **Serpent Mound**.

The route is fixed at its ends: NOLA → Santa Fe → Serpent Mound → the NOLA feint → Honey Island.
St. Louis / Mound City is unused.

## B07 card

`proposals/B07_FUNERAL_POST_AND_NOLA_BREAK_EVENT_CARD_PASS1_2026-09-26.md`. The 12-link chain
starts from the funeral, Lacuna's framing and Elias seeing Kade (author).

- **Recommends a civic break, not a structural one.** Compared with B03 and B06 it differs in
  kind: a named, public voice; a mobilised following rather than onlookers; a district's order
  breaking rather than a building.
- **Location:** Uptown recommended.
- **Flag:** the user-pasted NOLA palette's Loom entry *"Warehouse → Resonance Tear Opening"*
  collides with B08's search for the tear. The Warehouse can only be a symptom.
- **Flag:** Tremé as *"Riot of Light Ground Zero"* risks repeating B04's riot.
- **The post/break order** is set out as two readings, direct or shared accountability.
- **Elias:** *"wants reach, fame, influence"*; needs *"the livewire version of Kade"* (author
  12-15, verified).

## B08 card

`proposals/B08_SANTA_FE_FINDING_AND_KADE_COMPLICITY_EVENT_CARD_PASS1_2026-09-26.md`.

- **Search strand:** Santa Fe is where Tahl died and where *"Silence grieves and collects him"*
  (author 11-13). No identifiable Echo there. Seraphine's answer is reserved for the end, so Santa
  Fe can give doubt, not the answer. Recommended finding: the scar is a wound, not the origin,
  combined with the old way failing (F2+F1). Recommended pointer to Louisiana: the finding plus
  Elias's reported "Kade miracle" (reading 2). The site secret holds.
- **Fall strand:** complicity as **authorisation, not a strike**. This keeps the Rex near-kill
  intact and makes a rising line: the B07 post → B08 permission → B09 attempted authorisation
  (EliasEBCI). Victims (the Choirless, a shelter, or bystanders) are open. The crew learns of it
  through MT.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 97

===============================================================

# 98. Correction to §97: Mound City is on the route — the protagonists travel a circuit of wounds — 2026-09-26

**What was wrong.** §97 and the Loom ruling's follow-up said *"St. Louis / Mound City is unused."*
The author: *"I think your recommendation is right for the general public, but our other
protagonists know that there are other wounds at the Mound City, Serpent Mound, etc sites that
they must travel to."*

**What replaced it.** A second follow-up in `decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`:

- **Ruled:** the protagonists know of several wounds and must travel to them: Mound City, Serpent
  Mound, and others (*"etc"*). Santa Fe is one wound on that circuit.
- **Accepted:** the B08 card's F2 finding ("a wound, not the origin") as *"right for the general
  public."* Two readings of that phrase are recorded: public knowledge that differs from the
  crew's, or right in general with the circuit added.
- **Open:** which other wounds; their order; why the crew must go; how B08's *"may be back in
  Louisiana"* fits a circuit still unfinished when B09 opens at Serpent Mound.

The B08 card carries a note. §97's line is not edited; this entry corrects it.

**Pending:** the Elias / Kade / Lacuna export search the author asked for in the same message.

END OF ENTRY 98

===============================================================

# 99. Who believes what: the factions think Louisiana; the crew knows the wounds, Honey Island last — 2026-09-26

**The author:** *"the antagonist factions and others think it leads back to Louisiana (perhaps the
opening in the storm wall, makes this think this), but our primary protagonists know that there
are multiple wounds and that the Honey Swamp one must be repaired last. (Maybe getting that
information is what unravels Tahl)."* This is the third follow-up in
`decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md`.

**Ruled:**

- The factions and others believe it leads back to Louisiana.
- The primary protagonists know there are several wounds and **the Honey Island wound must be
  repaired last.**

This settles §98's two readings (the first applies) and refines the spine: B08's *"may be back in
Louisiana"* is the factions' conclusion.

**Hypotheses:**

- The storm-wall opening is what makes the factions think it.
- Getting the information is what unravels Tahl.

**Consequences:**

- The NOLA feint gains its engine: the factions are in the right state, at the wrong place.
- The crew's circuit is **repair**: Santa Fe → Mound City → Serpent Mound → (others?) → Honey
  Island last.
- Tahl's fatal VT contact at the Santa Fe rupture may be where the wound structure is learned.
  How the crew then has the knowledge is open.

**Flagged:**

- Pre-Mending "repair" against Mechanica §34 (a Rupture is a permanent scar), §35
  (stabilisation's four requirements) and §7.4 (nodes only after the Mending); D5 holds.
- Whether the circuit is Silence and Hope's hard-cap method or where Seraphine's *"another option"*
  diverges; the answer stays reserved for the end.
- The B08 and B06 cards carry notes.

**Pending:** the Elias / Kade / Lacuna export search.

END OF ENTRY 99

===============================================================

# 100. Elias, Kade and Lacuna recovered from the export — 2026-09-26

**Status:** recovery. `recovery/ELIAS_KADE_LACUNA_SOURCE_RECOVERY_2026-09-26.md`. No card, ruling or
grid change.

**Asked:** the author: *"there are several conversations about Elias and his motivations, how he
manipulates others (especially Kade), how Lacuna mistrusts him … how Kade gets wound up,
manipulated, and starts to question Brightbreak."*

**Method:** three read-only search agents, split by conversation. Every author quotation was
verified with its speaker header. One agent line reference was wrong ("black light brigade" is at
`PC` 59273, not 59267); corrected.

**Findings:**

1. **Kade's radicalisation predates Elias.** In November 2025 the author designed a Kade-led Neon
   Rebellion splinter that *"chase[s] our protagonists in the end game"* (`MDR` 10134). Elias
   began as the *"devil on his shoulder"* role (`NS` 3747). Brightbreak took the splinter's slot.
   No repo document had traced this.
2. **Strongly accepted Elias material:**
   - "Elias Canon v2" (*"Perfect, proceed"*): not possessive; *"predatory empathy"*; separates Kade
     from Lacuna because *"Grounded Kade cannot be radicalized"*; *"the illusion of being valued,
     not the reality of being loved."*
   - The authorisation model: *"Kade to authorize his story without realizing it."*
   - Brightbreak's structure (*"Lock A/A"*).
   - The Kade Bible (*"Save Kade Bible"*).
3. **The Tier-1 Elias cards contradict the author:**
   - EBCI gives Elias a Veil and a Neon presence, against *"no presence in Veil, no named presence
     in Neon"*;
   - ID says New Orleans *"pre-Neon"*, against his arriving for MT after the Brightbreak handle's
     loss;
   - the ID and POV cards have Lacuna *"barely register"*, against *"settling influence"* and the
     link being revealed *"when he starts to undermine Lacuna."*

   Corrections are proposed, **not applied** (Tier-1).
4. **The finale choreography has been consistent since November 2025:**
   1. Elias attacks first.
   2. Rex knocks him down.
   3. Kade, having tried to stop Elias, fears Rex will kill him and attacks Rex (*"save" Elias,
      representation of himself*).
   4. The echo, with Silence's boost.
   5. Kade talks down Brightbreak and stands with Rex, with the Choirless unresolved.
   6. *"Tahl then aids Rex."*

   The assistant's *"If Rex reaches her, the world ends"* is a second motive, recorded.
5. **Doubt:** in every author statement Kade breaks only at the echo. The one pre-echo doubt beat
   is the author's *"tell him to stop, wait, and let him try to talk with Rex."* READING: B08's
   complicity is the natural first doubt, which must stay a doubt.

**Supports today's cards:** B08 complicity-as-authorisation is directly sourced. The author once
floated that Lacuna nudges Kade to post to MT, which bears on the B07 card.

**Recorded, not resolved:** Elias named in B06 or not; Brightbreak as the Neon Rebellion's
splinter or a civilian network; whether Kade thought MT was private; the attack motive; a
"Solace" leading the Choirless; Elias's surname (Ward is locked) and age.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 100

===============================================================

# 101. Wounds, hard cap, and Elias answered; Elias card corrections specified — 2026-09-26

**Status:** records an author ruling and a proposal. No card, rule or grid change.

## 1. Wounds

`decisions/LOOM_WOUNDS_AND_ELIAS_AUTHOR_ANSWERS_2026-09-26.md` §1:

- **Repair is stabilisation** (ruled). Mechanica §35 applies; a stabilised scar is still a scar
  (§34); D5 holds.
- **Silence and Hope guide the crew to reinstate the hard cap. Seraphine grows to question it and
  begins the potential of a breathing veil** (ruled). *"there should be quite a bit of conversation
  on this idea"* is read as an in-story direction.
- The crew stabilises Santa Fe (lean).
- The author does not clearly recall the specifics of Tahl's death; a search is running.

## 2. Elias

`decisions/LOOM_WOUNDS_AND_ELIAS_AUTHOR_ANSWERS_2026-09-26.md` §2. Ruled:

- **Handle only in Neon**, as foreshadowing; naming is too soon. This supersedes *"Perhaps named
  in 6"* and the accepted Visibility Rule's B6 naming.
- **Some Neon Rebellion splinters become Brightbreak; others dissolve or stay independent.**
- **Lacuna nudges Kade to post, and Kade thought MT was private at first.** This supersedes
  `MDR` 11347.
- **Kade attacks Rex from fear that Rex will kill Elias.** The assistant's *"If Rex reaches her,
  the world ends"* is not the motive.
- **A Solace-led Choirless is acceptable.** The author recalls a dedicated conversation; a search
  is running.

## 3. Card corrections, specified, not applied

The author said *"give me specifics before doing so."*
`proposals/ELIAS_CARD_CORRECTIONS_PROPOSAL_2026-09-26.md` gives exact current and proposed text.

**Required (the cards contradict the author):**

- E1: EBCI Veil → no presence.
- E2: EBCI Neon → the handle only; no Kade.
- E3: ID New Orleans move. Option (a), late Neon for MT, is recommended; option (b) keeps an early
  stint and adds a return. The conflict with the chosen Dec 9 backstory (a move at about 20) is
  the author's to decide.
- E4: ID §XI Lacuna → the obstacle he underestimates. The misreading is kept.
- E5: POV "barely registers" → registers as an obstacle.

**Recommended:** E6 the core imprint line; E7 naming the Rex near-kill finale; E8 "attention, not
affection" and authorisation.

**Related:** E9 Brightbreak lineage; E10 Kade and Lacuna MT posting lines.

**Also:** the B07 card has a note (Lacuna prompts the posting; open whether the anchor post is
hers or his).

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 101

===============================================================

# 102. Solace: no earlier dedicated conversation; chronology corrected — 2026-09-26

**Asked:** the author recalled *"a dedicated conversation"* about a Solace-led Choirless.
`recovery/SOLACE_CHOIRLESS_SOURCE_RECOVERY_2026-09-26.md`.

**Found** (verified against `.json` timestamps and speaker headers):

- **No capitalised "Solace" exists before 2025-11-27.**
- Solace first appears at 11-27 15:46 as an assistant **Brightbreak** code name (`NS` 3979). It
  becomes Elias's nickname at the author's request (16:01).
- The first **Choirless** Solace is an assistant voice card at 11-30 06:00 (Concord_Saga_review
  5208). The author pasted it at 06:03 as *"not canon yet."* At 06:19 he said *"originally a
  Choirless persona,"* and at 06:23 *"Choirless could still be led by a Solace character."*
- The development he likely recalls is `NS` ~145335–146240: a masked **title**, *"Silence is
  mercy,"* *"the inverse of Tahl."* It is assistant material, accepted with "Proceed" only.

**Correction:** the Elias recovery's §3.9 quotes the author accurately but implies a chronology
the record does not support. This entry corrects it; the file is not edited.

**Tensions if Solace is used:**

- The pastoral version duplicates Saeko (*"coercion disguised as care"*).
- The canon Choirless has no leader and is fragmented in Loom (*"no longer need a name"*).
- The micro-bible's *"track the swamp node"* conflicts with the site secret.
- The B06 "Solace cult" (Dec 8 assistant backup) has an ambiguous owner.

**Open for the author:** whether `NS` ~145335 is the conversation he recalls; a masked title or a
public voice; a fragmented or unified remnant.

**Pending:** the Tahl death-specifics search.

END OF ENTRY 102

===============================================================

# 103. Tahl's death recovered from the export — 2026-09-26

**Asked:** the author: *"I do not clearly recall the specifics of Tahl's death."*
`recovery/TAHL_DEATH_SOURCE_RECOVERY_2026-09-26.md`. Author quotations and the key staging lines
were verified.

**The author fixed five things:**

1. **Late Book 6:** *"end of Book 6"*; *"I thought it was act III."*
2. **Cause:** *"We know it was caused by the VT link."*
3. **Silence collects him,** and Silence gains Intent at that collection.
4. **The jazz-funeral second line** opens Book 7.
5. **He and Kade *"never met."***

**Everything else is assistant material in at least six stagings.** The best-attested is `NS`
149826–150210 (a B6 Act III sequence), answered *"This direction is good"*:

1. He goes to Santa Fe against Elisabet's warning, to witness from the centre.
2. VT slip → *"MT goes black. Tahl dies in Santa Fe."*
3. *"No farewell post."*
4. Elisabet's maps then show *"all roads now converge on Louisiana's swamp."*

This answers the B6 card's link 11 as accepted direction; the card carries a note.

**Unravel hypothesis:** no source has Tahl learning of the wounds. The closest is Elisabet's
post-death mapping (knowledge that is hers). A line has Tahl *"briefly"* perceive VT's structure;
an art constraint says he *"cannot … map."* A combined reading is offered, not adopted.

**M20:** the author's own words lean later than today's lean (end of Act II); still open for Neon
mapping.

**Open for the author:**

- Is the Act III staging the one he remembers?
- Which act?
- Does Tahl glimpse the wound structure, does Elisabet map it, or both?
- A last post, or none?

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 103

===============================================================

# 104. Elias card corrections applied; Lacuna, Solace and Tahl answers — 2026-09-26

**Status:** records an author ruling and the Tier-1 card edits it approves.
`decisions/ELIAS_CARD_CORRECTIONS_AUTHOR_RULING_2026-09-26.md`.

## 1. Applied (the author: "looks good, proceed")

E1–E10 from `proposals/ELIAS_CARD_CORRECTIONS_PROPOSAL_2026-09-26.md`, with E3 as option (a):

- **EliasEBCI:** Veil none; Neon handle only; attention, not affection; authorisation; Lacuna
  targeted.
- **EliasID:** New Orleans in late Neon, for MT; the core imprint; Lacuna as the obstacle he
  underestimates; the finale named.
- **POV card:** Lacuna registers as an obstacle.
- **Brightbreak:** absorbs some Neon Rebellion splinters.
- **KadeEBCI and LacunaEBCI:** the private-diary MT start; Lacuna nudges him to post.

Each edited line keeps its old wording in a dated note.

## 2. Ruled

- **Lacuna prompts the B07 anchor post.**
- **Solace:** `NS` ~145335–146240 is the conversation the author recalled. Solace is a **masked
  title or removed**. A Solace event is **POOL-033, optional**. The Choirless stay **fragmented**.
- **Tahl dies at the end of B06.** This supersedes the Act II lean and the packet's A3 → A2
  correction. **He glimpses the wound pattern.** **The B06 epilogue carries his message to the
  group about it**, and it is his last message, superseding *"No farewell post."*
- **Task:** resolve Tahl's death specifics.

## 3. Corrected

§101 read *"there should be quite a bit of conversation on this idea"* as an on-page direction. The
author meant **earlier chats to recover**. The 09-26 wounds ruling carries a note.

## 4. Searches launched

- The hard cap against the breathing veil.
- The US wound sites, their order, and the crew's understanding.

The author says both are in the earlier chats.

## 5. Consistency notes

- **Tahl's posthumous message is mortal communication, not an Echo appearance.** Its delivery
  must not be VT. Its recipients ("the group"), content and delivery are open.
- The B06 epilogue now carries this message and M23's MT handoff; their order is open.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 104

===============================================================

# 105. Correction to §104: Lacuna inspires; Elias politicises from B07 Act III — 2026-09-26

**What was wrong.** §104 recorded *"Lacuna prompts the B07 anchor post"* as ruled, from the
author's one-word answer *"Lacuna."* That over-read it.

**The author:** *"Lacuna's involvement with Kade and his posting is one of inspiration, the
splintering and politicized posts is later Elias manipulations. I think Kade is mostly influenced by
Lacuna in B7, until Elias begins to subvert in act3 etc."*

**What replaced it** (`decisions/ELIAS_CARD_CORRECTIONS_AUTHOR_RULING_2026-09-26.md` §5):

- **Ruled:** Lacuna's part is inspiration; the politicised posts are Elias's.
- **Lean:** Kade is mostly Lacuna's in B07 until Elias subverts him in Act III.
- **Reading:** the B07 anchor post and the NOLA break fall in B07 Act III.
- The B07 card, CLAUDE.md, the decisions index and the wounds ruling are corrected.
- LacunaEBCI's *"Nudges Kade to post"* (E10) is inspiration, and stands.

**Lesson:** a one-word answer to an either/or question confirms the choice named, not the
elaboration attached to it. Record the choice, and ask before adding consequences.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 105

===============================================================

# 106. Loom wound sites recovered: the Alignment Chain — 2026-09-26

`recovery/LOOM_WOUND_SITES_SOURCE_RECOVERY_2026-09-26.md`. Verified against the export.

**Found:** the author saved (*"Proceed with save,"* `WB` 128752, 12-03) a four-node **Alignment
Chain**: Santa Fe Scar ("The Break") → Mound City / St. Louis ("The Direction") → Serpent Mound
("The Alignment") → Honey Island ("The Convergence / The Mending").

- **Honey Island is last because it is the original Tear.** Approved on 11-22: *"First the swamp
  ending is approved"*; *"Antagonists ALL assume … NOLA. They are wrong."*
- **The 11-30 Loom Endgame Card** (*"Confirm"*) is the source of `canon/trilogy_loom.md`'s Key
  Locations line, which already matches the ruled route.
- **The author curbed the secondary US nodes** (12-03: *"adding new information vs compiling"*).

**Source weight:**

- **No source has the crew stabilising a site, or ties Silence and Hope's hard cap to the nodes.**
  Both are new 09-26 author material.
- In the sources the crew discovers the swamp endpoint late.
- The author's 11-28 lean had the sites work through MT and supplements. His 2026 rulings have the
  crew travel; those govern.

**Reconciliation offered (reading):** Tahl's B06-epilogue message gives the crew the pattern; the
chain gives the particulars. The sources' discovery beats become confirmation beats.

**Site-secret risks** in the accepted cards: B08's *"all factions converging on the swamp"* and
Serpent Mound's *"multiple factions converge."* Framing that fits the rulings: the factions read the
vectors as Louisiana / New Orleans.

**Open for the author:**

- Are these all the wounds, or does "etc" add others?
- Is Mound City in B08, after Santa Fe?
- Is Serpent Mound one continuous event across the B08/B09 break?
- Does the knowledge split (Tahl gives the shape, the chain the particulars) match his intent?

**Pending:** the hard-cap / breathing-veil search.

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 106

===============================================================

# 107. The hard cap and the breathing veil recovered — 2026-09-26

`recovery/HARD_CAP_BREATHING_VEIL_SOURCE_RECOVERY_2026-09-26.md`. Verified against the export; two
agent line references corrected (`PC` 27473, 27745).

**Found — the author's own design, 13–15 November 2025 (`PC`), two locks, none of it in the repo:**

- **The breathing veil:** the old veil *"was too rigid … blocking"*; the new one *"breathes, it
  filters … the n95 mask for the world"*, with empathy as the filter (50415). Empathy is *"a word
  of power"*, withheld until the greatest moment (19155).
- **Silence and Hope's error:** they *"thought that only Seraphine had to ascend … the veil that
  breathes required more. It required guides"* (91822). Their old logic: *"One Loom, one Thread,
  one Ascendant."*
- **Locked (*"Lock it. Highest of fives"*, 51477):** Seraphine becomes the Breath of the Veil;
  Mira is her soft guide; Lucien's final test is to Listen.
- **Locked Finale Phase Map (*"Lock"*, 93904):**
  - the old metaphysicals believe the hard cap is the only way;
  - Seraphine *"feels (not knows yet)"*;
  - **A Loom (Seraphine) / Two Anchors (Lucien, Caro) / A Guide (Tahl/VT)**;
  - Silence and Hope disperse into the membrane's *"scaffolding, its laws."*
- **Saving Tahl's echo is Silence and Hope's first act of agency, *"the first crack in the cycle of
  hard cap veils"*** (author, `NB` 89177).

**Against the 09-26 rulings:**

- The coaching plan and Seraphine's growing doubt match.
- The answer stays reserved for the very end.
- Tahl / VT as the locked **Guide** matches the ruled LT conduit.

**Correction:** the wounds ruling's §1 line *"It grows wound by wound"* was an inference with no
source. It is now marked so. The sources tie her doubt to intuition and to becoming the Loom, not to
the nodes. No source ties the node circuit to the cap either (§106).

**Bears on a standing task:** *"who performs the Mending — five named human functions, of whom the
trio ascends"* (CLAUDE.md §4.1) should be re-read against the locked map.

**Open for the author:**

- Does the locked map still stand against the 12-07 ascension order?
- Does her doubt grow from the circuit or from becoming the Loom?
- The cost: only her, or the guides as well?
- Mira: the locked guide, or the retired "Mira Tremeaux"?

**Checks:** canon scope 0; 144 self-tests; sources unchanged.

END OF ENTRY 107

===============================================================

END RECOVERY LEDGER
