# VEIL (B01–B03): trilogy resolution sheet

Read-only verification sheet, 2026-10-28. No novel prose. Repo root: `repos/canon` @ 94b3d2c (§623).

**Status labels.** **RULED** means an author ruling (cited). **DESIGN** means a proposal, approved design (Tier B), EBCI or an author "direction". **GAP** means canon is silent. **CONFLICT** means sources disagree, and both are quoted.

**Source keys.**
- `LED` = recovery/RECOVERY_LEDGER_2026.md
- `dec/` = decisions/
- `prop/` = proposals/
- `rep/` = reports/
- `BC1/2/3` = book_context/book_context_B01/2/3.json
- `MS` = grids/milestones_payoffs.csv
- `MECH` = rules/Mechanica-v4.md
- `DOM` = canon/factions/Dominions.md
- `E2.nn` / `E3.nn` = ebci/B02 and ebci/B03 episode cards
- `§619dec` = dec/B01_RESONANCE_DISCOVERY_LADDER_AUTHOR_RULING_2026-10-27.md
- `§620dec` = dec/B01_ELISABET_SIGNATURE_BREACH_LEXICON_AUTHOR_RULING_2026-10-28.md
- `NYLA` = dec/NYLA_ARC_AND_VISIBLE_MOMENT_2026-10-25.md
- `I5` = dec/B01_I5_INSTITUTIONS_AUTHOR_RULINGS_2026-10-27.md
- `OBL` = prop/VEIL_OBLIGATIONS_BRIEF_B02_B03_2026-09-27.md
- `VTA` = rep/VEIL_TRILOGY_AUDIT_AND_STANDALONE_EVALUATION_2026-09-27.md
- `B3A` = rep/B03_AND_VEIL_TRILOGY_EBCI_AUDIT_2026-09-27.md
- `TCG` = prop/TRILOGY_CONFLICT_GUIDE_2026-09-29.md (the guide lives in proposals/, not reports/)
- `MEMO` = d01_zip/DECISION_MEMO.md
- `ADD` = d01_zip/CANON_REVIEW_ADDENDUM_ENDING.md

**Limitation.** The project knowledge base was **not readable in this session**: no project_search or project_read tool was exposed, and the four claude/ docs are not on disk. Nothing here is cited from claude/SAGA_MILESTONE_TIMELINE.md, claude/VEIL_SPINE_RESOLUTION.md, claude/EPILOGUE_STRUCTURE_RULING.md or claude/NOTION_01_SAGA_ARCHITECTURE.md. Check them against §1, §6 and §10 before relying on this sheet.

---

## 1. The trilogy's question

| Item | Status | Finding |
|---|---|---|
| A stated Veil dramatic question | **GAP** | canon/trilogy_veil.md has no question. Every section is TODO except the lead (L3–17). saga_overview.md:35 has "Veil (T1): TODO". |
| A stated Veil mystery question | **DESIGN** | Q-ES3 approves *"The Veil question **which way does it lean**"* (dec/B01_ENGINE_SHEET_Q_ES_AUTHOR_ANSWERS_2026-10-09.md:22). The proposal sets out the ladder (prop/B01_ENGINE_SHEET_PROPOSAL_2026-10-08.md:50): B01 plants a bias, B02 has drift, B03 answers "southwest". This is the only trilogy-level question an author has approved. It is approved design, not ruled. |
| Trilogy knowledge end-state | **DESIGN / CONFLICT** | The author's direction: *"by the end of the Veil trilogy the characters know what resonance is and how it works"* (dec/B01_SHAPE_SOLVED_MYSTERY…_2026-10-14.md:13–14, 31; "terms need confirming", L42). Against it, B3A:191: *"**No one understands Resonance**"* at the end of B03, and OBL:67–68: *"No one in Veil knows there is a cap"*. |

**Candidate formulations implied by the material** (none is ruled):

