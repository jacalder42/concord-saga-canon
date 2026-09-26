# Neon Milestone Atomic Promotion Delta — Pass 1

**Date:** 2026-09-26  
**Status:** PROMOTION-READY PROPOSAL / DO NOT APPLY PARTIALLY  
**Purpose:** exact structural delta for the Neon milestone revision, including downstream dependency repairs.

This file does **not** modify the live milestone grid.

## 1. Why this must be atomic

The live grid is not isolated. Derived `book_context` files currently carry continuity hooks generated from milestone IDs and `required_setups`.

The Neon revision retires/merges rows that are referenced later:
- M15 → M23 and derived B06/B07 continuity;
- M19 → M24 and M38;
- M21 → M32;
- M22 → M27, M52 and historical M36;
- M05 → M33.

Therefore do not patch only `grids/milestones_payoffs.csv`.

Promotion must:
1. update the grid;
2. repair all dependency IDs;
3. regenerate/reconcile B04–B09 book_context continuity hooks;
4. run dangling/backward-reference validation;
5. update ledger/report counts.

# 2. Author-direction assumptions used for this delta

These remain proposal-layer until explicit author promotion:
- Lucien voluntarily returns to Vienna in B04 after Baz; revised M05 culminates there.
- Kade's B04 public-influence milestone M15 retires.
- NOLA Colorstorm M19 is demoted from saga milestone; local event may survive.
- M21/M22 merge.
- Chicago is preferred B05 evacuation theater for Caro, reached through an ordinary long-postponed home visit.
- Tahl's public correction is consolidated into M37 rather than given a separate row.
- Caro, Elisabet, Caro/Elisabet, and Seraphine/Lucien receive missing durable Neon turns.

# 3. ID strategy

Preserve existing IDs where possible.

### Keep / revise
M05, M13, M14, M16, M17, M18, M20, M23, M37, M38, M39.

### Retire
- **M15** — Kade B04 public influence.
- **M19** — saga-milestone status only; retain event in event inventory if desired.
- **M22** — merge into M21.

### New IDs
Use next available IDs after M53:
- **M54 — Caro handoff**
- **M55 — Elisabet bounded action**
- **M56 — Caro/Elisabet chosen independent partnership**
- **M57 — Seraphine/Lucien chosen connection without rescue**

Do not create a separate Tahl-correction row. Fold it into M37.

# 4. Exact proposed row meanings

## M05 — REVISE
**Description**
Across B02–B04, Lucien moves from recognizing Dominion's containment logic, to refusing its return demand, to returning to Vienna on his own terms after Baz's death and making an irreversible choice that separates structure and care from Dominion obedience.

**Target:** T1→T2 bridge; culmination B04 A2.  
**Thread:** dominion.  
**Required setups:** M10 as character/chronological pressure; earlier B02/B03 beats are internal progression, not necessarily milestone dependencies.  
**Downstream:** retain M33←M05 as **character/thematic**, not physical.

## M13 — REVISE
After institutional failures become public, Technarc-aligned authorities expand monitoring and containment practices around Resonance-active people; the policy has specific human consequences and remains uneven rather than a universal global regime.

**Target:** B04 A2.  
**Setup:** M08 institutional.

## M14 — REVISE
Public movements promising safety through suppression, quieting or stricter control gain wider support as fear and institutional failure become ordinary civic experience.

**Target:** B04 visibility → B05 reach.  
**Setup:** M06 thematic.  
**Open:** exact current faction/actor mapping.

## M15 — RETIRE
Reason: conflicts with ruled post-Tahl Kade MT succession.

**Successor function:** no direct row. Human/audience seeding belongs to character/episode architecture.

## M37 — REVISE / CONSOLIDATE TAHL ACCOUNTABILITY
Tahl learns Baz's name from ordinary reporting and learns from the protagonists why Baz mattered; when later evidence undercuts one of his own consequential interpretations, he publicly corrects it despite losing authority with part of his audience.

**Target:** B04–B05, before M20.  
**Setups:** M10, M12.  
**Changed state:** MT's truth ethic becomes accountability to specific people plus correction, not a reputation for certainty.

This absorbs NEW-T1.

## M16 — KEEP / REWORD
A B04 civic confrontation makes the political split materially consequential; crowd violence, policing/institutional choices and any verified Resonance effects remain separately attributable.

**Target:** B04 A3.  
**Setups:** M13, M14.

