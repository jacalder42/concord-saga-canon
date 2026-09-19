# Locations, Combat, Antagonists — Primer Review Before Consolidation

**Status:** RECOVERY REVIEW / NOTHING CONSOLIDATED / NOTHING BUILT
**Date:** 2026-09-19
**Direction:** James, 2026-09-19 — locations and combat *"should have a lot of primer
material in notion, chat exports, and maybe early git materials. Those should be reviewed
prior to acting or consolidating."* On antagonists: *"primary antagonists are treated
similar to protagonists (i believe this system already exists or was begun) and antagonist
groups can operate at a pressure curve model."*

**Headline: the instinct was right on all three, and understated on two.** Locations and
combat are not gaps in the *project* — they are complete, CANON-marked systems in Notion
that never migrated to GitHub. The antagonist parity system does exist, and is **further
along than the protagonists'**.

---

## 1. Locations — a full canon system exists; the repository has none of it

### 1.1 `HYBRID RESONANCE GEOGRAPHY SYSTEM — CANON` (Notion, 2025-11-27)

Subtitled *Neon Zones → Loom Corridors (Evolution Model)*. Nine sections. This is the
location **system**, and it is built on the same spine as everything else:

> Resonance geography = emotional topography + civic stress + metaphysical pressure.

**It evolves per trilogy**, which is why no single static location list would have worked:

| Era | Geographic form |
| --- | --- |
| Veil | shards as Ghostwaves, Flickers, micro-fractures |
| Neon | **Neon Zones** — urban resonance bloom districts |
| Loom | **Loom Corridors** — unstable travel paths defined by emotional pressure |
| Post-Mending | **Echo Nodes** — gentle pools of stabilized resonance |

**Five Neon Zone types:** Blue Pulse (clarity hum) · Amber Drift (panic amplification) ·
Violet Bloom (near-rupture) · **Red Flare (violence flashpoints)** · Silver Static (metas
disrupt signal).

**Four Loom Corridor classes:** Humanitarian (Filament-built) · Concord (protagonist
routes, emotional stabilizers required) · Rupture (lead to shard-cluster fail zones) ·
Ghostline (emotional emptiness, hints at Hope's fraying modulation).

**A city-by-city geo-map** for New Orleans (five zone assignments plus three named Loom
corridors), Vienna, Singapore, Reykjavík and Marrakesh.

### 1.2 It already makes the distinction James raised

The narrative-location versus character-location split is **built into the document**:

- **§V City-by-City Geo-Map** is the narrative-location layer — places with resonance
  properties, naming conventions and narrative function.
- **§VIII Character Interaction Rules** is the character layer — what each character does
  *in* geography: Seraphine senses harmonic distortion first; Lucien identifies structural
  weakness in corridor geometry; Rex calculates safest routes inside corridor edges; Kade
  **destabilizes** Amber Drift zones; Lacuna hums a corridor calm; Tahl's Echo flickers at
  corridor pinch points.

So the answer to shape-question 1 is **not a design choice to be made** — it is a recovery
to be performed. The system says: one place layer, plus a character-interaction layer that
references it.

### 1.3 Two consequences worth flagging now

**It connects to the Warehouse Incident.** The New Orleans map reads
*"Violet Bloom: Warehouse District (Baz's death site)"* — and Violet Bloom is defined as
*near-shard rupture conditions*. That independently corroborates the Warehouse Incident as
a resonance-rupture event, which is what `BAZ_WAREHOUSE_INCIDENT_RECOVERY` concluded from
different evidence.

**It collides with the ECID on the word "Corridor".** `canon_rules.json` uses `CORRIDOR`
as an ECID field with vocabulary `U1`–`U7`, and Mechanica §24–25 defines Corridor Tiers as
resonance-intensity bands. The geography system uses **Corridor** for named Loom travel
routes with four classes. These are different objects sharing a token, exactly like the
`VT` collision recorded at `SUPPLEMENT_VEHICLES.md` §2. **Do not merge them and do not
rename either before James rules** — flagged, not resolved.

### 1.4 Other location canon located

- **`CONCORD SAGA — NEW ORLEANS CITY BIBLE (FINAL CANON)`** (2025-12-01) — *"defines New
  Orleans across all trilogies: geography, culture, resonance weather, shard history,
  civic fracture, Filaments, tech instability"*, at neighborhood granularity (Tremé and
  others). The newest location artifact.
