# B01 event census, Pass 2 — tier mapping and the measurements Pass 1 asked for

**Date:** 2026-09-25
**Status:** PROPOSAL / NON-CANONICAL DIAGNOSTIC. **No event is created, promoted, merged or
counted as settled. No episode function, supplement, or the locked B01 order is altered. No
EBCI.** Nothing here fills a placeholder or assigns a cause.

**Work-queue item:** `CLAUDE.md` §9 item 3 — *"complete the B01 event census … C events
separated from D receipts, no target count; resolve E23/E38/E40/E45."*

**Builds on, and does not replace:**
[census Pass 1](B01_NARRATIVE_CHANGE_CENSUS_AND_UNFILLED_TIMELINE_FUNCTIONS_PASS1_2026-09-24.md) ·
[four-window cards Pass 1](B01_E23_E38_E40_E45_CAUSAL_EVENT_CARDS_PASS1_2026-09-25.md) ·
[boundary adjudication Pass 2](B01_EVENT_BOUNDARY_HISTORICAL_SOURCE_ADJUDICATION_PASS2_2026-09-24.md) ·
[tier grammar](SAGA_EVENT_TIERS_AND_UNSLOTTED_POOL_PASS1_2026-09-23.md) ·
[author ruling D1–D7](../decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md).

---

## 1. First: the two letter schemes collide

§9 item 3 says *"C events separated from D receipts."* That is the **tier grammar**:

| Tier | Meaning |
| --- | --- |
| **A** | saga anchor |
| **B** | book turn |
| **C** | **local event** — a before/after in a decision, service, relationship, site, evidence or capacity |
| **D** | **receipt / scene observation** — a witness, record, trace or testimony that lets the reader test a higher-level claim |

But census Pass 1's ledger uses its own letters for something else:

| Census | Meaning |
| --- | --- |
| **C** | candidate-bearing **episode slot**, still needing a card |
| **Q** | possible event, independence not yet shown |
| **L** | lived-life, receipt, aftermath, setup or negative space |

**`C` means two different things and `D` is absent from the census.** A census `C` is a
*slot that may contain* an event; a tier `C` is *an event*. Census `L` silently contains
what the tier grammar calls `D`.

This repository has been bitten by exactly this before — the retired
`D=Notion / E=assistant / F=memory` lettering against the A–E source tiers (`CLAUDE.md` §5).

**[P] Proposed disambiguation, costing nothing:** keep both schemes, never write a bare
letter. Write **slot-C / slot-Q / slot-L** for census rows and **tier-C / tier-D** for
events. This document does so throughout.

**Restating §9 item 3 in that vocabulary:** the task is to determine, inside the 48 slots,
which changes are **tier-C local events** and which are **tier-D receipts attached to
them** — *"keep the receipt attached to its event; do not inflate each into a milestone."*

---

## 2. What slot classification can and cannot tell us

Census Pass 1: **22 slot-C, 6 slot-Q, 20 slot-L** (verified by reparsing its ledger: 48
rows, 22/6/20).

**A slot is not an event, in either direction.**

| | |
| --- | --- |
| A slot-C may contain | 0 tier-C events (investigation, setup, aftermath), 1, or several |
| A slot-L may contain | tier-D receipts — and occasionally a genuine tier-C relationship change, which Pass 1 protects at E30 |
| A slot-Q is | precisely the undecided case |

So **"22 events" is not a reading of this census and must never be quoted as one.** Pass 1
says so; this pass restates it because a bare number travels further than its caveat.

---

## 3. The five measurements Pass 1 asked for

Pass 1's gate 3 requested: (a) distinct causal changes, (b) events with physical Resonance,
(c) kind mix, (d) longest run without a changed option, (e) whether consequences get screen
time. **Three are computable now. Two are not, and saying which is the point.**

### (d) Longest run without a changed option — **computable, and the answer is reassuring**

| Measure | Value |
| --- | --- |
| Longest run of slots with **no slot-C** | **4** — E41, E42, E43, E44 |
| Longest run with **neither slot-C nor slot-Q** | **2** — E18, E19 |
| Longest run of consecutive slot-L | **2** (occurs at E18, E21, E31, E37, E41) |

**The book never goes more than two episodes without at least a possible changed option.**
Whatever else the rhythm pass finds, there is no dead stretch.

### (e) Do consequences get screen time — **computable by proxy**

Taking a following slot-L as consequence/receipt space, of the 28 slot-C/Q rows:

| | Count | Share |
| --- | --- | --- |
| slot-L immediately after | 15 | 54% |
| slot-L within two slots | 8 | 29% |
| neither | **5** | 18% |

