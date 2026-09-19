# Concord Saga — Author Rulings, Four Gates

**Status:** AUTHOR RULING — BINDING
**Date:** 2026-09-19
**Ruled by:** James
**Against:** `DECISION_BRIEF_2026-09-19.md`, `claude/gifted-goodall-st4n7r` @ `3bb37ca`
**Suggested destination:** `recovery/GATE_RULINGS_2026-09-19.md`

Supersedes the open items in `recovery/LOCATIONS_RECOVERY_2026-09-19.md` §2 and §3.
Clears the approval gate in
`proposals/concord-2026/CHARACTER_RECONCILIATION_MANIFEST_2026-09-20.md` §0.

---

## Ruling 1 — Location taxonomy: two layers, specifics preliminary

**Ruled: Option C, qualified.**

The geography system defines the **controlled vocabulary** of zone types and
corridor classes. `ENV` derives from that layer and only that layer.

City bibles define **named places** — proper nouns for specific ground — which
map onto a type from the controlled vocabulary. "Red Lantern Faultline" is a
name, not a type.

The Reykjavík scheme (Flicker → Ghostwave → Fracture → Rupture Threat) is the
**shard progression**, a severity scale that layers over places. It is not a
spatial taxonomy and is not to be treated as one.

### The qualification, and it governs everything below

**All specific type assignments are PRELIMINARY until vetted against narrative
and milestones.** This includes the contested ground — Tremé, Marigny, the French
Quarter, Bywater — and it includes the assignments both source documents already
carry. Nothing in the geography system or either city bible is locked by this
ruling. The *structure* is ruled; the *contents* are provisional.

Practical effect: build the two-layer shape, record assignments as provisional,
and do not lock any `ENV` value for contested ground until the narrative pass
reaches it.

### Scope of application

The zone-type vocabulary — Blue Pulse, Red Lantern, Violet Spiral, Violet Bloom,
Amber Drift — currently appears in **five files, all under `recovery/` and
`proposals/`. The canon substrate contains none of it.** There is nothing to
migrate and nothing to unpick; this is a forward-looking structure only.

---

## Ruling 2 — Corridor: one definition, contextual character

**Ruled: Option B, with the definition supplied by the author.**

> **A corridor is a linear path or area between two known points. Context
> determines whether it is safe, dangerous, or otherwise.**

### What this resolves

The four recorded senses are not four meanings. They are one definition, one
measurement scale applied to it, and two instance classes:

| Recorded sense | Under this ruling |
| --- | --- |
| `CORRIDOR` / `U1`–`U7` (Mechanica, `canon_rules.json`) | **Intensity measured on corridors.** Not a rival sense — a scale |
| Loom Corridors (geography system) | **A named class of corridors.** Instance layer |
| Laugavegur Corridor, River Corridor | **Ordinary instances.** Correct usage |
| "Blue Pulse Corridor" (New Orleans bible) | **Conditional — see the test below** |

### The test for "Blue Pulse Corridor"

The earlier objection — that corridors are safe and zones are chaotic, so a bloom
zone cannot be a corridor — **no longer holds**, because safety is not part of the
definition. The term stands or falls on geometry alone:

- If Blue Pulse is **linear and connective**, running between two known points,
  the name is correct and stays.
- If Blue Pulse is a **pocket or area without that connective geometry**, it is
  a zone and the word "Corridor" comes off the name.

This is a question about the referent, to be answered when the New Orleans
geography is vetted under Ruling 1 — not a naming decision to be made now.

### Consequential amendment

The geography system's framing that **corridors are safe routes and zones are
chaotic pockets** is superseded. Safety is contextual; the distinction is
geometric. That line requires amendment wherever it appears.

### Scope of application

Bare "Corridor" appears in **13 places across the canon substrate** — the EBCI
header (Environmental / Behavioral / Corridor Interface), Concord's Corridor
Preservation, corridor viability, corridor instability, corridor ecology
(`U1`–`U7`), corridor shifts. **All of these are correct under this definition
and none are to be changed.** No mass rename. No prose rewriting.

---

## Ruling 3 — Character reconciliation manifest: approved

**Ruled: APPROVE bundles A–I, with the stated caveat.**

| Bundle | Status |
| --- | --- |
| A — Filament / community | **Approved** |
| B — NOLA civic / cultural | **Approved, conditional on Ruling 1 vetting** |
| C — Dominion / Vienna | **Approved** |
| D — Technarch / Singapore | **Approved** |
| E — Choirless / ideological | **Approved** |
| F — Media / public voices | **Approved** |
| G — Global / place anchors | **Approved, conditional on Ruling 1 vetting** |
| H — Trilogy load / migration rules | **Approved** |
| I — Hold / recovery list | **Approved as a hold list — nothing in it is promoted** |

Standing carve-outs, unchanged by this approval:

- Every **HOLD** item stays held: manufactured-meta population, Arden Kess / LX-5,
  Lila Shore, Nix & Rio, Ayo Mensah.