- **`REYKJAVÍK — QUIET RESONANCE ZONE (Deep-Pass v1)`** (2025-11-27) — a second city
  bible, era-by-era.

**Both are in Notion's `- 05 • Canon Bibles`.** A "Deep-Pass v1" suffix on one city implies
the city-bible pass was a program, not a one-off, so more may exist unsearched.

---

## 2. Combat — also a full canon system, and the repo has one section of it

### 2.1 What the repository has

Exactly two things:

- **`rules/Mechanica-v4.md` §57 SCENE-TYPE APPLICATION**, which includes an
  **Action / Conflict** scene type: rising cost curves, environmental damage, failure risk
  escalating visibly.
- **`rules/resonance/EMOTIONAL_MODES_AND_INSTABILITY.md:207`**, an unticked checkbox:
  `[ ] Optional: add civic vs combat emotional profiles`.

That is the entire combat presence in the substrate — 3 canon mentions, 1 in `rules/`, 0 in
`grids/`.

### 2.2 What Notion has

| Page | Dated | What it is |
| --- | --- | --- |
| `CONCORD SAGA — CONFLICT ENGINE (v1.0)` | 2025-12-01 | The conflict system. Rules include: conflict must always have cost; must escalate when emotions spike; must **soften when resonance aligns** |
| `CONCORD SAGA — COMBAT SKILL TREES (INTEGRATED)` Part I — Core Seven Characters | 2025-12-01 | Per-character combat styles with tiers, e.g. Rex: *"Tech-assisted combat → precision movement → structural exploitation"*, TIER 1 Baseline (Veil) |
| `OPPONENT ARCHETYPES & CHARACTER RESPONSES` — *Resonant Combat System Module* | 2025-11-25 | Opponent taxonomy, incl. very-high-output/very-short-duration archetypes |
| `RES0NANT COMBAT BENTO v1` | 2025-11-26 | Scene-construction tool: pattern-threading, momentum amp, emotional destabilization, micro-tells |
| `HUMOR & CONFLICT BENTO — CONCORD SAGA CANON` | 2025-11-26 | Contains a **Conflict Ladder (tension scale)** |
| `Character Engine Canon - Compact Bento` | 2025-12-01 | **§VIII COMBAT / ACTION TRANSLATION**; *"CHARACTER ENGINE BENTO v3 — Unified Action–Resonance System (UARS)"* |

There is a whole Notion folder, **`Resonance Mastery Mechanics`**, holding most of it.

### 2.3 The shape question is already answered by the sources

The `Phase 1A Migration Plan` export enumerates what must exist in GitHub as authoritative
canon, and places combat **inside** section 2, *UARS action economy and cost model*:

> Action permissions by corridor/weather (what is "possible" in U1 vs U6; W0 vs W4).
> **Combat vs non-combat (how UARS expresses differently in action scenes vs civic scenes
> vs intimacy).**

So combat is **a mode of UARS expression, not a separate axis** — the opposite of the
`LOAD` case, where a genuinely missing dimension needed its own field. Mechanica §57
already implements the scene-type half of this. What is missing is the UARS-differential
detail, the conflict ladder, the opponent archetypes and the per-character skill trees.

**That means combat needs no new schema.** It needs migration into the existing
UARS/scene-type structure.

---

## 3. Antagonists — confirmed, and the parity is better than expected

### 3.1 Primary antagonists already have full protagonist treatment

James's recollection is correct. Counting files in `canon/characters/`:

