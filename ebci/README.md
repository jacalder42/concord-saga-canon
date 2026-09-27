# ebci/ — episode production packets

Status: PRODUCTION LAYER. **B01 is released, built in full, audited and compressed** (`decisions/B01_FULL_AUDIT_COMPRESSION_AND_CALENDAR_AUTHOR_RULING_2026-09-27.md`, Q-FB1). **B02 is released on a condition** (a five-packet verification of the compressed briefs, Q-FB4), with a stop after B02 for its book-level audit. The verification did not cleanly pass, and **the author passed the gate** (`decisions/B01_COMPRESSION_GATE_AND_B02_EBCI_RELEASE_AUTHOR_RULING_2026-09-27.md`): **B02 is released.** **B03 stays held.**

Originally: **B01 two-packet pilot only.** Created 2026-09-27 when the author released
the B01 EBCI hold for the pilot (`decisions/SAGA_LOCK_AND_B01_EBCI_PILOT_RELEASE_AUTHOR_ANSWERS_2026-09-27.md`,
Q-LS2). **Nothing else in B01, and nothing in B02 or B03, is released.**

## What is here

| File | Episode | Status |
| --- | --- | --- |
| `B01/S1.T1.B01.PR.E00.md` … `B01/S1.T1.B01.A1.E17.md` | **Act I**: the prologue and E01–E17 (S01–S03 inside E05, E08, E10) | DRAFT; Act I audit passed |
| `B01/S1.T1.B01.A2.E18.md` … `B01/S1.T1.B01.A3.E48.md` | **Acts II–III** (S04–S06 inside E28, E35, E48); **labels in reading order** (old E37 → E36, E36 → E37, E44 → E43, E43 → E44) | DRAFT, awaiting the full-B01 audit |
| `B01/S1.T1.B01.A2.E31.md`, `…E33.md` | the pilot (Life/Reward; event) | REVIEWED |

**B01 is complete at EBCI resolution:** 49 packets (the prologue and 48 episodes), beat rows in
`grids/episode_beats.csv` (114 after compression; 248 before), six supplement rows in `grids/supplement_deployment.csv`.

## Rules

- **Two layers in one file** (pilot review R3): the **Narrative brief** is what a prose packet is built from; the **Control layer** (ECID, event record, breadcrumbs, tracking, provenance) is not passed to prose generation by default.
- **Packets are not prose.** No dialogue, no scene text. They are built from the template in
  `templates/EBCI_PACKET_TEMPLATE.md` and are never fed raw to prose generation (a smaller Sudowrite
  packet is derived from a locked packet; `CLAUDE.md` §9 step 6).
- **The validator scans this directory** and holds it to canon scope: `CHK_BID_FORMAT`,
  `CHK_EPISODE_BAND` (CORRIDOR `N/A` only for a non-mortal POV), `CHK_PACKET_LINKS`, `CHK_POV` (cast, `pov_entities`, or a declared anonymous class), plus vocabulary, SID and retired-term checks.
- **The gate is a narrative review, not the validator** (`decisions/POST_AUDIT_SEQUENCE_AND_EBCI_PILOT_AUTHOR_INSTRUCTION_2026-09-27.md`
  §4): *"If I handed this to a good novelist, would it help them write a better scene—or would they
  spend their energy satisfying the packet?"* If E31 reads as predetermined, EBCI is simplified before
  any further packet is built.
- **The full-B01 audit is written** (`reports/B01_FULL_EBCI_AUDIT_2026-09-27.md`): the architecture passes; the briefs are overbuilt, and a compression pass is proposed before B02 EBCI. Five brief defects were fixed (POV breaches, a name leak, scaffolding).
- **Compressed 09-27 (Q-FB1).** The brief states what the episode is for, what must be true at its end and what the page must never do; it does not stage the scene. ***Silence is permission:*** anything the brief does not constrain is prose's. Event images beyond the required observable are **writer options** in the control layer. Each header has an approximate **When** (B01: late February to late April). Pre-compression briefs are in git at `6e9f3e1`.
- **B02 built 09-27** (`ebci/B02/`, 47 packets; S01–S04 inside E07, E27, E29, E40; S05 deferred), under the compressed template from pass 5 with the Veil audit overrides (E03, E15, E19, E30, E40, E47), refinements §4 (E47's crude-rule extension) and nine-book V1 (the triangle mark on every anonymous MT post) and V3 (E31 Seraphine-led). 99 beat rows, four supplement rows. POVs follow pass 3's owners; provisional ones are `[P]`. **When is `[P]` throughout** (no B02 season is approved). **Audited 09-27** (`reports/B02_EBCI_AUDIT_2026-09-27.md`): all six tests pass; four brief corrections applied. **Answered 09-27** (Q-B2-1–6 applied; E03's POV is the anonymous-ensemble class; E41's CORRIDOR is N/A). **B03 is released.**
- **B03 built 09-27** (`ebci/B03/`, 48 packets: 45 and a three-episode epilogue, `EP` E46–E48; S01–S04 inside E04, E18, E31, E42), from pass 4 as revised by pass 5, with the Veil audit and refinements overrides (E07's Detroit condition, E13, E29/E32/E36's avoided exposure, E35) and nine-book V1 (the mark on every anonymous MT post, and on Tahl's E48 post), V2 (E35, E44 Seraphine-led) and V4 (no sky at E47). Unnamed people hold POVs through the anonymous classes (E19, E28, E29, E32, E34, E39). 98 beat rows, four supplement rows. **An `EP` overlay** (`act_overlays/act_overlay_S1_T1_B03_EP.json`) inherits A3's band verbatim; no new envelope. **When is `[P]`** (no B03 calendar approved). **Audited 09-27** with the trilogy (`reports/B03_AND_VEIL_TRILOGY_EBCI_AUDIT_2026-09-27.md`): all tests pass; Baz's death-tells, forward pointers and one unintroduced term moved out of the briefs. **Veil is prose-ready (09-27).** Q-V3-1–4 applied (B03 E21 Seraphine's; calendar September–early October).
- **Death-tells stay out of briefs** (B03 + Veil audit): a guard that names a character's future death (*no death foreshadowing*) goes in the control layer as *"Guard, control layer only"*; the brief states the life positively.
- **Prose packets** (`ebci/prose/`, 09-27) derive from the **Narrative Brief only**; the control layer, Writer Options included, stays behind the writer unless an option is promoted for one episode. The B01 E31/E33 pilot awaits review.
