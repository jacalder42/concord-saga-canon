# Concord 2026 — Migration Map: Book Context + Act Overlays

Status: PROPOSAL / NON-CANONICAL
Purpose: compare the recovered nine-book authority layer against the existing GitHub `book_context/` and `act_overlays/` scaffold and identify what can be migrated directly, what requires synthesis, and what should remain unresolved.

## Executive finding

The existing `book_context_B01-B09.json` files are scaffolds, not developed canon. They contain correct book/trilogy IDs but TODO placeholders for title, POV targets, entry state, exit locks, locations, escalation permissions, and continuity hooks.

The existing 27 `act_overlay_*.json` files are likewise scaffolds. They preserve the correct structural IDs and a reusable schema, but `act_thesis`, pressure vectors, character-state deltas, success criteria, and forbidden shortcuts are unpopulated. The same default LOW soft-modulation values appear in the sampled Veil, Neon, and Loom overlays and therefore should be treated as template defaults rather than recovered act-specific canon.

Conclusion: these files do not contradict the recovered story architecture. They are empty containers awaiting migration.

---

# 1. What should be preserved from the existing scaffold

## Book context
Preserve:
- `schema_version`
- `book_id`
- `trilogy_id`
- field names / basic data shape

Do not treat current TODO values as canon.

## Act overlays
Preserve:
- `schema_version`
- `act_id`
- `book_id`
- `trilogy_id`
- general concept of act-level deltas

Review rather than automatically preserve:
- hard-coded `soft_modulation` defaults of LOW for fun / slice-of-life / wonder. These appear to be template defaults, not source-derived act decisions.

---

# 2. Book-context migration status by field

## `title`
Status: DIRECTLY MIGRATABLE from recovered Final Canon.

- B01 — Veil: The First Thread
- B02 — Veil: The Second Breath
- B03 — Veil: The Fracture Point
- B04 — Neon: First Fracture
- B05 — Neon: Fracture Patterns
- B06 — Neon: The Breaking (Santa Fe)
- B07 — Loom: The Quiet Front
- B08 — Loom: The Swamp of Alignment
- B09 — Loom: The Mending

## `pov_targets`
Status: PARTIAL / REQUIRES RULE SYNTHESIS.

Recovered Episode Expansion specifies a book-level 30/30/30/10 POV distribution framework, but this should not be blindly copied to all nine books without checking the Trilogy Structural Canons and book-specific POV baton rules.

Migration action:
- preserve field;
- populate only after POV canon cross-check;
- do not infer exact weights from macro beats alone.

## `entry_state.world`
Status: RECOVERABLE, but requires concise synthesis from prior-book exit and current-book opening beats.

This is a derived summary field, not an archival source field. It should be generated from the recovered authority layer after approval.

## `entry_state.key_character_states`
Status: RECOVERABLE, but derived.

Use character-transition cross-check + prior-book exit. Important special cases:
- B04 must carry the unresolved/probable Baz death transition without inventing exact circumstances.
- B07 must open in explicit post-Tahl-death grief/funeral state.

## `exit_state_locks`
Status: STRONGLY RECOVERABLE.

These can be derived from each book's final act / epilogue and should be phrased as locks rather than summaries.

Examples:
- B03: Baz alive at close; Tahl has first VT brush and begins proto-MT writing; truth-telling commitment established.
- B06: Tahl dead; MT silent then Kade rises; Seraphine near-shatter; Lucien in Silence-precursor spiral; world enters Loom grief state.
- B09: Mending completed; Tahl remains echo-only; Kade writes first post-Mending MT; LT handshake invitation opens next layer.

## `locations_in_play`
Status: PARTIAL / DIRECTLY MIGRATABLE WHERE EXPLICIT.

Strong recovered examples include:
- NOLA / swamp / Jackson Square for B01
- Southwest / Santa Fe as convergence through late Veil and Neon
- NOLA, Santa Fe, Mound City, Serpent Mound, Honey Island across Loom

Do not add locations from general character/world knowledge unless the book beats actually place them in the book.

## `escalation_permissions`
Status: DO NOT POPULATE FROM STORY BEATS ALONE.

Fields:
- `max_corridor_tier`
- `max_weather`
- `max_fx`

These must be cross-derived from Mechanica v4 + trilogy envelope rules + any recovered VFX ceiling tables. This is exactly the kind of field that should remain TODO until systems reconciliation is complete.

## `continuity_hooks`
Status: STRONGLY RECOVERABLE.

Populate from explicit book-to-book bridges, not generic foreshadowing.

High-confidence examples:
- B03 -> B04: Tahl recovery / proto-MT / truth-telling commitment; Baz alive at B03 close; probable B04 removal event flagged.
- B06 -> B07: Tahl death -> funeral / grief / Kade succession.
- B08 -> B09: chamber revealed / Mending path locked / siege convergence.

---

# 3. Book-by-book migration readiness

## B01 — The First Thread
Readiness: HIGH.
Directly recoverable:
- title
- broad entry state
- locations
- act structure
- exit locks
- continuity hooks
Additional advantage:
- detailed Episode Expansion exists through E18.
Still blocked:
- exact escalation permissions
- final POV target weights

## B02 — The Second Breath
Readiness: HIGH at macro level.
Directly recoverable:
- title
- act structure
- major pressure escalation
- exit direction toward Southwest fragility
Blocked/derived:
- exact character entry/exit phrasing
- escalation permissions
- POV weights

## B03 — The Fracture Point
Readiness: VERY HIGH.
Directly recoverable:
- title
- act structure
- Tahl entrance and transfer preparation
- Santa Fe convergence
- VT brush
- Veil->Neon epilogue
- Baz alive at exit
Key continuity flag:
- B04 Baz death/removal event remains missing in exact form.

