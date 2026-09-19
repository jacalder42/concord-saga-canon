# Interim Per-Act Envelope Values — v2, Banded

**Prepared:** 2026-09-19 · **Supersedes** the ceiling-only v1 of the same date.

**Two rulings applied since v1:**

- **`FX2` in Book 1 Act I is correct** — "start with a bang." So
  `trilogy_context_T1_veil.json`'s `default_vfx_ceiling: FX1` is the thing that is
  wrong, and Veil's FX ceiling rises to `FX2`. The recovered E16 packet stands
  unamended.
- **Bands replace ceilings**, on every axis, in every act — not only in Loom.

Everything below the two rulings is still inferred. **[observed]** marks a value
anchored in a recovered packet; everything else is interpolated from the act function
and the escalation curve.

---

## 1. Why bands, and why everywhere

v1 found that a ceiling alone misdescribes an act in both directions. `B3.A3` sits at
`U1` for eleven of eighteen episodes and touches `U5`/`W4` once — a ceiling of `W4`
there would licence eighteen landfalls. And in Loom every act pinned to the same
`U6`/`W4`/`FX3` ceiling, so the ceiling stopped discriminating between them.

Both are the same defect. What distinguishes an act is not how high it may go but
**the band it lives in** — Loom's signature is that calm stops being available, which
a ceiling cannot express at all.

Applying bands only to Loom would have left three different schemas across the 27
acts. One shape everywhere is cheaper to validate and easier to read.

### Proposed schema, per act

```json
"escalation_permissions": {
  "corridor": { "min": "U3", "max": "U6" },
  "weather":  { "min": "W2", "max": "W4" },
  "fx":       { "min": "FX2", "max": "FX3" },
  "exceptions": [
    { "sid": "S1.T1.B03.A3.E14", "axis": "weather", "value": "W4",
      "scope": "brief", "reason": "First and only VT brush in the Veil trilogy" }
  ]
}
```

**One exception mechanism, both directions.** A sanctioned spike above `max` and a
sanctioned dip below `min` use the same list. `E14` is the first entry; Loom's rare
quiet episode will be the second. `scope: "brief"` carries the duration bound your own
`W4 (brief)` was already reaching for.

**The floor is the ambient world, not the scene.** An act's `min` describes what the
world is doing, so a sheltered interior inside a Loom storm is a dip that needs an
exception entry — which is the point: those moments should be deliberate and countable,
not incidental.

---

## 2. VEIL — subtle, low amplitude, early shard precursors

FX ceiling now `FX2` trilogy-wide per the ruling above.

| Act | Function | Corridor | Weather | FX | Basis |
| --- | --- | --- | --- | --- | --- |
| B01.A1 | Denial | `U1`–`U4` | `W0`–`W2` | `FX0`–`FX2` | **[observed]** E16 at U3→U4, W1, FX2 |
| B01.A2 | Discovery | `U1`–`U4` | `W0`–`W2` | `FX0`–`FX2` | **[observed]** E17/E18 at U2→U3, W1, FX1 |
| B01.A3 | Fracture (small) | `U1`–`U5` | `W0`–`W2` | `FX0`–`FX2` | [inferred] |
| B02.A1 | Controlled discovery | `U1`–`U4` | `W0`–`W2` | `FX0`–`FX2` | [inferred] |
| B02.A2 | Institutional friction | `U1`–`U4` | `W0`–`W2` | `FX0`–`FX2` | [inferred] friction is civic |
| B02.A3 | Civic fracture | `U1`–`U5` | `W0`–`W3` | `FX0`–`FX2` | [inferred] first gale |
| B03.A1 | Shard escalation | `U1`–`U5` | `W0`–`W3` | `FX1`–`FX2` | [inferred] **FX floor rises** — flickers become constant |
| B03.A2 | Emotional collapse | `U1`–`U5` | `W0`–`W3` | `FX1`–`FX2` | [inferred] |
| B03.A3 | First rupture | `U1`–`U5` | `W0`–`W3` | `FX1`–`FX2` | **[observed]** floor U1/W0 at E15–E18; peak U4/W3 at E13; **`W4` exception at E14** |

Veil keeps a floor of `U1`/`W0` throughout: the world is still normal most of the time,
which is what "institutional suppression" means.

---

## 3. NEON — fracture increases, shards emerge, cost curves steepen

The Neon signature is the **floor leaving `U1`**. Normal stops being available before
catastrophe becomes common.

| Act | Function | Corridor | Weather | FX | Basis |
| --- | --- | --- | --- | --- | --- |
| B04.A1 | Civic polarization | `U2`–`U5` | `W1`–`W2` | `FX1`–`FX2` | [inferred] **floor leaves U1/W0** |
| B04.A2 | Firestorm politics | `U2`–`U5` | `W1`–`W3` | `FX1`–`FX2` | [inferred] |
| B04.A3 | Riot of Light | `U2`–`U5` | `W1`–`W3` | `FX2`–`FX3` | [inferred] first `FX3` |
| B05.A1 | Public panic | `U2`–`U5` | `W1`–`W3` | `FX2`–`FX3` | [inferred] |
| B05.A2 | Metas destabilize | `U3`–`U6` | `W1`–`W3` | `FX2`–`FX3` | [inferred] **first `U6`** — destabilization is shard-laced by definition |
| B05.A3 | Harmonic Storm | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] **first unexceptional `W4`**; the act is named for it |
| B06.A1 | Desperation | `U3`–`U6` | `W2`–`W3` | `FX2`–`FX3` | [inferred] |
| B06.A2 | Tahl's death | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] the saga's pivot |
| B06.A3 | Global chaos | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] |

