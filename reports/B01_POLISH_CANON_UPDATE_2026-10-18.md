# B01 polish rulings applied to canon: change report

Status: NON-CANONICAL report, 2026-10-18. It records the canon update the author approved ("Yes", 2026-10-18) to
bring canon up to date with the B01 polish rulings. Ledger §591. The rulings themselves are in `decisions/`; this
report changes nothing on its own. The prose is private, in the manuscript repository; chapter keys (C01–C44, P, E)
refer to its final B01 (`B01/final-2026-10-18/`), and nothing is quoted beyond identifying phrases.

**Authority applied:**
- `decisions/B01_POLISH_DIALECT_RULINGS_2026-10-18.md`, with the Caldas addendum (§587);
- `decisions/B01_POLISH_CANON_AUDIT_RULINGS_2026-10-18.md` (§588);
- `decisions/B01_POLISH_WARMTH_AND_INTERIOR_DIRECTION_2026-10-18.md` (§589);
- `decisions/B01_POLISH_RECOMMENDATIONS_APPROVED_2026-10-18.md` (§590);
- the earlier B01 decisions where they still hold, chiefly `decisions/B01_FINAL_PASS_RULINGS_C_BASE_2026-10-18.md`
  (§585, now superseded on the posting and on "which then grows") and `decisions/B01_C_AND_B_RULINGS_2026-10-17.md`.

**Checklists used** (manuscript repo, `draft-notes/final-2026-10-18/`): AUDIT_CHARACTER_CANON.md §4;
RESEARCH_CONCORD_FUNDER_ORIGIN.md §4; AUDIT_CALDAS_ORIGIN.md §5.5; AUDIT_NICKNAMES.md §5. Only items a decision or
the final page supports were applied. **Every page fact written to canon was grep-checked against the final B01
chapters.** Where the audit's claim could not be confirmed on the page, it was left out (listed in §3).

**Method:** additive only. Every change is a dated note or appended clause citing its decision and ledger §591; no
canon text was removed or reworded, and superseded lines stay as the superseded reading. Validation after the
changes: `validate_canon.py` exit 0 (no violations); `test_validate_canon.py` 171 tests OK;
`derive_book_context.py --check` no drift; the ledger diff is additions only.

---

## 1. Files changed

