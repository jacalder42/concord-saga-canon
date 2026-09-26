# Neon design rows — vetting, Pass 1

**Date:** 2026-09-26
**Status:** PROPOSAL / NON-CANONICAL. This pass vets the twelve Neon grid rows that were kept as
`proposed` design after the ChatGPT session (M05, M13, M14, M16, M17, M18, M21, M23, M54, M55, M56,
M57). **No grid row is changed.** Each suggested wording below rewrites existing text, which is a
destructive change, so it waits for the author's ruling
(`decisions/ASSISTANT_CHANGE_AUTHORITY_AND_PROCEED_AUTHOR_RULING_2026-09-26.md`).

**Asked:** *"Start vetting the Neon design rows"* (author, 2026-09-26).

**Method.** Three read-only research passes covered four rows each. They searched the author's
turns in the export, checked the current canon cards and rulings, and classified every claim in
each row. **Claude re-checked each key quote and its speaker against the export.** Three line
references were off by one to three lines and are corrected here.

**Classes used in the tables:**

- **AUTHOR**: the author's own words.
- **APPROVED**: assistant text the author accepted. *"Proceed"* approves the proposal immediately
  before it (ruled 09-26); *"Approve and save"* approves what it answers.
- **UNAPPROVED**: assistant text only.
- **DESIGN**: no source found.
- **CONFLICT**: disagrees with a ruling, a canon card or an approval.

**Abbreviations:** export files in `sources/chatgpt_export_2026-09/`.

| Key | File |
| --- | --- |
| `MDR` | `2025-11-17__Master_document_rebuild` |
| `NB` | `2025-11-21__Concord_Saga_Notion_Blueprint` |
| `NS` | `2025-11-27__Narrative_Structure` |
| `PC` | `2025-11-10__Prompt_crafting_types` |
| `BB` | `2025-12-07__Beat_bible_recovery_process` |
| `AF` | `2026-01-04__Antagonist_and_Faction_Files` |

---

## 1. What the pass found across the rows

1. **ChatGPT's recovery missed approved Neon material.** Several sources the author approved
   carry the author's decisions, and ChatGPT's replacement wording does not cite them:
   - **The Neon act bibles in `MDR`.** The author approved them after reading: *"Approve and save
     Book 4 Act iii"* (17205), *"Approved and save Book 5 Act II"* (19822), *"Approved and save"*
     (20159), and *"Approve Cohesion pass"* (17583).
   - **The Notion Book 4 and Book 5 bibles**, each followed by *"Proceed"* (`NB` 103585, 103768).
   - **The 11-27 Neon location map ("Layer 5")**, followed by *"Proceed"* (`NS` 110083).

   Several of ChatGPT's design choices **depart from these approvals**: M05, M16, M54, M55 and M57.
   Some approvals also **disagree with each other**; the Riot of Light is approved in both B04 and
   B05. Later author rulings win where they apply.
2. **Only M21 is strongly author-sourced**, and ChatGPT's rewrite dropped two of the author's own
   points.
3. **Saeko is not superseded** (M14). Only her 11-21 "public face" assignment is.
4. **Two rows conflict with rulings or canon:**
   - **M23**'s timing against the ruled Lacuna nudge at the funeral;
   - **M54**'s lesson against Caro's Tier-1 card, which puts delegation in Loom.

## 2. Row by row

### M05: Lucien, B02–B04 (B04 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| Guilt after Baz: he brought him to New Orleans | **AUTHOR** | `BB` 12817: *"Lucien should ask Baz to come to New Orleans to feed into his guilt loop."* |
| He withdraws after Baz, and returns later in Neon | **AUTHOR** | `NB` 81793: *"Lucien drifts away after Baz's death, then returns as he gets his feet later in Neon."* It does not say where he goes |
| Refuses Dominion recall (B02–B03) | **APPROVED** | 12-07 B02 rebuild: *"Lucien refuses again"* (`BB` ~1780). `NS` 187140–41 (B03): *"Receives orders from Dominions to return to Vienna"* / *"Deletes the message"* |
| An irreversible break in B04 | **APPROVED** | `NB` 103490–91 (Book 4 E8; *"Proceed"* at 103585): *"Dominion emissaries demand Lucien return for "reassignments.""* / *"He rejects them fully, committing to NOLA."* |
| **The break happens after a voluntary Vienna return** | **DESIGN** (preferred direction, not locked) | **CONFLICT with the approved *"committing to NOLA"*** |
| Separates structure and care from obedience | **DESIGN** | `LucienID.md` puts *"restraint reframed as chosen care"* in **Loom**. B04 can only begin it |