| # | Formulation | Source | Status |
|---|---|---|---|
| a | "What is happening, and who is using it?" | TCG:55 (*"Veil asks what is happening and who is using it"*) | DESIGN |
| b | "What happens when people can feel the world changing before anyone can agree what the change means?" (notice → name/model/argue → publish/suppress/pay) | recovery/VEIL_TRILOGY_RECONCILIATION_MAP_2026-09-20.md:23–35 | non-canonical |
| c | "What is happening and why?" answered by *resonance anomalies* and *the thinning Veil*. This is B01's solved mystery, extended to the trilogy curve | dec/B01_SHAPE…:12–14, 26–28 | DESIGN |
| d | "Which way does it lean?" | Q-ES3 above | DESIGN |
| e | Dramatic: "truth has a cost, and who pays?" | VTA:270, 303 | report |

**Recommended synthesis for author ruling** (my inference; it rules nothing):
- **Mystery:** what is this weather, how does it behave, and where is it going? The answer by the end of B03: it breaks through at weak places, worsens where it has broken before, and leans southwest. Why the Veil exists stays reserved.
- **Dramatic:** who controls what is known about it, and what does telling the truth cost?

---

## 2. Lead and POV baton, antagonist pressure, theatre and locations, time span

| Item | Status | Finding |
|---|---|---|
| Trilogy lead | **RULED** | Baz (trilogy_veil.md:17; saga_overview.md:26; dec/POV_DISTRIBUTION…_2026-09-26.md:25). His arc is one of the three "set" items (dec/B01_STANDALONE_REVIEW_SCOPE…:10–16). |
| Saga lead | **RULED** | Seraphine (POV ruling :25). Her B01 arc is open except where B09 constrains it (Q-SB0, dec/B01_STANDALONE_BRAID_REDESIGN_Q_SB…:37). |
| POV shares | **RULED, diagnostic** | 30/30/30/10 as "general targets, not hard calculations" (POV ruling :10–15, 29–31). The BC1–3 weights are still "TODO: authored". |
| B01 shape | **DESIGN** | A braid: Lucien is the causal link through whom Seraphine and Baz meet (dec/B01_STANDALONE_BRAID_AND_OPPOSITION…:13–15, 30–32). Baz arrives in Act II, and the Q-SB file lists this among its ruled items (Q-SB file :28). |
| Baton handoff | **RULED** | Tahl is anonymous through B03 and named in the B03 epilogue (M12, MS:13; E3.47). No named Tahl POV before then (OBL:41). |
| Dominion, through Caldas Ren | **DESIGN** | Caldas's ladder: surveillance in B01, intimidation in B02, lethal pursuit in B03 (dec/HAN_WEI_ON_PAGE…:63–66; DOM:236). In B02 he is restrained by leadership; in B03 he has free rein (DOM:270–275, "Consider"). |
| Dominion's lethal aim | **RULED** | In B03 Caldas's lethal intent is aimed at Baz (NYLA:8; LED §615 L19107). |
| Hollen is a Dominion front | **RULED** | The Institute and the Foundation are both fronts. Baz knows the front from his Vienna years. He does **not** learn in B01 that his Houston funder is a Dominion faction (I5:39–45; LED §617). |
| Dominion's internal funder faction | **RULED / direction** | The faction funds Baz's work. Baz believes he has left Dominion but is still paid by it, and the split comes at his death (BC3:211, 217; DOM:251–262). |
| Technarc | **DESIGN** | Ambient in B01 (Technarc stays unnamed; Q-ES8). In B02 it makes a polite request (E2.13) and a map offer that is declined (E2.24). In B03 its retrieval team is exposed at the Warehouse (E3.33, E3.42). Han Wei is brief in B03 around E28 (canon/factions/Technarc.md:229). |
| Theatre | **DESIGN** | New Orleans throughout. Departures: Houston (B01 C11, BC1:147), Marrakesh by phone (E2.06), a dance hall out west (E3.24) and Detroit (E3.43). Vienna stays offstage (OBL:94, Lucien does not travel). The anchors are Jackson Square (B01), Bywater (B02) and the Warehouse District (B03) (VTA:146–150). The per-book location roster is a **GAP** (BC1–3 `_gap`). |
| Time span | **RULED (B01) / DESIGN (B02, B03)** | B01: Tue 17 Mar to Sun 10 May (BC1:147). B02: May to August (E2.01:44, "approved, Q-B2-6"). B03: September to early October, with the epilogue days after (E3.01–E3.48 headers). The year and the gap across the trilogy are **GAP**. |