| File | Change |
|---|---|
| `canon/cast_registry.csv` | 16 rows amended (C02 Caldas: Portuguese, Lisbon English, family name, Ren/Ren Bellande, final chapter keys, recall terms, Q-BH6; C03 Marius: M./N. split, suspends the posting; C04 Helena: chain and suspension, A3 and M05 stand; B07 Ramon: OPEN link; B11 Rieux; B12 Odile: Doucet load-bearing, program at six, *cher* hers alone; B13 Renée; B14 Dré: death in the ambulance or at the hospital; B15 Miss Tavie; B16 Denise: four steps to the personnel-file warning; B17 Marisol; B18 Guidry; B19 Sal; B20 Mr. Ledet: house on Kerlerec, guest at Easter; B21 Philomène: not in final B01; A01 Inez). B21 repaired (see §4). **22 new rows:** B22 Lorraine, B23 Lanette, B24 Nyla, B25 Dion, B26 Gwen, B27 Mr. Vidrine, B28 Mrs. Arceneaux, B29 Vernice, B30 Isaiah, B31 Tamika, B32 Mrs. Carmouche, B33 Miss Hazel, B34 Mr. Alcide, B35 Miss Pearl, B36 Mr. Fontenot, B37 Ms. Tran, B38 Lena, B39 Hedwig Pospischil, B40 Keon A. Joseph, B41 Joanne Pryor, B42 Curtis Guillory, C06 Annelie Strobl. Recurrence beyond B01 is marked OPEN on every new row. |
| `canon/characters/SeraphineIdentity.md` | §III: "Fifine" (new canon); §VII: disciplinary steps in final keys, the personnel-file warning; §XI: death not at the camp, "Was Dré first?" once and unanswered. |
| `canon/characters/LucienID.md` | Posting suspended, papers to Vienna (replaces outright loss); N./M. chain; his on-record correction approved as is, with B02 E08/E34 OPEN; Q-VI3 rung spent at C44; no endearment in B01; "Mr. Kael" as her pet name after the fourth kiss; Q-VI10's E48 French word stale; the father's watch. |
| `canon/characters/BazID.md` | Funder a Dominion splinter; Houston resignation; July offer; split, founding and co-opted name; Q-BH6 amended; C-1 bullet stale; BASTIEN ARNAUD and Banks Street; Caldas keys; the "Veil" word's source; "Dominion" spoken (C34); Lena's mother; contractions and French interior syntax; Mr. Tree, Mr. Baz, the Bastien arc; the cup. |
| `canon/characters/CaroID.md` | Keys (festival standby, Algiers call in C44); sixteen years; the two-charts warning; "mija", "güera", "the ambulance" (refines the 10-05 Spanish-waits note for these forms only); the Caro–Elisabet opening. |
| `canon/characters/CaroAppearance.md` | The hand tell is at C20 and Elisabet points it out; the CHICAGO FIRE DEPT sweatshirt is not on the final page. |
| `canon/characters/ElisabetID.md` | B01's flirtation is with Caro (H2/CP14 superseded for B01); in New Orleans C13–C42; the E48 re-filing text is gone, the cone return is paid in Caro's C44 call; the Institute-funded field season and burned notebooks; KNOWN; contractions. |
| `canon/characters/ElisabetAppearance.md` | Height: the page now fits the card (one meter eighty); 1.86 m retired; range stands. |
| `canon/characters/TripID.md` | Baz's pallet and BAZ tape; red beans on Thursdays for Baz. |
| `canon/factions/Concord/Concord-Mandate.md` | The founding stated: ethic emerges, organization founded after the split; funder a Dominion splinter; name co-opted. OPEN: book of split and founding; classification and §VII. |
| `canon/factions/Concord/Concord-EraFunction.md` | Veil precursor (funder-backed work); Neon reads with the ruled order; a rival holder of the name. OPEN: books. |
| `canon/factions/Concord/Concord-Relationships.md` | Dominion entanglement at the root; the co-opting organization. OPEN: §III toward the splinter and co-opter. |
| `canon/factions/Concord/Concord-Structure.md` | History behind "no long-term dependency". |
| `canon/factions/Concord/Concord-Limits.md` | Name capture beside failure mode E. OPEN: the co-opter after the Mending (§V, D11). |
| `canon/factions/Dominions.md` | The splinter funder; Caldas reads the review. OPEN: "No redemption arc" for the splinter; "Dominion" spoken in B01 against the 10-09 note; the owed City–Dominion note. |
| `book_context/book_context_B01.json` | entry_state: appended amendments to Lucien (Dominion spoken in C34, OPEN; posting suspended), Baz (Houston Group, resigned; funder a splinter), Elisabet (in the city C13–C42), Offstage (Lacuna cameo at C22); new `_calendar_final_2026_10_18` (datelines; 17 March to 10 May). |
| `book_context/book_context_B02.json`, `B03.json`, `B04.json` | New hand-authored key `_concord_funder_thread_2026_10_18`: the ruled items, a per-book line, and the OPEN placements. Derived blocks untouched. |
| `grids/breadcrumbs.csv` | BC-LACUNA-CAMEO notes: the cameo is the unnamed C22 singer (R8). SID locator not remapped. |
| `ebci/prose/AUDIO_NARRATION_SHEET_B01.md` | Corrections 2026-10-18: Caldas Portuguese and Lisbon English, never an accent; "Caldas" a family name, KAL-dus default, "Ren" shared with Ren Bellande; *cher* Odile's alone; new names to check (Fifine, Nannan, mija, güera, mon cœur). |
| `decisions/B01_FINAL_PASS_RULINGS_C_BASE_2026-10-18.md` | Pointer: #2 superseded on the posting and on "which then grows". |
| `decisions/B01_POLISH_CANON_AUDIT_RULINGS_2026-10-18.md` | Pointer: #1 and #3 answered in §590; #4–#8 applied. |
| `decisions/B01_POLISH_RECOMMENDATIONS_APPROVED_2026-10-18.md` | Pointer: nickname ruling 2's "Odile's sister" against the page (see §2, item 1). |
| `recovery/RECOVERY_LEDGER_2026.md` | §591 appended before END. |
| `reports/B01_POLISH_CANON_UPDATE_2026-10-18.md` | This report. |

