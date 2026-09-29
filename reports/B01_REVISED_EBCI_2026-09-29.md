# B01's revised EBCI for the ~150k redraft

**Date:** 2026-09-29
**Status:** BUILD REPORT, with questions for the author. It records steps (3) and (4a) of the approved order (Q-AC1):
selective breadcrumb and relationship updates, and **B01's EBCI revised against the approved merged outline**
(Q-MO1). The author's instruction of 2026-09-29 was: *"Proceed with outline reconciliation, the Veil B02–B03 beat
revision, and revised B01 EBCI"* (`decisions/THIRD_PRESSURE_REVISED_SET_AUTHOR_ANSWERS_2026-09-29.md`).

**Update 2026-09-29 (ledger §284):** ChatGPT's review is checked in `reports/REVISED_EBCI_AND_VEIL_PASS6_REVIEW_RECONCILIATION_2026-09-29.md`; its §5 revised answer set replaces this file's questions.

**What it does not change:**
- No ruling, milestone row or canon card.
- No B02 or B03 packet. The Veil revision is a proposal awaiting Q-VB1–12.
- No manuscript text.
- **No prose packet is derived yet.** Act I's prose packets are the next step, after the author has seen this.

## 1. What was built

**Fifty packets in `ebci/B01/`,** one per merged-outline piece:
- **Brief flags:** 13 U, 33 C, 4 N.
- **The new pieces:** E24, the pump station; E25, Metairie I; E39, the stop-work and the stakeout; E44, Metairie II.
- **Supplements:** S02 (inside E07) and S06 (inside E49).
- **Length:** about 148,700 words of narrative, which matches the outline.

`ebci/B01/REDRAFT_CONCORDANCE.md` maps every new SID to the packets it supersedes.

**The redraft fields.** Every packet carries the fields added to the template on 2026-09-29:
- *Length*;
- a *Conflict* block (Objective, Opposition by whose will, **Pressed by**, Turn, Consequence, Unresolved);
- *Exit conditions*, facts only, with no required repair;
- a control-only *Engine* line (clues, surface rules with their epistemic status, wrong theories, trace guards);
- a *Sign-off* section: Q-CE5, Q-EN8, and the author's test (*the choice in this piece → its consequence*).

**Mechanics:**

| What | Done |
| --- | --- |
| The 49 pre-redraft packets and 55 prose packets | Moved to `superseded_2026-09-29/` folders, each with a status line naming its new home (Q-AC2: retired, never deleted). The validator keeps scanning them for SID format and retired terms, but not for live bands, placements or beat rows (a new self-test covers this) |
| Beat grid | The 114 pre-redraft B01 rows are archived beside the superseded packets. **159 new rows** replace them, one per packet beat id, all resolving |
| Supplement grid | S01, S03, S04 and S05 are retired (S01 is folded into E05). S02 now follows E07, and S06 follows E49 |
| Act overlays and book context | A renumbering note. **The A1 W3 exception moves from E15 to E14** (the Square), unchanged otherwise. The authored act theses keep their pre-redraft labels (Q-RE8) |
| Breadcrumb ledger | Twelve B01 rows re-mapped to the new SIDs, each with a note (details in §2) |
| Relationship register | An additive note: R1's carried blame (E39) and R4's grievance (E48) enter B02; B02 E12 must not replay the blame as a new break |
| Test fixture | Moved to A2.E30, where BC-LACUNA-CAMEO (LOCKED) now sits |

**Validation:**
- canon scope: **0 violations** across 452 files;
- **172 self-tests pass**;
- `derive_book_context --check`: no drift.

## 2. Breadcrumb locators

Re-mapped as locators only, under Q-MO5. Each row gets a dated note.

**The LOCKED rows:**
- **BC-SOUTHWEST-LADDER:** E11 → E10.
- **BC-DOMINION-LADDER:** E17 → E15.
- **BC-LACUNA-CAMEO:** E31 → E30.
- **BC-BOUNDED-RESPONSIBILITY:** E33, E45 and E48 → E32, E46 and E49.
- **BC-SWAMP-WOUND** loses two stale B01 locators:
  - the old E22 was retired into Baz's E18, where Seraphine's memory is withheld, not on the page;
  - the old E28 was the brunch, which has no camp recall.

  Its E46 locator now names the piece where she admits the camp room.

**The SOFT rows** (ASKED-HIM-HERE, CARO-ELISABET, FILAMENT-ETHIC, JACKSON-SQUARE, VELVET-VEIN, REMOTE-SIMILAR,
PULSE-NAMING) follow their content. VELVET-VEIN gains E41 and E49 (S06).

