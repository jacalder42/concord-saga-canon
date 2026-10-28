# Neon and Loom architecture: propagation of the October rulings (2026-10-28)

**Status:** PROPOSAL ONLY. Non-canonical. No existing file is edited by this document and nothing is committed.
**Author instruction:** "Agreed proceed" (propagation pass, after §626; `decisions/NYLA_SAGA_PLACE_AUTHOR_RULING_2026-10-28.md` §4 "Next").
**Scope:** the Neon (B04–B06) and Loom (B07–B09) **episode architecture**, which is design-level (Tier B, provisional). Changes are stated at the level of **Story job / turn** and **Exit state**, with placement. No beats, no prose, no dialogue.

**Classes:**
- **MECH**: wording or lexicon only; it follows mechanically from a ruling and is safe to apply later without a new decision.
- **DESIGN**: changes a story job, an exit state, a placement or an episode's owner; needs author approval.
- **AUTHOR**: a question the author must answer before the DESIGN item can be applied.

**Source keys:**
- **A4–A9**: `proposals/B0{4..9}_EPISODE_ARCHITECTURE_PASS3_2026-09-27.md`
- **NREC / LREC**: `proposals/{NEON,LOOM}_RECONCILIATION_FOR_EPISODE_ARCHITECTURE_2026-09-27.md`
- **BX4–BX9**: `book_context/book_context_B0{4..9}.json`
- **DOM**: `canon/factions/Dominions.md`
- **GRID**: `grids/milestones_payoffs.csv`
- **SN / SL**: `reports/TRILOGY_SHEET_{NEON,LOOM}_2026-10-28.md`
- **MX**: `proposals/TRILOGY_RESOLUTION_MATRIX_2026-10-28.md`
- **R624**: `decisions/TRILOGY_CONTRACT_AND_QUESTIONS_AUTHOR_RULING_2026-10-28.md`
- **R625/R626**: `decisions/NYLA_SAGA_PLACE_AUTHOR_RULING_2026-10-28.md` (§1–§3 = §625; §4 = §626)
- **R620**: `decisions/B01_ELISABET_SIGNATURE_BREACH_LEXICON_AUTHOR_RULING_2026-10-28.md`
- **COI**: `decisions/B01_CANON_OPEN_ITEMS_AUTHOR_ANSWERS_2026-10-18.md` (as carried in DOM:244–262 and BX4 `_concord_open_items_answers_2026_10_18`)

**Already done elsewhere (not repeated here):** the trilogy cards `canon/trilogy_neon.md` and `canon/trilogy_loom.md` carry the §624 questions, the contract and the §625/§626 book-3 answers (commit 210c610). This proposal only brings the **episode architecture** into line with them.

---

## 0. Summary of what changes

