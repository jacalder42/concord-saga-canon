# What "Proceed" approves, and what assistants may change — author ruling

**Date:** 2026-09-26
**Status:** CURRENT AUTHOR RULING on governance. It applies to **every assistant working in this
repository**: Claude, ChatGPT and any other. It changes no grid row, card, rule or book context.
It refines the same day's clarification in
[`NEON_MILESTONE_ARCHITECTURE_AUTHOR_RULING_2026-09-26.md`](NEON_MILESTONE_ARCHITECTURE_AUTHOR_RULING_2026-09-26.md) §0.

**The author's words, verbatim:**

> Keep the four rows; I approve of the majority of ChatGPT's proposed changes and don't want to lose
> them, we just to vet and validate them.
>
> In general my use of "Proceed" means I approves the immediately preceding proposed development or
> changes.
>
> ChatGPT has been instructed that additive modifications to the repo are approved but destructive
> ones need specific rulings from me.

---

## 1. Ruled

| # | Ruling | Consequence |
| --- | --- | --- |
| 1 | **Keep M54–M57.** The author approves the **majority** of ChatGPT's proposed Neon changes and wants them **vetted and validated**, not lost | The four rows stay in the grid as `proposed`, as they already are. The ratchet test already requires rows beyond M53 to be `proposed`. **No change needed.** Vetting them is a task |
| 2 | **"Proceed" approves the immediately preceding proposed development or changes** | Its scope is **the proposal immediately before it**. It is an approval, not a weak acceptance (§3) |
| 3 | **Additive modifications to the repository are approved. Destructive ones need a specific ruling from the author** | A standing rule for all assistants (CLAUDE.md §2) |

## 2. How rulings 2 and 3 fit the earlier clarification (READING)

The earlier clarification said: *"'Proceed' authorized ChatGPT to continue developing the
architecture; it should not have converted every resulting design choice into ruled canon."* Read
together with today's words:

- **"Proceed" approves what it answers**: the proposal put immediately before it. Material developed
  **after** it, while proceeding, is not covered by that "Proceed". Each later proposal needs its
  own approval.
- **Approval lets the development go ahead as approved design.** It is Tier B in CLAUDE.md §5,
  *"explicitly approved development outputs."* **It does not by itself turn a grid row or a card
  into ruled canon.** Changing a row's status to `ruled` or `retired`, or rewriting a ruled row,
  changes canon state, and under ruling 3 that needs a specific ruling. This is why M05's Vienna
  return and M54's Chicago are **approved direction** but stay `proposed`.

**What counts as destructive.** These are examples; the list is not exhaustive:

- deleting or truncating a file or a ledger entry;
- writing over existing text rather than appending, and above all in `recovery/`;
- retiring, demoting or promoting a status;
- rewriting a `ruled` row or an author ruling;
- removing a dependency;
- editing a canon card or a rule file against its current content.

**Not destructive:**

- adding a file, a row or a ledger entry;
- regenerating derived blocks with `tools/derive_book_context.py` from the approved grid.

If the author reads either line differently, this section is the one to correct.

## 3. Historical "Proceed" answers, re-weighted

The recovery documents of 2026-09-26 classed a bare *"Proceed"* as **weak acceptance**. Under
ruling 2, each of these is an **approval of the proposal it answered**. **Later author rulings still
win where they conflict.** The recovery files are not edited (`recovery/` is never altered in place);
this table is the correction.

| Where | What "Proceed" approved | Standing now |
| --- | --- | --- |
| `PC` 182257 | *Character Ascension Canon v1* (Bible #7): Silence and Hope *"created by the original hard-cap Veil"*; *"NO true Intent … fixed roles"* | **Creation line superseded** by the 09-26 ruling (they are older than the cap, and have no clear beginning). *"No true Intent … fixed roles"* is **approved, historical**, and not yet tested against *"their first act of agency"* (author, 11-23) |
| `PC` 182147–182187 | Breathable Veil Bible v1 (Bible #5) | **Approved.** It leaves out Silence and Hope's coaching plan; that is an omission, not a conflict |
| `WB` 64735–65420 | The St. Louis and Serpent Mound environment bibles (*"Node 3 of 4"*, *"The swamp is the only end-point"*) | **Approved.** Their "node" is an **Alignment Chain** node, not a Mechanica §7.4 Echo Node. The term needs care |
| `WB` ~75241 | Serpent Mound: the world almost chooses the Mending site there, and rejects it | **Approved** |
| `NS` 73340–74420, 136750–137725 | The crew's methods: Elisabet's triangulation, Seraphine's *"tinnitus that points"*, Rex proving the pattern, the Filament watchers | **Approved.** They now serve as confirmation beats (ruled 09-26) |
| `NS` ~4234 | The Solace v1 profile | **Superseded in part.** Solace is a masked title or removed (ruled 09-26) |
| `NS` 5316ff | Kade as "Elias's Tahl" | **Approved** |
| `NS` 145699ff | The Brightbreak "Final Canon v1" micro-bible (a civilian mutual-aid network) | **Superseded in part.** *"The civilian mutual-aid network variant is not the lineage"* (ruled 09-26) |
| `V` 68444ff, `T` 6099ff, `T` 6392ff | The Elias Tier-1, POV and EBCI cards | **Approved.** The repo's cards derive from them and were corrected on 09-26 by author approval |
| `NS` 18632 | *"Integrate proposals and proceed"*: the Mira memory-anchor retcon | **Approved then; reversed** by the 09-26 Mira rulings |

**Not re-weighted here:** documents written before 2026-09-26 may class "Proceed" the same way.
Sweeping them is a follow-up task.

## What this ruling does not change

No grid row, status, card, rule or book context. The 20 `ruled` rows and the four retirements stand.
M54–M57 and the other Neon design rows stay `proposed` until they are vetted. The ledger's
append-only rule (CLAUDE.md §2) is unchanged; ruling 3 makes it one case of a general rule.
