# Saga structural pass 1 — what can be measured, the nine-book map, and B08

**Date:** 2026-09-25
**Status:** PROPOSAL / NON-CANONICAL. **No milestone row, grid value, book context, act
overlay or episode is changed. No event is placed, promoted or retired. No cause assigned.
No EBCI.** Every author question is put, not answered.

**Work-queue item:** `CLAUDE.md` §9 step 1, saga-wide structural pass. **A reconciliation
first**, per §9: the 09-19 → 09-24 saga work already contains a 36-row milestone review, an
adjudication pass, an author decision packet, a 21-candidate unslotted event pool with tier
grammar, and B07/B08/Loom ledgers. This pass reads them together and reports what they do not
say individually.

Inputs: `grids/milestones_payoffs.csv` ·
[M01–M36 review](../reports/M01_M36_MILESTONE_DESCRIPTION_AND_DEPENDENCY_REVIEW_2026-09-23.md) ·
[adjudication](M01_M36_EDITORIAL_ADJUDICATION_PASS_2026-09-23.md) ·
[decision packet](MILESTONE_GATE_AUTHOR_EDITOR_DECISION_PACKET_2026-09-23.md) ·
[event tiers and pool](SAGA_EVENT_TIERS_AND_UNSLOTTED_POOL_PASS1_2026-09-23.md) ·
[Veil structure rulings](../recovery/VEIL_STRUCTURE_2026-09-19.md) ·
[B03→B04 handoff](concord-2026/B03_B04_HANDOFF_RECONCILIATION_2026-09-19.md) ·
`book_context/`.

---

## 1. The first finding is about measurement, and it constrains everything after it

The saga pass is asked to judge nine-book rhythm, density, balance and escalation. **The
nine books do not exist at the same resolution**, and comparing them as if they did would
manufacture findings.

| Books | Best available resolution |
| --- | --- |
| **B01** | A locked 48-episode architecture plus prologue and six supplements; census, cards, rhythm pass — **14** episode/beat-level documents |
| **B02, B03** | Recovered episode audits (E01–E18 per act from the 09-20 forensic pass) and reconciliation maps — **3** each |
| **B04–B09** | **Zero** episode- or beat-level documents. Three to five milestone rows per book, plus unslotted pool candidates |

**Two traps follow, and both would be silent:**

1. **A density comparison would find Veil "dense" and Neon/Loom "sparse" purely because
   more of Veil has been written down.** That is a data artifact, not a pacing finding. It
   is the same class of error as §83's v3/v4.1b numbering split — two things that look
   comparable and are not.
2. **The B04–B09 book contexts cannot corroborate the milestone grid.** Their
   `exit_state_locks`, `continuity_hooks` and `entry_state` are marked `_basis: derived` —
   *"DERIVED 2026-09-20 from grids/milestones_payoffs.csv."* Using them as a second witness
   would count the same 36 rows twice.

**So the saga pass works at the one resolution all nine books share: milestone rows plus
pool candidates.** Veil's episode detail waits for step 4, the trilogy audit, where it can be
compared with itself. Every finding below is stated at that shared grain.

---

## 2. The nine-book map, at shared resolution

Milestone acts are from the live grid. Where the 09-23 review recommends a correction, it is
shown and marked — **the grid is not changed**. Pool rows are listed by the book their source
window names; `dup` marks a pool row flagged as a duplicate or alternate of another book's.

| Book | Protected anchor (tier A) | Milestones by act | Pool candidates | Trilogy role |
| --- | --- | --- | --- | --- |
| **B01** | — | A1 · A2 · A3 | 001 | Opens Veil |
| **B02** | — | A1 · A2 ×3 | 002 | |
| **B03** | **POOL-003 Warehouse; Baz dies** | A3 ×2 · EP ×2 | 003 | **T1→T2 handoff in EP** |
| **B04** | — | A1 · A2 ×3 · A3 | 004, 005 | Opens Neon |
| **B05** | — | A2 ×2 · A3 | 006 | |
| **B06** | **POOL-008 Santa Fe; Tahl dies** | A3 ×3 · EP — *review: M20 → A2* | 007, 008 | **T2→T3 handoff in EP** |
| **B07** | — | A1 · A2 ×2 · A3 ×2 | 009–016 — **eight** | Opens Loom |
| **B08** | — | **A3 ×3 only** — *review: retire M29* | 017, 018, 019, 020 + 011/012/015/016 `dup` | |
| **B09** | **POOL-021 Mending** | A3 ×3 · EP ×2 | 021 | Closes the saga |

### What the map shows