| Character | Files | Pattern | POV file |
| --- | --- | --- | --- |
| Saeko | **5** | ID · EBCI · Appearance · Render · **Backstory** | `SaekoPOV.md` |
| Ito | **5** | ID · EBCI · Appearance · Render · **Backstory** | `ItoPOV.md` |
| Han Wei | **5** | ID · EBCI · Appearance · Render · **Backstory** | `HanWeiPOV.md` |
| Elias | 4 | ID · EBCI · Appearance · Render | `elias_ward_pov.md` |
| Virelli | 4 | ID · EBCI · Appearance · Render | `VirelliPOV.md` |

Every protagonist carries exactly four. **Three antagonists carry five** — a `Backstory`
file no protagonist has. The antagonist layer is not merely at parity; it is the more
developed of the two.

### 3.2 The gap is on the protagonist side, and it is the lead

**Seraphine has three files and no EBCI**: `SeraphineAppearance.md`,
`SeraphineIdentity.md`, `SeraphineRender.md`. She is the only main character without an
`*EBCI.md`, and the only one whose identity file breaks the `*ID.md` convention.

That is striking given `source_canon/characters/seraphine_full.md` is 830 lines stamped
`FINAL CANON · LOSSLESS · EXPORT READY` — the material exists and is blocked behind the
unresolved `source_canon/` authority conflict (`CLAUDE.md` §1.1, work-queue item 9).

### 3.3 Group pressure-curve — the template exists, and so does the curve

**A group template already exists**, used for two factions and not the others:

| Faction | Treatment |
| --- | --- |
| Concord | directory, 5 files — EraFunction · Limits · Mandate · Relationships · Structure |
| Filaments | directory, 6 files — Aesthetics · CanonLocks · EraFunction · Origin · Relationships · Structure |
| Technarc, Dominions, Choirless, Brightbreak, Manufactured Metas | **single files** |

`EraFunction` is the pressure-curve field in everything but name — it is what a faction
*does per era*. Extending the directory pattern to the antagonist factions is the concrete
form of James's proposal, and it is an existing convention rather than a new one.

**The saga-level curve is already written**, in `_ Narrative Structure _` :

> **4. Antagonist Evolution (Saga-wide)** — Veil: secretive, institutional antagonism.
> Neon: splinter groups, weaponized tech, fear populism. Loom: global panic and
> collapse-level human conflict.

And per-faction curves exist in the `Saga Beat Expansion Pipeline` audit, e.g.:

> Choirless: Whispered ideology in Neon 4 → traction in Neon 5 → violence in Neon 6 →
> full militant splinter in Loom.

Plus `Technarch Hardliners` pressure around Santa Fe, and Manufactured Metas confined to
Neon 6 failures. **So the pressure-curve model does not need inventing — it needs
extracting into the faction files and binding to `episode_beats.csv`'s existing
`antagonist_pressure` column.**

`canon/factions/` is also the layer where Notion's `05.07 • Antagonist Architecture Bible`
and ND-020–ND-029 belong.

---

## 4. Early git materials — nothing was lost

Checked the full history with `--diff-filter=A` and `--diff-filter=D` across all refs:

- **No location, geography, environment, combat or action file has ever existed** in the
  repository.
- Only two files have ever been deleted: a superseded unsplit export HTML, and a stray
  `.pyc`.

So "early git materials" is a dead end for these two subjects — not because something was
removed, but because it was never migrated. The repository began with character and faction
files (the earliest commits are `Create ItoPOV.md`, `Create SaekoID.md`, `Create
Choirless.md`), and the systems layer arrived later and partially.

---

## 5. Incidental finding — 14 advisory groups, none of them migrated

`Character involvement pacing__part02` contains the **Project Model Set**, described as
*"a clean, authoritative list … ONLY what is actually saved."* Five items. The repository
has captured item 1 and part of item 2.