**83% of candidate-bearing slots have receipt space within two episodes.** The five without
are **E07, E15, E23, E47, E48** — and **E47/E48 are an artifact of the book ending**, not a
rhythm finding. The real observation is three interior runs of three consecutive
slot-C/Q: **E07–E09, E15–E17, E23–E25.**

**These are observations for item 4, not defects.** E15–E17 is the civic disturbance into
the comparative reports into Lucien's call to Baz — a deliberately dense sequence. Naming it
is not proposing to break it up.

### Order-invariance — these three survive D7

Pass 1 says *"plot a timeline only after the two unresolved order exceptions are decided."*
For **these** measures that is not required. Recomputed under both numeric order and the
file order the ruling describes (E37 before E36, E44 before E43), all three are
**identical**: longest no-slot-C run 4; the same five slots without nearby receipt space;
the same three dense runs.

**So the rhythm pass can use these measures before the sequence decision.** What still
needs D7 is any measure of **prose position or density along the body**, which is what
Pass 1's caution is really about.

### (a) and (b) — **not computable, and must not be estimated**

- **(a) distinct causal changes** requires event-boundary adjudication, which is the work
  the four-window cards are doing. Producing a number now would be arithmetic on slots,
  which §3 of the cards document explicitly warns against: *"do not alter the earlier
  22/6/20 slot audit by arithmetic; it was not a census of event IDs."*
- **(b) events with physical Resonance** is **gated by author ruling D5**: causal physics is
  held until each retained effect has a private medium, limits, cost, residue and a
  plausible competing explanation. **Counting them would presume the rulings not yet made.**

### (c) kind mix — **partially computable**

Only the four carded windows carry kind tags today (institutional, informational,
local human/physical, civic, logistical, physical/perceptual). The other 44 slots have
descriptions, not kinds. **[P] Tagging kind is cheap and does not require any causal
decision** — it is a classification of what changes, not why. Recommended as the next
mechanical step, because it is the one input (c) needs and it is unblocked.

---

## 4. The four windows — what Pass 1 resolved, and what each still needs

Cards Pass 1 produced nine card shells and a merge/rejection register. Its own net finding:
**one E40 candidate and two E45 candidates** defensible at function level, with six shells
needing concrete decisions.

| Window | Standing | What would resolve it | Blocked on |
| --- | --- | --- | --- |
| **E23** | `B1-23A` HOLD, `B1-23B` HOLD | A named holder, an actual imposed constraint, and an investigator route that demonstrably changes. For Elisabet: a specific record and a receiver, used or rejected at E25/E39 | Source recovery, then author |
| **E38** | `A`/`B` HOLD, `C` CONDITIONAL | Whether current E38 retains a **finite allocation/retreat**. If it shows only mood and reports, Pass 1 says downgrade to montage | Reading current E38 against v4.1b |
| **E40** | `B1-40B` **one current candidate**; `40A` HOLD | Whether a civic service decision exists **independent of** the gathering — separate people, site, choice, downstream effect | Source, then author |
| **E45** | `45A` and `45B` **two candidates** | `45A`: a private causal contract (medium, limits, cost, residue). `45B`: whether the widened-inquiry commitment is distinct from E48's book-end commitment | **D5** for 45A; a merge test for 45B |

**Pass 2 does not advance any of these**, and that is the correct outcome rather than a
shortfall. Every one turns on either a source reading that has not been done or a ruling
that is explicitly held. **Resolving them by editorial judgement would be inventing the
answer** — the failure mode `CLAUDE.md` §4 exists to prevent.

**One genuinely resolvable test is available now, and it is a merge test, not a promotion:**
`B1-45B` against `E48`. Both are commitments to continued inquiry; the census flags E48 as
*"separate continued inquiry only if an independently new commitment follows."* That
comparison needs no new source and no ruling — only a careful read of the two v4.1b beats
side by side. **[P] Recommended as the next concrete step in this window.**

---

## 5. Decisions for the author

| # | Decision |
| --- | --- |
| 1 | **Adopt slot-C/Q/L vs tier-C/D as written vocabulary** (§1), so the two schemes stop colliding |
| 2 | **Tag kind across all 48 slots** as the next mechanical step, unblocking measurement (c) |
| 3 | Confirm that **(a) and (b) stay uncomputed** until boundary review and D5 respectively — i.e. that no event total is published meanwhile |
| 4 | The four windows remain as Pass 1 left them; **E23/E38/E40 need source work before another editorial pass adds value** |

None of these blocks item 4. **The three order-invariant measurements in §3 are available to
the rhythm pass today.**

---

## 6. What this document does not do

It creates, promotes, merges or counts no event; assigns no cause; fills none of the eight
placeholders; changes no episode function, supplement or the locked order; and does not
touch EBCI. It publishes **no event total**, and §2 exists to stop one being inferred.

Its measurements are reproducible: reparse census Pass 1's 48-row ledger and recompute under
both episode orders.
