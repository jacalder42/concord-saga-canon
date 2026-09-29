# B01: the 13 manuscript-versus-ruling conflicts (Q-OL4)

**Date:** 2026-09-29
**Status:** CURRENT AUTHOR RULING for #1 and #9; approved design for the rest. These are the author's answers to Q-OL4
in `reports/B01_TIERED_STRUCTURAL_OUTLINES_2026-09-29.md` §3–§4. The conflicts are set out in the private manuscript
repository, `draft-notes/b01-structural-outlines/OBLIGATIONS.md` §4. The author answered:

> *"1a, 9 yes, 2a, 3 agreed, 4 agreed, 5 agreed, 6 agreed, 8 agreed, 11 agreed, 7 agreed, 10 agreed, 12 agreed, 13
> thread alone does not bother me in this context"*

The options answered are those Claude put to the author on 2026-09-29, after Q-OL1–3
(`decisions/CALDER_COMPANIONS_AND_B01_SHAPE_AUTHOR_ANSWERS_2026-09-29.md`).

**What it does not change:**
- No earlier decision file is edited. #1 and #9 amend earlier rulings **from this file**.
- The manuscript is not edited now. Manuscript fixes go into the redraft's new prose packets, because a ~150k redraft is
  coming (Q-OL1).
- No Mechanica, no milestone row, no card.

## 1. Rulings

| # | Conflict | Ruled |
| --- | --- | --- |
| **1** | The child is named **Dré** in the manuscript. `decisions/MIRA_AND_SILENCE_HOPE_ORIGIN_AUTHOR_RULING_2026-09-26.md` says *"The B01 v4.1b child stays unnamed"* (§2 and its list of what it does not change) | **(a) The wording is amended.** The B01 child **may be named** (Dré). **He is not Mira and has no guide role**, which was that ruling's point. Hypothesis A stays not taken. The child's imprint stays a fading, place-bound imprint (obligation 65) |
| **9** | E48: Seraphine carries one stranger. The ruled D6 (`decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md`) says *"The team observes more than intervenes."* The later approved T7 (`decisions/VEIL_TRILOGY_AUDIT_AUTHOR_ANSWERS_2026-09-27.md`; `proposals/VEIL_AUDIT_AMENDMENTS_2026-09-27.md`) has Seraphine time and constrain a response at visible cost | **Yes: T7 amends D6.** The team observes more than it intervenes, **and Seraphine carries one person by choice, at bodily cost**, declining to hold the whole Square. The rest of D6 stands (a positive, quiet, independently checkable observation near an imperfect window; absence of hum alone cannot carry it) |

## 2. Approved design: manuscript fixes, applied in the redraft's new packets

| # | Conflict | Decided |
| --- | --- | --- |
| **2** | Lacuna's E31 cameo has become **Nadine**, a named house bassist who recurs (S04, S05, E41) | **(a)** The E31 bassist is **unnamed**, and her recurrence is removed. She is the B01 Lacuna cameo, with zero portent (BC-LACUNA-CAMEO; VAA §3 T8). Other nights at the Vein may have other musicians |
| **3** | Elisabet reads as resident (*"I'm here until October"*) against the ruled *"E23 is a visit"* | **Agreed.** She leaves after E30 for her other wells; *October* survives only as her answer on television. B02 E05's return then has something to return from |
| **4** | Baz's *"Then I'll come in December"* and Lucien's *"July. The quay"* | **Agreed.** Both plans are undated |
| **5** | Lucien withholds his true sentence from his office in B01, pre-spending B02 E08's first partial obedience | **Agreed.** The withheld sentence goes **to the coroner**, as the outline spine has it; his office gets a procedural report, off the page |
| **6** | The *widen inquiry, not certainty* agreement is thin | **Agreed.** One explicit exchange after E45, carrying E39's supply-boat thread as the one ambiguous far thing |
| **8** | E39 argues about going back to the camp, against Q-DR7 | **Agreed.** Replaced in the redraft with Lucien wanting the city's 311 clock |
| **11** | M02's recurring care is carried in Act II by other faces; Mara is nearly absent from E10 to E39 | **Agreed.** Mara is on the page in Act II (the outline places her at the Ursulines box) |
| **13** | E00's *"the reach between them had worn thin as thread"* touches the prologue's guard against any LT motif | **Kept.** *"Thread alone does not bother me in this context."* No change; E00 stays as written |

## 3. Approved design: canon housekeeping, done now

| # | Conflict | Done 2026-09-29 |
| --- | --- | --- |
| **7** | BC-SWAMP-WOUND is logged as introduced at E29, where the prose packet and DR7 keep the pressure in the Marigny, unlocated | `grids/breadcrumbs.csv`: introduced at **E01** (the camp), reinforced at E02, E22, E28 and E46, with a dated note; the payoff is unchanged. v4.1b's E29 beat carries a supersession note. The EBCI packets follow: E29 no longer claims the breadcrumb (`CHK_PACKET_LINKS` flagged it), and E01 (introduced) and E02 (reinforced) carry it |
| **10** | Two calendars | **Calendar C governs** (`decisions/B01_ACT_II_CHECKPOINT_DECISIONS_D1_D5_AUTHOR_ANSWERS_2026-09-28.md` D1). `book_context/book_context_B01.json` `_calendar` is rewritten, keeping the old anchors as a superseded note; `rules/saga_context_S1.json` `chronology` gains a note. The anchors are now **E15 mid-March (about 17 March), E33 mid-April (about 11 April), E45 late April (about 26 April), E48 late April (about 29 April)**, about 9–10 weeks. 35 EBCI `When:` lines and 25 prose-packet month phrases move to match (E07 to E46). `tools/derive_book_context.py` does not generate `_calendar` |
| **12** | Errors in v4.1b itself | Corrected in place in `proposals/B01_REVISED_BEAT_BIBLE_V4_1B_INTEGRATED_2026-09-22.md`, each with a dated note: S05 calls Trip *she* (S06 names no pronoun); Lacuna's B01 entry is **a cameo**, not *DEFERRED*, in its end states and lock checksum. **The named recorders Clement and Isaiah** (DR7 Q-DR13) are recorded against LP3 Q-E15-2's *"both unnamed"*; that decision is not edited |

## 4. What happens next

As ordered in `decisions/CALDER_COMPANIONS_AND_B01_SHAPE_AUTHOR_ANSWERS_2026-09-29.md`:
1. the instruction repair (the controlled comparison is complete; its result goes to the author);
2. a human read;
3. new prose packets for the ~150k shape, carrying §2's fixes;
4. the redraft, with the checker and the promises ledger.

The Veil continuity reconciliation and B02's packets wait.