## B04 — First Fracture
Readiness: HIGH with one major reconciliation flag.
Directly recoverable:
- title
- Lucien dissociation escalation
- Tahl MT emergence
- first Neon-scale fracture
- crisis-voice / public-truth function
Unresolved:
- exact Baz killing beat, circumstances, placement, and culprit.
Migration rule:
- book context may state `Baz absent/killed during early B04 — exact event unresolved` only in proposal metadata, not as final structured canon until approved.

## B05 — Fracture Patterns
Readiness: HIGH.
Directly recoverable:
- title
- shard escalation
- Seraphine/Lucien deterioration
- Tahl load/burnout
- Santa Fe convergence
Blocked:
- exact permissions/threshold fields

## B06 — The Breaking (Santa Fe)
Readiness: VERY HIGH.
Directly recoverable:
- title
- Santa Fe collapse
- Tahl death
- MT silence
- Kade succession
- Neon->Loom grief state
Blocked:
- exact systems ceilings if not already explicit in Mechanica tables

## B07 — The Quiet Front
Readiness: VERY HIGH.
Directly recoverable:
- title
- Tahl funeral opening
- Kade reluctant succession
- Seraphine/Lucien grief-state continuity
- Honey Island/Mending-point investigation
- major locations

## B08 — The Swamp of Alignment
Readiness: HIGH.
Directly recoverable:
- title
- Honey Island approach
- node-site investigations
- Brightbreak/Kade escalation
- Lucien Silence crisis
- chamber reveal

## B09 — The Mending
Readiness: VERY HIGH.
Directly recoverable:
- title
- siege / breach structure
- Kade/Elias crisis
- Rex intervention
- Tahl echo flare
- Seraphine + Lucien + Caro Mending
- post-Mending MT + LT handshake

---

# 4. Act-overlay migration map

Each act overlay currently contains these unfilled fields:
- `act_thesis`
- `deltas.pressure_vectors`
- `deltas.character_state_deltas`
- `act_success_criteria`
- `forbidden_shortcuts`

These are all derivable from recovered act-level canon, but they are **interpretive structured summaries**, not archival source text.

Recommended migration method:
1. keep the recovered Final Canon act beat text in human-readable authority files;
2. derive the JSON overlay from that text;
3. cite/source the authority file in a future schema revision or metadata field;
4. regenerate overlays if the authority layer changes.

## `act_thesis`
Can be derived from the act's movement, but should be written conservatively.
Example:
- B03 A3: truth crosses from mapping into lived consequence; Tahl becomes the carrier as Santa Fe becomes explicit.
This is a synthesis, not original source wording.

## `pressure_vectors`
Can be derived from explicit act pressures:
- environmental / resonance escalation
- institutional / antagonist pressure
- internal / relational fracture
Prefer controlled labels and links to source beats rather than prose inflation.

## `character_state_deltas`
High value and directly useful for generation.
Should encode only meaningful state changes across the act, e.g.:
- Tahl: mapper/investigator -> first VT brush / beginning writer
- Lucien: misalignment -> dissociation/Silence precursor
- Kade: reluctant MT successor -> Brightbreak-aligned public force

## `soft_modulation`
Current values are identical template defaults across sampled acts in Veil, Neon, and Loom.
Status: TEMPLATE, NOT RECOVERED CANON.
Recommendation:
- move to trilogy/book defaults or derive per-act later;
- do not treat all 27 acts as canonically LOW simply because the scaffold says so.

## `act_success_criteria`
Useful as a generation guardrail.
Should describe what must be true by the end of the act, not retell all beats.

## `forbidden_shortcuts`
Potentially very valuable but requires careful derivation from canon rules.
Examples of the type of constraint:
- do not reveal Santa Fe too early;
- do not make Tahl mystical by intent;
- do not let MT transmit resonance;
- do not resurrect Tahl after B06.
Exact per-act entries require systems + story synthesis.

---

# 5. Scaffold conflicts / stale assumptions

## No story-level contradictions found
The book and act files are effectively blank, so they do not conflict with recovered narrative canon.

## One stale architectural assumption identified
The same LOW soft-modulation values are repeated across sampled acts from B01, B04, B06, and B09.
This should be treated as a generic template default, not an act-specific decision.

## One schema gap identified
The current scaffold has no provenance/status fields.
For 2026 use, derived files should ideally know:
- source authority
- status (`recovered`, `derived`, `open`, `conflict`)
- source path / source IDs

This would sharply reduce the risk of a derived summary later being mistaken for primary canon.

---

# 6. Proposed 2026 migration order

1. **Do not overwrite current main-branch scaffold yet.**
2. Preserve recovered human-readable authority layer on proposal branch.
3. Add proposal-level book-context files populated only with fields supported by recovered canon.
4. Leave escalation permissions and unresolved Baz details explicitly OPEN rather than guessing.
5. Derive proposal-level act overlays from recovered act beats.
6. Have Claude independently review the proposal branch against main GitHub canon and flag contradictions / unsupported synthesis.
7. Resolve remaining user decisions.
8. Only then promote reviewed files to canonical main-branch locations.

---

# 7. Architecture recommendation

The scaffold should become a **derived machine layer**, not the primary place where humans author story canon.

Recommended authority flow:

`human-readable Saga/Trilogy/Book/Act authority`
-> `book_context JSON`
-> `act_overlay JSON`
-> `episode/BID records`
-> `Sudowrite / NovelAI generation packets`

This keeps the useful schemas while eliminating the old synchronization problem where JSON scaffolds, chats, and Beat Bibles could all appear to be competing canon.