**Recommendation: HOLD the Vienna clause for the author's lock.** Suggested wording:

> Across B02–B04, Lucien repeatedly refuses Dominion recall; after Baz's death he makes an
> irreversible break with Dominion authority, where (Vienna or New Orleans) is open.

### M57: Seraphine and Lucien (B05 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| Lucien is her main pair; they drift in Neon | **AUTHOR** | `PC` 146112: *"Lucien is her main pair throughout the series."* `NB` 81793 (above) |
| B04 strain | **APPROVED** | `NB` Book 4 E9: *"A painful pseudo-breakup (not romantic, but soul-level disconnect)."* |
| They choose to stay together | **APPROVED**, but in **B05 Act III**, not A2 | `NB` 103710–11 (Book 5 E12): *"After being emotionally distant for most of Book 4 and early Book 5, they admit:"* / *"They're afraid of losing each other."* |
| Neither regulates or contains the other | **DESIGN** | Consistent with Mechanica (consent and regulation). A mild tension with `LucienID` §IX, *"his containment gives her bloom safe edges"* |
| "withdrawal **to Vienna**" | Depends on M05 | — |

**Recommendation: REVISE.** Drop "to Vienna" until M05 is locked, and choose the act: **A3**, as
approved, or A2, which moves the approved beat. Suggested wording:

> After Baz's death and Lucien's withdrawal, Seraphine and Lucien choose to remain in relationship
> without making Seraphine responsible for regulating his grief or Lucien responsible for containing
> her instability.

### M13: Protocol 9 (B04 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| Director Han Wei launches **Protocol 9** in B04 | **APPROVED** | `NB` 103486 (*"Proceed"* at 103585): *"Director Han Wei launches **Protocol 9**: enforced monitoring of resonance-active individuals."* |
| It escalates in B05 | **APPROVED** | Book 5 E7: *"Technarch establishes Resonance Checkpoints."* |
| It follows public institutional failure | **AUTHOR** (general) | `Project_review` 14081: *"Confusion, incompetence, the tightening of concern, striving to maintain control without information."* |
| It is uneven, not a global regime | Supported | Worldbuilding pastes: clampdowns *"in some zones"* |

**Recommendation: REVISE**, restoring the approved names. The row's *"name, authority … remain
open"* understates the evidence. Suggested wording:

> After institutional failures become public, Technarc under Director Han Wei launches Protocol 9,
> expanding monitoring and containment of Resonance-active people; the policy has specific human
> consequences and stays uneven rather than a universal global regime.

### M14: suppression politics (B04 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| Saeko as *"the face of civic fear"*; her movement goes *"national"* | **APPROVED** (11-21), now **superseded** | `NB` 103481, 103670. Superseded by the Jan 4 role split: cast registry E01 *"not a populist demagogue"* |
| Saeko as the quieting-doctrine engineer | **CURRENT CANON** | `AF` 4323 (author): *"The files I attached are the most correct and current"*. `SaekoID` NEON: *"Designs PureTone logic and quieting methodologies"*. Registry E01 **KEEP** |
| Ito as the public amplifier | **CURRENT CANON** | Registry E03 |
| Visible in B04, wider reach in B05 | **APPROVED** placement | Book 4 E6, Book 5 E6 |

**Recommendation: REVISE the note.** The description is accurate. The note *"do not restore
superseded Saeko assignments silently"* invites dropping Saeko, who is a KEEP Tier-1 antagonist.
Suggested note:

