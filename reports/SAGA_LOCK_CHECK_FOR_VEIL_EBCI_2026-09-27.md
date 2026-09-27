# Compact saga lock check — for Veil EBCI

**Date:** 2026-09-27
**Status:** EDITORIAL REPORT — NON-CANONICAL. Step 3 of
`decisions/POST_AUDIT_SEQUENCE_AND_EBCI_PILOT_AUTHOR_INSTRUCTION_2026-09-27.md`. The question, in the
author's words: *"Are there any remaining episode-architecture questions whose answer could materially
alter Veil EBCI?"* (Not to be confused with `reports/SAGA_LOCK_CHECK_2026-09-27.md`, ledger §141,
which locked the saga for Veil's step 3.)

**Method:** every open item in `CLAUDE.md` §4.1, the deferred D-items, the six Pass 4 cast decisions
(ledger §80), the preflight's open rows, and the Neon and Loom answers since, each asked one
question: **could its answer change what a Veil EBCI packet says?**

**What it does not change:** nothing. It proposes no architecture.

---

## 1. Answer

**No.** No open episode-architecture question could materially alter Veil EBCI. Everything that
bears on Veil is settled (ruled or approved design) and queued in named files; what is still open
lives in Neon or Loom, or is an EBCI-level execution choice that Veil EBCI itself makes.

**Recommended:** saga-scale architecture work **ends for now**, to be reopened only by a discovery
in EBCI or prose (Q-LS1).

## 2. What bears on Veil, and where it already sits

| Settled item | Where the packets find it |
| --- | --- |
| The Veil audit amendments and refinements | `proposals/VEIL_AUDIT_AMENDMENTS_2026-09-27.md` (§1–§4) |
| The nine-book amendments V1–V5 (the triangle's Veil half; B02 E31, B03 E35, E44 Seraphine-led; no B03 E47 sky line; the B01 E28 note) | `proposals/NINE_BOOK_AUDIT_AMENDMENTS_2026-09-27.md` §1 |
| The four B01 private causal cards | `proposals/B01_PRIVATE_CAUSAL_CARDS_E15_E33_E45_E48_PASS1_2026-09-27.md` (approved) |
| B01's overlays and entry state | `act_overlays/act_overlay_S1_T1_B01_A{1,2,3}.json`; `book_context/book_context_B01.json` |
| The packet template, storage, physics and VFX rules, validator plan | `proposals/B01_EBCI_PREFLIGHT_2026-09-27.md` (answered) |
| The macro-Möbius guardrails (the prologue names nothing; no LT motif) | `proposals/MACRO_MOBIUS_PROLOGUE_EPILOGUE_DESIGN_2026-09-27.md` §4 |
| The release-time envelope work (the `PR` overlay; the A1 exceptions; the E36/E37 and E43/E44 relabel) | the overlay drafts §5 |
| The execution principles (point at none; breadcrumbs narratively incidental) | the post-audit instruction §3 |

## 3. What is still open, and why none of it reaches Veil EBCI

| Open item | Lives in | Why it does not alter Veil EBCI |
| --- | --- | --- |
| The entity's name (D11); MT's new name (D12) | B09 epilogue | No Veil packet names either |
| Tahl's fragment's exact wording | B06 E43, E47 | Not in Veil; B09 E48 must not echo it (LX9) |
| VT's origin | metaphysics | The prologue names nothing and explains nothing (macro guardrail) |
| Ito's Loom presence (antagonist shaping) | Neon, Loom | Ito first appears in B04 |
| Pass 4 cast decisions 1–6 | cast | **Mara Niht is unplaced and absent from Veil**; Ren Bellande (B04), Roland Baptiste (Neon/Loom) and the Loom *Sparrow* are outside Veil; decisions 5–6 are provenance. Veil's Mara is `Mara` / `M` only |
| The Mechanica line-by-line review (it may reopen `STRAIN`) | rules | Packets use plain words and the preflight's R-rules; a reopened term could change a label, not an episode. **Watch item** |
| The post-Mending era file (held) | Loom | — |
| The editorial-lens fields (deferred by ruling) | review tooling | Not packet content |
| Neon pass 4's re-owning choices; the Loom execution notes (LX1–LX9) | Neon, Loom | — |
| **Seasons** (Q-NB3: left to EBCI) | EBCI | An EBCI choice Veil EBCI makes itself (§4) |
| v4.1b's explicit non-decisions (Seraphine's exact role; Caro's and Baz's employers; who sent Lucien) | EBCI | v4.1b permits them to stay unstated; a packet may leave them OPEN |

## 4. What the pilot does need (EBCI-level inputs, not architecture)

**The pilot is independent of the release-time envelope work.** E31 and E33 are both Act II episodes;
**both sit inside the A2 bands** (U1–U4 / W0–W2 / FX0–FX2; the causal cards: *"E33, E45 and E48 sit
inside their bands without exception"*); neither is touched by the relabel, the A1 exceptions or the
`PR` overlay. The pilot needs only the template installed in `templates/` (preflight Q4), `ebci/B01/`
created (Q5), and the four validator checks (BID format, episode band, packet links, POV), built at release before the pilot (Q8). The amendments that touch them
are already written: **E31** carries VAA T8 (Lacuna a cameo, zero portent; the night succeeds and is
not attacked); **E33** carries its causal card.

Three inputs, for the author at release (**Q-LS3**):

| # | Input | Finding | Recommended |
| --- | --- | --- | --- |
| **PI1** | **`soft_modulation`** | **All 81 values across the 27 overlays are `LOW`**: a template default, recorded as *"TEMPLATE, NOT RECOVERED CANON"* in `proposals/concord-2026/MIGRATION_MAP_BOOK_CONTEXT_ACT_OVERLAYS.md`. E31 is *"someone having more fun than expected"* against a `LOW` fun ceiling: the exact failure mode the E31 test is built to catch | **The pilot treats `soft_modulation` as scaffolding, not a ceiling**, and records what E31 actually needs; B01's per-act values are set after the pilot |
| **PI2** | **E33's district** | Q-E33-1 left it *"chosen at EBCI"* (inside the zone E27 predicted) | **The E33 packet offers two or three districts; the author picks at the pilot review** |
| **PI3** | **B01's season** | Q-NB3 left seasons to EBCI; E31 (a night out) and E33 (glass, heat) feel it | **The pilot marks the season `[P]` and does not lock it**; the author sets B01's season when Act I is released |

## 5. Questions for the author

| # | Question | Recommended |
| --- | --- | --- |
| **Q-LS1** | **End saga-scale architecture work for now**, reopening it only on a discovery in EBCI or prose | **Yes** |
| **Q-LS2** | **Release the B01 EBCI hold for the two-packet pilot only** (E31, E33): template, validators, the two packets, then the narrative review. **This is the author's act**; nothing in this report releases it | Your call; nothing found here stands in the way |
| **Q-LS3** | **The pilot inputs PI1–PI3** as recommended | **Yes** |
