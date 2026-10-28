# B03 EBCI: propagation of the October rulings (§615–§626)

Status: PROPOSAL / PROPAGATION MAP. MECH items are **applied** in `ebci/B03/`. DESIGN items are **proposed only**: no Narrative brief carries them yet.
Date: 2026-10-28. Author instruction: "Agreed proceed" (ledger §626, *Next: the propagation pass*).
Governing files:
- `decisions/NYLA_ARC_AND_VISIBLE_MOMENT_2026-10-25.md` (§615);
- `decisions/B01_HOLDS_REVIEW_RULINGS_2026-10-25.md` (§616);
- `decisions/B01_I5_INSTITUTIONS_AUTHOR_RULINGS_2026-10-27.md` (§617, §618);
- `decisions/B01_RESONANCE_DISCOVERY_LADDER_AUTHOR_RULING_2026-10-27.md` (§619);
- `decisions/B01_ELISABET_SIGNATURE_BREACH_LEXICON_AUTHOR_RULING_2026-10-28.md` (§620–§622);
- `decisions/TRILOGY_CONTRACT_AND_QUESTIONS_AUTHOR_RULING_2026-10-28.md` (§624);
- `decisions/NYLA_SAGA_PLACE_AUTHOR_RULING_2026-10-28.md` (§625, §626).

§623 (the I7 brief gate) is B01-only and touches no B03 card.

**Not committed.** Only `ebci/B03/` and this file were changed. The validator passes (`tools/validate_canon.py`: no violations).

## 0. Counts
- **Cards touched:** 48 of 48 (every card gets the guardrail MECH change).
- **Card-specific MECH:** 11 cards (E13, E14, E17, E23, E30, E31, E32, E36, E42, E46, E47). Only **two** change a Narrative brief field: E14's *Keep* and E31's *Story job*.
- **DESIGN pending notes:** 25 cards, keyed to items **D1–D9** below. No brief field was changed for a DESIGN item.

## 1. MECH (applied)

### M-G. The standing guardrails, all 48 cards (§616, §617, §619, §620, §625)
This is the *Amendments applied* string, which is control layer. There are two variants: 39 cards carry the 09-27 wording of the blame clause and 9 carry the 10-03 wording. Both were changed the same way.