**Not yet added:** BC-TECHNARC-KIT pre-rungs. The outline put *"the file that went upstairs"* and the cases under this
one row, but they are **two different hands**, and B02 separates them (Q-RE1).

## 3. A correction, not a decision

**The lapsed card is Dré's Medicaid coverage.** The engine designs, and from them the outline and the working lines, read
it as Seraphine's own licence or CPR card. **The manuscript (E01, E03) and the pre-redraft packets establish something
else:** his coverage lapsed in January when a notice went to a former address, and the renewal sat unfinished on her
desk.

The packet writer for E00–E09 caught it. It is corrected:
- in the private outline and working lines (manuscript commit `7fe5c7c`);
- in every packet that touches it: E01, E03, E21, E25 and E44.

So **there is no licensing pressure on her.** At E44 what she tells Renée is the renewal on her desk.

## 4. Other readings made by the packet writers (recorded; no question needed)

- **Guards narrowed where the outline now names the thing:**
  - E43's dry wind;
  - E35's *"off the case except the column"*.
- **E18's old exit is dropped.** The old E22 exit (*holds community knowledge more carefully*) contradicts the outline,
  where she adopts W3 with its disconfirmer hidden.
- **Elisabet gives no length of stay** (Q-OL4 #3), and at E28 she leaves; she does not return to her work.
- **E26:** Lucien keeps the page, and Baz has a copy.
- **E41's place is left open.** The outline says the Vein; the manuscript says elsewhere.
- **E47's call that rings with no sound** stays an optional, unexplained image. R4 (machines fail after it, never first)
  holds.
- **E45:** Mrs. Carmouche's *credit* is read as the gathering being her idea.
- **Control-layer values:**
  - E31's weather is W0 (nothing happens);
  - E39's load is L2 (L3 is kept for the rebound);
  - E40's corridor is U2.

## 5. Questions for the author

| # | Question | Recommended |
| --- | --- | --- |
| **Q-RE1** | **The two hands in the breadcrumb ledger.** (a) The **cases, the lanyards turned in, the collector, and the man who wanted the minute** become SOFT pre-rungs of BC-TECHNARC-KIT: E20, E25, E31, E34, E36, E39, E48, E49. (b) The **file's route** (the index card, R.'s *March*, the city's call to Denise, Guidry's copy) becomes a **new SOFT row**, a file that went upstairs, paid at B02 E08 (Helena's clause). This leaves the LOCKED Dominion ladder untouched. Some packets now mark authority-side plants (E14, E15, E37, E38) as *proposed* TECHNARC-KIT pre-rungs; those notes move to the new row on the answer | **(a) and (b)** |
| **Q-RE2** | **Q-DR12, the whole-crowd fall at the Square** (E14), is recorded as a lean (*"likely accept"*). R2 and C4 rest on it | **Confirm** |
| **Q-RE3** | **Lucien's site visit to the camp at E04** is the Act I scene the old packets had. Q-DR7 bars a *return* to the camp. Is this first visit permitted? | **Yes:** it is not a return |
| **Q-RE4** | **The pump station** is placed Mid-City or canal-side, and the outline's *"behind the stadium"* is dropped. That wording reads as downtown, against the guard that nothing is near the Warehouse District | **Yes** |
| **Q-RE5** | **The page word for the grey boxes is *case*,** in every brief, so they never collide with Mara's food boxes | **Yes** |
| **Q-RE6** | **The stranger at E49 is named Jody,** as in the outline and the manuscript. He has no later role and does not recur | **Yes** |
| **Q-RE7** | **S06's Darnell** shares a first name with *Darnell Ross*, a later-book courier in a Tier D proposal | **Keep S06's Darnell;** they are different people. Rename the Tier D courier if he is ever used |
| **Q-RE8** | **The act overlays' theses and carriers** keep their pre-redraft labels. Refresh them to the redraft's numbering and engine as approved design, drafted with Act I's prose packets? | **Yes,** then |

**Answer format:** for example *"Q-RE1–8 as recommended."*

## 6. Next

1. **The author's answers:** Q-VB1–12 (the Veil revision, ledger §282) and Q-RE1–8.
2. **Then B01 Act I's prose packets,** derived from these Narrative Briefs only. The drafting stack adds the working
   pressure lines, as they stand at each piece.
3. **Then the sequential redraft.**
4. **When the Veil revision is applied,** B02 and B03 packets that cite B01 episode numbers move to the redraft's
   numbering (the concordance gives the map).