---

## 2. OPEN items (need an author ruling)

1. **Lorraine's relation.** Nickname ruling 2 calls her *"Odile's sister and Dré's aunt"*. The page (C19 "my sister's
   baby"; C40, standing behind her sister Renée's chair) and registry B13 make her **Renée's** sister and Odile's
   daughter. Canon follows the page (B22). Confirm the decision's wording is a slip.
2. **The book of the split and of the founding.** Ruled: the circle splits from the funder, then founds Concord. Not
   ruled: when ("perhaps after Baz's death", end of B03). A founding at the B04 opening fits Concord-EraFunction §III.
3. **Concord-Mandate's classification and §VII.** *Multinational Civilian–Operational Coalition* and *Why Concord is
   not the protagonist* against a Concord founded by the protagonists' circle.
4. **Concord-Relationships §III** (*does not challenge Dominion authority head-on*) toward the splinter and the
   co-opter, which are not the Dominion proper.
5. **Is the splinter compromised?** Dominions.md's *"No redemption arc"* holds only if it is. The page keeps the
   shadow (the *first* wording in C11, the appetite for consents), but no ruling says so.
6. **The co-opter after the Mending,** against Concord-Limits §V (*no successor organization*), and its bearing on the
   B09 naming question (D11).
7. **When Baz knows or suspects what the funder is,** and when the co-opted name first shows.
8. **"Dominion" spoken in B01** (C34) against the 2026-10-09 Dominions.md note that the faction stays unnamed on
   B01's page. The 10-14/10-15 rewrite direction lets Dominion act more overtly but does not say it is named.