---

## 3. Entry load and standalone status

| Book | Minimum a reader needs | Status | Does it stand alone? |
|---|---|---|---|
| **B01** | Ordinary New Orleans. Seraphine is a Beaulieu Center care worker; Caro is her friend; Lucien is a field inspector of record whose employer is Hollen. Nothing is publicly known about the phenomenon. The watchers' Prologue names nothing. | **DESIGN** (BC1:32–113, "APPROVED DESIGN… not ruled"); the Lucien detail is **RULED** (LED §605). | Yes, by design. Spine C is ruled (LED §601–602), and §619 makes the Square a visible victory. **Stale entry facts:** BC1 W2 (*"subtle and low-amplitude"*, :40) and P4 (*"precursor level"*, :136) contradict §619. BC1:82 (*"The Dominion is not named in B01"*) contradicts §617. |
| **B02** "previously" | Square survived. Dominion and Hollen exist and use Lucien's reports. Nyla was kept safe. Lucien is suspended and his papers went to Vienna. Elisabet went to Vienna. Baz chose to stay. Caldas was recalled upstairs. | **GAP**: BC2 `key_character_states` reads *"Not invented here"*. | Partly. VTA:263 says *"Some reliance on B01… E01–E07 re-establish enough"*, but that judgement predates the October B01. |
| **B03** "previously" | Bywater order. No Reset. Drift southwest. Anonymous MT. Lucien's two secrets. Caro and Elisabet's "after". Nyla's escape (§615, unbuilt). | **GAP** (BC3 same). | B3A:45–72 says it passes *"It answers its own question"*. VTA:292 asks for T2 and T10, which are applied (E3.13, E3.35). |

---

## 4. Discovery ladder, B01 → B03

| Layer | B01 (§619 ladder; **RULED**) | B02 (EBCI; **DESIGN**) | B03 (EBCI; **DESIGN**) |
|---|---|---|---|
| **Phenomenon: what is learned** | Behaviour is discoverable and origin is not (§619dec:34–35). Emotion governs coupling, not origin (:52). "What makes a warning useful?" (:65–70, Ursulines). Breaches escalate, which is the clock (:83). The water signature shows that a window is open (§620dec:75–91). At the Square: the forecast works; a third, bigger pulse; the edge moves; the seated crowd changes the event, observed but not understood (:84–89). Nyla converts and does not emit; light comes in the Epilogue (:71–75; NYLA:16). | The city names "pulse" (E2.03). Not unique: Marrakesh (E2.06–07). Pocket signs, v1 (E2.10). Interval, v2 (E2.17). The model misses (E2.14). One-block forecast (E2.22). The cluster (E2.29). "Not one thing": each pulse leans (E2.38). Drift southwest (E2.40, E2.42). **No Reset / no decay** (E2.46). | A map of standing conditions (E3.01). Constituencies around the map (E3.04). Corridor versus building as rival models (E3.23). An intermittent building, *"a little larger each time"* (E3.13), which is the breach rule in effect. The event *"exceeds every model"* (E3.36). Contested public record (E3.42). Tahl publishes the southwest pattern (E3.48). |
| **Veil (cosmic)** | Reserved: the cap, Mira, Silence and Hope, the cycle, the Loom, breathing, the four Wounds (§619dec:55–60). The Epilogue's watchers see the light (NYLA:16). | Brush from Silence and Hope's side, with no action (E2.41; M09). A wordless presence (E2.35, the Mira seed). | The brush Tahl notices (E3.47; M09). No cap knowledge (OBL:67). |
| **Antagonists** | Dominion's forecast is the plot engine. Its model is incomplete: it predicts the event, not human survival (§619dec:63–64). Hollen is its front (§617). The count and camera at the Square (MEMO §3, approved in principle only). | Helena asks (E2.08). Clearance needs "grounds" (E2.23). The method is used in Dominion hands (E2.34). The zone is extended by the crude rule (E2.47). | "Advise and contain" (E3.09). Helena's price: Baz himself (E3.14). Caldas's canvass (E3.21). Technarc exposed (E3.33, E3.42). |
| **Escalation: Mechanica §7.1** | §7.1 as amended: *"escalating, physically consequential, increasingly measurable"* (MECH:153). BC1 band W0–W2 (:194–196) is likely stale against three pulses and a whole-crowd fall. | W0–W3 (BC2). Named, public, persistent. | W0–W3 (BC3), peak U5/W3/FX2 (B3A:208). **CONFLICT:** MECH:150 still lists *"Early shard precursors only (flickers, ghostwaves)"* for Veil, against M08 *"The Warehouse **Rupture**"* (MS:10). Rupture is rung 4 of §34 (MECH:680). No ruling reconciles the two. |
| **Antagonist escalation** | Surveillance plus a forecast operation. | Intimidation, restrained. Policy harm. | Free rein, lethal pursuit (unbuilt; §10). |
| **Personal stakes** | Nyla, Dré's family, Lucien's lie (LED §601). | The list. Rosette. Households displaced (E2.25–31). | Baz's life. The child. The father (E3.35). Lucien's confession (E3.17). |

