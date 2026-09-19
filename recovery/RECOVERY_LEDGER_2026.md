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

END RECOVERY LEDGER