> Saeko's 11-21 public-face assignment is superseded by the Jan 4 role split (Ito is the public
> amplifier; Saeko is the doctrinal engineer); Saeko herself is current canon.

### M16: B04 civic confrontation (B04 A3)

| Claim | Class | Evidence |
| --- | --- | --- |
| A Riot of Light in **B04 A3** | **APPROVED** | `MDR` 17098 *"E7 — [The Riot of Light]"*, approved at 17205 and in the cohesion pass (17583) |
| A Riot of Light in **B05 A3** | **APPROVED as well** | `MDR` 19974 *"E5 — The Riot of Light Erupts"*, approved at 20159. The same bible starts Tahl's *"death arc"* there (20163), which bears on M20 |
| It survives as an event | **LEAN** | Milestone-gate ruling, answer 3 |
| Crowd violence and Resonance effects are separately attributable | **DESIGN** | The review's guardrail; D5 |

**Recommendation: READY TO RULE as worded.** The neutral wording deliberately avoids choosing a
book. **The author picks B04 A3 or B05 A3**, and whether the name survives.

### M17: Technarc legitimacy break (setup B05 A2, payoff B06 A1)

| Claim | Class | Evidence |
| --- | --- | --- |
| Metas are failing constructs; no operative boost | **AUTHOR** | `PC` 32724: *"The meta essentially became a sacrificial power source trapped without intent."* `NB` 155783 |
| A failure breaks legitimacy | Consistent with canon | `Manufactured_Metas.md` Neon: *"Catastrophic breakdowns"* |
| "bounded" harm | **DESIGN** | Tension with *"Catastrophic"* |
| Payoff in B06 A1 | **UNAPPROVED** | The Dec 8 master is assistant output. The approved `MDR` bibles have public meta incidents in B04 A3, B05 A1 and B05 A3. This row can only be **a local legitimacy break, not the first public failure** |
| Singapore | **DESIGN**, weak support | The author picked *"Singapore"* from a menu (`NB` 225631); the deep-dive has no acceptance. **Open question:** is Rex in Singapore or Detroit during Neon? `RexID` has *"selects Detroit deliberately"* |

**Recommendation: REVISE the notes.** The description stands. Suggested note:

> Setup B05 A2 → payoff B06 A1 is design; Singapore is a design candidate, not recovered placement.
> The approved public meta incidents (B04 A3, B05 A1, B05 A3) stand; this is a local legitimacy
> break, not the first public failure. No battery-to-operative transfer.

### M18: Filament division (B05 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| Filaments split over care against intervention | **APPROVED** | `MDR` 17034: *"Filament fracture becomes irreversible."* (B04 A3, approved 17205). `MDR` 19805: *"Filament splinters are forming"* (B05 A2, approved 19822) |
| *"Connection is survival"* against *"Action is survival"* | **UNAPPROVED** | Notion bible text |
| Changes in coordination, trust or resources | **DESIGN** | Compatible with the Filament canon locks |
| Note: *"Later splinters may feed Brightbreak"* | **CONFLICT risk** | The ruled lineage runs through **Neon Rebellion** splinters. Author, `MDR` 10294: *"Eventually these filaments would evolve in the Neon Rebellion after Baz's death"* |

**Recommendation: REVISE the note.**

> Some later splinters may pass through the Neon Rebellion into Brightbreak (ruled: some Rebellion
> splinters become Brightbreak, others dissolve or stay independent); not all dissent is extremist.

**Also:** the approved crack is irreversible in **B04 A3**, so B05 A2 is its consolidation.

### M21: Silence collects Tahl's echo (B06 A3)

| Claim | Class | Evidence |
| --- | --- | --- |
| Silence collects him | **AUTHOR** (11-13), not only recalled | `PC` 53373: *"Tahl dies, Silence grieves and collects him."* `PC` 158951, the author correcting item 24: *"Silence gains Intent after collecting Tahl's echo after his death."* |
| It is their first act of agency | **AUTHOR** | `NB` 89177: *"Saving Tahl's echo is their first act of agency, which is the first crack in the cycle of hard cap veils."* **"Their" is Silence and Hope** |
| One identifiable flare, in B09 | **RULED** | M52 |
| "consequential", "bounded" | **DESIGN** | "bounded" assumes limits the notes call open |