**CONFLICT: the ladder now runs backwards.** Since §619, B01 ends with a working forecast, three surprises and a crowd that changes the event. B02 restarts the protagonists at signs and intervals (E2.10, E2.17), and Dominion "will not clear a block on a number" (E2.23). VTA:62's *"Nothing escalates backwards"* predates the October rulings. None of the B02 or B03 cards cites §615–§620, except E2.05 (grep).

---

## 5. Per-book resolution

| Book | Closes | Opens (the hook) | Status |
|---|---|---|---|
| **B01** | Spine: *"Lucien's reports found Dré's family. Will they find Nyla's?"* (LED §601). The answer is no. Nyla is safe, *lost at the Square* (NYLA:6, 10). The notebook goes to Vienna without her page (LED §602.3). The mystery "what is happening" is answered as resonance anomalies and a thinning Veil (dec/B01_SHAPE…:26–28). | The Epilogue's light under Nyla (NYLA:16). *The Veil* and *Resonanz* rise (LED §612 F8). Lucien suspended and his papers sent to Vienna (BC1:82). Elisabet's Vienna consultation (§620dec:114–117). The funder's offer (BC2:167). | **RULED** spine and ending. **CONFLICT:** the older central question, *"is it only where I am?"* (Q-ES1, 10-09), has not been retired against §601 and §619. |
| **B02** | "Will they act on evidence they cannot trust, and at what cost?" (VTA:245). They send the bounded version (E2.26), the order helps and costs (E2.27–31), and Lucien withholds drift (E2.47). | No Reset. Southwest. Lucien's secrets. Seraphine takes Lucien off her rounds (E2.31). **§615 requires** Dominion to take Nyla, Lanette to lead the recovery, and an escape on the E44 pulse. None of it is in the EBCI (§10). | **DESIGN** |
| **B03** | "What does a rule that waits for certainty cost?" (B3A:47). The Warehouse. The rescue. Baz's death (E3.36–38). The confession (E3.17). The first kiss (E3.24). The finite circle (E3.12, E3.35). | Tahl named, with his rule (E3.47–48). The death is unconfirmed to the cast (M10). Technarc exposed (M13 hook). Rex (E3.43). | **DESIGN**. M12 is **RULED** |

---

## 6. Trilogy resolution at the end of B03