## M17 — REVISE
A specific engineered-control intervention fails or causes bounded human harm despite prior warnings and internal dissent, causing a consequential community, operator group or local authority to stop treating Technarc direction as presumptively safe or authoritative.

**Target:** setup B05 A2 → payoff B06 A1.  
**Owner:** Rex/Technarc + affected human case.  
**Setup:** M13.  
**Downstream:** M30.  
**Mechanica hold:** no unverified meta battery→operative transfer.

## M18 — REVISE
Filament networks divide over how much risk, intervention and coercion care can justify, and the disagreement changes actual coordination, trust or resource flow.

**Target:** B04 crack → B05 durable split.  
**Setup:** M02.  
**Remove:** M15 dependency.

## M19 — RETIRE FROM SAGA GRID
Reason: spectacle/local event does not currently carry a unique durable changed state.

Preserve in event inventory if desired:
A bounded New Orleans atmospheric/overhead anomaly may survive; remote reports and global coupling remain separate claims.

### Downstream repair
- M24 must not depend on M19.
- M38 must not depend on M19.

## M38 — REVISE
By late B05, Tahl's bounded VT warning and independent mortal evidence make Santa Fe a credible danger requiring action; responses remain incomplete or contested. In B06 the threatened condition escalates into the Santa Fe rupture where Tahl dies.

**Target:** B05 A3 → B06 A3.  
**Setup:** M55 informational/decision support; M37 can be thematic/credibility support but should not be a physical prerequisite.  
**Downstream:** M20.

## M54 — ADD — CARO HANDOFF
During a large evacuation or care crisis, Caro reaches the limit of what she can personally carry, entrusts a consequential task or group of people to someone else, and leaves before the work is finished; the response succeeds better because responsibility is distributed.

**Target:** B05 A2–A3.  
**Owner:** Caro.  
**Preferred theater:** Chicago.  
**Setup:** Caro established overfunctioning trajectory; no milestone ID required unless a character-arc grid later exists.  
**Changed state:** handoff is not abandonment.  
**Downstream:** M33 character/thematic support is possible but do not add as a hard dependency yet.

## M55 — ADD — ELISABET BOUNDED ACTION
With evidence still incomplete, Elisabet recommends a bounded protective action before certainty, states what is known versus inferred and what could falsify the model, and accepts responsibility for the costs of acting too early or too late.

**Target:** B05 A3.  
**Owner:** Elisabet.  
**Preferred theater:** Reykjavík/field + distributed evidence chain.  
**Changed state:** clarity becomes responsible action under declared uncertainty.  
**Downstream:** M38 informational/decision support; later reconstruction role.

## M56 — ADD — CARO / ELISABET
Caro and Elisabet explicitly choose their relationship while also choosing separate necessary work, establishing that commitment does not require constant co-location or one partner abandoning her independent responsibility.

**Target:** B05.  
**Setup:** M07.  
**Downstream:** B06 separation; B09 Elisabet/Caro goodbye.

## M57 — ADD — SERAPHINE / LUCIEN
After Baz's death and Lucien's withdrawal to Vienna, Seraphine and Lucien choose to remain in relationship without making Seraphine responsible for regulating his grief or Lucien responsible for containing her instability.

**Target:** setup B04 → payoff B05.  
**Setups:** M05 character; Veil relationship foundation need not be encoded as another milestone dependency.  
**Downstream:** B06/B08 reciprocal care; M33 thematic/relationship support.

## M20 — KEEP / WORDING TIGHTEN
Tahl dies at the end of B06 at the Santa Fe rupture after a late fatal VeilThread contact; the death is not a knowingly chosen sacrifice, and he glimpses enough of the wound pattern to leave a mortal informational legacy.

**Setup:** M12 character; M38 material.  
**Attendance:** Tahl only required principal.

## M21 — REVISE AS MERGED M21+M22
At Tahl's death, Silence makes its first consequential act of agency by preserving a bounded echo of him; the echo remains non-identifiable to the living cast until its single ruled identifiable flare in B09.

**Setups:** M09 character; M20 chronological.  
**Downstream successor for old M22:** M27, M52; any surviving M36 relation.

## M22 — RETIRE / MERGED INTO M21
All downstream dependencies on M22 move to M21.

## M39 — KEEP
A message Tahl created by mortal means reaches the group after his death and gives them the shape of the wound pattern without providing a complete solution.

**Setup:** M20.

## M23 — REVISE
After Tahl's death, Kade writes grief into MT's comment space believing it private; the writing becomes visible/read, creating the seed of a public responsibility he has not yet consciously accepted.

