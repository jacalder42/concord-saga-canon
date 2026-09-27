# ebci/ — episode production packets

Status: PRODUCTION LAYER. **The pilot passed (2026-09-27, `decisions/B01_EBCI_PILOT_REVIEW_AND_ACT_I_RELEASE_AUTHOR_RULING_2026-09-27.md`); the hold is released for B01 Act I only** (the prologue and E01–E17). A2 and A3 beyond E31/E33, and B02–B03, stay held.

Originally: **B01 two-packet pilot only.** Created 2026-09-27 when the author released
the B01 EBCI hold for the pilot (`decisions/SAGA_LOCK_AND_B01_EBCI_PILOT_RELEASE_AUTHOR_ANSWERS_2026-09-27.md`,
Q-LS2). **Nothing else in B01, and nothing in B02 or B03, is released.**

## What is here

| File | Episode | Test |
| --- | --- | --- |
| `B01/S1.T1.B01.A2.E31.md` | *The Night They Were Going to Have* | **Life/Reward**: can the packet stay loose, human and inviting? |
| `B01/S1.T1.B01.A2.E33.md` | *The Pulse Strikes* | **Event**: causality, observation class, limits, cost, residue |

Each packet's beats also have rows in `grids/episode_beats.csv`.

## Rules

- **Two layers in one file** (pilot review R3): the **Narrative brief** is what a prose packet is built from; the **Control layer** (ECID, event record, breadcrumbs, tracking, provenance) is not passed to prose generation by default.
- **Packets are not prose.** No dialogue, no scene text. They are built from the template in
  `templates/EBCI_PACKET_TEMPLATE.md` and are never fed raw to prose generation (a smaller Sudowrite
  packet is derived from a locked packet; `CLAUDE.md` §9 step 6).
- **The validator scans this directory** and holds it to canon scope: `CHK_BID_FORMAT`,
  `CHK_EPISODE_BAND`, `CHK_PACKET_LINKS`, `CHK_POV`, plus vocabulary, SID and retired-term checks.
- **The gate is a narrative review, not the validator** (`decisions/POST_AUDIT_SEQUENCE_AND_EBCI_PILOT_AUTHOR_INSTRUCTION_2026-09-27.md`
  §4): *"If I handed this to a good novelist, would it help them write a better scene—or would they
  spend their energy satisfying the packet?"* If E31 reads as predetermined, EBCI is simplified before
  any further packet is built.
- **Now:** B01 Act I, with its release-time envelope work (the `PR` overlay, the A1 exception). **After Act I, stop for an audit** (did EBCI change downstream architecture; do the packets leave room for prose?), then return for authorisation for the rest of B01. The E36/E37 and E43/E44 relabel belongs to the A2/A3 release.