| Strand | What lands | Status |
|---|---|---|
| **Plot** | The Warehouse Rupture (M08). Baz rescues a child and dies (M10; E3.37–39). | **DESIGN** (both M-rows are `proposed`) |
| **Baz's death** | The reader sees it (E3.38). The cast learns at B04's start (M10, MS:12). The reported "first responder" is Baz (MS:12 note). | **DESIGN**; the death in B03 is **RULED** in effect (BazID:49; BC3 `_ruled_constraints`) |
| **Who is to blame for the death** | The heavy implication and outright suspicion of Caldas and Dominion are permitted. The narrator may not state cause (dec/HAN_WEI…:69–83). **CONFLICT:** MS:9 and MS:12 (M11, M10) still carry *"no blame just inference"*. | **CONFLICT** |
| **Caldas** | Lethal intent at Baz (NYLA:8). What free rein licenses on the page is *"not ruled"* (E3.14:45–47; BC3 `open`). E3.14:17 still reads *"pressure, not a stated threat"*. E3.21 is a door-to-door canvass. **Caldas has no B03 lethal beat and no Veil endpoint.** | **GAP / CONFLICT** |
| **Dominion faction split** | *"B03 payoff (the split at his death)"* (I5:44). Against that: the split *"leans to the B03→B04 boundary… exact book not locked"* (BC3:217; DOM:261–262). M10 has the cast learning of the death only in B04, so the split cannot complete inside B03. **No B03 card carries the funder at all**; only E3.14:47 mentions it, in its notes. | **CONFLICT** |
| **Antagonist arc** | Dominion becomes "advise and contain" and makes its demand for Baz. Technarc is exposed. Neither is defeated (TCG:48). | **DESIGN** |
| **Character arcs** | Seraphine: restraint, then consent, then delegation (VTA:296). Lucien: refusal and confession (E3.16–17). Caro reaches her limit and **does not hand over** (E3.22; M54 protected, OBL:38). | **DESIGN** |
| **Mystery answers** | Behaviour, persistence, escalation and direction (§4). Why stays reserved. | **DESIGN** (see the §1 CONFLICT) |
| **Relationships** | Caro and Elisabet: first kiss (M07 reading, MS:8). Seraphine and Lucien: *"necessity… not resolved"* (E3.18). Lucien and Baz: repaired (E3.17, E3.26). | **RULED** (M07 reading); the rest **DESIGN** |
| **How B03 ends** | Quiet. A vigil (E3.45), then a three-episode epilogue for Tahl (E3.46–48). VTA:64–71: *"All three books end quiet… Not a defect."* | **DESIGN** |

---

## 7. Left open for Neon or the saga

