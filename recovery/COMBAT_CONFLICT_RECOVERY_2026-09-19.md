# Combat and Conflict — Recovery Pass 2

**Status:** RECOVERED FROM NOTION / TIER D — RECOVERED PRIOR CANON / NOTHING MIGRATED
**Date:** 2026-09-19
**Sources:** `CONCORD SAGA — CONFLICT ENGINE (v1.0)` (Notion `- 05 • Canon Bibles`,
2025-12-01) and `CONCORD SAGA — COMBAT SKILL TREES (INTEGRATED) Part I — Core Seven
Characters` (Notion `Resonance Mastery Mechanics`, 2025-12-01)

**The shape question is settled by the recovered structure, not by a decision.** Ledger
§29 read the `Phase 1A` export as placing combat inside the UARS action economy rather
than on its own axis. The skill trees confirm it from the other direction: their six tiers
**are** UARS categories — Tier 3 is literally *Resonance Boost*, Tier 5 is *Failure Mode*.
Combat is how UARS expresses in one scene type. **No new schema is needed.**

---

## 1. `CONFLICT ENGINE (v1.0)` — ten sections

### 1.1 Core principles

> • All conflict = emotional, even when physical or political.
> • No villain is a caricature — antagonists are human, afraid, or misled.
> • Conflict escalates only when resonance pressure + emotional pressure align.
> • Conflict reveals wounds → growth → change.
> • No conflict exists without a cost.

These restate `canon_rules.json`'s `antagonists_human_or_human_made_only` invariant from
the conflict side, and the third line is the mechanical hook: **escalation requires both
pressures**, which is what makes conflict a resonance phenomenon rather than a separate
system.

### 1.2 Conflict Tiers 0–5 — the *kind and scale* of conflict

| Tier | Name | Stakes |
| --- | --- | --- |
| 0 | Micro-Tension | awkward silence, misread cues; fuels humor or romance, can spiral |
| 1 | Emotional Disagreement | the relationship / the moment |
| 2 | Ideological Conflict | worldview and group safety — Filaments vs Dominions, Technarc vs Concord |
| 3 | Personal Break Point | the character's core wound |
| 4 | Systemic Conflict | societal survival — city-wide collapse, institutional power grabs, resonance storms |
| 5 | Resonant Convergence | metaphysical + emotional aligned; deaths, ascension, irreversible change |

### 1.3 Conflict Modes M1–M5 — *how* tension manifests

`M1` Internal (*"always the deepest form"*, drives resonance behaviour) · `M2`
Interpersonal (banter → tension → rupture → repair) · `M3` Environmental (the world pushes
back) · `M4` Social/Factional (ideology weaponized) · `M5` Cosmological (**Silence paradox
loops, Hope overload, VT instability** — the Veil itself becomes adversarial).

### 1.4 Conflict Escalation Ladder C0–C5 — the *state within a scene*

`C0` Static Hum · `C1` Friction · `C2` Acute Clash · `C3` Breaking Point · `C4`
Irreversible Turn · `C5` Existential/Metaphysical Crisis.

### 1.5 Resonance–conflict interface

The mechanical core, and the part that binds conflict to Mechanica:

- **R-pressure increases** — emotions spike → resonance blooms → conflict escalates C1→C2→C3
- **R-pressure decreases** — grounding, breathwork, clarity rituals → C3→C1
- **Misaligned resonance = False Conflict** — characters fight the wrong target;
  *"common in Neon riot sequences"*
- **Aligned resonance = True Conflict** — characters confront the real wound;
  *"foundational for arcs in Loom"*

### 1.6 Resolution patterns and relationship maps

Five resolution types: `A` Vulnerability (romance arcs) · `B` Alignment (action and team
building) · `C` **Sacrifice — "used for big trilogy beats (Baz's death)"** · `D`
Structural Shift — *"the Veil mending is this type"* · `E` Grief — *"Lacuna's specialty"*.

Five relationship conflict maps are given (Lucien↔Seraphine, Caro↔Elisabet, Kade↔Lacuna,
Kade→Tahl one-directional, and a Seraphine↔Lucien↔Caro **Tri-Anchor Conflict** where
emotional misfires destabilize resonance). These overlap
`ROMANCE_RELATIONSHIP_RECONCILIATION_2026-09-19.md` and agree with it: Kade↔Lacuna is
marked *"no romance → emotional teaching conflict arcs"*.

### 1.7 Character vulnerability triggers — **including Silence and Hope**

A ten-entry compressed list. Eight are the core cast. The last two matter for work-queue
item 9b:

- **Silence** — paradox loops, emotional noise
- **Hope** — emotional overload, compassion fractures

`M5` adds *"Silence paradox loops, Hope overload, VT instability"*. **This is the first
located source that characterizes Silence and Hope mechanically** rather than naming them.
It is thin — two lines — but it is not nothing, and §22 recorded the exports as holding
essentially nothing on them. Recorded for 9b; Notion `08.10` and `08.11` remain the
primary targets.

### 1.8 The scene-brief bento

Nine fields, and this is the closest thing recovered to a grid schema for conflict:

`Conflict Tier (0–5)` · `Conflict Mode (M1–M5)` · `Emotional Wound Triggered` ·
`Stakes (internal/external)` · `Desired Outcome (what POV wants)` ·
`Escalation Path (C0–C3)` · `De-escalation Path` · `Resonance Behavior (sync/misfire/spike)`
· `Repair Beat Needed (yes/no)`.

Note the bento asks for **Tier and C-path separately**, which confirms §1.2 and §1.4 are
two axes rather than one scale written twice.

---

## 2. `COMBAT SKILL TREES (INTEGRATED)` — Part I, seven characters