- **Promises are end-weighted within books.** Five of nine books — B03, B05, B06, B08, B09 —
  carry no Act 1 milestone. This is **not** evidence that nothing happens in those Act 1s:
  the grid lists high-visibility promises, not plot. It says each book's *promised* turn lands
  late, which is conventional serial structure and probably intended. **Recorded as shape,
  not as a defect.**
- **The three tier-A anchors sit at B03, B06 and B09 — each trilogy's closing book.** The
  two trilogy handoffs are both in `EP` positions. The saga's skeleton is a clean
  three-by-three, and that part of the architecture is sound.
- **Thread pressure carries almost no shape information from B04's Act 3 onward.** Of the
  seventeen rows from M16 to M32, **sixteen end at 5**; thirteen score 5→5, **eleven of them
  consecutively** (M19–M29), broken only by M30's 5→4. *(Counted by script; a first draft of
  this line said "seventeen consecutive" by conflating the span with the run.)* The 09-23
  review already says so — *"do not compare a 5 in Veil with a 5
  in Loom … many 5→5 rows may be continuity, plateau, or an uncalibrated scoring artifact."*
  **Pressure cannot be used as a saga rhythm signal until it is rescored per trilogy**, which
  the decision packet sequences *after* the five author decisions.

---

## 3. B08: the problem is not emptiness — it is that B08 is squeezed from both sides

`CLAUDE.md` §8 records that *"B08 has no recovered independent non-finale turn."* Read at
shared resolution, **the pool has plenty of B08 material. Almost all of it belongs to a
neighbour.**

| Pool row | Source window | Flag | Collides with |
| --- | --- | --- | --- |
| 011 service degradation | B7 E5/E6, *repeated* B8 E6 | **duplicate-risk** | B07 |
| 012 route/camp allocation | B7 A2, B8 care | **alternate** | B07 |
| 015 alignment-site hypothesis | B7 A1/A2, *repeated* B8 A2 | **duplicate-risk** | B07 |
| 016 meta fate / Technarc remnant | B7 E8, B8 E8/E13 | **alternate** | B07 |
| 020 storm obstruction / chamber | B8 A3 | **duplicate-risk** | **B09** |
| 019 finite field choice | B8 A2/A3 | *"do not repeat B7 care/meta encounter at higher volume"* | B07, by warning |
| 018 Kade's credibility appropriated | **PROPOSAL** | *"no recovered concrete incident"* | — |
| **017 coercive quieting** | **B8 A2/A3, D function** | **none** | **none** |

**Of eight B08-associated candidates, four collide with B07, one with B09, and one is warned
against repeating B07. One more is a proposal with no recovered incident.**

**Only POOL-017 is B08-native, supported by the author-pasted December macro, and free of any
duplicate flag.** It is also the only one that cannot steal B09's ending: it concerns
Choirless coercion of a community, not access to Honey Island.

**This reframes §9's instruction.** *"Strengthen B07–B08 without stealing B09's ending"* is
at least as much **disentangling B07 from B08** as it is finding new B08 material. B07 is the
richest book in the pool — eight candidates — and it is richest partly because it is
standing on B08's ground.

**[P] Two proposals, for review and nothing more:**

1. **Adjudicate the four B07/B08 collisions before searching for new B08 events.** For each of
   011, 012, 015 and 016, decide whether it is one event with two versions, a consequence, or
   two differently costly actions — the pool's own §5 step 3. Every collision resolved in
   B08's favour gives it material without invention.
2. **Treat POOL-017 as the leading B08 non-finale turn candidate** for the author's
   consideration. It needs everything its row says is open — community, Saeko and Ito's
   roles, physical presence, any Resonance effect — and **it is not placed or approved by
   this document.**

One observation, not a design: **017 and the proposal-only 018 share a subject — control of a
public voice**, by silencing in one and by appropriation in the other. That is coherent with
MissingThread's arc. Whether to use it is the author's to decide.

---

## 4. Decision #1 of the milestone packet is narrower than it was put

The decision packet's first question asks whether Tahl is first named in the **B3 epilogue
(option A)** or **B4 (option B)**, describing option B as having *"an earlier same-day
explicit ruling"* in `VEIL_STRUCTURE_2026-09-19.md`, and assigns Claude to *"compare the two
same-day ruling records by actual utterance."* Done.

**The only verbatim author utterance is in `VEIL_STRUCTURE`:**

> Tahl isn't named until Book 3, but MT can be visible before that — possibly B2. … Tahl
> accidentally exposes the incident that Baz gets killed at, and **his remorse in B4 is his
> protagonist arc beginning.**