**Recommendation: REVISE**, restoring the author's two points ChatGPT dropped. Suggested wording:

> At Tahl's death, Silence collects Tahl's echo: Silence and Hope's first act of agency and the
> first crack in the cycle of hard-cap veils. The echo remains non-identifiable to the living cast
> until its single identifiable flare in B09 (M52).

**Question:** is the agency Silence's alone (*"Silence gains Intent after collecting"*), or shared
(*"their first act of agency"*)?

### M23: Kade's grief writing (B06 EP)

| Claim | Class | Evidence |
| --- | --- | --- |
| He keeps a grief diary in MT's comments | **AUTHOR** | `MDR` 11349: *"in his grief keeps a stream of consciousness diary of sorts in the comments on MT threads"*. `PC` 119967 |
| He believes it is private; it is read | **AUTHOR / RULED** | `NS` 86868: *"Kade thinks it's private because of the Veil static"*. `PC` 119969: *"Little does he know it's broadcast"* |
| He loses Tahl from afar | **APPROVED** | `NS` 149852, accepted at 150224: *"This direction is good."* |
| **Placed in B06 EP, before the funeral** | **CONFLICT** (ordering) | `NS` 86868: *"Perhaps Lacuna is who pushes / hints that Kade should post his feelings to MT."* The funeral nudge is ruled (M40). `NS` 68447: *"the funeral (and how Lacuna frames it) is what elevates him"* |

**Recommendation: HOLD**, pending one answer. Two options:

- **(a)** Keep M23 in B06 EP as grief comments on Tahl's threads, with the private diary beginning at
  Lacuna's nudge (M40).
- **(b)** Move M23 into B07 A1 and merge it with M40.

### M54: Caro's handoff (B05 A3)

| Claim | Class | Evidence |
| --- | --- | --- |
| Over-responsibility and self-neglect | **Canon** | `CaroID`: *"self-neglect normalized in service of others"* |
| **She learns to delegate in B05** | **CONFLICT** | `CaroID` 53–54: *"Neon: action becomes sustained triage; endurance costs accumulate"* / *"Loom: action reframed as sustainable care; pacing and delegation learned"* |
| A care crisis with burnout in B05 | **Weakly accepted** (Layer 6) | `NS` 110233: *"Holds families together in mid-collapse communities"* |
| Chicago | **DESIGN** | **Tension with the APPROVED Layer 5**: `NS` 110038, *"Caro → New Orleans → Santa Fe closure"* (*"Proceed"* at 110083) |
| Setup M07 | **Error** | ChatGPT's own delta says no setup is needed; M07 belongs to M56 |

**Recommendation: HOLD.** If the author keeps B05, it should be Caro's **first crack**, with the
lesson itself in Loom. Suggested wording:

> During a large evacuation or care crisis, Caro reaches the limit of what she can personally carry
> and, for the first time, entrusts a consequential task or group of people to someone else and
> leaves before the work is finished; the handoff holds, but the belief that she must carry it
> herself is shaken, not yet unlearned.

Clear the M07 setup.

### M55: Elisabet acts before certainty (B05 A3)

| Claim | Class | Evidence |
| --- | --- | --- |
| She recommends protective action before certainty | **DESIGN**, grounded in canon | `ElisabetID`: *"Neon: … delayed action proves costly"*. It is an arc turn against her EBCI baseline (*"refuse premature action"*) |
| Her B05 Santa Fe modelling | **Weakly accepted** (Layer 6) | `NS` 110238: *"Make predictive models pointing to Santa Fe as worst-case outcome"* |
| Reykjavík as her theater | **DESIGN**; **tension with the APPROVED Layer 5** | `NS` 110039: *"Elisabet → Vienna → St. Louis → Santa Fe map"*. Reykjavík is her *"quiet zone"* (110023) |
| Note: *"Tahl originates the critical VT warning"* | **CONFLICT** | The author's clarification item 9: not locked |
| Note: *"Elisabet does not become a supernatural detector"* | **Tension with AUTHOR** | `MDR` 8356: *"she begins with high sensitivity but low output … She sensed the events"* |

