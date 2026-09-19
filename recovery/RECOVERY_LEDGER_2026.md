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

END OF ENTRY 26

===============================================================

END RECOVERY LEDGER
