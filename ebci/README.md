# ebci/ — episode production packets

Status: PRODUCTION LAYER. **B01 is released and built in full** (the pilot, then Act I, then Acts II–III: `decisions/B01_ACT_I_AUDIT_AND_FULL_B01_RELEASE_AUTHOR_RULING_2026-09-27.md`). **B02 and B03 stay held.** Next: the full-B01 audit, then a stop.

Originally: **B01 two-packet pilot only.** Created 2026-09-27 when the author released
the B01 EBCI hold for the pilot (`decisions/SAGA_LOCK_AND_B01_EBCI_PILOT_RELEASE_AUTHOR_ANSWERS_2026-09-27.md`,
Q-LS2). **Nothing else in B01, and nothing in B02 or B03, is released.**

## What is here

| File | Episode | Status |
| --- | --- | --- |
| `B01/S1.T1.B01.PR.E00.md` … `B01/S1.T1.B01.A1.E17.md` | **Act I**: the prologue and E01–E17 (S01–S03 inside E05, E08, E10) | DRAFT; Act I audit passed |
| `B01/S1.T1.B01.A2.E18.md` … `B01/S1.T1.B01.A3.E48.md` | **Acts II–III** (S04–S06 inside E28, E35, E48); **labels in reading order** (old E37 → E36, E36 → E37, E44 → E43, E43 → E44) | DRAFT, awaiting the full-B01 audit |
| `B01/S1.T1.B01.A2.E31.md`, `…E33.md` | the pilot (Life/Reward; event) | REVIEWED |

**B01 is complete at EBCI resolution:** 49 packets (the prologue and 48 episodes), 247 beat rows in
`grids/episode_beats.csv`, six supplement rows in `grids/supplement_deployment.csv`.

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
- **Now:** the full-B01 audit (ten tests and the anti-optimisation test, `decisions/B01_ACT_I_AUDIT_AND_FULL_B01_RELEASE_AUTHOR_RULING_2026-09-27.md` §3), then a stop.
