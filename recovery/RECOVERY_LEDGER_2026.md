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

END RECOVERY LEDGER