| Change | Ruling |
|---|---|
| Struck: ~~physics observed, never explained by the page (characters may ask and theorise, Q-DQ4)~~. Replaced with: the behaviour is discoverable and the origin reserved; characters may describe, hypothesise, test, teach and explain in their own words; Mechanica's vocabulary stays off the page; nobody knows a reserved truth without evidence. | §619; Mechanica §60 as amended |
| Struck: ~~metas rumour only~~. Replaced with: no conversion procedure on the page, never shown as procedure on a child, felt through Lanette, Seraphine and Baz. | §625 §1.5 (supersedes §615's "metas stay rumour until B04") |
| Added: the October standing guards. Dominion may be named freely, and Hollen is its front (mechanics off the page). Dominion's theories may be explained as belief and are never certified. Dominion holds the forecast; the protagonists' method finds the people. Emotion governs coupling, not origin. Breaches escalate. The ladder never resets. The lexicon is breach / scar / *Wound*, with *Wound* and *breathing* reserved. X1 stands. | §616 X2/F8, §617, §619, §620, §624 rule 4, §615 |
| Kept and flagged: the Warehouse blame clause (*the narration does not state cause as fact*). It now carries a bracket: the cause is ruled, and certification is **D4**. | §625/§626; 10-03 §379 |

Each card's Notes gets `Propagation 2026-10-28 (§616, §617, §619, §620, §625)`.

### Card-specific MECH
| Card | Field | Change | Ruling |
|---|---|---|---|
| **A1.E14** Helena's Price | **Brief: Keep** | Struck: ~~No Dominion exposition … the demand is pressure, not a stated threat~~. Replaced with: Dominion may be named, and its belief explained as belief; Caldas's menace toward Baz is real and may be plain; nothing says whom Helena answers to. | §615, §616 X2, §617 |
| A1.E14 | Notes (10-18) | Struck: ~~*Keep* stands (the demand is pressure, not a stated threat); what "free rein" licenses on the page is not ruled~~. Added: Baz's knowledge (he knows the Hollen front, not the funder). | §615, §617 |
| **A3.E31** In Person | **Brief: Story job** | "before it is a ~~scar~~ breach" | §620 |
| A3.E31 | Notes | Control: S03's coordinates are now ruled to draw the amplifying crowd, and Caldas's revenge runs through them. | §624 §4, §625 §1 |
| **EP.E47** Named | Notes | The stale W4 pointer ~~(at the pre-pass-3 `S1.T1.B03.A3.E14`)~~ is restated so it cannot be read as the live A1.E14. | Q-V3-3; §624 hygiene |
| A3.E36 The Rupture | Notes | Lexicon: the sealed site is an active **breach** (permanent, escalating), not a scar. *A mechanism* (Prohibited) is read with §60 as amended. | §619, §620 |
| A1.E13 | Notes | "a little larger each time" is the ruled escalation; *breach* is available in its ordinary sense. | §619, §620 |
| A2.E17 | Notes | "the people behind the Institute" = Dominion, and the page may say so; Baz knows the front, not the funder. | §617 |
| A2.E23, A2.E30 | Notes | Elisabet's water signature, if read, is coarse: a window is open; no count, no place, never out-forecasting Dominion. | §620 §3 |
| A3.E32 | Notes | The post → crowd link is ruled canon. The brief's *narrator does not certify* stands until D4. | §625 §1, M11 |
| A3.E42 | Notes | Checked: Q-V3-2 (*Resonance* off the Veil page) stands beside §60 as amended. | §619 |
| EP.E46 | Notes | The counterfactual is partly answered in canon (the crowd amplified the leak). The page never answers it. | §625 §1, §22 |

**Searched, no B03 text found:** "permanent scar" (it lives in Mechanica §34 and M08/M28, outside scope); "breathing"; "Wound"; Pryor (§618); Line 8 (§624 §5); Hollen. **Out of scope, flagged:** the `act_overlays/act_overlay_S1_T1_B03_A3.json` *basis_note* "W4 exception at E14"; the `grids/episode_beats.csv` rows for any DESIGN beat; the B02 EBCI, which does not yet carry Nyla's capture and E44 escape. **B02 propagation is a prerequisite for D1 and D2.**

## 2. DESIGN (proposed; not applied)
Each item is at Story job / Change / Exit state level. There is no prose and no dialogue. **Death-tells:** where a D-item concerns Baz's death, it is written for the control layer only. Any brief text derived from it states his life positively (README).

### D1. The ladder floor and the forecast, re-scoped (E01, E09, E15, E27, E28, E30)
- **Story job:** B03 opens on B02's ceiling, never B02's floor. Dominion's forecast sees the window and is held. Baz's method finds the people. Breaches escalate, and that is the visible clock.
- **Change:**
  - E01's *What still works from B02 (the signs and the interval)* becomes whatever B02's propagated end-state is.
  - *No model forecasts a shock* (E09, E27) is restricted to the public protocol models.
  - E28's containment shows that Dominion has a forecast it does not share.
  - E36's *exceeds every model* stays: like the Square's third pulse, the leak exceeds the forecast.
- **Exit state:** the reader knows someone could forecast and did not tell, which is the dramatic question in motion.
- **Depends on** the B02 propagation.

### D2. The coercion that retakes Nyla (A1, offstage; felt through Lanette)
- **Story job:** the B02 escape stands, and B03 takes her back without a capture set-piece.
- **Change:** someone close to Nyla is leveraged, or a threat is made (the mechanism is open, §625 §3).
- **Placement:**
  - **Recommended:** felt in A1 through Seraphine's finite circle (E12) or Inez's gathering (E07), with Lanette present. Lanette has **no B03 card**, so this needs either a Lanette presence inside an existing episode or one new A1/A2 episode [P].
  - Through A2 it is felt as absence and Lanette's search: E18 or E22 are candidates.
  - Paper stays the justification, not the vehicle (§615 amendment).
- **Exit state:** Nyla is gone again. Lanette knows it was coerced. Nobody on the cast knows where she is.
- **Open:** whether Seraphine knows before the post lights her phone at E35. That changes what her staying costs. *Nobody is where Baz is* holds either way.

### D3. The funder reveal to the reader, one revelation with the conversion (§624 §3, §626)
- **Story job:** before Baz dies, the reader learns that Baz's Houston funder is a faction inside Dominion and that it runs Nyla's conversion. The cast learns in B04.
- **Placement options:**
  - **(a) Recommended:** Baz discovers it himself at the program site (E37), in the act of finding Nyla. The faction's form word (*first*), the consents and the funder's people or kit are recognised, not explained. This closes his lead arc (he believes he left Dominion while still being paid by it), and only the reader sees it (consistent with E38).
  - **(b)** The page shows it earlier, through the institutional-analysts ensemble (E28) or a faction-side scene [P]. That gives dramatic irony through A2 to A3.
  - **(c)** Both: a seed in A2 (E20's permits and counts, or E14/E16 with Helena as a possible faction member) and confirmation at E37.
- **Exit state:** the reader knows; Baz knows; nobody else does.
- **Guard:** nothing hints it to Baz before the placed moment (§617).

### D4. The Warehouse as the leak (E13, E21, E27–E29, E31, E33–E36, E42)
- **Story job:** the Rupture is the failure of a forced conversion. A manufactured meta holds what it cannot spend, and the load leaks (Mechanica §48). The page reads it as a store of pressure breaking out, without naming the cap (§625 §1.6).
- **Change:**
  - The program site is in the older section (E29's late unload bay; E33's upper floors).
  - The E13/E27 precursor ("comes and goes, a little larger each time") becomes the program's earlier leakage at a weak place, which escalates like a breach.
  - Technarc's unmarked readers (E21, E33) are drawn by that signal; they stay non-causal.
  - E36's *Required observable* is kept physical.
  - E36's *Prohibited* changes:
    - *a mechanism* becomes *no procedure and no Mechanica vocabulary*;
    - *the crowd as the cause* becomes *the crowd as amplifier: shown, not certified* [P].
- **Decision needed:** how far the page certifies the cause (the blame clause flagged in every card). The options:
  - **(i)** implication only, the 10-03 default;
  - **(ii)** the reader certain through D3, while the narration states nothing.

  **(ii) is recommended:** D3 makes the cause plain to the reader, so certification by the narrator adds nothing.
- **Exit state:** the district is a permanent breach. The reader knows why; the city argues.

### D5. Baz pulls Nyla free (E34, E36–E40)
- **Story job:** the child is Nyla (M10; §625 §1).
- **Change:**
  - E36: the person pinned is Nyla, inside the program's room, not the teenager's sibling in the lofts' entry.
  - E37: Baz reaches her and pulls her free. The procedure is felt, never shown (§625 §1.5).
  - E38: the dock door and the second fall are unchanged.
  - E39: responders find her on the river side.
  - E40: Lanette arrives at the staging point, and the rota's records show no child of that name, so the erasure is felt through Lanette.
  - **The teenager and sibling thread (E32, E34, E39, E40):**
    - **recommended:** keep the teenager as crowd and cut the smaller figure;
    - **or** keep the sibling as a separate rescue by others.
- **Risk to M10:** Nyla may know Baz by name. Her account must not identify him to the cast before B04: she is non-verbal or unstable, or her account is not credited, or it is erased with her name [P].
- **Exit state:** Nyla is alive, converted, unstable, and erased on paper (§48).

### D6. Caldas: defeated in B03, his revenge landing (§624 §4)
- **Story job:** Caldas's Veil arc closes on the page. The kill that takes Baz still succeeds, through Tahl's coordinates and the crowd.
- **Placement:** the defeat comes late in A2 (around E26–E30), so the revenge lands after it.
  - The form is open: exposure (Seraphine's E21 door, or a record), ruin (leadership drops him, or the faction outmanoeuvres him), or death.
  - Whether he set the plan before his defeat stays ambiguous.
- **Seams to reconcile:**
  - **E30/E31's Review C04, *his own reason takes him there*.** Caldas's design may arrange what Baz learns, for example where Nyla is, without commanding his choice.
  - **E38's *No one murders him* (P3 §5),** held, not struck. The leak kills; the design and the exposure share the guilt (M11).
  - **Caldas is leadership's man**, and he reads the faction's review without being part of it (Dominions.md). His revenge "runs through" a faction operation (§625 §1). He exploits it; he does not run it.
- **Exit state:** Caldas is defeated. Baz is dead. Guilt is shared and unproven to the cast.

### D7. The seated-crowd follow-up (one in B03; §619, matrix §5 Veil 4)
- **Story job:** B01's seated, connected crowd changed the event. B03 returns to that once, shown and argued, never confirmed (X1).
- **Placement:**
  - Argued as *unknown* on Elisabet's whiteboard (E23) or in E15's separate rooms.
  - Its inverse shown at E36: a drawn, frightened and unconnected crowd amplifies (§22: crowds multiply whatever state they are in).
- **Guards:** nobody deliberately uses collective rhythm, and nothing names rhythm as the cause.
- **Exit state:** the question is sharper, and nobody has answered it.

### D8. B03's ending answers both Veil questions (E42, S04, E44, E46, E48)
- **Mystery** (by the close, in the cast's and the city's possession, argued in ordinary words):
  - it breaks through at weak places (E13, E23);
  - breaches worsen where it has broken before (E13, E30);
  - it can tear a district permanently (E42's sealed site);
  - it leans southwest (E15, E48).

  E42's Exit state *Undeniable; unexplained* becomes *undeniable; how it behaves known, why it exists not*. The origin stays reserved.
- **Dramatic:**
  - *who controls what is known*: S04's official account controls it, and it also leaves out the child, an erasure the reader can see (D5). Trip's board, E42's receipts and Tahl's rule (E48) answer it from below.
  - *what telling the truth costs*: Baz's life (the reader only), Lucien's call to Helena (E44), and Tahl's remorse.
- **Exit state:** Veil's questions are answered for the reader. The cast's funder split is carried to B04.

### D9. Nyla's exit state and the Neon handoff (E40, E45, E48)
- **Story job:** B03 does not close her.
- **Change:**
  - She leaves B03 converted, unstable, unable to ascend, and erased on paper, with Lanette.
  - The E45 vigil is for the missing; she is not among them.
  - The EP stays Tahl's. Her arc carries to Neon as the scandal behind Dominion's fall (reading (a): the faction escapes as "Concord").
- **Exit state:** open by design. In the control layer, a breadcrumb such as BC-NYLA-NEON is proposed [P].

## 3. Open for the author
1. **D4:** may the page certify the cause through the reader's knowledge (ii)?
2. **D5:** cut the sibling, or keep it as a separate rescue?
3. **D3:** where does the reveal fall: (a) E37, (b) earlier, or (c) both?
4. **D2:** is a new Lanette episode needed, or does she fold into existing ones?
5. **D6:** what form does Caldas's defeat take, and when?

## 4. Applied (2026-10-28, §627)
Author: "Approve all as recommended" (`decisions/PROPAGATION_DESIGN_APPROVAL_AUTHOR_RULING_2026-10-28.md`). D1–D9 are applied to `ebci/B03/` at the recommended options. Every *DESIGN pending* note is now an **Applied 2026-10-28 (§627, Dn)** note, and three cards with no pending note gained one (E29, E33, E46). **Not committed.** `grids/episode_beats.csv` was **not edited** (coordinator instruction: a concurrent B02 edit); the B03 row changes are listed below for the coordinator to apply. The validator passes (`tools/validate_canon.py`: no violations).

### Cards changed
- **All 48:** the blame-clause bracket in *Amendments applied* now records D4 (ii): the reader is made certain through E37; the narration states no cause.
- **Narrative brief changed (17):** A1.E01, E09, E12, E15; A2.E21, E23, E27, E28, E30; A3.E32, E34, E36, E37, E38, E39, E40, E42 (S04 included). E37 also gains Writer options (control layer).
- **Notes only (11):** A1.E13, E14; A2.E20, E29; A3.E31, E33, E35, E44, E45; EP.E46, E48. With the briefs above, that makes 28 cards carrying design work.

### Per item
| Item | Applied as | Cards |
|---|---|---|
| **D1** | B03's floor is B02's ceiling (E01 *Keep*: the signs, the interval, the method that finds people, escalating breaches; it follows B02's propagated end state). *No model forecasts* → *no public model* (E09, E27, E30). Dominion's forecast is shown to exist and never read out (E15, E28). E36's *exceeds every model* kept. | E01, E09, E15, E27, E28, E30, E36 |
| **D2** | Recommended placement: felt in A1 through Lanette inside Seraphine's finite circle (E12); **no new Lanette episode**. Coercion, offstage; the mechanism stays open and off the page; paper at most the excuse. Seraphine knows Nyla is taken, not where (E35). A2 carries her as an absence offstage; E40 pays it. | E12, E35 |
| **D3** | Option (a) only: Baz finds the program site himself at E37 and recognises his Houston funder working inside Dominion. Recognised, not explained; Baz and the reader only. No seed at E14, E20, E28 or E44. | E37 (brief); E14, E20, E28, E44 (notes) |
| **D4** | (ii): the reader is certain through D3; the narration states nothing. E36 *Prohibited* restated (no procedure or Mechanica vocabulary; the crowd as amplifier, shown, not certified); the Required observable stays physical. Program site in the older section (E29's bay; Technarc's upper floors read it, E33); the E13 precursor is its earlier leakage (control only). | all 48 (bracket); E36 (brief); E13, E29, E31, E32, E33 (notes) |
| **D5** | The child is Nyla (E36 *a child*, because Baz does not yet know; E37–E40 Nyla). **Sibling thread cut; the teenager stays as crowd** (E32, E34, E39; E40's parent is now Lanette). M10: her account is fragments and names no one; it is not credited (E39, E44). Erased on paper and felt through Lanette (E40). | E32, E34, E36–E40 |
| **D6** | See below. Seams: E30/E31 (C04 held), E38 (*No one murders him* held, now in *Keep*). | E14, E21, E28, E30, E31, E38 |
| **D7** | Argued once as *unknown* on Elisabet's whiteboard (E23); its inverse shown at E36 (a drawn, frightened, unconnected crowd makes it worse, never stated as cause). Not at E15. | E23, E36 |
| **D8** | E42: the behaviour is held in ordinary words (weak places, worse where it broke before, a district torn and kept torn, the southwest lean); Exit *undeniable; how it behaves known, why it exists not*; origin reserved. S04 also leaves out the child. Costs of the truth noted at E44, E46, E48. | E42, E44, E46, E48 |
| **D9** | Nyla leaves B03 with Lanette and on no list (E40). Converted, unstable and unable to ascend in the control layer only. Not among the vigil's missing (E45); the EP does not close her (E48). **BC-NYLA-NEON [P] is not added** to `grids/breadcrumbs.csv` (out of scope; a packet that cites it would fail CHK_PACKET_LINKS); proposed for the ledger. | E40, E45, E48 |

### D6: Caldas's form of defeat. **Ruin through exposure** (writer-thread choice; the author may override)
- **On the page:**
  - **E21:** the exposure begins. Seraphine puts his registry canvass, with his name, on the rota's record, where it joins the trail B01 left on him (Mr. Ledet's complaint, the deputy's report, C43).
  - **E28 (late A2):** the defeat. At the protocol meeting, seen by the anonymous institutional ensemble, the Dominion takes back his free rein and his place. The fall is plain and final, and nothing points to what he does next.
- **The revenge:**
  - The faction's dawn run in the older section is its own operation.
  - Caldas only routes the booking to Baz's table (E30), so Baz's own reason takes him there.
  - Tahl's coordinates, which are Tahl's alone, draw the crowd that amplifies the leak.
  - Who sent the booking, and whether before E28, stays ambiguous.
  - *No one murders him* is held: the leak and the second fall kill him. The guilt is shared between Caldas's design and Tahl's coordinates (M11) and is unproven to the cast.
- **Why ruin, not death or bare exposure:**
  1. **Death** would force the plan to predate the defeat, which removes the ambiguity the author allowed. It would also put a second death beside Baz's in a book that forbids a second spectacle.
  2. **Exposure alone** leaves him with his post, so his arc would not read as closed.
  3. **Ruin** leaves him with no command, which is exactly why his revenge can only exploit the faction's operation and cannot run it. That is the seam D6 asked for.
  4. **It is built from existing cards:**
     - E21's door and its *one with a name*;
     - B01's recall *upstairs* and its paper trail;
     - his status as leadership's man, which means leadership can drop him (Dominions.md).
  5. **It fits Neon Q2:** Helena, not Caldas, delivers the B04 E16 demand, so a ruined Caldas needs no Neon errand.
  6. **It answers the Veil question** of *who controls what is known* (a record defeats him).

### B03 beat-row changes for `grids/episode_beats.csv` (not applied; for the coordinator)
Change only the `beat_function` cell in each row below. ECID values are unchanged, and no rows are added or removed.

| BID | beat_function: was | beat_function: now |
|---|---|---|
| S1.T1.B03.A1.E12-BT01 | the circle | the circle, and Lanette |
| S1.T1.B03.A2.E28-BT01 | the protocol meeting | the protocol meeting, and Caldas dropped |
| S1.T1.B03.A2.E30-BT01 | the logs | the logs and the dawn booking |
| S1.T1.B03.A3.E37-BT02 | freeing the child | the room, and freeing Nyla |
| S1.T1.B03.A3.E40-BT01 | the staging point | the staging point, and Lanette |

### Still open (unchanged by §627)
- The coercion mechanism (§625 §3).
- The time span between trilogies.
- Whether D1's E01 list matches B02's propagated end state. Check it after the B02 pass lands.

### Flagged, out of scope
- `act_overlays/act_overlay_S1_T1_B03_A3.json` still carries the *W4 exception at E14* basis note (§1).
- `canon/characters/BazID.md`, `canon/factions/Dominions.md` and the Caldas row in `canon/cast_registry.csv` should record the ruin at E28 once the author confirms the form.