| | Neon | Loom |
|---|---|---|
| **Biggest DESIGN moves** | The split is staged in B04 Act I (from Baz's effects). Nyla's conversion becomes **B05's Act III public set-piece**, which also cures B05's weak standalone. Virelli's leadership falls in B06 Act I. The Concord co-option runs B04 → B06 in five steps | The Concord's collapse is placed in **B08 Act II** (recommended) as the day its authorship comes out through MT. The triangle is shown with Kade knowing it (B07 E16). The Choirless are named in B07–B08. The swamp's meaning is given on the page at B07 E08 |
| **MECH sweeps** | The breach / scar / Wound lexicon in A6 and GRID. Record the questions in A4 and A6 §0. M10's "child" is Nyla | The lexicon in A7–A8, GRID M45 and `trilogy_loom.md` Key Locations. "No Nyla" in the protected checks. Line 8 relabelled |
| **AUTHOR questions** | Q1 Elisabet's route; Q2 who delivers M05 if Caldas is defeated in B03; Q5 the Hope–Caro turn | Q3 the collapse book; Q4 the Wound count; Q6 Ren Bellande as M46's hands |

---

## 1. Neon (B04–B06)

### N1. The trilogy questions are recorded in the architecture
- **Ruling:** R624 §2 (Neon row).
- **Files and episodes:** A4 §0 Identity; A6 §0 and §6 Exit state; A5 §0.
- **Proposed change:**
  - A4 §0 gains a line: *Trilogy questions (§624):* the mystery and dramatic questions, verbatim.
  - A6 §6 gains: *Answers:* the mystery is answered at E47 (linked, several, in order, the first one last); the dramatic question is answered **no** at E45, with a partial yes by mortal means at E43/E47.
- **Class:** **MECH**.

### N1b. The mystery question is asked on the B04 page
- **Ruling:** R624 §1 rule 1 (asked in book 1). SN §4 marks B04's Wound axis a GAP ("Santa Fe at most a direction", A4 Checks).
- **File and episode:** A4 **E27** "Elsewhere, Too" (Tahl, a report theatre).
- **Proposed change:**
  - **Story job:** among the multi-city static reports, one **Southwest reading he cannot place or link**. He publishes it as unknown. No Santa Fe name and no count.
  - **Turn:** MT's question is now "is it linked?"
  - B04 E30 already carries the dramatic question ("the right act is not enough"). Record it there; no change.
- **Class:** **DESIGN** (small).

### N2. The funder split: the cast learns in B04, around Baz's death
- **Rulings:** R624 §3 (the reader learns in B03, the cast in B04, and that is the cause of the split); R626 (the funder faction ran Nyla's conversion: **one revelation**); COI as carried in DOM:254–262 (Baz is still paid by Dominion; Virelli suspects by M05; Helena is a possible member).
- **Files and episodes:** A4 E01, S01, **E04**, **E06**, **E08**, E10; A4 §0 Entry state; A4 §5 Exit state; BX4 `this_book` for both Concord keys.
- **Proposed changes:**

| A4 ep | Current job | Proposed Story job / turn |
|---|---|---|
| **E01** | Helena's favour gives access; "a debt to the Dominion" | Unchanged. **Note added:** the debt may be to the faction rather than to leadership (Helena is a possible member, not locked). No page claim |
| **S01** | The corrected notice omits the entry rule and Technarc | **Also omits the child.** The conversion erased her name on paper (R625 §1.2). The record says Baz died "rescuing a civilian" |
| **E04** | Baz's sister arrives | **She brings his effects.** Among them is what Baz found in B03 before he died (R624 §3: "Baz discovers it, or the page shows it"). **Turn:** the circle holds the proof without having read it yet |
| **E06** | Rex, Detroit (short; "compressed", A4:E06 note) | **Re-purposed as "The Split"** (owner: **Elisabet**, which lifts her from 3 POV). The circle refuses the funder's continued money and consents. **Turn:** the New Orleans circle stands alone, with no patron. Its funding is open and signed-for, plus mutual aid (provisional, COI 10:02; see N15). **Rex's Detroit content folds into E10** |
| **E08** | Lucien and Seraphine: guilt meets guilt | **Same, plus they read Baz's discovery:** Baz's funder was a faction inside Dominion, it paid him to the end, and it ran the operation on Nyla. **Turn:** each one's guilt acquires an author outside themselves, and the strain begins anyway |
| **E10** | Rex arrives in NOLA | Absorbs E06's "contract lost" in a line or two. Rex POV goes from 6 to 5 |

- **A4 §5 Exit state** gains:
  - the circle has split from the funder;
  - it knows the faction ran Nyla's conversion;
  - **it cannot prove it in public:** the paper runs through Hollen, leadership's front, so the record points at "Dominion".
- **Class:** **DESIGN**.

### N3. Nyla's Neon arc
- **Rulings:** R625 §1.2–§1.5; R626 (reading (a)).
- **Files and episodes:** A4 E02, E29; A5 E05, E08, **E41**, **E44**, E45; A6 A1 (a new supplement), and one A2 Seraphine episode.
- **Proposed change:** see **§3.1** for the full placement table.
  - **Exit-state additions:**
    - **A4 §5:** Nyla is alive, converted, unstable and nameless on paper. Lanette keeps her hidden. Protocol 9 makes hiding dangerous.
    - **A5 §5:** the scandal is public; "Dominion" is blamed; the faction speaks as "Concord".
    - **A6 §6:** Dominion's leadership has fallen. Nyla's name is restored on paper. **Her arc is closed: no Loom hook.**
- **Guards:**
  - The procedure is never shown (R625 §1.5).
  - Nyla is about 9–10, so she has no POV. Her role is carried through Lanette and MT (R625 §3).
  - Going public is **their choice**, never an accident or leak event.
  - Nothing names the cap, Mira or the cycle (R625 §1.6).
- **Class:** **DESIGN**.

### N4. Dominion's rise and wane, now with a cause: Virelli falls
- **Rulings:** R625 §1.3 (the scandal **causes** the wane); R626 (Virelli's leadership falls in Neon); DOM:108–111 (rise early in Neon, wane by its end). This resolves SN §10 #5 ("the ladder stops after one demand").
- **Files and episodes:** A4 E07, E16; A6 A1 (new supplement S-POL, and **E08**); A6 §6.
- **Proposed changes:**
  - **A4 E07:** Dominion's Warehouse perimeter is part of the public record fight. This is the **"overt prominence" rung**: Dominion is visibly a public actor.
  - **A4 E16 (M05):** the demand ("bring your data") is coloured by **Virelli's suspicion of the faction** (COI: "by B04 … he suspects"). Lucien refuses. The turn is unchanged. Virelli stays "outgrown" (GRID:6). See N16 for who delivers it.
  - **A6 A1, new POL supplement** (after E07, before E15): **Virelli's leadership falls**, framed publicly as accountability for the B05 scandal.
  - **A6 E08 "Geometry"** (Lucien) receives it as a remote receipt from Vienna, through Helena or Holt. The receipt sits beside his dissociation and does not replace it. It adds a Lucien beat to B06, whose Lucien load is thin (A6 Checks).
  - **A6 §6 Exit state:** Dominion's institutional legitimacy has gone and its doctrines persist (DOM:100–106); "Concord" holds the vacuum.
- **Class:** **DESIGN**.

### N5. The Concord co-option, staged
- **Rulings:** R626 ("the faction escapes the blame by co-opting the name 'Concord'"); COI (it co-opts the name "when resonance goes public in Neon", drifts into insincerity, and collides with the loose network that keeps the word honestly); SN §10 #2 (zero mentions in A4–A6).
- **Files and episodes:** A4 E06, E25, E41; A5 S02, E44–E45; A6 A1 supplement; A6 §6.
- **Proposed change:** five steps; see **§3.2**.
- **Class:** **DESIGN**.

### N6. Re-plant the B01 camp before B06 E47
- **Rulings:** R624 §1 rule 3 (a partial payoff inside the trilogy); MX §5 Neon fix 1. Guards: R620 §1 (the camp is a **breach**, not a Wound) and §4 ("the camp is not the origin"); FT:22 (the camp's link to Honey Island is "allowed later", OPEN).
- **Files and episodes:** A5 **E31**; A6 E05 (kept); A6 E47.
- **Proposed changes:**
  - **A5 E31 "The Colorstorm Turns"** (Seraphine): **the episode is set at the camp's edge, in the swamp.** The Colorstorm "points nowhere"; **her old ache does point somewhere**, and she does not say where. It is a breach she feels as hers.
    - **Turn:** a Neon reader now has the place on the page.
    - **Guard:** no cause, no origin, no count, and no Dré exposition beyond his name.
  - **A6 E05** keeps its re-plant ("unnamed and unexplained").
  - **A6 E47** pays off a place the reader has now seen in this trilogy.
- **Class:** **DESIGN**.

### N7. Show the B03 VT brush again in Neon
- **Ruling:** MX §5 Neon fix 2. Constraint: there is **no Tahl VT contact in B04–B05** (ruled, NREC:53).
- **Files and episodes:** A4 **E03**; A5 E34; A6 E42.
- **Proposed changes:**
  - **A4 E03 "The Morning Feed":** the private counterfactual gains **the brush as memory, specific to the senses** (what it was like, where he stood). This is not contact.
    - **Turn:** the reader carries the feeling into B05.
  - **A5 E34:** "it matches what he felt in B03" now points back to a Neon page.
  - **A6 E42:** the third rung is unchanged.
- **Class:** **DESIGN** (small).

### N8. Hope–Caro: one Neon-level turn
- **Rulings:** MX §5 Neon fix 4. Constraints: in B05, "Hope only notices" (A5 Checks); in B06 E45, "Hope does not act"; Hope's first act is B07 E03.
- **Files and episodes:** A6 **E45** (the VT side) and A6 E32.
- **Proposed change:**
  - **A6 E45:** in the VT-side moment after Silence collects Tahl, **Hope's attention is shown on Caro in New Orleans, holding Seraphine (E32)**. Her not acting is a **choice with a cost**: she keeps to Caro.
  - **Turn:** the relationship acquires a price inside Neon, without Hope acting on the world.
  - **Exit state:** Hope has a preference. Caro knows nothing.
- **Class:** **DESIGN** and **AUTHOR** (Q5).

### N9. Lucien–Silence: one Neon-level turn
- **Ruling:** MX §5 Neon fix 4. Constraint: B07 E12 keeps "Silence's guidance begins".
- **Files and episodes:** A6 **E26** "The Spiral"; A6 E30.
- **Proposed change:**
  - **A6 E26:** the dissociation (*Silence as fracture*) **costs him something concrete**: he is absent during the channel's live window with Tahl. That window is part of the dread that E30's "Six Hours" closes.
  - **Turn:** his fracture has a price in this trilogy.
  - **A6 E28:** Seraphine's "holding, not fixing" now answers a real cost.
  - No contact with Silence occurs in Neon.
- **Class:** **DESIGN**.

### N10. The elders' corridor: one Neon-level turn
- **Ruling:** MX §5 Neon fix 4 (BC-ELDERS-CORRIDOR, B04 E38 → B08 E10).
- **Files and episodes:** A6 **E21** "Inside", or E25 "Landfall" (Tahl, Santa Fe).
- **Proposed change:**
  - **Santa Fe's Filament elders try the corridor technique**, which reached them through the network after the Riot. **It holds one evacuation corridor for a finite interval and cannot touch the Rupture.**
  - **Turn:** a discovery. The technique scales to people, not to a Wound.
  - It sets up B08 E10 as the next rung (with the crew, and a hold that is temporary and costly).
  - **D5 card owed.**
- **Class:** **DESIGN**.

### N11. B04 as an entry point
- **Ruling:** R624 §1 rule 2; SN §3a (two GAPs: the split, and "what resonance is").
- **Files and episodes:** A4 **E15**, **E25**, E02; A4 §0.
- **Proposed changes:**
  - **The split** is re-delivered by N2 (E04, E06, E08).
  - **"What resonance is" (Veil's behavioural answer, §619 principle):**
    - **A4 E15 "The Aftershock":** Elisabet's measurement at the vigil shows on the page that **it breaks through at weak places**, that **each later break at the same breach is worse**, and that **a warning changes outcomes unevenly**. The crowd's competing explanations are kept.
    - **A4 E25 "Known, Inferred, Mapped":** her map makes the same distinctions usable, as known / inferred / unknown.
    - **Guard:** behaviour, not cause. No cap, no "holding back" (R620 §3).
  - **Nyla** is re-delivered at E02 (§3.1).
  - **A4 §0** gains a line: *Entry point (contract test 2): the split, Nyla, and resonance's behaviour are re-delivered at E02–E15.*
- **Class:** **DESIGN**.

### N12. B05's weak standalone
- **Rulings:** R624 §1 rule 5 (an ending that lands). SN §3c: B05 is the "weakest standalone"; A5 §0 has no Act III set-piece "by design".
- **Files and episodes:** A5 §0; A5 **E41**, **E44**, **E45**; A5 §5.
- **Proposed changes:**
  - **A5 §0:** amend "Act III is not a second set-piece" to read: **Act III's set-piece is civic, not weather: the Nyla disclosure** (§3.1).
  - **A5 E44** (Tahl, "Imminent, Unprovable"): **two posts in one episode.** What he cannot prove (Santa Fe) is filed. What he can prove (Lanette's consented testimony and the paper trail) spreads everywhere.
    - **Turn:** the world acts on scandal and not on warning. This is Neon's dramatic question in miniature.
  - **A5 E45:** the book closes on a public that has been moved, at the wrong target and for the wrong danger.
  - **A5 §5:** B05 now answers its own question: can commitment survive distance? Yes, and the truth, once public, moves the world in the wrong direction.
- **Class:** **DESIGN**.

### N13. The Santa Fe Rupture stays open as the "no"
- **Rulings:** R624 §2 (Neon dramatic: "Answer: no"); this is the condition MX §5 Neon 5 / D5 attached to keeping the Rupture open.
- **Files and episodes:** A6 §0 and §6; A6 E16 (unchanged).
- **Proposed change:** A6 §6 gains a line: *the persisting Rupture is the trilogy's answer, not a dependency* (closed in B08 E10). MX D5 is answered by §624's "no".
- **Class:** **MECH**.

### N14. Lexicon: Santa Fe is a Wound; breaches and scars are local
- **Ruling:** R620 §1 (breach / scar / **Wound**: the four, capital W, reserved).
- **Files and episodes, with proposed wording:**
  - **A6 E42** (line 110): "the shape of the wound pattern" → "the shape of the **Wound** pattern".
  - **A6 E47** (line 120): "the tears are linked, there is more than one" → architecture text: "the **Wounds** are linked …". **Tahl's own words in the fragment stay with B06 EBCI (D8)**, and a character may say "tears" there.
  - **A6 §6** (line 142): "several linked tears" → "several linked **Wounds**".
  - **GRID M20 and M39** (lines 23, 26): "wound pattern" → "**Wound** pattern".
  - **A4 E15:** the Warehouse site after the aftershock is an active **breach**, not a scar (R620 §1).
  - **A6 §0:** add a note. Santa Fe is Wound 1 at author level. On the Neon page it is never called a Wound, and no count is given. M38's terms Fracture and Rupture stay as they are.
  - **IDs** (BC-SWAMP-WOUND and the rest) are left unrenamed.
- **Class:** **MECH**.

### N15. Elisabet's open money against her route to Reykjavík
- **Sources:** COI 10:02, provisional: open money she can sign for "gives Elisabet a reason to stay in New Orleans". A5 E10/E20 and A6 E02–E41 send her to Reykjavík in B05 A1 and keep her there through B06 (SN §10 #4).
- **Files and episodes:** A4 E06 (N2); A5 **E10**.
- **Options:**
  - **(a) Recommended. The money becomes the reason for the route.** The Nordic civil-protection funding she signs for in B04 E06 carries a condition: the comparison work is done in Reykjavík. A5 E10 then becomes "the grant's terms pull her north". The network's money continues under her signature at a distance. This fits COI's option "if her grant comes with strings, she recognises the pattern fastest", so she sees it as a funder's leash and accepts it knowingly.
  - **(b)** Keep the route and drop the "reason to stay" clause from the provisional direction.
  - **(c)** Keep her in New Orleans. This rebuilds about 10 Reykjavík episodes and loses B06's instrument of distance. Not recommended.
- **Class:** **DESIGN** and **AUTHOR** (Q1).

### N16. Caldas is defeated in B03, but B04 E16 has him deliver M05
- **Sources:** R624 §4 (Caldas is defeated in B03; the form of defeat is open); A4 E16 ("**Caldas Ren** delivers the Dominion's demand"; D18).
- **File and episode:** A4 **E16**.
- **Proposed change:** depends on the form of defeat.
  - **Ruin or exposure:** E16 can stand, as a diminished Caldas carrying a last errand. But his Veil arc must read as closed, so the errand is a bearer's role, not a pursuit.
  - **Death:** **Helena delivers it** (she gave the favour in E01, so the price arrives from the same hand), or an unnamed officer does.
  - **Recommended either way: Helena.** That keeps Caldas closed in Veil.
- **Class:** **DESIGN** and **AUTHOR** (Q2).

### N17. Stale wording tied to Nyla
- **Ruling:** R625 §1.1 (M10's "the child" is Nyla).
- **Files and episodes:**
  - **A4 E02:** "The child's rescuer has a face" → "**Nyla's** rescuer has a face". See §3.1 for the re-scope.
  - **GRID M10** (line 12): add a note. The child is Nyla (§625).
  - **Outside architecture (noted only):** the `canon/cast_registry.csv` B24 guard "no new catastrophe built on her" is superseded by §625.
- **Class:** **MECH**.

### N18. Guard: the northern scar and Reykjavík
- **Ruling:** R620 §5 (the northern site is far north, rural, unnamed, never Reykjavík city, not a Wound, not linked).
- **Files and episodes:** A5 E20, E28; A6 E02.
- **Proposed change:** add a guard line to the A5 Checks. Elisabet's Reykjavík comparison never links her northern scar to the Southwest or counts sites.
- **Class:** **MECH**.

---

## 2. Loom (B07–B09)

### L1. The trilogy questions are recorded and asked early
- **Ruling:** R624 §2 (Loom row).
- **Files and episodes:** A7 §0; A7 E17, E19, **E16**; A9 E41, E45.
- **Proposed changes:**
  - **A7 §0** gains the two questions verbatim (MECH). Record where they are asked:
    - the mystery at **E17** (renew the cap; the price hidden) and E29 (Mira: "it cost");
    - "close the circuit before the factions find the site" at **E19**.
  - **Kade's half** ("responsibility over righteousness") is currently first tested at E36. Ask it at **E16 "Taking Over"**: he takes MT knowing what Tahl's rule cost and decides what his own rule is (see L4 for the same episode). DESIGN.
  - **A9 §5:** the answers are E45 (no; held jointly) and E41 (Kade's stand).
- **Class:** **MECH** (record); **DESIGN** (E16).

### L2. The Concord's collapse is placed: the day its authorship of the Nyla program comes out
- **Rulings:** R626 ("In Loom, the Concord's collapse is the day its authorship of the Nyla program comes out"); BX9 (collapsed **by the Mending**; no successor).
- **Files and episodes:** A7 E10, E28; A8 **E23–E27**, a new **S02**; A9 E47; BX7–BX9 Concord keys (`this_book`).
- **Proposed changes:**
  - **B07 re-establishes the Concord** for a Loom-first reader:
    - **E10 "Uneven":** a Concord relief point among the dark clinic and the closed bridge;
    - **E28 "Uptown, Failing":** the Concord is among the relief that withdraws. This is its insincerity, visible.
  - **B08 A2 (recommended):**
    - **Holt's sealed Warehouse file** (A4 E23; left with Holt in A5 E04) reaches Lucien **after Dominion's fall** as a remote receipt (with E23).
    - Lucien sends it into **MT**, because "the strands meet only through MT" (A8 §0).
    - **E27 "A Face"** (Kade): in the same episode where he faces one person his permission hurt, **he publishes the Concord's authorship**, as known against inferred.
    - **Turn:** he exposes someone else's crime with full righteousness while unable to own his own. This is Loom's dramatic question, sharpened.
    - **New S02 (POL):** the Concord's collapse, in public. Nyla appears only as the already-public Neon scandal: **no new Nyla scene and no Nyla load** (R625 §1.3).
  - **A9 E47:** the name "Concord" is free again for the loose network. This bears on the GAP "Accord or Concord" (SL §7), which is left open.
- **Class:** **DESIGN** and **AUTHOR** (Q3: B08 A2 recommended, or B07 A2).

### L3. Nyla carries no Loom load
- **Rulings:** R625 §1.3; R624 §5 (Line 8 is not a reserved reveal).
- **Files and episodes:** A7–A9 §Checks "Protected"; MX §7 D6; SL §9a (the Line 8 row) and 10.7.
- **Proposed changes:**
  - Add "**No Nyla** (§625: her arc ends in Neon)" to the Protected rows of A7, A8 and A9.
  - **MX D6** is closed by ruling: Line 8 stays Dominion's misreading (see L10), and no one-who-feels-it-first is staged in Loom.
  - SL 10.7's "she is the obvious one who feels it first" is withdrawn.
- **Class:** **MECH**.

### L4. M53: Tahl's triangle on MT, with Kade knowing it, in B07–B08
- **Rulings:** MX §5 Loom fix 1; GRID:53 (M53, ruled; the triangle is implied in B09 E48).
- **Files and episodes:** A7 **E16**; A8 **E13**.
- **Proposed changes:**
  - **A7 E16 "Taking Over":** he finds the triangle on every one of Tahl's posts and **decides not to use it: it is Tahl's.**
    - **Turn:** the reader sees Kade knowing it as Tahl's mark.
    - E48's triangle then reads as Tahl's, unambiguously.
  - **A8 E13 "His Last Broadcast"** (Rex): the triangle is on the recovered device's last post. It is a second sighting in Loom, unremarked.
- **Class:** **DESIGN**.

### L5. The Choirless are introduced in B07–B08
- **Sources:** MX §5 Loom fix 3; SL 10.1 (zero mentions in A7–A8). Constraints: Choirless.md Loom era ("quiet policies enacted at scale", "no longer need a name"); D18 (not in the NOLA search); unresolved into the cutaway (B09 E41).
- **Files and episodes:** A7 **E28**, **E32**; A8 **E16** or **E32**; an A8 governance glimpse; A9 E37.
- **Proposed changes:**
  - **A7 E28:** the "quiet-zone pressure" is **named as the Choirless's doctrine, now ordinance**.
  - **A7 E32:** quiet-zone enforcers are one of the separately attributable parts of the civic break.
  - **A8 E16 or E32** (Kade, Houston): **Choirless quiet patrols are the foil the angry splinter defines itself against.** This seeds the B09 E37 collision.
  - **A8:** one of the three governance glimpses (Mound City) is a Choirless-derived quiet policy enacted at scale.
  - A9 E37 then pays off pressure the reader has seen.
- **Class:** **DESIGN**.

### L6. Why the swamp matters, within the FIRST_TEAR guard
- **Sources:** MX §5 Loom fix 2; SL §9a. Guards: FT:22; R620 §4 ("the camp is not the origin"); `canon/characters/SeraphineIdentity.md`:276 ("she never learns her part").
- **Files and episodes:** A7 **E08**; A9 **E30**.
- **Proposed changes:**
  - **A7 E08 "The Fragment, Together":** when she tells the channel the first one is the swamp, **she says why it is hers**: Dré's death at the camp, the ache since, and the place (re-planted in Neon, N6).
    - **Turn:** a B07-first reader has the significance.
    - **Guard:** she states a feeling and a history, not a cause. Nobody says "origin". Her part stays unknown.
  - **A9 E30 "The Edge":** at Honey Island's edge, Dré's memory is present. One line of job, no exposition.
- **Class:** **DESIGN**.

### L7. How many Wounds the fragment gives
- **Sources:** LCK:24 (ruled: "the shape (four wounds, Honey Island last)") against GRID:26 M39 (ruled: "several … no place named"); MX D7; SL 10.2.
- **Files and episodes:** A6 E47; A7 E17, E26; A8 E18.
- **Recommended reading (it reconciles both rulings):**
  - **The fragment says "several"** (M39).
  - **"Honey Island last"** reaches the crew at **B07 E17**, through Silence and Hope's plan (already in A7).
  - **"Four"** is Elisabet's mapping at **B07 E26** (inferred), **confirmed at B08 E18** (M47; already "four Wounds; this is the second").
  - **LCK:24** is then read as what the crew holds by B08, not what the fragment says.
- **Class:** **DESIGN** and **AUTHOR** (Q4).

### L8. Loom lexicon, including "Santa Fe Scar"
- **Ruling:** R620 §1.
- **Files and episodes, with proposed wording:**
  - **`canon/trilogy_loom.md:13` Key Locations:** "Santa Fe Scar" → "Santa Fe (Wound)". The card's own lexicon note (line 38) already flags it.
  - **A7 §0** (line 29): "Tahl's shape of the wounds" → "**Wounds**". The same applies at **E17** (line 86) and at E19 and E26.
  - **A8 Act I** (line 55): "the scar holds" → "the **Wound** holds".
  - **A8 E05:** "The scar, the memorial" → "the **Wound**, the memorial".
  - **A8 E08** (line 67): "the scar shows … this is a wound, not where it began" → "the **Wound** shows … this is a **Wound**, not where it began".
    - **The public version** "a wound, not the origin" → "**a breach, not the origin**". The public never learns the four.
  - **A8 E10:** "the scar remains (§42A.2)" → "the **Wound** remains marked (§42A.2 read as breach)".
  - **A8 §5** (line 175): "Three wounds held" → "Three **Wounds** held".
  - **GRID M45** (line 39): "the first wound … the scar shows the old way failing; it is a wound" → "**Wound**".
  - **Kept:** A7 E29 "the Warehouse scar" and NOLA-06 "(the scar)" are correct **only if** the Warehouse breach has been quiet since B04 E15. Record that condition in A7.
- **Class:** **MECH**.

### L9. B08's cliffhanger as a standalone risk
- **Sources:** R624 §1 rule 5; SL §5 (B08 is a standalone risk); M48 (ruled: Serpent Mound runs continuously across the break; it stays).
- **Files and episodes:** A8 **E42**, **E43**; A8 §5.
- **Proposed changes:**
  - **A8 E43 "Finish It"** is marked **B08's answer beat**. Can the Wounds be held? Yes: three are held, at a price. The question closes before the cut.
  - **A8 E42 "Watching"** (Kade): "posts something ambiguous" becomes a **decisive act**. He **lets the miracle claim stand as his own**, a chosen lie.
    - **Turn:** Kade's B08 strand lands ("the fall"). It sets up B09 E03.
  - **A8 E45** stays the cut.
  - **A8 §5** gains: *B08 answers its questions at E42–E43; E45 is the hook only.*
- **Class:** **DESIGN**.

### L10. Line 8 is Dominion's wrong belief, so its inversion can pay off
- **Ruling:** R624 §5. Provenance: `proposals/B01_REWRITE_ENGINE_KNOWLEDGE_MAP_AND_LADDERS_2026-10-14.md`:22. The X1 rhythm gate stands on its own wording.
- **Files and episodes:** SL 10.6 and 10.8; A5 E44 (Neon); A8 E27 (L2); A9 **E45**.
- **Proposed changes:**
  - **Relabel (MECH):** SL 10.6's "reserved collective-rhythm answer" becomes "Dominion's doctrine (the hunt for firsts)".
  - **The Neon partial payoff (DESIGN):** the Nyla program **is** the doctrine's cost. A5 E44's disclosure is the doctrine made public (the faction "seeks firsts", DOM:251).
  - **The Loom payoff (DESIGN):**
    - **A8 E27:** the Concord's authorship exposes a program built on "find the first and you find the lever".
    - **A9 E45:** Seraphine's answer, held jointly, is **the inversion understood on the page**: no first and no lever, the Veil held by many.
    - **Guard:** no crowd staged and no rhythm confirmed beyond what Mechanica's B09 reveal allows. Whether Line 8 stays on the B01 page is the editing thread's call.
- **Class:** **MECH** (relabel); **DESIGN** (payoffs).

### L11. Ren Bellande's required Loom payoff
- **Source:** `canon/cast_registry.csv`:10 (A09): "helper → direct action → coercion … not evil, not secretly controlled, not Choirless"; "**OPEN BUT PAYOFF REQUIRED in Loom**". Neon has Ren at A4 E26 and E39 only. A7–A9 have none (SL 10.14).
- **Files and episodes:** A5 **E21**; A8 **E16**, **E20**; A9 **E47**.
- **Proposed changes:**
  - **A5 E21 "Not a Symbol":** Ren's faction is one of the two that want Seraphine as their symbol. This keeps him alive across B05.
  - **A8 E16 / E20:** **Ren's people are the Houston group that wants to act.** The splinter's hands at M46 reach the coercion rung of his arc. Kade authorises; Ren's people strike.
    - **Guard:** not evil, not Brightbreak, not Choirless.
  - **A9 E47:** **Ren is among the rebellion's people Kade reintegrates** (M35). That is his payoff, a return, not a punishment.
- **Class:** **DESIGN** and **AUTHOR** (Q6).

### L12. B07 as an entry point: the world the factions left
- **Ruling:** R624 §1 rule 2.
- **Files and episodes:** A7 E10; A7 §0.
- **Proposed change:**
  - **A7 E10:** carries a one-line state of the world: Dominion's legitimacy has gone, the "Concord" holds the name, and the Nyla scandal is the reason (background only).
  - **A7 §0 Entry state** gains the same line.
- **Class:** **DESIGN** (small).

---

## 3. Recommended placements

### 3.1 Nyla's Neon arc (books and episodes)

| Book / ep | Owner | Story job / turn | Exit state |
|---|---|---|---|
| **B04 E02** (re-scoped) | Seraphine | She brings Baz's name to **Lanette**. Nyla is alive, converted, unstable, and nameless on paper. **Turn:** her B03 choice now has a cost with a name, and a living child | The reader knows Nyla's state (entry-point re-delivery) |
| **B04 E08** (N2) | Lucien + Seraphine | Baz's discovery: the faction ran the operation on Nyla | The cast knows; the public does not |
| **B04 E29** (optional) | Seraphine + Caro | Protocol 9's registrars make hiding a leaking child dangerous. They protect the household. Nyla's case is **the reason hiding stops working** | Pressure toward going public |
| **B05 E05 / E06** | Tahl | Seraphine brings Lanette's question to the meeting or the channel: what MT would do with a true thing that names an institution. **No decision** | The channel is a possible route |
| **B05 E08** (unchanged job) | Tahl | The Last Clear Act ("people altered by an institution"). **Lanette reads it** (one beat) | She knows which institution |
| **B05 E41** (re-scoped) | Seraphine | The quiet-zone knock comes to **Lanette's** block. **Lanette and Nyla choose to go public**, as their choice. Seraphine holds a door | The decision is made |
| **B05 E44** (re-scoped, N12) | Tahl | **The disclosure through MT:** Lanette's consented testimony and the paper trail through Hollen, as known against inferred. The child is not shown. The procedure is never described. It spreads; Santa Fe is filed | **The scandal is public; "Dominion" is blamed** |
| **B05 E45** | Seraphine | The book closes on a public moved by scandal and deaf to warning | B05's answer |
| **B06 A1 S-POL + E08** (N4) | — / Lucien | **Virelli's leadership falls.** The faction speaks as "Concord" | Dominion has waned |
| **B06 A2: E19 or E28** (one beat) | Seraphine | **Nyla's name is restored on paper.** Lanette's last on-page beat | **Her arc is closed. No Loom hook** |

**Why B05 Act III and not B06:**
- It gives B05 its set-piece and its answer (N12).
- It leaves B06 to Santa Fe, where the fall arrives as a supplement and receipts.
- It completes the wane "by Neon's end" (DOM:111) with B06 still to come.

**Why the cast cannot blame the faction in Neon:**
- The proof is the procedure record (Holt's file).
- Publishing it would show procedure on a child (R625 §1.5), which Lanette's consent excludes.
- Tahl's rule publishes only what is known.
- So the public sees "Dominion" (reading (a)), and the faction's authorship waits for Loom without the procedure (L2).

### 3.2 The Concord co-option (Neon) and its collapse (Loom)

| Step | Book / ep | Story job / turn | Exit state |
|---|---|---|---|
| 1. The refusal | **B04 E06** (N2) | The circle refuses the funder's money and consents | Patronless; the faction loses its "firsts" source in New Orleans |
| 2. The honest word | **B04 E25** | Elisabet gives her data to responders "through the network", the loose collection that keeps the word honestly (COI). Informal; no founding | The word is in honest use |
| 3. The first co-opted use | **B04 E41** (Tahl) | Among the camps claiming the Riot, **a "Concord" relief appeal appears**, funded and polished. Tahl notes it and does not know it yet | The name is taken in public |
| 4. The drift | **B05 S02** (the Chicago after-action record) | The record credits Caro's handoff to "**Concord** volunteers". This is credit theft, and the faction offers what the characters want (TGD:49) | The collision begins |
| 5. The escape | **B05 E44–E45 → B06 A1 S-POL** | When the scandal breaks, "Concord" condemns "Dominion" and steps into the vacuum Virelli leaves | **The faction escapes as Concord** (R626) |
| 6. Loom presence | **B07 E10, E28** (L2, L12) | Concord relief, then its withdrawal in Uptown | Re-established for the Loom reader |
| 7. **The collapse** | **B08 A2: E23 receipt → E27 MT post → S02** (L2) | Holt's file → Lucien → MT. Kade publishes the authorship. The Concord collapses | It is gone before B09, satisfying "collapsed by the Mending" (BX9) |
| 8. Coda | **B09 E47** | The name is free for the loose network (the name itself stays deferred, SL §7) | — |

---

## 4. AUTHOR questions

| # | Question | Recommendation |
|---|---|---|
| **Q1** | Elisabet's open money "keeps her in New Orleans", but the architecture sends her to Reykjavík in B05 (N15). Which gives way? | **(a)** The grant's terms send her north, knowingly |
| **Q2** | Caldas is defeated in B03, but A4 E16 has him deliver M05 (N16). What form does the defeat take, and who delivers the demand? | **Helena** delivers it, whatever the form |
| **Q3** | In which book does the Concord's collapse fall (L2)? | **B08 A2**, through MT (Kade, E27). Alternative: B07 A2 |
| **Q4** | Does the fragment say "several" or "four, Honey Island last" (L7; MX D7)? | **"Several"** in the fragment; four is inferred at B07 E26 and confirmed at B08 E18 |
| **Q5** | Does Hope's *attention* on Caro at B06 E45 stay within "Hope does not act" (N8)? | Yes: attention, not action. If not, the Neon turn moves to Caro's side alone |
| **Q6** | Are Ren Bellande's people the hands of M46's harm (L11)? | Yes, with his payoff the B09 E47 reintegration |

**Approvals needed (DESIGN, no question):**
- N2 (E06 re-purposed; Rex folded into E10);
- N12 (B05 Act III gains a civic set-piece, replacing "no set-piece by design");
- L9 (E42 becomes decisive).

## 5. Application order once approved
1. **MECH:** N1, N13, N14, N17, N18; L3, L8, L10 (relabel). These are safe now.
2. **After Q2:** N2, N4, N5, N11 (B04 re-scopes).
3. N3 and N12 (B05 Act III), then the B06 placements (N4, N8–N10).
4. **After Q3 and Q4:** L1, L2, L4–L7, L9–L12.
5. Update BX4–BX9 `this_book` in the Concord keys, then the GRID notes (M10, M20, M39, M45).