Stated purpose: define how each core character fights in alignment with resonant physics
(boosts, scaling, limitations), emotional arcs (fear → control → mastery), environmental
realities (Neon → Loom) and **opponent archetypes**.

### 2.1 The six-tier schema is UARS, not a progression

Despite the name, the tiers are **categories**, not levels:

| Tier | Category | Era tag |
| --- | --- | --- |
| 1 | Native skill / baseline | Veil |
| 2 | Emotional catalysts | — |
| 3 | **Resonance augmentation** | Neon |
| 4 | Tactical application | — |
| 5 | **Failure modes** | — |
| 6 | Mastery path | Loom → Ascension |

Tiers 3 and 5 map directly onto the `Phase 1A` UARS inventory's *boost taxonomy* and
*failure modes*. Tier 4 always resolves against the same three-way opponent taxonomy:
**against humans · against splinter resonants · against metas.**

### 2.2 The seven, in brief

| Character | Epithet | Style | Named analogy |
| --- | --- | --- | --- |
| Seraphine | **"The Luminous Thread"** | defensive filtration → emotional diffusion → precision de-escalation | breath fighter; Tai Chi + Aikido redirection |
| Lucien | "The Shadow Thread" | precision containment → structured takedowns | Krav Maga + Jujitsu + resonance compression |
| Caro | "The Hope Thread" | emotional ignition → explosive close-range | Muay Thai + street brawler |
| Elisabet | "The Clarity Thread" | pattern recognition → timing → psychological deflection | Aikido + Icelandic grounding |
| Rex | "The Rational Thread" | tech-assisted → precision movement → structural exploitation | Systema + engineer's mind |
| Kade | "The Wild Thread" | emotional ferocity → unpredictable burst aggression | street brawl + capoeira chaos |
| Lacuna | "The Soul Thread" | rhythm-based modulation → grief-tone harmonics | ritual aikido + sound redirection |

**Non-violence is built in.** Elisabet's tactical line against humans is *"nonviolent
neutralization"*; Lacuna's is *"nonviolent de-escalation"*; Seraphine *"turns aggression
into exhaustion"*. Only Rex carries *"weapon proficiency high"*. This is a combat system
whose defaults are de-escalation, which is consistent with the Conflict Engine's principles
and with `no supernatural villains`.

**Tier 6 corroborates the Mending.** Lucien's mastery is *"Silence Reborn → redefines
resonance geometry"* and Caro's is *"Hope Reborn → calibrates battlefield emotional
field"* — independently consistent with `B09.A3.E14`'s *"Silence dissolves into Lucien.
Hope dissolves into Caro."*

---

## 3. CONFLICT — two protagonist surnames disagree with Tier-1 canon

| Notion combat trees | Repository Tier-1 canon | Canon files carrying it |
| --- | --- | --- |
| **Caro Gauthier** | **Carolina "Caro" Alvarez** (`CaroID.md`) | 5 |
| **Kade Rios** | **Kade Harper** (`KadeID.md`) | 5 |

`Gauthier` appears **zero** times in `canon/`; `Rios` appears zero times in `canon/`.
Seraphine Vael, Lucien Kael, Elisabet Arnardóttir and Rex Tan all agree across both.

Under `CLAUDE.md` §5 the repository is tier C and Notion is tier D, and under ND-045 the
later explicit decision wins — but these Notion pages are 2025-12-01 and the GitHub
migration is later still. **Recorded, not resolved.** This belongs with the parallel
session's `CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md`, which is the right instrument
for identity decisions; it does not currently cover Caro or Kade.

## 4. CONFLICT — "The Luminous Thread" is Seraphine's combat epithet too

The skill tree titles Seraphine **"THE LUMINOUS THREAD"**. Ledger §24 recorded `LT` as
having three referents — Seraphine's ascended identity, the resonance state, and Kade's
renamed network — and `B09_ENDGAME` §10 ruled for recovery purposes that *Luminous Thread
is post-Mending only*.

This page uses it as Seraphine's **Veil-era through Loom** epithet, in a document where
every one of the seven carries a matching "… Thread" title. So the seven epithets are a
**character-archetype naming scheme**, not channel references — which is probably the
origin of the whole conflation. Recorded as evidence for the held `LT` question; it does
not resolve it.

## 5. What was not recovered

- **Part II.** The skill trees are labelled *"Part I — Core Seven Characters"*. A Part II
  almost certainly covers antagonists or secondary cast. Not located; a search target.
- **`OPPONENT ARCHETYPES & CHARACTER RESPONSES`** (2025-11-25) and **`RES0NANT COMBAT
  BENTO v1`** (2025-11-26) were identified but not fetched in this pass. The opponent
  taxonomy referenced throughout Tier 4 lives there.
- **`HUMOR & CONFLICT BENTO`** (2025-11-26) carries a second conflict ladder that needs
  cross-checking against §1.4 — two ladders may or may not be the same one.

## 6. For the author

1. **Caro's and Kade's surnames** (§3) — Alvarez/Harper as canon holds, or Gauthier/Rios?
2. **Does the Conflict Engine's two-axis model (Tier 0–5 plus C0–C5) stand**, or collapse
   into one? The bento treats them as two; they read as near-duplicates at the extremes.
3. **Do the seven "… Thread" epithets stay** (§4), given they are the likely source of the
   `Luminous Thread` conflation?
4. **Is the Conflict Engine's `Tier 0–5` the same scale** as `reader_pressure.csv`'s
   `intensity_1_5` and the milestone load's `pressure_before`/`pressure_after`? They may
   be three unrelated 1–5 scales, which would be worth knowing before any of them is
   loaded.

END OF DOCUMENT