**Item 3 — Advisory Groups (Core, Canon), saved 2025-11-16, "part of the living canon":**
Art Direction Council · Continuity Wardens · Humanity Pass Council · Paratext Architecture
Board · Breadcrumb / Foreshadowing Weavers · **Action Realism Board** *(grounded conflict,
violence realism, physical logic)* · **Environmental Texture Board** *(ensures each
location maintains distinct sensory/cultural identity)* · Serial Release Calibration Team.

**Item 4 — Advisory Groups (Provisional / Pending Review):** Visual Effects / Cinematic
Imagery Panel · Resonant Tech Calibration Review · Emotional Authenticity Advisory ·
Mystery/Conspiracy Calibration Circle · Narrative Soundtrack Council · **Geography &
Location Logic Panel**.

**All fourteen are absent from the substrate** — verified against `canon/`, `rules/`,
`grids/`, `book_context/` and `act_overlays/`.

This matters for the two subjects under review: **locations and combat each already have a
governance body in canon**, and locations have a second one pending. `canon/editorial_lenses.md`
holds only the Editorial Board, Secondary Consultants, Reader Archetype Panel and
Publication Advisory Group — i.e. item 1. The topical boards were never brought over.

Item 5 also names an unresolved question to preserve: *"Filaments Call Sign 'K' Question —
a topic to revisit later; not yet resolved."*

---

## 6. Incidental finding — the December memory exports are the newest canon index

Two Notion pages postdate everything else reviewed in this project:

- **`25.12.06 Memory List`** (2025-12-06) — names ActionState routing
  (Baseline→Rupture→Proto-Ascendant), UARS, corridor + weather symbolism, resonance-state
  rules, Beat-to-Action output.
- **`Memory Set 25-1212`** (2025-12-13), in a distinct `Concord Saga 25-1212 Export`
  folder — resonance physics, UARS action system, corridor ecology, environmental
  modifiers, resonance weather, the RP equation and the >20% boost rule.

Everything else surveyed is 2025-11-23 to 2025-12-01. Under ND-045's rule that later
explicit material outranks earlier "Final Canon" labels, **these two are the best available
index of what the project's canon state actually was at the end**, and should be read
before any consolidation pass. They were not among the 21 sanitized exports.

---

## 7. What this changes about the build priorities

`NARRATIVE_BUILD_PRIORITIES_2026-09-19.md` listed locations, combat and antagonist arcs as
three layers that "do not exist" and needed author direction on shape. **That was true of
the repository and false of the project.** Revised:

| Layer | Earlier assessment | Actual |
| --- | --- | --- |
| Locations | absent, needs shape decision | **Full canon system in Notion.** Recovery + collision ruling, not design |
| Combat | absent, needs shape decision | **Full canon system in Notion.** Migration into existing UARS/scene-type structure; no new schema |
| Antagonist arcs | material without structure | **Template and curves both exist.** Extend the faction directory pattern; bind to `antagonist_pressure` |

**None of the three needs a design proposal. All three need a recovery pass**, and the
locations pass should run before the `ENV` vocabulary is defined, because the geography
system supplies it.

## 8. Open questions this review produced

1. **The `Corridor` token collision** (§1.3) — Loom travel routes versus ECID `CORRIDOR`
   `U1`–`U7`. Same word, two objects. Needs a ruling before either is migrated.
2. **Are the 8 canon advisory groups still canon** (§5), and do the 6 provisional ones get
   ratified? The Action Realism and Environmental Texture boards govern exactly the two
   subjects under review.
3. **Seraphine's missing `EBCI` and nonstandard `Identity` filename** (§3.2) — is this an
   oversight to fix, or is `SeraphineIdentity.md` deliberate? It is entangled with the
   `source_canon/` authority conflict.
4. **Should the December memory exports be treated as the canon-state index** for the
   extraction pass (§6)?
5. **The `Filaments Call Sign "K"` question**, recorded as explicitly unresolved (§5).

END OF DOCUMENT
