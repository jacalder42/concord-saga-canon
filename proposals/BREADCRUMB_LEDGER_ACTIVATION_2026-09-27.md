# Breadcrumb ledger — activation

**Date:** 2026-09-27
**Status:** PROPOSAL / WORKING LEDGER NOTE — NON-CANONICAL. It records how `grids/breadcrumbs.csv`
went live and how it is kept, under the author's instruction
(`decisions/PROGRESSIVE_RESOLUTION_SEQUENCE_AUTHOR_INSTRUCTION_2026-09-27.md` item 3).

**What it does not change:** no ruling, grid row status, card or rule text. A breadcrumb row
records what architecture already plants; **it never promotes a plant or a payoff.** The B01 EBCI
hold stands.

---

## 1. What the ledger is for

A breadcrumb is **a plant with a named payoff**. The ledger records the plant's function, where
architecture currently places it, and **how firmly its payoff is fixed**, so that later work
(Neon and Loom architecture, the nine-book audit, Veil EBCI, prose) can see what depends on what.

**A breadcrumb's identity is its function and its payoff, not an episode.** The SID columns are
locators. When an episode moves, the row's locator changes and its id does not.

## 2. Schema

The first nine columns are the original header. **Three were appended** while the file had no
rows, so nothing was lost: `payoff_dependency`, `payoff_function`, `payoff_locator`. The schema is
declared in `rules/canon_rules.json` `breadcrumb_grid` and checked by
`tools/validate_canon.py` **CHK_BREADCRUMB_GRID** (structure only), with nine self-tests.

| Column | Holds |
| --- | --- |
| `breadcrumb_id` | `BC-` plus a function slug. Never an episode number |
| `type` | `plant` · `seed` (hidden or unexplained) · `ladder` (graduated reinforcement) · `mobius` (a return or inversion) · `callback` |
| `what_is_hinted` | The plant's function, in a phrase. No prose |
| `introduced_in_SID` | Locator of the first plant. A supplement is located at the episode it follows, and named in `notes` |
| `reinforced_in_SIDs` | Locators, `; `-separated |
| `payoff_milestone_id` | The grid row it pays off, if one exists |
| `visibility_level` | `hidden` · `subtle` · `legible` · `overt` |
| `status` | The **plant's** state: `placed` (approved architecture), `provisional` (Neon or Loom architecture), `unplaced` (a payoff needs a plant nothing carries yet), `retired` |
| `notes` | Authority for plant and payoff; guardrails; gaps |
| `payoff_dependency` | **LOCKED** · **SOFT** · **PROVISIONAL** (§3) |
| `payoff_function` | What the payoff does. **Required**: a plant without one is an orphan |
| `payoff_locator` | Book and act of the payoff (a locator, not a SID) |

## 3. The dependency classes, and how to plant against them

| Class | The payoff is | Plant | The check enforces |
| --- | --- | --- | --- |
| **LOCKED** | **Ruled** | **Precisely.** The payoff will not move | `payoff_milestone_id` names a `ruled` row |
| **SOFT** | **Approved design** | **Polyvalently**: so more than one execution satisfies it | — |
| **PROVISIONAL** | In **provisional episode architecture** | **Directionally.** Upstream continuity must not depend on the exact placement | — |

**The class describes the payoff, not the plant.** A LOCKED payoff can have a plant still under
design (for example `BC-TAHL-SIGNATURE-TRIANGLE`, which is unplaced).

## 4. What was seeded (32 rows)

Seeded from existing Veil plants the architecture itself marks as plants, seeds, ladders or Möbius
returns, and from the known saga payoffs they point at. **Nothing was added to fill the ledger.**

