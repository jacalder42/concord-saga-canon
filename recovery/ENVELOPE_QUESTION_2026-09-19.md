# The Trilogy Envelope Question — Full Statement

**Status:** QUESTION ONLY. No option chosen. This is decisions §8 item 1, reserved to
James.
**Prepared:** 2026-09-19, in answer to *"clarify what the full question is"*.
**Blocks:** work-queue items 4, 5 and 5a — the entire migration path. Nothing else is
waiting on anything.

---

## 1. The question in one sentence

**What rule governs how high resonance conditions may go in a given book or act, now
that the fixed per-trilogy ceilings have been ruled unintended?**

---

## 2. Why it blocks everything

`proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md` instructs that the
`escalation_permissions` fields in each book context —
`max_corridor_tier`, `max_weather`, `max_fx` — "must be cross-derived from Mechanica v4
+ trilogy envelope rules", and should stay `TODO` until systems reconciliation
completes.

Those 27 `TODO` values are the **entire** substrate violation count in
`reports/VALIDATION_BASELINE_2026-09-19.md`. They cannot be filled until this is
answered, and the act overlays that sit beneath them cannot be populated either. That
is items 4 and 5a. Item 5 is blocked separately but by the same fact — see §5.

---

## 3. What is there now, and what §6.2 found wrong with it

`rules/trilogy_context_T{1,2,3}_*.json` carry:

| | `default_vfx_ceiling` | `weather_max` | `corridor_max` | `allowed_heat_range` |
| --- | --- | --- | --- | --- |
| **T1 Veil** | `FX1` | `W3` | `U5` | `H0`–`H4` |
| **T2 Neon** | `FX2` | `W3` | `U5` | `H0`–`H4` |
| **T3 Loom** | `FX3` | `W3` | `U5` | `H0`–`H4` |

Only the FX ceiling escalates. Weather, corridor and heat are identical across all three
trilogies.

Decisions §6.2 ruled this **unintended**, and that values "should be fluid and matched
to narrative momentum". It did not say what replaces it.

**Why the current shape is wrong on its own terms.** `rules/Mechanica-v4.md` §7.3
describes Loom as:

> Systemic collapse · Resonance storms dominate · Corridor failures widespread · Shards
> shape geography

Those are the definitions of the two tiers the envelope forbids. §25 defines `U6` as
*"Shard-Laced — fractures present, severe instability, catastrophic failure likely"*;
§30 defines `W4` as *"Landfall — catastrophic pressure, resonance storms, shards or
rupture-level events likely"*. Loom is described in exactly the vocabulary its own
envelope makes unreachable.

---

## 4. Two things that reframe the question

Both emerged from reading the Mechanica definitions rather than the envelope files, and
both change what a good answer looks like.

### 4.1 `U7` is not an escalation tier — it is Post-Mending, and has no envelope

`Mechanica-v4.md` §25:

> **U7 — Quiet Veil.** Hush and stillness · Post-Mending clarity · Limited access ·
> **No escalation permitted**

`U7` is not "higher than `U6`". It is a different era's condition — the calm after the
Mending, not a peak of the storm. So `U7` being unreachable in Veil, Neon and Loom is
**correct**, not a defect.

But that exposes a real gap: **there is no Post-Mending envelope file.** There are three
`trilogy_context_T*.json` files and `Mechanica-v4.md` §7.4 defines a fourth era, the
Post-Mending world, where the Breathable Veil filters resonance and only Echo Nodes
remain. `U7` and the `NODE` resonance state both belong to it, and nothing holds them.

**So the "unreachable tokens" problem is two problems:** `U6` and `W4` are wrongly
excluded from Loom; `U7` is rightly excluded from all three trilogies and has nowhere
else to live.

### 4.2 Heat is flat, and that is probably right

`allowed_heat_range` is `H0`–`H4` in all three trilogies. This looks like the same
defect but is not: `HEAT` is the romance ladder (`romance_system.heat_ladder`, `H0`
spark → `H4` white_hot), and romance intensity is not an environmental condition that
escalates with the resonance crisis. A Veil-era scene can reach `H4` without any
metaphysical escalation at all.

**Confirm or correct this.** If heat is genuinely unbounded per trilogy, the field could
be removed from the envelope files rather than left looking like an oversight.

---

## 5. The constraint any answer must satisfy

Recovered Veil packet `S1.T1.B3.A3.E14` — *"THE SLIP — Tahl's First VT Brush"* —
carries:

```
U-Level: U5
Weather: W4 (brief)
Resonance State: RUPTURE → VT-BRUSH
Anchor: **FIRST AND ONLY VT BRUSH IN VEIL TRILOGY.**
```