---

## 4. LOOM — corrected

This is what the ruling changes. In v1 all nine acts read `U6`/`W4`/`FX3` and were
indistinguishable. Banded, the acts separate — and they separate **on the floor**,
which is what "corridor failures widespread" and "storms turn to climate" actually
describe.

| Act | Function | Corridor | Weather | FX | Basis |
| --- | --- | --- | --- | --- | --- |
| B07.A1 | Collapse begins | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] continuous with Neon's end |
| B07.A2 | Diaspora fragmentation | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] movement across varied ground |
| B07.A3 | Resonance weather | `U4`–`U6` | `W3`–`W4` | `FX2`–`FX3` | [inferred] **storms become climate** — floor reaches gale |
| B08.A1 | Near-darkness | `U4`–`U6` | `W3`–`W4` | `FX3`–`FX3` | [inferred] the nadir; FX pinned |
| B08.A2 | Emotional reckoning | `U3`–`U6` | `W2`–`W4` | `FX2`–`FX3` | [inferred] **floor deliberately drops** — an interior act needs room for human scale |
| B08.A3 | Approaching the swamp | `U4`–`U6` | `W3`–`W4` | `FX2`–`FX3` | [inferred] convergence; floor rises again |
| B09.A1 | Cataclysm | `U5`–`U6` | `W3`–`W4` | `FX3`–`FX3` | [inferred] the highest floor in the saga |
| B09.A2 | Ascension | `U5`–`U6` | `W3`–`W4` | `FX3`–`FX3` | [inferred] |
| B09.A3 | Breathable Veil | see §5 | see §5 | see §5 | [inferred] era boundary |

Three things the bands now say that the ceilings could not:

- **B07.A3 is where weather stops being weather.** Its floor is `W3` — gale as the
  resting state. That is the act named "resonance weather" earning its name.
- **B08.A2 dips on purpose.** "Emotional reckoning" is an interior act, and a floor of
  `U4` would make an intimate scene illegal. Dropping the floor to `U3` is a deliberate
  trough in the middle of the trilogy's worst stretch, which is also where the story
  can breathe.
- **B09.A1 has the highest floor in the saga** at `U5`/`W3`. Nothing calm happens in
  the cataclysm — which a ceiling of `U6` never expressed, since `U6` was also Book 7's
  ceiling.

---

## 5. B09.A3 and the era boundary

The Mending happens inside this act, so it spans two eras. Recommended: **split the act
at the Mending beat** rather than give one act two bands.

| Portion | Corridor | Weather | FX | Governed by |
| --- | --- | --- | --- | --- |
| B09.A3 pre-Mending | `U5`–`U6` | `W3`–`W4` | `FX3` | Loom |
| B09.A3 post-Mending | `U1`–`U7` | `W0`–`W1` | `FX0`–`FX1` | Post-Mending era file |
| Epilogue — MT reborn | `U1`–`U7` | `W0`–`W1` | `FX0`–`FX1` | Post-Mending era file |

The split is cleaner than dual bands because the validator can then check each portion
against one envelope instead of deciding which half an episode belongs to.

---

## 6. Post-Mending envelope — new file

`rules/era_context_post_mending.json`. `Mechanica-v4.md` §7.4 defines this era and
nothing holds it; `U7` and `NODE` belong here.

| Field | Value | Basis |
| --- | --- | --- |
| `corridor` | `U1`–`U7` | §25: U7 is Post-Mending clarity |
| `weather` | `W0`–`W1` | escalation curve: "breath-like oscillation" |
| `fx` | `FX0`–`FX1` | [inferred] "color signatures soften" |
| `res_states_permitted` | `CALM` · `BLOOM` · `NODE` | §7.4: no new shards or ruptures — `SHARD` and `RUPTURE` are **forbidden**, not merely unlikely |
| `escalation` | none permitted | §25 U7, verbatim |
| `exceptions` | none | escalation is prohibited, so the mechanism does not apply here |

The forbidding of `SHARD` and `RUPTURE` is an exclusion, not a ceiling. The schema
cannot express it today — it bounds values but never removes a permitted token from an
era. That is a validator addition, not just a data entry.

---

## 7. Checked against the recovered packets

Every corridor, weather and FX value in the 22 recovered episodes falls inside its
act's band, with exactly one exception: `B3.A3.E14`'s `W4`, which is the sanctioned
entry in §1's exceptions list. Nothing else needs an exception, and nothing already
written falls outside its own envelope.

---

## 8. Still open

1. **`allowed_heat_range` comes out of the envelope files.** Flat `H0`–`H4` is correct
   — `HEAT` is the romance ladder and does not escalate with a metaphysical crisis —
   but it reads as an oversight sitting beside real bands. Recommended removal; your
   call.
2. **The act overlay schema needs the `escalation_permissions` block.** The nine book
   contexts have one; the 27 act overlays do not. Nothing here can land until it exists.
3. **What the nine book contexts hold now.** With bands at act level, book-level
   `escalation_permissions` is either derived (the union of its three acts) or removed.
   Derived is safer — it keeps a book-level view without a second place to edit.
4. **Confirm B08.A2's deliberate dip.** It is the one place I lowered a floor against
   the trilogy's direction, on the reasoning that an interior act needs human scale. If
   the reckoning happens in the storm rather than beside it, that floor goes back to
   `U4`.
5. The 18 Neon and Loom acts remain inferred from act titles. They are placeholders
   that let the validator run, not proposals about the story.
