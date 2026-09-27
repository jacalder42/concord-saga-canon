# B01 EBCI pilot — build notes for the narrative review

**Date:** 2026-09-27
**Status:** EDITORIAL REPORT — NON-CANONICAL. What building the two pilot packets showed, for the
author's narrative review (`decisions/POST_AUDIT_SEQUENCE_AND_EBCI_PILOT_AUTHOR_INSTRUCTION_2026-09-27.md`
§4). **The review is the gate; these notes are not a verdict.** Claude wrote the packets it describes.

**Reviewed 2026-09-27: the pilot passes, with revisions** (`decisions/B01_EBCI_PILOT_REVIEW_AND_ACT_I_RELEASE_AUTHOR_RULING_2026-09-27.md`): E31 Seraphine, E33 Baz and Tremé approved; F1 answered by the two-layer template (R3); F3 by `ENV` NONE (A4); F5 by POV-capable entities (R4); F7 kept as descriptive tracking (A3). **Act I released.**

**What was built:** `templates/EBCI_PACKET_TEMPLATE.md`; `ebci/B01/S1.T1.B01.A2.E31.md` and
`ebci/B01/S1.T1.B01.A2.E33.md`; 14 beat rows in `grids/episode_beats.csv`; four validator checks with
nine self-tests (162 in all, passing).

**What it does not change:** no ruling, milestone, card or rule text; no other B01 packet.

---

## 1. For the review: where to look

| Question | E31 | E33 |
| --- | --- | --- |
| Would a novelist be helped or constrained? | **Episode contract and Beats** (the novelist's part) | **Episode contract, Beats and Chronology guard** |
| Is anything filled because the template has it? | Opposition, Unresolved, Event record and Wonder are **`none` on purpose** | The event record is needed here |
| What is writer-only? | ECID, Obligations, Tracking, Notes | ECID, Event record, Obligations, Notes |

**Claude's own read, for what it is worth:** E31's contract and beats stay loose (six beats, no
turn forced beyond *"someone has more fun than expected"*). **Its overhead is the ECID block and the
Obligations section**, which a novelist does not need; they are for the machine and the ledger.

## 2. Findings

| # | Finding | Proposed response (for after the review) |
| --- | --- | --- |
| **F1** | **For a Life/Reward episode the ECID block is pure overhead** (U1 / W0 / FX0 / CALM tells a writer nothing) | Keep ECID in EBCI for the machine; **leave it out of the prose-facing Sudowrite packet** (already the plan: `CLAUDE.md` §9 step 6) |
| **F2** | **The ECID "end state" rule fits an event episode badly.** E33's packet ECID is U3, the state after the event; the story is the curve. The beat rows carry the curve (U2 before, U3 from the windows on) | Packet ECID = end state; **beat rows carry the curve**. No change needed, only a template note |
| **F3** | **`ENV` has no value for an ordinary place.** Its vocabulary is the zone taxonomy; both packets use `NONE`, and most Veil episodes will | Make `ENV` optional below zone level, or accept `NONE` as the Veil default. **An author question at Act I** |
| **F4** | **`CHK_PACKET_LINKS` found a real ledger gap on its first run:** `BC-BOUNDED-RESPONSIBILITY` (LOCKED) did not list B01 E33 or E45, although the approved overlays and the causal cards' Seraphine ladder put the overreach rung there | **Fixed:** both added as reinforcements, with a dated note |
| **F5** | **Silence and Hope are not known cast** (no card, no registry row), so the prologue packet would fail `CHK_POV` | Register them (they are ruled characters) **before the Act I release**, or allow a named non-human POV |
| **F6** | **Two real choices surfaced as `[P]`:** E31's POV (Seraphine, recommended; Lucien or Caro possible) and **E33's POV (Baz, recommended as the witness; Seraphine the alternative, which puts her attuned reading on the page)** | The author's, at the review |
| **F7** | **The Tracking line** (fun · slice of life · wonder) costs one line and records presence, per the author's clarification | Keep; sum it per act later to see whether they occur enough |

## 3. The pilot inputs

- **E33's district (PI2):** Tremé (recommended), Central City, or Marigny (the E29 zone, beside the Vein).
- **The season (PI3):** `[P]` in both packets.
- **`soft_modulation` (PI1):** not a ceiling; the B01 overlays carry the author's clarification.
