# B01 Act I EBCI audit

**Date:** 2026-09-27
**Status:** EDITORIAL REPORT — NON-CANONICAL. The stop after Act I required by
`decisions/B01_EBCI_PILOT_REVIEW_AND_ACT_I_RELEASE_AUTHOR_RULING_2026-09-27.md` §4, answering its two
questions. **Claude built the packets it audits**; the measurements in §3 are there so the author can
check the judgement.

**What it audits:** the 18 Act I packets in `ebci/B01/` (the prologue and E01–E17; S01–S03 inside E05,
E08 and E10), their 85 beat rows, the `PR` overlay and the A1 exception (ledger §212).

**What it does not change:** nothing. The remainder of B01 stays held until the author authorises it.

---

## 1. Verdict

1. **Did EBCI discover anything that materially changes downstream book or saga architecture? No.**
   Act I produced one release question closed, two small envelope and tooling items, one cross-act
   obligation, and one tracking pattern. None moves a milestone, an episode, a breadcrumb's payoff or a
   later book (§2).
2. **Do the packets leave enough room for prose discovery? Yes, with one watch item.** The briefs are
   short (about 170 words, four or five beats) and mostly restate v4.1b's architecture; the choices
   they add are POV, place level and page-safe constraints. **The watch item is the length of some
   "must not spend" lists** (§3).

**Recommended:** return for authorisation to release the remainder of B01 (Q-AI1), with the A2/A3
release work in §4.

## 2. What EBCI found (question 1)

| # | Finding | Kind | Changes architecture? |
| --- | --- | --- | --- |
| **E1** | **The A1 widening's mapping is confirmed by v4.1b itself** (E15 *"source E13"*, E16 *"source E14"*). The W3 exception is declared at E15 only; nothing for E16 | Closes a release question | No |
| **E2** | **The prologue has no weather ruling**; its overlay carries A1's W0–W2 alongside the ruled U7/FX3 | Envelope detail | No. A ruling can replace it later (Q-AI3) |
| **E3** | **A latent validator bug:** a `PR` SID inside a file path produced a phantom `...B01.P`. Fixed, with a regression test | Tooling | No |
| **E4** | **A cross-act obligation:** E15's recordings reach Baz *"by consent before E25"*; E16 now mentions a file in the cleanup, so **E25's packet must pick up the custody** (who has which copy) | Continuity inside B01 | No; it is carried to the A2 build (§4) |
| **E5** | **Tracking shows Act I has no wonder after the prologue**, and fun only once at strength (E06). B01's first wonder episode is E26 (A2). v4.1b designs Act I as grief and discovery, so this is the design working, not a defect, **and exactly the pattern tracking exists to show** | Tracking data | No. Q-AI2 asks whether prose may find light wonder in an LR unit, without a new beat |
| **E6** | **EBCI was mostly translational in Act I.** Beats follow v4.1b closely; what EBCI decided was POV (three `[P]`: E06, E09, E14), place level, the page-safe causal constraints (E15), and the envelope. **The generative work concentrated in the event episode and the prologue** | Evidence for the prose-order lean | No. It is input to the post-audit instruction §5 (EBCI before prose): **ordinary episodes translate; event episodes generate** |

**Nothing found reaches B02, B03 or later books.** No breadcrumb, milestone or Möbius row changed.

## 3. Room for prose (question 2)

**Measured across the 18 Act I packets:**

| Measure | Act I | Note |
| --- | --- | --- |
| Narrative brief | **about 170 words** on average (100 at E14, 295 at E15) | E15 carries its page-safe constraints |
| Control layer | about 190 words | Heavier than the brief, as the author expected, and not passed to prose |
| Beats | **4.7** on average | Loose units; none carries dialogue or exact behaviour |
| Negations in "must preserve / must not spend" | **3.1** on average; **8 at the prologue**, 6 at E03 | The prologue's are its guardrails; E03's protect Caro from an introduction package |
| Choices left to prose, marked `[P]` or "prose's to find" | E06's turn, E14's kindness, E01's household, every season | — |

**What keeps room:**
- Turns name the change and leave the discovery: E06 *"The room works on her the way a good room
  does"*, E14 *"which small kindness lands, and how, is prose's"*.
- **Life/Reward units stay light.** E03, E12 and E14 have no opposition, consequence or event record.
- **Where beats look prescriptive, they are v4.1b's protected beats**, not EBCI's additions: E13's
  mutual permission (the first relationship rung) and E17's call.

**The watch item:** the "must not spend" lists are all negatives, and some run long. They are right
for the control review; **a prose packet should carry them positively and shortest-first**, keeping
every prohibition that protects the page (no Virelli, no death foreshadowing, no LT motif) and leaving
ledger-only guards in the control layer. **A Sudowrite-derivation rule, not a packet change** (Q-AI2).

## 4. If the remainder of B01 is released: the A2/A3 work

- **The relabel** (OQA B3): E36/E37 and E43/E44 to reading order; S05's placement; the breadcrumb
  locators that name them (`BC-FILAMENT-ETHIC`, `BC-PULSE-NAMING`).
- **A2's `basis_note`** uses recovered numbering; note it as at A1.
- **E25 carries E15's custody** (E4 above).
- **The E45 and E48 causal cards** are approved; E48's observable is still water (Q-E48-1).
- **S04–S06** follow the S01–S03 pattern (inside the preceding packet; a deployment row each).
- **E31 and E33 are already reviewed** and stay as they are.

## 5. Questions for the author

| # | Question | Recommended |
| --- | --- | --- |
| **Q-AI1** | **Release the remainder of B01 EBCI** (A2 and A3), with §4's release work; B02 and B03 stay held | **Yes**: Act I passes both tests |
| **Q-AI2** | **Two light rules:** (a) prose may find light wonder in an Act I LR unit without a new beat (tracking stays descriptive); (b) prose packets carry the "must not spend" constraints positively and shortest-first, keeping every page-protecting prohibition | **Yes** to both |
| **Q-AI3** | **Confirm the three `[P]` POVs** (E06 Seraphine, not Trip; E09 Mara, not Seraphine; E14 Lucien, not Seraphine) and the **prologue's weather band** (A1's W0–W2, pending any ruling) | **Yes** |