| Payoff lands in | Rows | Dependency |
| --- | --- | --- |
| **The macro-Möbius and Loom** | 10: `BC-MACRO-MOBIUS-SKY`, `BC-TAHL-SIGNATURE-TRIANGLE`, `BC-SILENCE-HOPE-OBSERVE`, `BC-VT-BRUSH-LADDER`, `BC-HONEY-ISLAND-SITE`, `BC-SWAMP-WOUND`, `BC-MIRA-SEED`, `BC-LUCIEN-LISTENING`, `BC-BOUNDED-RESPONSIBILITY`, `BC-LACUNA-CAMEO` | All LOCKED |
| **Neon, or carried into it** | 13: the southwest ladder, the anonymous MT voice, Tahl's own rule, the Dominion ladder, *"I asked him to come here"*, *the person she could not save*, the Warehouse record, Technarc's kit, Caro's over-carrying, known/inferred/unknown, the Caro–Elisabet ladder, Rex's repair ethic, the Filament ethic | 4 LOCKED, 8 SOFT, 1 PROVISIONAL |
| **Inside Veil** | 9: arrive together, Jackson Square, the Velvet Vein room, the remote item, pulse naming, the second-line invitation, the forklift operator, the Warehouse precursor, the chorba and the sister | All SOFT |

### Left out on purpose

- **Short within-book setups** that architecture already carries: the dialysis rider (B02
  E16→E20), Helena's grounds (B02 E08→E23), the interval (B02 E14→E17), the loft party (B03
  E10→E25), the anticipated night (B01 E28→E31), the public acting on uncertain information (B02
  E43→B03). They are scene setups, not saga breadcrumbs.
- **Baz's personhood.** B01–B03's Life/Reward scenes make his loss the loss of a person. **They
  stay ordinary**; treating them as plants would turn Life/Reward into machinery (the author's
  item 5).
- **Mme Rosette** as a *"civic-memory seed"*: she is a recurring person, not a hint.
- **The December "Saga Breadcrumb Layer v1.0"** (ND-001's ten seeds): recorded Tier B in 09-19
  analysis, but never mapped to the current episodes. **The nine-book audit** decides whether any
  of its ten functions still earns a row. One of them, *Lucien's Silence-echo precursors*, has no
  current Veil carrier.
- **Unmarked candidates:** B03 E47's *"the night sky is not quiet"*, and the B03 second line
  against B07's jazz funeral. Both are **candidate nested Möbius** structures. The author's item 4
  keeps nested Möbius open to discovery, so they go to the audit, not the ledger.

## 5. Findings from seeding

1. **`BC-TAHL-SIGNATURE-TRIANGLE` is unplaced, against a LOCKED payoff.** The author's locked
   11-29 design makes a small triangle Tahl's MT signature, and the epilogue's LT prompt shows only
   that triangle (M53: *"his triangle is implied"*). **No Veil or Neon MT post carries it.** It
   needs a plant. The macro-Möbius card (§5 there) puts where for the author.
2. **The southwest ladder's explicit B03 line is unplaced.** v4.1b's lock checksum expects B03 to
   carry an explicit *"everything curves southwest"* stage. B03's passes carry the direction
   (E01, S01, E48) but not that line. **Low severity:** B03 E48's *"a problem, not a visit"* may
   already be the explicit stage. For the nine-book audit.
3. **Tahl's own rule** (B03 E48) had no named payoff. It now points at the Warehouse mirror (he goes
   to Santa Fe in person), which is approved design. It is SOFT and polyvalent: Neon may also test
   the rule before B06.

## 6. How the ledger is kept

- **Neon and Loom passes add rows as `provisional`** when they plant, and update locators when
  episodes move. Every Neon row names the payoff it serves.
- **A row is never deleted.** A plant that stops serving becomes `retired`, with the reason.
- **When a payoff's authority changes** (a proposed row is ruled, or a design is dropped), the
  row's `payoff_dependency` changes with it, and `notes` records the date.
- **Unplaced rows are debts.** The nine-book audit reviews every one.
- **Precision follows the class.** A Veil plant against a SOFT or PROVISIONAL payoff is written so
  more than one execution can satisfy it.
