# B01 merged draft: post-merge review, Session A — report

Status: NON-CANONICAL REPORT, 2026-10-05. It is a read-only review of the merged B01 after the beta-panel pass
(manuscript `B01/merged-2026-10-05/` at `1a8be36`, 173,456 words; ledger §419). It covers Session A of a four-part
post-merge review brief written in a chat session: Tasks 1–4, the spelling-copyedit audit, the language ledger, rules
validation, and a re-check of the beta-panel additions. The full notes, with locators and short quotes, are private, in
the manuscript's `draft-notes/post-merge-review/`. **No manuscript text is quoted here.**

**It does not change** any ruling, card, packet, rule or manuscript file. Its findings bind nothing until the author
rules. Every finding is typed:
- `conflict`: needs a ruling;
- `drift`: inconsistent, but needs no ruling;
- `gap`: missing from the page or a card;
- `ok`.

## 1. Results

| Task | Result |
| --- | --- |
| **1. Spelling copyedit** (Q-AR1, Q-FR4) | The two rulings' commits are clean: 102 and 89 token changes, **0 outside the listed classes**, and no diacritic, italic or non-English word touched. Q-AR1's diff reached the author on its branch before `main` (ledger §240–§241); a 2-form follow-up went straight to `main` (gap, trivial). **Both commits changed the old track, not the merged text.** The merged text was built later from the redraft experiment and draft 3. It has **0 UK spellings** (ok). The merged build's *round → around* pass changed 81 forms: **46 in Lucien's or Baz's own narration** (conflict with Q-FR4's exception) and **1 in Elisabet's dialogue** (conflict with Q-AR1's "American mouths"). It changed 9 American speakers' dialogue lines, where the earlier pass left all dialogue alone (policy question), and **missed 4 in American narration** (drift). 16 non-US usage forms remain in American POVs (drift) |
| **2. Language ledger** (Q-FL8) | 8 rendered non-English words or phrases (9 uses) and 11 narrated language switches; ledger rows give meaning, pronunciation, speaker, function and locator. **Plain type and diacritics: ok.** **Three approved tells never appear:** Lucien's French in intimacy, Baz's mother's Arabic, and Caro's Spanish in warmth or humor (gap; tells are permissions, not quotas, so this is not a defect). Lucien's German at a peak of stress: 0 of about 9 moments while awake. Baz's translating tell: once. Seraphine's elders' French: one form of address. **8 items need a native-speaker check** (Q-FL6, Q-FL8; gap). New fact: one supporting character's Sicilian (gap, for the cards) |
| **3. Rules validation** | `validate_canon.py`: 0 violations in canon scope. Retired terms applied to the manuscript by script: **0**. *Veil* placement: ok, with the one bridal-garment use already with the author. Technical or metaphysical vocabulary: 0, with one judgment item (instrument names in an official request). Mechanism explained: 0. **Numbers as imagery: 1 candidate** (E01; conflict, candidate). Interruptions: 93 dashes and 0 trailing ellipses in dialogue; telling a cut-off from a trail-off needs a read (judgment) |
| **4. Beta-panel additions** | Every addition was checked for continuity, POV, guards, protected lines, the E49 telling (ledger §387) and the timeline. **All six §387 design points are present**, and *Veil* is still the last spoken line. The pass's two probable slips are verified fixed. Trims leave no orphan references. The E42–E49 weekday chain holds. The rebuilt reading copy matches the source text paragraph for paragraph. **One candidate §9 item:** the new interlude's narration ties the presences' "leaning" to things on the ground giving way (conflict, candidate). One unstated step: the replacement phone's number (drift). New facts for the card review: Elisabet's return text, and Caro's Saturday shift |

**Process note:** the merged build report (ledger §415) says *around* was applied "book-wide". That is inexact: 4
adverbial forms survive in American narration, and the pass also reached the two characters Q-FR4 exempts.

## 2. Questions for the author

Options are listed. The private notes give the evidence for each.

- **Q-PM1. Scope of the Q-FR4 exception.**
  (a) Lucien's and Baz's narration and speech keep European usage: revert the 46.
  (b) Speech only: make their narration US throughout.
  (c) Leave it as it is.
  The old-track pass and the profile wording read closest to (a).
- **Q-PM2. Elisabet's one changed form.** (a) Restore it: she is not American (recommended, per Q-AR1). (b) Keep it.
- **Q-PM3. The 16 residual non-US usage forms in American POVs.** (a) One mechanical pass under the existing rulings,
  with a reviewed diff. (b) Leave them to the line pass. (c) Leave them.
- **Q-PM4. Dialogue usage.** (a) American speakers' dialogue takes US usage: keep the 9. (b) Dialogue is never
  copyedited for usage: revert the 9.
- **Q-PM5. Record the correction** to §415's "book-wide" in the ledger. (a) Yes: done in §420. (b) No.
- **Q-PM6. The unused approved tells.** (a) Leave them. (b) Add them to the B02 packet watch-list as available.
  (c) Consider them at the line pass. No lines are proposed.
- **Q-PM7. Native-speaker checks for the 8 items.** (a) Before the book leaves draft. (b) At the publication copyedit.
- **Q-PM8. The supporting character's Sicilian heritage.** (a) Add it to the registry row. (b) Leave it as texture.
- **Q-PM9. Seraphine's elders' strand** (Cajun or Creole; language notes §4, still open). (a) Confirm it now.
  (b) Leave it until the B02 packets.
- **Q-PM10. The E01 number-as-imagery candidate** (§9, ruled). (a) Flag it for the line pass. (b) It is a rough
  quantity, outside the rule's intent. (c) Author's ear.
- **Q-PM11. Trail-offs.** (a) Accept dash or full stop for both. (b) A reading pass to restore ellipses where a speaker
  trails off, per Q-FR4.
- **Q-PM12. Instrument names in an official request** (E15). (a) Allowed. (b) Plainer words.
- **Q-PM13. The interlude's link between the leaning and the collapses** (§9 and Q-SR3). (a) Keep it: correlation in
  the presences' register. (b) Soften it to juxtaposition. (c) Author's ear.
- **Q-PM14. The replacement phone's number** (E48). (a) Leave it. (b) One clause at the line pass.

## 3. Next

Session B covers voice distinctiveness and the card-versus-prose conflicts, Tasks 5–6. Session C covers the rungs
chart, grid conformance, chapter numbering and the calendar, Tasks 7–10. They are independent of each other. Veil
continuity reconciliation and the B02 packets wait for the author's read (Q-FR2 order).