**The B03-epilogue rule has no quoted source.** It appears in the handoff document's list of
*"governing current author rulings"* as a paraphrase, and ledger §26.6 already records it as
one of the *"four author locks living only in proposals."*

**Read against each other, they do not conflict.**

| | Says | Sets |
| --- | --- | --- |
| The author's words | *"isn't named until Book 3"* | Named in Book 3 — or, read strictly, **not before** Book 3 |
| The author's words | *"his remorse in B4 is his protagonist arc beginning"* | **The arc** begins in B4 — **not the naming** |
| The paraphrase | *"may not even be named before the B03 epilogue"* | Not before the B03 epilogue |

**Option B rests on reading "remorse in B4" as "named in B4."** No author sentence names B4 as
the point of first naming. Both texts are satisfied together by option A — named in B3's
epilogue, remorse arc opening in B4.

**What remains for the author is therefore smaller:** the verbatim text puts naming in **Book
3**; the **epilogue** specifically comes only from the paraphrase and from
`VEIL_STRUCTURE`'s own analysis that Tahl's MT voice is *"born out of remorse"* in the
epilogue shells. **The live question is "the B3 epilogue, or earlier in B3?" — not "B3 or
B4."** B4 first-naming remains open only if *"until"* was meant as a bare floor, and the
author can say so.

---

## 5. Which §9 dimensions the saga pass can judge now

| Dimension | At shared resolution? | What is needed |
| --- | --- | --- |
| Anchors and book turns | **Yes** | Five author decisions (§6) |
| Unslotted pool, carry-forward | **Yes** | B07/B08 collision adjudication (§3) |
| Milestone/payoff architecture | **Yes**, as proposal | The decisions, then a proposed grid *copy* |
| Trilogy transitions | **Yes** | Decision 1 governs T1→T2 |
| Causal dependencies | **Partly** | Packet: separate chronological, informational and physical links |
| Nine-book rhythm and density | **Only coarsely** | Neon/Loom have no episode data — §1 |
| Thread pressure / escalation curves | **No** | Rescoring per trilogy, sequenced after the decisions |
| Life/Reward, wonder, fun, romance, heat, humour | **No** | These live at episode grain; only B01 has it |
| Character bandwidth, place recurrence | **Partly** | 26 of 57 cast rows lack a `range` (ledger §80) |
| Antagonist/faction pressure | **Partly** | Pool 016/017/018; Neon set-piece survival (decision 3) |
| Mechanica/Resonance escalation | **Partly** | D5-style causal cards for B3, B6, B8, B9 events |
| Reveals, mysteries, anticipation | **Partly** | Decision 1; Echo arc M22/M27/M36 held |

**Several of the dimensions §9 lists cannot be judged saga-wide until later steps produce
data.** That is not a reason to skip them; it is a reason to say, in each case, *at what step*
they become judgeable, and not to fake a nine-book reading from B01 alone.

---

## 6. The five author decisions, shortest form, with #1 revised

These had been open since 2026-09-23 and gate the milestone layer.

> **Answered 2026-09-26** — `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`.
> #1, #2's first sentence and #5 are ruled; #3 and #4 are **leans**. The list below is the
> record of what was asked.

1. **Tahl's naming: the B3 epilogue, or earlier in Book 3?** *(Revised by §4 — "B4" has no
   supporting author sentence.)* B4 remorse arc stands either way.
2. **Tahl's exposure: what did he expose, to whom, and did the response worsen Baz's rescue?**
   The accidental-exposure ruling stands; its mechanism is open.
3. **Neon set pieces: do the B4 Riot of Light, B5 first public meta and B5 NOLA Colorstorm
   survive as required events,** or only their broader functions?
4. **B08's end image: an objective storm aperture, a structural route change, or a discovered
   path?** Keep the chamber reveal; no pre-Mending formal Echo Node.
5. **LT: a distinct post-Mending public identity, or an explicit MT rebrand?**

## 7. Pass 2 — proposed order

1. **Adjudicate the four B07/B08 pool collisions** (§3) — unblocked, source work only.
2. **The packet's remaining Claude-checkable items**: dependency *type* for every
   `required_setups` link; primary sources for M13, M14, M15, M18, M30.
3. **After the five decisions:** a proposed grid copy, per-trilogy pressure rescoring, and a
   causal-card list for the tier-A events.

## 8. What this document does not do

It changes no milestone, grid value, book context, act overlay or episode; places, promotes or
retires no event; assigns no cause; answers no author question; and does not touch EBCI.
POOL-017 is named as a candidate, not approved. The B01 order and hold are untouched.
