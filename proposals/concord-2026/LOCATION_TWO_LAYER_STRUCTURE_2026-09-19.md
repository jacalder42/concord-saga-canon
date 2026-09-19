# Location Structure — Two Layers

**Status:** STRUCTURE RULED / ALL CONTENTS PROVISIONAL / NOTHING IN THE CANON SUBSTRATE
**Date:** 2026-09-19
**Authority:** `recovery/GATE_RULINGS_2026-09-19.md` Rulings 1 and 2
**Companion data:** `proposals/concord-2026/location_places_PROVISIONAL_2026-09-19.csv`

> Ruling 1: *"The **structure** is ruled; the **contents** are provisional."*

---

## 1. The two layers

| | **Type layer** | **Name layer** |
| --- | --- | --- |
| Holds | the **controlled vocabulary** | **named places** — proper nouns for specific ground |
| Source of truth | `HYBRID RESONANCE GEOGRAPHY SYSTEM` | the city bibles |
| Membership | **ruled** | open — new places can be named at any time |
| `ENV` derives from | **this layer, and only this layer** | never |
| Example | `Violet Bloom` | "Violet Spiral", "Red Lantern Faultline" |

**The rule that settles the old conflict:** *"Red Lantern Faultline is a name, not a
type."* A city bible naming ground does not add to, compete with, or override the
vocabulary. That is why the three "rival taxonomies" were never rivals.

### 1.1 The third thing — severity, not geography

The Reykjavík scheme (`Flicker → Ghostwave → Fracture → Rupture Threat`) is the **shard
progression**: a severity scale that **layers over** places. Ruling 1 is explicit that it
**is not a spatial taxonomy and is not to be treated as one**. It does not belong in
either layer above, and it does not contribute to `ENV`.

Practical consequence: Bywater's NOLA-bible entry ("Veil-era Flickers → Ghostwaves") is
**not a competing type assignment**. It is a severity reading of that ground at a point in
time, which is why Bywater is recorded as contested on the geography system's `Amber Drift`
alone rather than as a two-source disagreement.

---

## 2. The type layer — the controlled vocabulary

Ten members, in three groups, taken from the geography system's era model.

### 2.1 Neon Zone types — five

| Token | Type | Behaviour, as the source gives it |
| --- | --- | --- |
| `ZONE_BLUE_PULSE` | Blue Pulse District | clarity hum, calm-before-chaos |
| `ZONE_AMBER_DRIFT` | Amber Drift Zone | emotional panic amplification |
| `ZONE_VIOLET_BLOOM` | Violet Bloom Stripe | near-shard rupture conditions |
| `ZONE_RED_FLARE` | Red Flare Intersection | violence flashpoints |
| `ZONE_SILVER_STATIC` | Silver Static Block | metas disrupt resonance signal |

### 2.2 Loom Corridor classes — four

| Token | Class | As the source gives it |
| --- | --- | --- |
| `CORR_HUMANITARIAN` | Humanitarian | Filament-built; lantern signals, quiet boats, grounded rituals |
| `CORR_CONCORD` | Concord | protagonist routes; emotional stabilizers required |
| `CORR_RUPTURE` | Rupture | extremely dangerous; lead toward shard-cluster fail zones |
| `CORR_GHOSTLINE` | Ghostline | almost silent; emotional emptiness |

**These four are not a safety gradient.** They sort by who built or uses a corridor and
what it leads to. `CORR_RUPTURE` is a corridor *and* extremely dangerous, which is only a
contradiction under the framing Ruling 2 superseded.

### 2.3 Post-Mending — one

| Token | Type | As the source gives it |
| --- | --- | --- |
| `NODE_ECHO` | Echo Node | gentle pools of stabilized resonance at former shard fractures |

### 2.4 One holding token

| Token | Meaning |
| --- | --- |
| `CORR_UNCLASSED` | A named Loom corridor whose **class the source does not state.** Nine of the eleven recovered corridors are in this position |