`W4` inside Veil, which caps at `W3`. Decisions §6.2 states explicitly that whatever
replaces the current rule **must admit this packet**.

It is not a candidate for quiet downgrade to `W3`: it is the trilogy's single declared
VT contact, and the `W4` is what makes the contact physically possible under Mechanica.
The parenthetical `(brief)` is itself a clue — it reads as an author already reaching
for a duration-bounded exception.

---

## 6. The three options, with consequences

From decisions §8 item 1, with what each would cost.

### Option A — Advisory guidance, no enforced ceiling

Envelope values become guidance. Nothing mechanically prevents any corridor or weather
value in any book.

- **For:** matches "fluid and matched to narrative momentum" most directly. No exception
  mechanism needed — `E14` is simply fine.
- **Against:** `escalation_permissions` in the nine book contexts becomes meaningless
  and should be removed rather than left holding advisory numbers that read as limits.
  The validator loses the ability to catch a Veil episode written at `W4` by mistake
  rather than by intent — it can still check that `W4` is a *valid token*, never that it
  is *appropriate here*.
- **Watch for:** this is the option where the ceilings stop being data and become prose.
  If that is the intent, the envelope files shrink to tone and era description.

### Option B — Per-act ceilings

Ceilings move from the three trilogy files down to the 27 act overlays.

- **For:** granularity matches the actual shape of escalation — a book's third act
  peaks higher than its first. `E14` becomes legal because Book 3 Act III is set to
  permit `W4`.
- **Against:** 27 sets of values to author, and they cannot be derived mechanically —
  each is a judgement. It also front-loads the work: item 4 currently populates nine act
  overlays, and this makes that the harder half of the job rather than the easy half.
- **Watch for:** per-act ceilings still need a rule for the one-episode spike. If Book 3
  Act III is set to `W4`, every episode in it may reach `W4`, which is not what
  *"FIRST AND ONLY"* means.

### Option C — Ceiling tied to a momentum marker

Ceilings attach to a narrative-position marker rather than a structural unit, so they
rise and fall with the story's pressure curve.

- **For:** closest to "matched to narrative momentum" as written. Handles the
  one-episode spike naturally: `E14` is at a momentum peak, so `W4` is available there
  and not in the episodes around it.
- **Against:** requires a momentum model that does not exist. Nothing in the repository
  tracks narrative momentum — `grids/reader_pressure.csv` has `pressure_state` and
  `intensity_1_5` and is header-only. This option's prerequisite is that grid being
  populated, which is itself downstream of migration. **It may be circular in the short
  term.**
- **Watch for:** if this is the preferred long-term answer, an interim rule is still
  needed to unblock items 4, 5 and 5a now.

---

## 7. Sub-questions that need answering whichever option wins

1. **Does a Post-Mending envelope get created?** `U7` and `NODE` currently belong to no
   era file (§4.1).
2. **Is `E14`'s `W4` a sanctioned exception or the new normal for Loom-adjacent Veil
   peaks?** The answer differs between "one packet is special" and "Veil's ceiling was
   always wrong".
3. **Does `allowed_heat_range` stay in the envelope files at all?** (§4.2)
4. **What happens to `escalation_permissions` in the nine book contexts?** Populated
   under B, removed under A, or made derived under C — those 27 `TODO`s resolve
   differently in each case.
5. **Is there an exception mechanism, and what shape?** `E14` needs one under B and
   arguably under C. None exists in the schema today.

---

## 8. What would unblock the migration minimally

If a full replacement rule is not ready, the smallest answer that unblocks items 4, 5
and 5a is:

> **Raise the Loom corridor and weather ceilings to `U6`/`W4`, and grant `S1.T1.B3.A3.E14`
> a named exception, while the permanent rule is decided.**

That is not a recommendation — §4 of `CLAUDE.md` reserves this — but it is the minimum
input that lets migration proceed without pre-empting the eventual answer, because both
changes are consistent with all three options.

---

## 9. What is not in question

- The controlled vocabulary itself. `U1`–`U7`, `W0`–`W4`, `FX0`–`FX3` are Mechanica's
  and are not in dispute. Narrowing them was considered and excluded — §6.2 finds the
  ceilings wrong, not the vocabulary.
- Whether the current identical envelopes are wrong. §6.2 ruled them unintended. The
  only question is what replaces them.
- Anything the validator does. It checks membership and format; it cannot check whether
  a permitted value is *appropriate*, under any of the three options. That judgement
  stays human.