**Recommendation: READY TO RULE as worded; revise the notes.** Suggested note:

> The recommendation rests on mortal evidence; the VT origin of the warning (recalled) and
> Elisabet's own resonance sensitivity (MDR 8356) stay open.

### M56: Caro and Elisabet (B05 A2)

| Claim | Class | Evidence |
| --- | --- | --- |
| A primary romance that blooms in Neon | **AUTHOR** | `NB` 81791: *"both Seraphine-Lucien and Caro-Elisabet are romantic."* `MDR` 8355: *"the relationship blooms during the tumult of Neon."* |
| They explicitly choose each other in B05 | **DESIGN**; tension | `NB` 80721: *"they are a couple for most of the series"*. The Notion B04 end has *"fully bonded"*. If they are already a couple, B05 is a recommitment |
| Separate necessary work | **DESIGN**, supported | The cast-separation ruling; the 12-07 goodbye |
| Note: *"Supports B06 separation"* | **DESIGN** | No source for a B06 separation |

**Recommendation: REVISE.** Suggested wording:

> Caro and Elisabet, already partners, explicitly recommit to their relationship while each chooses
> separate necessary work, establishing that commitment does not require constant co-location or one
> partner abandoning her independent responsibility.

## 3. Summary

| Row | Recommendation | Waits on |
| --- | --- | --- |
| M16 | **Ready to rule as worded** | Which book (B04 A3 or B05 A3) |
| M55 | **Ready to rule as worded**; revise the notes | Where Elisabet is |
| M13 | Revise: restore Protocol 9 and Han Wei | Approval of the wording |
| M14 | Revise the note; optionally name Ito and Saeko | Approval |
| M17 | Revise the notes | Rex: Singapore or Detroit |
| M18 | Revise the note (Brightbreak lineage) | Approval |
| M21 | Revise: restore the author's agency and "first crack" | Silence alone, or with Hope |
| M56 | Revise: a recommitment | Already partners by B05? |
| M57 | Revise: drop "to Vienna"; choose A2 or A3 | M05; the act |
| M05 | **Hold** the Vienna clause | Vienna against the approved "committing to NOLA" |
| M23 | **Hold** | Diary before the funeral, or from Lacuna's nudge |
| M54 | **Hold** | B05 first crack or the lesson; Chicago against the approved New Orleans → Santa Fe route |

## 4. For the author

1. **M05:** does Lucien's B04 Vienna return replace the approved *"rejects them fully, committing to
   NOLA"* (Book 4 E8)? Does he come back to New Orleans within Neon?
2. **M57:** the reconnection at the approved **B05 Act III**, or moved to Act II?
3. **M13:** restore **Protocol 9** and **Han Wei** by name?
4. **M14:** name **Ito** (public amplifier) and **Saeko** (doctrinal engineer), or stay neutral?
5. **M16:** the Riot of Light in **B04 A3** or **B05 A3** (you approved both)? Keep the name?
6. **M17:** is Rex in **Singapore** or **Detroit** during Neon?
7. **M21:** is the first act of agency **Silence's alone**, or **Silence and Hope's**?
8. **M23:** does Kade's grief diary begin in the **B06 epilogue**, or only after **Lacuna's nudge**
   at the funeral?
9. **M54:** B05 as Caro's **first crack** (with delegation learned in Loom, per her card), or the
   lesson itself? Chicago, or the approved **New Orleans → Santa Fe** route?
10. **M55:** where is Elisabet when she recommends action: **Reykjavík**, or **Vienna / St. Louis**
    per the approved map?
11. **M56:** already partners by B05 (a **recommitment**), or is B05 the **first declaration**?

**And:** approve the suggested wordings above, row by row, or amend them.

## What this pass does not change

No grid row, card, rule or book context. Every suggested wording is a proposal. The rows stay
`proposed`, and the 20 `ruled` rows are untouched.