| Open item | Lands | Verdict |
|---|---|---|
| The cast's grief for Baz; Lucien in Vienna (M05); Seraphine and Lucien (M57) | B04, B05 | **Fair.** The reader sees the death in E3.38. |
| Tahl's remorse arc (M12 → M37 → M20) | B04–B06 | **Fair hook, but** the trilogy's last 3 episodes spend themselves on the *next* lead. The recovered export titled them *"EPILOGUE — VEIL → NEON BRIDGE"* (LED L2400). |
| Protocol 9 from Technarc's exposure (M13) | B04 | Fair |
| Caro and Elisabet commit (M56) | B05 | Fair. The kiss is the Veil payoff. |
| The southwest lean leads to Santa Fe | B06, B08 | **Fair.** "A direction, not a visit" is a Veil-level answer (OBL:104). |
| Dominion faction split; Concord co-opted | B03/B04, Neon | **Dependency.** §617 promises a B03 payoff, and nothing is built. |
| What Nyla is (a converter), and her fate | "tested against the later saga" (§619dec:75) | **Dependency risk.** B03 keeps her offstage (NYLA:8). Her Veil-level payoff is the B02 escape, which is unbuilt. |
| The watchers, the cap, Mira | Loom | **Fair only if** the frame poses no question that Veil promises to answer (F5, LED §616). |
| Caldas | — | **Dependency.** The trilogy's named antagonist face has no Veil endpoint. |
| The Honey Island seed; the northern scar | B09; never | Fair: unexplained and unnoticed (VTA dec #8; §620dec:106–110) |

---

## 8. Saga milestones Veil delivers

| M | Book/Act | Content (short) | Row status |
|---|---|---|---|
| M01 | B01 A1 | First bounded public anomaly | proposed (note still *"low amplitude"*, MS:2; stale vs §619) |
| M02 | B01 A2 | Filaments recognisable | proposed |
| M03 | B01 A3 | Seraphine times and constrains a response, at cost | proposed / HOLD (MS:4) |
| M04 | B02 A1 | The anonymous MT voice begins | proposed |
| M06 | B02 A2 | Public pulse cluster | proposed / HOLD |
| M07 | B02 A2 | Caro and Elisabet deepen; kiss in B03 | proposed (reading ruled) |
| M11 | B03 A3 | Tahl's coordinates post | **ruled** |
| M08 | B03 A3 | Warehouse Rupture | proposed |
| M09 | B02 A3 / B03 EP | Two VT brushes | proposed |
| M10 | B03 A3 | Baz dies | proposed |
| M12 | B03 EP | Tahl named | **ruled** |

Veil owes forward: M05, M13, M14, M18, M20, M21, M37, M49, M56, M57 (BC1:225–247; BC2, BC3 `continuity_hooks`). **No M-row exists** for Nyla (§615), the Square victory (§619), the forecast engine, Caldas or the funder split.

---

## 9. Dependency check

| Type | Item | Finding |
|---|---|---|
| A Veil payoff that needs later setup | **None found.** Every Veil payoff's setup sits in B01–B03 (BC2 and BC3 `collects` come only from Veil). | — |
| A Veil setup with no Veil-level payoff (million-word risk) | **The funder is Dominion** (B01 setup, §617/§592) | Payoff leans B04 (BC3:217). **High risk.** |
| Same | **Caldas's lethal pursuit** | No B03 beat, no outcome. **High risk.** |
| Same | **Nyla as converter** (B01 Epilogue light) | The B02 escape gives a partial payoff, but it is unbuilt. **Medium risk.** |
| Same | **The watchers' frame** (B01 Prologue and Epilogue, B02 E41) | No Veil answer by design. **Medium risk** unless the frame stays non-interrogative. |
| Same | **The seated crowd changes the event** (§619dec:88) | B02 and B03 never return to it. The X1 gate (NYLA:21) bars only confirming that the Veil answers rhythm, so a Veil-level follow-up is allowed. **Medium risk.** |
| Same | **Elisabet's Vienna consultation** (§620dec:114–117) | B02 E05 has no Vienna outcome (E2.05:15 is a university re-file). **Low–medium risk.** |
| Partial payoff exists | Southwest (B02 E40 → B03 E48); MT (M04 → M12); VT brushes; Rex (E3.07 seed → E3.43) | OK |

---

## 10. Gaps, conflicts and stale items after the October rulings

| Item | Status | Detail |
|---|---|---|
| **B02: Nyla taken; escape on the E44 pulse** | **RULED but GAP in EBCI** | NYLA:7: *"Dominion takes Nyla. Lanette leads the recovery… gets out on the night of the big B02 pulse (E44)"*. Paper is the justification, not the vehicle (:12–13). The Pontalba footage gives Dominion its grounds (:17). The words "Nyla" and "Lanette" appear in **0** B02 or B03 cards. E2.44 (*"The Pocket That Stays"*) carries no escape. P12 *"becomes an early-B02 beat"* (:7) is also unbuilt. The rows to update are listed in a manuscript-repo memo (:10). |
| **The Nyla decision against MEMO D10** | **RULED** | MEMO §9 held Nyla's timing open. ADD:3–5: *"Variant C is NOT adopted. §615's B01 row stands"*. The Bridge 1→2 draft is shelved. |
| **B03: Caldas lethal toward Baz** | **RULED intent / GAP in EBCI / CONFLICT** | NYLA:8 says *"lethal intent… aimed at **Baz**"*; DOM:270–275 says free rein. Against that, E3.14:17 has *"No Dominion exposition… pressure, not a stated threat"*. What free rein licenses is *"not ruled"* (E3.14:46–47). The "No Dominion exposition" line is also stale against §616/§617. |
| **Breach and scar lexicon** | **RULED; partly stale** | Breach is active; scar is an old breach gone quiet; Wound is reserved (§620dec:64–68; MECH:891). Stale or colliding wording: MECH:708 Rupture *"Permanent scar creation"*; E3.31 *"before it is a scar"*; M08 *"durable New Orleans scar"* (MS:10); M28 "Warehouse scar" (MS:36). After a Rupture the Warehouse is a **breach**, and it becomes a scar only once quiet. B02's "no decay" (E2.46) and B03's "larger each time" (E3.13) are breach behaviour but never use the term. Pending upstream: VTA dec #6 keeps B01's *"swamp wound"* as a seed of the Tear; it needs checking against "Wound" being reserved. |
| **The forecast engine** | **RULED for B01 / CONFLICT downstream** | §619dec:63 says Dominion *"can predict where and when"*. B02 makes the protagonists the forecasters, and Dominion needs Baz's grounds (E2.22–23, E2.34). B03 says *"no model forecasts a shock"* (E3.09, E3.27). If Dominion has a forecast, B02's engine needs re-scoping, e.g. Dominion's model sees the window and Baz's method sees the people. |
| **Elisabet's Vienna exit** | **RULED / GAP in B02** | The consultation is confirmed (§620dec:114–117; ElisabetID:96). E2.05 has her *"comes back to stay"*, with the university re-filing on its terms (Q-VB3, 09-29), and no Vienna outcome. The Review is Hollen, a Dominion front, *"the same body that suspended Lucien"* (§620dec:117). She had earlier funding from Hollen (ElisabetID:93). Her stopped readings in B02 (§620dec:127, 146) are not on any card. |
| **Hollen is a Dominion front** | **RULED / GAP downstream** | I5:39–41. "Hollen" appears in **0** B02 or B03 cards. **Open:** is the Houston funder the Hollen Foundation? If it were, Baz would know (he knows the front), which would break §617's ruling that he does not know his funder is Dominion. Canon does not name the funder, so this is a **GAP to rule**. BC1:82 and DOM:266–268 ("named once") are superseded by DOM:269. |
| **The B02/B03 guard "physics observed, never explained by the page"** | **Stale** | Every B02 and B03 card carries it (e.g. E2.01:37). It should be updated to loosened W2 and §619's §60 amendment (dec/B01_HOLDS_REVIEW_RULINGS…:33; §619dec:39–42). |
| **BC3 W4 exception at `S1.T1.B03.A3.E14`** | **Stale** | BC3:88–94 ties the noticed VT brush to A3.E14. The brush is now EP E47, and A1.E14 is "Helena's Price". |
| **MEMO trilogy framing (Prologue B01/B04/B07, Epilogue B03/B06/B09, 8 Bridges)** | **GAP in canon** | MEMO:81–95 (D08, D09: "Approve as provisional saga convention"). **No decision or ledger entry in the canon repo rules on it.** A grep for Bridge, D08, D09 and Packet 20 finds no hits in decisions/ or LED §600–623. The only record is the editing thread's ADD:6, *"remains the author's provisional direction for later books, with B01 keeping its Prologue and its Epilogue"*. That is consistent with §612 and §615, which rule B01's Epilogue. Canon has prologue and epilogue numbering (LED L535–537) but no per-trilogy convention. |
| **Trilogy summary and question** | **GAP** | trilogy_veil.md has only TODO sections (L3–14); saga_overview.md:35 is a TODO. |