- **Terminal Witness** remains **RECOVER MORE / DO NOT PROMOTE**. Tier E
  recollection, no source-level corroboration. Protect the slot; invent nothing.
- The author-locked controls are untouched: **Tahl Morgan / MissingThread** and
  **Baz Foix** remain as locked. † *— see **Amendment 1**, below. The Baz surname is
  amended; the rest of this line stands.*

B and G are approved in substance; their *place* references inherit Ruling 1's
preliminary status, like every other specific location assignment.

This authorizes **controlled canon migration planning and application** per
manifest §0 — search, classify, migrate in batches, validate, update ledgers,
then retire obsolete aliases. It does not authorize invention of unresolved
material.

---

## Ruling 4 — Working branch to main: as recommended

**Ruled: Option B.**

`claude/gifted-goodall-st4n7r` merges into `main` once Rulings 1–3 are applied
and `tools/validate_canon.py` reports at or below the current baseline of
**27 violations (canon scope) / 62 (all scope)**. Objective gate condition, not a
judgement call.

**Independent of that:** if the applied work runs beyond a week, `CLAUDE.md` and
`tools/` go to `main` on their own. They are additions, they conflict with
nothing, and a session cloning the default branch currently gets neither the
operating instructions nor the validator.

The proposal-branch fast-forward (`CANON_DECISIONS_2026-09-18` §6.1) proceeds
separately and is not gated on any of this.

---

## Derived work queue

In order. Nothing here requires a further ruling.

1. **Record these rulings** at `recovery/GATE_RULINGS_2026-09-19.md`; update
   `recovery/RECOVERY_LEDGER_2026.md` and close the open items in
   `LOCATIONS_RECOVERY_2026-09-19.md` §2 and §3.
2. **Amend the safe-route framing** wherever the corridor/zone distinction is
   stated as one of safety rather than geometry.
3. **Build the two-layer location structure** — controlled vocabulary at the
   geography-system layer, named places mapping onto it, every specific
   assignment marked provisional.
4. **Derive `ENV`** from the type layer only, leaving contested ground unassigned
   rather than provisionally assigned.
5. **Open the character migration plan** under manifest §0, batched by bundle,
   B and G last.
6. **Validate**, then merge per Ruling 4.

The two blockers on the locations layer are now cleared. Place and cast both have
rulings. The saga timeline — the one container the cascade lacks — is the first
thing downstream of this queue that can actually be built.


---

# AMENDMENT 1 — Baz's surname

**Status:** AUTHOR RULING — BINDING
**Date:** 2026-09-19
**Ruled by:** James
**Amends:** Ruling 3's standing carve-out, above. **Ruling 3's body is not rewritten** —
it records what was ruled on 2026-09-19 and stands as issued. This amendment sits after
it, and the carve-out carries a pointer.

---

## The ruling

> **Bastien "Baz" Arnaud is canon.**
> The manifest's preference for **Basil "Baz" Foix** is **overruled**.
> **"Foix" is retired as a Baz surname.**

## What this settles

The discrepancy recorded at ledger §33 §4 and carried forward into
`CHARACTER_MIGRATION_PLAN_2026-09-19.md` §4.3 is closed. Ruling 3's carve-out named the
locked control as *"Baz Foix"*; `canon/characters/BazID.md` reads **Bastien "Baz"
Arnaud**; the two are now reconciled **in favour of canon**, consistent with the
2026-09-19 ruling that `canon/characters/` is final (`CLAUDE.md` §3, ledger §31).

The earlier reading — that the *rename decision* was what stayed locked rather than the
name `Foix` itself — was the cautious one, and it is superseded by a direct ruling. It is
recorded here rather than deleted, because it is what the previous passes acted on.

## Scope

- **Applies to Baz only.** `Foix` is retired **as a Baz surname**.
- **`Janvier "Jan" Foix`** (manifest §4, bundle C) inherited the rejected surname and
  becomes **`Janvier "Jan" Arnaud`**. His function is unchanged: Baz's family, grief that
  does not centre Lucien, ending `OPEN`. Recorded as a **consequential rename, reversible**.
- **The canon substrate is already correct** and is not touched. `canon/` reads
  `Bastien "Baz" Arnaud` throughout with zero `Foix`.
- **Quotations are annotated, not rewritten.** Where a `recovery/` or `proposals/`
  document **quotes a source that said `Foix`**, the quotation stands and carries a note.
  *A recovery document must not be edited to make its source appear to have said something
  it did not.* Same rule the `Technarc`, `Ito Masayuki` and safe-route passes used.

## What does not change

Everything else in Ruling 3 — the approval of bundles A–I, the HOLD carve-outs, Terminal
Witness as `RECOVER MORE / DO NOT PROMOTE`, and the **Tahl Morgan / MissingThread** lock —
is unaffected.

END OF AMENDMENT 1