**Target:** B06 EP.  
**Setups:** M20 chronological/character.  
**Remove:** M15.  
**Downstream:** M40, M26, M35.

# 5. Downstream dependency rewrite table

| Current edge | Proposed edge | Reason |
| --- | --- | --- |
| M18 ← M15 | **REMOVE** | Kade not prerequisite to Filament division |
| M23 ← M15 | **REMOVE** | Kade's grief seed follows Tahl, not B04 influence |
| M24 ← M19 | **M24 ← M38** or no direct milestone dependency pending Loom review | uneven service degradation follows broader late-Neon conditions, not NOLA Colorstorm |
| M38 ← M19 | **M38 ← M55** (informational/decision) | Santa Fe warning does not require Colorstorm |
| M22 ← M21 | row removed | merged |
| M27 ← M22 | **M27 ← M21** | merged echo row |
| M52 ← M22 | **M52 ← M21** | B09 identifiable flare |
| M36 ← M22 | **M36 ← M21** if M36 survives; otherwise retire separately | merged echo row |
| M32 ← M21 | **KEEP** | Silence agency arc remains valid |
| M33 ← M05 | **KEEP as character/thematic** | chosen structure supports guide role |
| M33 ← M27 | no change in this delta | M27 itself remains under later review |
| M30 ← M17 | **KEEP** | bounded Technarc legitimacy/failure setup |
| M40 ← M23 | **KEEP** | private grief seed precedes deliberate funeral post |
| M26 ← M23 | **KEEP** | involuntary visibility precedes conscious stewardship |
| M35 ← M23 | **KEEP** | Kade's MT trajectory carries into reconstruction |

# 6. B04–B06 exit-state implications

## B04
Should eventually include:
- revised M05 culmination;
- M13;
- M14;
- M16 if retained;
- M18 first crack may span B04→B05;
- M37 may span B04→B05.

Do not force every spanning milestone into an exit lock without deciding the grid's convention for multi-book rows.

## B05
Should eventually include:
- M17 setup/turn;
- M54;
- M55;
- M56;
- M57 payoff;
- M38 warning/threshold;
- M18 durable split.

## B06
Should include:
- M17 payoff if represented as spanning;
- M38 escalation;
- M20;
- M21 merged echo;
- M39;
- M23.

# 7. B07–B09 integrity after delta

### B07
- M40 remains valid from M20 + M23.
- M26 remains valid from M23 + infrastructure condition.
- M27, if retained, now points to M21.
- M28 remains driven by M39 + M42 in current live grid.
- B07 funeral becomes a genuine re-gathering because B06 does not require ensemble Santa Fe attendance.

### B08
- M30 remains linked to revised M17; this is stronger because M17 now establishes a bounded legitimacy/failure lineage rather than an unverified “first public meta.”
- wound circuit unaffected.

### B09
- M32 can still depend on M21 as Silence's first agency precedent.
- M52 must depend on M21 rather than M22.
- M33 retains M05 as character/thematic support; revised M05 improves that relationship.
- M56 gives the Elisabet/Caro goodbye an actual relationship-state antecedent, but should initially remain **soft/thematic**, not a hard M33 dependency.
- M57 similarly supports mature Lucien/Seraphine partnership without becoming physical Mending machinery.

# 8. Rhythm result

The revised Neon milestone spine has a clearer cadence:

### B04 — old systems reclaimed and refused
- Baz becomes specific to Tahl.
- Lucien goes home and refuses reabsorption.
- institutions/public movements harden.
- Filaments begin to divide.
- civic conflict becomes materially real.

### B05 — adaptation and chosen responsibility
- relationships survive separation.
- Caro learns distributed care.
- Elisabet acts before certainty.
- Rex/Technarc control logic becomes humanly consequential.
- Santa Fe becomes actionable warning.

### B06 — prevention fails
- engineered control loses legitimacy.
- Santa Fe crosses threshold.
- Tahl dies.
- Silence acts.
- mortal information survives.
- Kade's grief accidentally enters public life.

This is escalation by **changed responsibility**, not simply larger VFX.

# 9. Promotion gate

Before live edit:
- author confirms/adjusts the four new rows M54–M57;
- author confirms M15/M19/M22 retirements;
- author confirms revised M05 Vienna architecture;
- decide whether M24 should depend on M38 or have no direct Neon milestone prerequisite;
- then apply grid + derived context regeneration atomically.

END.