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

END RECOVERY LEDGER