9. **B02 E08 and E34.** Lucien's corrected statement (C43) puts on record what F3/CP9 kept unproven until B02;
   approved "fine as is" (§588 #2). How E08 and E34 are re-scoped is open.
10. **Caldas's B03 "lethal pursuit" rung** against the B01 recall terms (no warrant; free for B02 E27 and B03 E14), and
    the **City–Dominion note** owed by `B01_C_AND_B_RULINGS_2026-10-17.md` #3 (R4): not drafted; needs drafting and
    approval.
11. **Ramon (B07).** Is the C22 bus driver Ramon (thirty-six years on the Magazine line) registry B07, Ramon Espina?
12. **Recurrence of the 22 new rows** beyond B01. The audit calls them locals who carry into B02; no ruling says so,
    so every new row reads "recurrence OPEN".
13. **Philomène in B02.** Ruling #7 leaves her to "whatever serves the story and the saga best"; she is not in the
    final B01, and B21 keeps her B02 recurrence open.

---

## 3. Not changed, and why

- **`recovery/ACCOUNT_EXPORT_CONCORD_TIER1_PAIR_AUDIT_2026-09-20.md`** (research §4 proposed a supersession pointer).
  `recovery/` is never edited in place (CLAUDE.md §1); the refinement of "Concord is NOT founded — it EMERGES" is
  recorded in ledger §591 and in Concord-Mandate's note instead.
- **`decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` / D11.** The bearing of a rival holder of the name
  on the B09 naming is recorded as an OPEN item in Concord-Limits rather than as a note on a ruling the new direction
  does not touch.
- **`canon/characters/LacunaID.md`, `rules/canon_rules.json` (CORR_CONCORD).** Research §4: no change needed.
- **A registry row for the funder.** The registry is a cast list; the funder is an unnamed organization. It is
  recorded in BazID, the Concord files, Dominions.md, the B02–B04 contexts and Ms. Tran's row (B37).
- **The manuscript's `STYLE_SHEET_B01.md`** (two notes: §8's "Mais non to Odile, Ch 44" example is gone; the Cajun
  reader's range should read "1–2, 33, 44"). The file is manuscript-side, outside this canon repository; left for the
  manuscript session.
- **SeraphineIdentity §XII (the 2026-10-14 camp note).** Unaffected by Dré's place of death: it concerns where the
  boundary gave, not where he died.
- **`book_context` entry_state for B02–B09.** Derived by the tool; the funder thread went into a hand-authored key
  instead, so regeneration keeps it.
- **Audit claims not confirmed on the page, left out:** Renée "on leave pending the certificate" (C19); Lorraine's
  husband; Mr. Ledet's sister in Gretna (the C24 line is ambiguous); "yellow is his color" for Dré; Marisol's Spanish
  being absent; Isaiah and Tamika as cousins; Rieux giving Baz his own number; the Lena's-mother call detail beyond
  "he telephones her"; Ms. Tran's title; Gwen's "Mrs." insistence; Mr. Ledet's left-handed signature. None changes a
  ruling; they can be added if a later check confirms them.
- **Dialect ruling 1 (Gwen's plate-sale day), ruling 2 (Mr. Ledet re-voiced), ruling 4 (authenticity readers),
  the POV-interior rulings, the humor direction, repetition/realism/continuity defaults, the C43 locked edit:** page
  and process rulings with no canon-card consequence beyond what is recorded above.
- **Seraphine's §XI "three weeks" for the unfinished renewal** against the page's "nine weeks" for the yellow tab
  (C40): not in any checklist and not clearly the same span; noted here, not changed.

---

## 4. Repair

`canon/cast_registry.csv` row **B21** (Philomène) had been written on 2026-10-12 with unquoted commas inside its
function field, which shifted the rest of the row into the wrong columns (17 fields for 15). The text was rejoined
and requoted unchanged; the repair is noted at the head of the field. No other row's bytes changed apart from the
appended amendments.

---

## Summary

Canon now matches the final B01 and the 2026-10-18 polish rulings: Lucien's posting is suspended with his papers sent
to Vienna; Baz's funder is a Dominion splinter, the New Orleans circle later splits from it and only then founds
Concord, and the name is co-opted by the former funder and then an institutional Concord; Caldas is Portuguese with a
Lisbon-schooled English and reads the review in B02; Dré may die in the ambulance or at the hospital; Elisabet's page
height fits her card; the house, Philomène, Lacuna, nickname and dateline rulings are applied; and 22 B01 locals have
registry rows. Twenty-five files changed and this report added, all additively; validation passes. Thirteen items wait on the author (§2),
the most consequential being the book of the split and founding, the Mandate's classification, whether the splinter is
compromised, and "Dominion" being spoken in B01.

---

## Addendum, 2026-10-18 (later): author answers applied (ledger §592)

The author answered nine of the thirteen §2 items (09:54), ruled on the funder's nature (09:59, "Agreed as
recommended") and gave a provisional funding direction (10:02, "Yes"). They are recorded verbatim in
`decisions/B01_CANON_OPEN_ITEMS_AUTHOR_ANSWERS_2026-10-18.md`. Method as above: additive dated notes and pointers only;
no canon text removed. Validation after the changes: `validate_canon.py` exit 0 (no violations); `test_validate_canon.py`
171 tests OK; `derive_book_context.py --check` no drift; the ledger diff is additions only (10 lines); every changed
registry field is the old value with text appended.

### A.1 What was applied

| §2 item | Answer | Applied as |
|---|---|---|
| 2, split and founding | "I lean 3 or 4, potential tie in to Baz's demise." | Leaning: the B03→B04 boundary, caused by the circle learning, around Baz's death, that he was still paid by Dominion (09:59). Exact book not locked. |
| (new) Concord's nature | A loose collection of people; the term co-opted by an organization that turns insincere | The protagonists' Concord is a loose collection; "the organization is founded after the split" superseded where it implies formality; Dec 12 "not founded — emerges" largely stands again. Each Tier-1 Concord file annotated with which parts fit the loose collection and which the co-opting organization. |
| (new) the funder, 09:59 | An internal faction within Dominion | Supersedes "Dominion splinter". It is the co-opting organization (funder lineage), co-opts the name in Neon and collapses in Loom. Virelli does not know at first and suspects by B04. Helena is a possible member. |
| 5, compromised? | "I'm open but lean yes." | Leaning: "no redemption arc" applies provisionally, to the faction's leadership (09:59, point 2). |
| 6, after the Mending | "no they collapse in Loom." | Ruled: the co-opting organization collapses in B07–B09; Concord-Limits §V holds. B07–B09 contexts carry the item. |
| 8, "Dominion" in B01 | "naming is approved." | Named once, at C34; pointer on the 10-09 decision; B01 entry_state resolved. |
| 9, B02 E08/E34 | "as best fits the saga." | Proposal under delegation in both packets and LucienID: E08 loses the first naming and widens (the camp report was read too); E34 becomes an escalation (the method used beyond New Orleans). |
| 10, Caldas | Restrained by leadership in B02, free rein in B03 | Registry C02, Dominions.md, B02 E27, B03 E14. City–Dominion note drafted from the page for confirmation. |
| 11, Ramon | "if that fits, yes." | It fits: C22 Ramon is B07 Ramon Espina (pointer on the row). Guardrail: C22 is a service party, not a retirement. |
| 12, recurrence | "open to whatever fits the saga and prose best." | Recommendations appended to all 22 rows. Strong: Lanette, Nyla, Mrs. Carmouche, Ms. Tran, Pryor, Curtis, Annelie Strobl, Lena (already ruled), Mr. Vidrine (as B02's oxygen resident). Light or texture: Lorraine, Gwen, Vernice, Isaiah, Tamika, Miss Hazel, Mr. Alcide, Miss Pearl, Mr. Fontenot. B01 only: Dion, Keon. No recurrence: Mrs. Arceneaux, Hedwig Pospischil (both dead). |
| (new) funding, 10:02 | Elisabet's open money and mutual aid | Provisional: ElisabetID, RexID (not the funder), Concord-Structure §VI, Concord-EraFunction, B03/B04 contexts. |

### A.2 Files changed

| File | Change |
|---|---|
| `decisions/B01_CANON_OPEN_ITEMS_AUTHOR_ANSWERS_2026-10-18.md` | New: the answers verbatim, the 09:59 ruling and the 10:02 direction, with scope. |
| `canon/factions/Concord/Concord-Mandate.md` | Loose collection vs co-opting organization; the classification and §VII read as the organization's; OPEN carried. |
| `canon/factions/Concord/Concord-Structure.md` | §I, IV–VII, IX–X for the loose collection; §II–III's apparatus and §VIII's drift for the organization; §VI funding (provisional). |
| `canon/factions/Concord/Concord-EraFunction.md` | Veil, Neon and Loom reread; the co-opting organization collapses in Loom; funding (provisional). |
| `canon/factions/Concord/Concord-Relationships.md` | Internal faction; collision; how to read §II–IX; §III OPEN carried. |
| `canon/factions/Concord/Concord-Limits.md` | §V answered (collapse in Loom); §IV "failure is not evil" holds for the loose collection only. |
| `canon/factions/Dominions.md` | Internal faction (supersedes splinter); Virelli; leadership's "no redemption arc"; Helena possible; naming approved; Caldas's ladder; **City–Dominion DRAFT**. |
| `canon/characters/BazID.md` | Internal faction; still paid, does not suspect in B01; split cause and timing; loose collection; naming. |
| `canon/characters/LucienID.md` | Naming; E08/E34 proposal; may notice "first" and say nothing; Helena; Virelli suspects by B04. |
| `canon/characters/VirelliID.md` | The faction inside his house; does not know at first, suspects by B04. |
| `canon/characters/ElisabetID.md` | Open, signed-for money after the split (provisional); a reason to stay. |
| `canon/characters/RexID.md` | Not the funder; possible later infrastructure. |
| `canon/cast_registry.csv` | 25 rows appended: recurrence recommendations on B22–B42 and C06; B07 Ramon merged; C02 Caldas ladder; C04 Helena possible member; B37 funder note. |
| `book_context/book_context_B01.json` | entry_state: naming resolved (Lucien); funder an internal faction (Baz). |
| `book_context/book_context_B02.json`–`B04.json` | New hand-authored key `_concord_open_items_answers_2026_10_18` (funding block on B03 and B04). |
| `book_context/book_context_B07.json`–`B09.json` | New hand-authored key `_concord_cooption_collapse_2026_10_18`. |
| `ebci/B02/S1.T1.B02.A1.E08.md`, `S1.T1.B02.A3.E34.md` | Delegated re-scope (proposal). |
| `ebci/B02/S1.T1.B02.A2.E27.md`, `ebci/B03/S1.T1.B03.A1.E14.md` | Caldas restrained (B02) and free rein (B03). |
| `decisions/B01_POLISH_CANON_AUDIT_RULINGS_2026-10-18.md`, `B01_POLISH_RECOMMENDATIONS_APPROVED_2026-10-18.md`, `B01_C_AND_B_RULINGS_2026-10-17.md`, `B01_DIRECT_CONFLICT_HOUSTON_AND_SPLITS_AUTHOR_ANSWERS_2026-10-09.md` | Dated pointers. |
| `recovery/RECOVERY_LEDGER_2026.md` | §592 appended before END. |
| `reports/B01_POLISH_CANON_UPDATE_2026-10-18.md` | This addendum. |

### A.3 Still OPEN

From §2, not answered: **3** Concord-Mandate's classification and §VII (now annotated as the co-opting organization's,
pending a ruling); **4** Concord-Relationships §III (*does not challenge Dominion authority head-on*) toward a Dominion
faction that carries Concord's name; **13** Philomène in B02. **7** is answered in part (Baz does not suspect in B01;
the circle learns around his death; the name is co-opted when resonance goes public in Neon): the Neon book of the first
co-opted use is open. Item 1 (Lorraine) was resolved earlier as a slip.

New: the exact book of the split (end of B03 or start of B04); the book and manner of the faction's collapse in Loom;
what Caldas's B03 free rein licenses on the page; Helena's membership (a possibility only); the funding details
(provisional); **author confirmation** of the City–Dominion draft, the E08/E34 proposal and the recurrence
recommendations; one reconciliation for the B02 pass (Mr. Vidrine is on Ursulines; E27 clears the Bywater block).

### A.4 For the manuscript side

- **No B01 page change** is required by any of these answers (09:59, point 4: Lucien may notice the shared word
  *first* and say nothing, as the page stands).
- **No Ramon rename.** One guardrail for later passes: C22 must not read as a retirement party, since he drives in B02.
- Carried from §3: the two `STYLE_SHEET_B01.md` notes.

### Summary

The answers are recorded and applied. The protagonists' Concord is now a loose collection of people, not a founded
organization. Baz's funder is an internal Dominion faction that still pays him. It later co-opts the name, turns
insincere and collapses in Loom. The split leans to the B03→B04 boundary and comes when the circle learns about the
money around Baz's death. "Dominion" is named once in B01. Caldas is held back in B02 and given free rein in B03. The
C22 Ramon is B07. Recurrence recommendations sit on all 22 new rows, and the E08/E34 re-scope and the City–Dominion
note wait for the author's confirmation. Validation passes. Three original §2 items stay open (3, 4, 13), and item 7
is partly open.