`CORR_UNCLASSED` is bookkeeping, not a class. It exists so a known corridor can be
recorded without inventing which of the four it belongs to. It resolves to one of §2.2
during the vetting pass, or the author adds a class.

### 2.5 On the token spellings

**The membership of this vocabulary is ruled; the token spellings are mechanical.** The
geography system supplies names, not codes, and a CSV field needs a code. These were
derived by a fixed rule — group prefix plus the source's own colour or class word — and
**no token carries meaning the source did not already state.**

If the author prefers different spellings, changing them is a find-and-replace across two
`proposals/` files and one `rules/` key. Nothing downstream depends on the letters.

---

## 3. The name layer

31 named places recorded in the companion CSV, across five cities, with four statuses:

| Status | Count | Meaning |
| --- | --- | --- |
| `PROVISIONAL` | 17 | A type is recorded, **preliminary until vetted against narrative and milestones** |
| `UNASSIGNED_NO_TYPE_IN_SOURCE` | 8 | A named place no source assigns a type to. Not contested — simply unmapped |
| `CONTESTED_UNASSIGNED` | 5 | **Deliberately left blank.** Sources disagree, or the ground is named in the ruling as contested |
| `PENDING_GEOMETRY_TEST` | 1 | "Blue Pulse Corridor", awaiting the Ruling 2 test |

**Every row with a non-`PROVISIONAL` status has an empty `mapped_type`.** That is asserted
by a check, not by inspection: contested ground is *unassigned*, never
*provisionally assigned*.

### 3.1 The five contested entries

`Tremé` · `Marigny` · `French Quarter` · `Bywater` — the four the ruling names — plus
**`Red Lantern Faultline`**, which is the NOLA bible's name spanning Tremé → Esplanade →
Marigny. It inherits their contested status: a name cannot be mapped to a type while the
ground it covers is unmapped.

### 3.2 "Blue Pulse Corridor" is held, not decided

Ruling 2's test is about **geometry**, and it is a question *about the referent*:

- linear and connective, running between two known points → the name is correct, it stays;
- a pocket without that connective geometry → it is a zone and "Corridor" comes off.

The recovered extent is *Convention Center → Riverwalk → French Quarter*, which **reads as
linear** — but it terminates in contested ground, and the ruling places this question in
the Ruling 1 vetting pass rather than now. **Recorded as pending; not answered here.**

### 3.3 Two sources, one piece of ground — the shape working

The Warehouse District is the clearest demonstration that the two-layer model resolves
what looked like conflict:

| | |
| --- | --- |
| Type | `ZONE_VIOLET_BLOOM` (geography system) |
| Name | "Violet Spiral" (NOLA bible) |
| Ground | the Warehouse District — Baz's death site |

Recorded at §30 as a near-miss disagreement ("agrees in colour, differs in term"). Under
Ruling 1 there is no disagreement: one type, one name, one place.

---

## 4. What this structure does not do

- **It assigns nothing permanently.** Every type in the CSV is preliminary, including the
  geography system's own, per Ruling 1's qualification.
- **It does not touch the canon substrate.** The ruling's scope note: the zone-type
  vocabulary appears in five files, all under `recovery/` and `proposals/`, and the
  substrate contains none of it. This adds a sixth and a seventh, both under `proposals/`.
- **It renames nothing.** Ruling 2's 13 bare `Corridor` uses in the substrate are correct
  and untouched.
- **It does not settle Vienna, Singapore or Marrakesh.** Those cities appear in the
  geography system's map but have no located city bible, so their name layers are thin.
  Still gated on work-queue item 6.

## 5. What vetting will need to answer

Not author questions — work items for the narrative pass Ruling 1 points at:

1. The four contested neighbourhoods, plus `Red Lantern Faultline` downstream of them.
2. The `Blue Pulse Corridor` geometry test.
3. Nine `CORR_UNCLASSED` corridors, each needing one of the four classes.
4. Eight named places with no type in any source — some may genuinely have none.
5. Whether the 17 `PROVISIONAL` assignments survive contact with narrative and milestones.

END OF DOCUMENT
