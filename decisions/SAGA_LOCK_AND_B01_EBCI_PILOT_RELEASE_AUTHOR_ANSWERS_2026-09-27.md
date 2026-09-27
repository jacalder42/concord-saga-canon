# The saga lock, the B01 EBCI pilot release, and fun and wonder as tracked presence — author answers

**Date:** 2026-09-27
**Status:** CURRENT AUTHOR ANSWERS. **Q-LS2 releases the B01 EBCI hold for the two-packet pilot
only.** Q-LS1 is a working direction; Q-LS3 is approved design; the note on fun and wonder is an
**author clarification** of what an existing field means. No milestone, rule text or card changes.

**Questions put:** Q-LS1–Q-LS3, `reports/SAGA_LOCK_CHECK_FOR_VEIL_EBCI_2026-09-27.md` §5 (ledger
§209).

**The author's words, verbatim:**

> As a note the Fun/Wonder was not meant to operate as a ceiling. Those metrics are intended to be
> tracked to ensure they occur enough.
>
> LS1-LS3 as recommended

---

## 1. What is decided

| # | Decided |
| --- | --- |
| **Q-LS1** | **Saga-scale architecture work ends for now.** It reopens only on a discovery in EBCI or prose. The progressive-resolution instruction's step (d) is complete; its step (e) now runs |
| **Q-LS2** | **The B01 EBCI hold is released for the two-packet pilot only: E31 and E33.** The report put this as the author's act, with nothing in the way; *"as recommended"* is read with the post-audit instruction's step 4, which set the form (*"Release the B01 EBCI hold for the two-packet pilot only"*). **In scope:** the packet template installed in `templates/` (preflight Q4); `ebci/B01/` created (Q5); the four validator checks (Q8); the E31 and E33 packets and their beat rows in `grids/episode_beats.csv`. **Out of scope until the author's narrative review:** every other B01 packet, the release-time envelope work (the `PR` overlay, the A1 exceptions, the relabel), and any B02/B03 packet |
| **Q-LS3** | **The pilot inputs as recommended.** PI1: the packets do not treat `soft_modulation` as a ceiling. PI2: the E33 packet offers districts inside the zone E27 predicted, and the author picks one at the review. PI3: the season is marked `[P]` in the pilot and set when Act I is released |

## 2. The clarification: fun and wonder are tracked for presence, not capped

**`soft_modulation` (fun, slice of life, wonder) was never meant to be a ceiling.** The metrics exist
**to be tracked, to make sure these things occur enough.** So:

- **The field records a presence to track, not a maximum.** Its key name, `max_intensity`, is
  scaffolding from the template and reads as a ceiling; that reading is wrong. (All 81 values across
  the 27 overlays are the template's `LOW`, already recorded as *"TEMPLATE, NOT RECOVERED CANON"* in
  `proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md`.)
- **Packets track it.** The EBCI template carries a **tracking line** (fun · slice of life · wonder:
  what the episode actually delivers). It is a record, not an obligation: an episode may deliver none
  of them.
- **Not done here:** renaming the key or rewriting the 27 overlays' values. Once the pilot shows what
  tracking needs, a schema proposal (for example `track_presence` with a target per act) can follow.
  Until then, a dated note on the B01 overlays records the meaning.

## 3. What this does not change

- **Only E31 and E33 are released.** The hold stands for everything else in B01, and for B02 and B03.
- The pilot's gate is the **narrative review** (post-audit instruction §4): *"If I handed this to a
  good novelist, would it help them write a better scene—or would they spend their energy satisfying
  the packet?"* If E31 comes out predetermined, **simplify EBCI before multiplying it**.
- No ruling, milestone status, card or rule text.
