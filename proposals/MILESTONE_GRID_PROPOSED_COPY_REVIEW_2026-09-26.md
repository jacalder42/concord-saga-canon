# Milestone grid — proposed copy for review

**Date:** 2026-09-26
**Status:** PROPOSAL / NON-CANONICAL. A proposed copy of `grids/milestones_payoffs.csv` for the
author's review. **The live grid is untouched.** No episode is placed, no rule or card is edited,
and the EBCI hold stands.

**Files:**

- [`milestones_payoffs_PROPOSED_COPY_2026-09-26.csv`](milestones_payoffs_PROPOSED_COPY_2026-09-26.csv):
  the copy, **in the live schema**, so it can replace the live grid on approval. Each row's `notes`
  starts with its change, its basis and its authority, and ends with the live row's original note
  (*"Was: …"*).
- This document: the same rows **side by side**, original against proposed (§6).

**Why now:** the decision packet's release criterion
([packet](MILESTONE_GATE_AUTHOR_EDITOR_DECISION_PACKET_2026-09-23.md), last line) was: answers 1–5
recorded, then the B3/B6/B8 event cards, then *"a proposed grid copy with original and revised
descriptions side by side."* The answers and cards are done, and so are the Loom rulings of
2026-09-26. The author asked for it: *"Then proceed with the proposed grid copy."*

**Checked:** the copy passes the live grid's own checks in `tools/validate_canon.py`
(`check_milestone_grid`: schema, unique IDs, resolving setups, two-digit books, act values,
thread vocabulary, status vocabulary). **0 violations.**

---

## 1. Authority key

| Key | Document |
| --- | --- |
| GATE | `decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md` |
| WH | `decisions/B03_WAREHOUSE_AUTHOR_RULING_2026-09-26.md` |
| B6B8 | `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` |
| SPINE | `decisions/LOOM_SPINE_AND_ANCHORS_AUTHOR_RULING_2026-09-26.md` |
| WOUNDS | `decisions/LOOM_WOUNDS_AND_ELIAS_AUTHOR_ANSWERS_2026-09-26.md` |
| ELIAS | `decisions/ELIAS_CARD_CORRECTIONS_AUTHOR_RULING_2026-09-26.md` |
| CHAIN | `decisions/LOOM_CHAIN_KNOWLEDGE_AND_MENDING_COST_AUTHOR_RULING_2026-09-26.md` |
| MIRA | `decisions/MIRA_AND_SILENCE_HOPE_ORIGIN_AUTHOR_RULING_2026-09-26.md` |
| LTA | `decisions/LT_ACCESS_AND_B09_EPILOGUE_AUTHOR_RULING_2026-09-26.md` |
| OVL | `proposals/M01_M36_SIDE_BY_SIDE_MILESTONE_WORDING_OVERLAY_2026-09-23.md` |
| REV | `reports/M01_M36_MILESTONE_DESCRIPTION_AND_DEPENDENCY_REVIEW_2026-09-23.md` |
| LOOM1 | `proposals/LOOM_STRUCTURAL_PASS1_B07_B09_2026-09-26.md` |
| VS | `recovery/VEIL_STRUCTURE_2026-09-19.md` |

**Basis labels:** **RULED** (every element of the description has an author ruling); **PARTLY
RULED**; **RECALLED** (the author's hedged recollection); **LEAN**; **INTENT** (stated intent,
used as a governing constraint); **REVIEW** (the 09-23 editorial review, no author ruling).

## 2. What changed, in numbers

| | Rows |
| --- | --- |
| Live grid | 36 |
| Proposed copy | **53**: 36 carried (one retired) + **17 new** |
| Proposed `status: ruled` | **20**, where every element of the description is ruled |
| Proposed `status: proposed` | 32 |
| Proposed `status: retired` | 1 (M29) |

**Status is proposed, not applied.** The grid's `ruled` means *"Author has ruled on this
milestone"* (`canon_rules.json`). The copy marks a row `ruled` only when its description is ruled
end to end. Approving the copy approves those statuses; the author can approve the wording and keep
any row at `proposed`.

**File order is story order.** New IDs (M37–M53) are numbered in the order they occur.

## 3. The shape of the change

### Veil (T1)

- **M11 becomes the act, not the reveal.** Tahl posts the coordinates (GATE #2), not knowing Baz is
  there (WH #2). It moves before the Warehouse (B03 A3). The crowd-and-delay link stays the author's
  hypothesis and is typed as such in M10's setups.
- **M12 moves from B04 A1 to the B03 epilogue** (GATE #1). B04 still opens his remorse.
- M01–M07 and M09 take the 09-23 review's wording. They have no new author ruling. M09 loses its
  fixed E14 slot.

### Neon (T2)

- **New M37:** Tahl learns Baz's name from a news report, and why Baz mattered from the
  protagonists (B6B8 §1.4).
- **New M38: the Santa Fe escalation**, which the grid lacked as an event. Fracture at the close of
  B06 Act I, Rupture in Act II (the ladder mapping the author accepted as intent), with VT-origin
  warnings unheeded (recalled).
- **M20: Tahl dies at the end of B06** (ELIAS §4). This supersedes both the packet's A3 → A2
  correction and the later lean to the end of A2. He glimpses the wound pattern.
- **M21 gets its author source:** *"Saving Tahl's echo is their first act of agency, which is the
  first crack in the cycle of hard cap veils"* (author, 11-23), with the recalled *"Tahl's soul is
  caught/collected by Silence."* *"Constructs built without agency"* goes: the author ruled they
  have no clear beginning (MIRA §5).
- **M22 is not identifiable to the cast.**
- **New M39: Tahl's last message** reaches the group after his death and gives them the wound
  pattern (ELIAS §4; CHAIN §1).
- M13–M17 and M19 stay held; M18's function is kept. Lean 3 keeps M16, M17 and M19 in the search
  **as events**, with their "first" and "global" claims still retired.

### Loom (T3): rebuilt around the spine

The live grid's Loom was the Notion version: global conditions, an exodus toward the swamp, a
pre-Mending Echo Node and a B08 swamp convergence. **The rulings replace it.**

| Book | Proposed sequence |
| --- | --- |
| **B07** | M40 Tahl's funeral, Lacuna prominent → M41 Elias finds Kade → M24/M25 conditions → M26 Kade takes over MT → M27 (held) → M49 Seraphine drawn into the Loom, Mira guiding → **M42 Kade's post and the New Orleans break** → M28 the crew leaves to stabilise the wounds → M43 the split foreshadowed |
| **B08** | M44 the split → **M45 Santa Fe, the first wound** → **M46 Kade's first complicity** → M47 Mound City → M30 (held) → M48 Serpent Mound → **M31 the fleeting opening; Elias's claim; the factions think "Louisiana"** |
| **B09** | M48's escape → M50 the NOLA feint → **M51 the factions learn the site (A3)** → M32 (held) → **M52 Elias, Rex, Kade and the flare** → **M33 the Mending** → M34 → M35 MT continues; reconstruction → **M53 the night sky and the LT handshake** → M36 (held) |

**B08 now has turns.** CLAUDE.md §8 records that *"B08 has no recovered independent non-finale
turn."* With M44, M45, M46 and M47, all ruled or partly ruled, it has four, and B08's end no
longer borrows B09's site.

**The site secret holds in every row.** The factions believe "Louisiana" (M31) and learn the swamp
in B09 Act III (M51). No B07 or B08 row tells them.

**The most protected beat in Loom is now in the grid:** M52. The Loom pass noted it was missing.

## 4. Conflicts carried, not resolved

| Row | Conflict | For |
| --- | --- | --- |
| **M38 / M20** | The accepted ladder puts the Santa Fe **Rupture in B06 Act II**; Tahl's death is ruled at **the end of B06**, and his fatal contact is at the rupture. Either the Rupture moves later, or he dies later than the Rupture's onset | Author; part of the Tahl's-death task |
| **M15** | A **B04 public Kade voice** against the rulings that start Kade's MT voice **after Tahl's death**, as a grief diary he believes private | Author |
| **M26** | The review's objection to *"last intact channel"* against two corrected cards that say MT is *"the only worldwide channel left"* (LacunaEBCI) and *"the last broadly working channel"* (EliasEBCI). The proposed wording follows the cards | Author |
| **M31 / M48** | The order of the Serpent Mound visit, the fleeting opening and Elias's claim at B08's end | **DEFERRED** by the author until the book, act and episode milestones are extrapolated |
| **M32** | A confession scene beside the 12-07 order, which the author ruled governs | Author |
| **M36** | An identifiable farewell would be a second appearance. Options: fold into M53's implied triangle, merge into M52's flare, or retire | Author |
| **M51** | Stated as author intent with a firm reason and used as a governing constraint. Approving the copy would make it a ruling | Author |
| **M21 / M22** | May merge: the first act of agency is the saving of the echo | Author |

## 5. Deliberately not done

- **Thread pressure is not recalibrated.** Existing rows keep their live values, and new rows are
  blank. The values were scored before the per-thread rule (`canon_rules.json`
  `_pressure_note`), and the packet warns against changing them *"just to make sequences look
  smooth."* Recalibration is a separate pass, after the wording is approved, per thread and per
  trilogy.
- **No episode slots.** M09, M33 and M34 lose their fixed E14/E15. New rows carry acts only where a
  ruling names one.
- **Channel, reader group and supplement fields** are carried unchanged, except M35 (`MT`, it
  continues) and M53 (`LT`). New rows leave reader group and supplements blank.
- **Thread assignments for new rows** use the existing vocabulary. Rows about the factions' belief
  (M50, M51) are `UNSCORED`: no faction thread fits one belief shared by several factions.
- **The live grid, `canon_rules.json` and the validator** are unchanged.

## 6. Side by side

| ID | Change | Basis → proposed status | Original description | Proposed description | Target: was → proposed | Setups: was → proposed (type) | Authority | Open |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **M01** | REVISE | REVIEW → `proposed` | First micro-Shard: the Veil is demonstrably failing and resonance becomes observable to ordinary people | First bounded public anomaly in Book 1 makes the local pattern worth investigating; whether its ordinary observations share one Resonance cause remains open | B01 A1 → B01 A1 | none → none | OVL; REV; B01 v4.1b (no micro-Shard, low amplitude) | — |
| **M02** | REVISE | REVIEW → `proposed` | Filaments become a named presence: grassroots emotional care exists as an organised thing | Filaments become recognizable through human-scale recurring care and coordination, without a recruitment or organization-chart reveal | B01 A2 → B01 A2 | M01 → none | OVL; REV | First on-page naming |
| **M03** | HOLD | REVIEW → `proposed` | Seraphine filters a Shard pulse instinctively; first prismatic signature appears | Seraphine learns to time and constrain a response to bounded pressure, at visible cost; no Book 1 Shard filtration or prismatic debut | B01 A3 → B01 A3 | M01 → none | OVL; REV; B01 v4.1b ceiling | Whether B01 needs any Loom foreshadow beyond restraint and cost |
| **M04** | REVISE | REVIEW → `proposed` | MT appears anonymously: an unattributed public voice begins reporting resonance | An anonymous MissingThread voice begins reporting anomalies through ordinary mortal media | B02 A1 → B02 A1 | M01 → M01:informational | OVL; REV; channel ruling 09-19 (MT visible ~B2, unnamed until the B03 epilogue) | First actual post |
| **M05** | HOLD | REVIEW → `proposed` | Lucien breaks from the Dominion; the structural lineage loses its heir | Lucien makes a concrete professional or ethical break with Dominion authority | B02 A2 → B02 A2 | none → none | OVL; REV | The act and its date (B02 or B03); 'lineage loses its heir' unproven |
| **M06** | HOLD | REVIEW → `proposed` | The Ghostwave: mass involuntary emotional bleedthrough; the public can no longer be told nothing happened | A Ghostwave or pulse cluster becomes publicly observable in B02, with bounded witnesses, medium and aftermath | B02 A2 → B02 A2 | M01,M04 → M01:thematic; M04:informational | OVL; REV | Survival as a named event (lean 3 is about Neon only) |
| **M07** | KEEP | REVIEW → `proposed` | Caro and Elisabet bond: the saga's steady emotional centre forms | Caro and Elisabet's bond deepens from B01 recognition and instinctive safety into a durable relationship coordinate | B02 A2 → B02 A2 | none → none | OVL; REV; ruled canon 2026-09-19 | Exact B02 rung |
| **M11** | REVISE | RULED → `ruled` | Tahl's exposure is revealed as the cause of the incident that killed Baz | Tahl anonymously posts the coordinates of the event Baz is investigating, not knowing Baz is there | B03 EP → B03 A3 | M09,M10 → M04:character | GATE #2 (coordinates, RULED); WH #2 (did not know, RULED); WH #1 (staging: supplemental text or effect-only) | Staging (two options); platform and audience; the crowd-and-delay consequence is the author's hypothesis ('perhaps') |
| **M08** | REVISE | REVIEW → `proposed` | First Rupture, the Warehouse Incident: Rupture-level events are possible; NOLA carries a permanent resonance scar | The Warehouse Rupture: partial structural collapse as Baz rescues a child; any durable New Orleans scar is measured separately | B03 A3 → B03 A3 | M06 → M06:thematic; M11:chronological | OVL; REV; Warehouse card pass 1; WH (Dominion expected at the perimeter, Technarc not: DELEGATED working assumption) | 'First' Rupture comparison; scar duration; D5 holds the physics |
| **M09** | REVISE | REVIEW → `proposed` | The chronicler's VT slip: a mortal touches VT; Silence and Hope now know a human | Tahl's first and only Veil-era VeilThread brush: accidental, private and costly; mortal devices do not reach VT | B03 A3 E14 → B03 A3 | M04 → M04:character | OVL; REV | Placement in late B03 (the E14 packet slot is not approved) |
| **M10** | REVISE | REVIEW → `proposed` | Baz dies | Baz dies rescuing a child in the Warehouse collapse at the end of B03; the rest of the cast learns at the start of B04 | B03 EP → B03 A3 | M08,M09 → M08:material; M11:material (HYPOTHESIS: the crowd slowed evacuation) | OVL; REV; Baz death timing lock (in proposals, ledger 26.6); WH (bystanders hampering efforts: hedged) | A3 or EP; whether the reported dead 'first responder' is Baz or a second death |
| **M12** | REVISE | RULED → `ruled` | Tahl is named and revealed as MT's author; his remorse opens his protagonist arc | Tahl is named in the B03 epilogue and linked to the MT voice; B04 opens his remorse arc | B04 A1 → B03 EP | M04,M11 → M04:character; M10:chronological; M11:informational | GATE #1 (B03 epilogue, RULED); WH #1 (aftermath reports: hedged, examples); VS (B04 remorse) | Which epilogue episode; the aftermath reports he reads (unexpected bystanders, a dead first responder) are hedged examples |
| **M13** | HOLD | REVIEW → `proposed` | Protocol 9 launched: resonance-active people become a monitored class | Protocol 9 expands monitoring and containment of Resonance-active people after the institutions fail to predict the Warehouse | B04 A2 → B04 A2 | M08 → M08:institutional | OVL; REV; WH (Technarc's unsanctioned Warehouse presence as a reason to conceal: DELEGATED) | Launch scope and authority |
| **M14** | HOLD | REVIEW → `proposed` | Saeko Morita's anti-resonance movement goes national | Saeko's anti-Resonance politics gain wider reach | B04 A2 → B04 A2 | M06 → M06:thematic | OVL; REV | Whether 'national' is measurable; when |
| **M15** | HOLD | REVIEW → `proposed` | Kade is seen: an accidental folk voice exists and Filament youth have a centre | Kade gains visible influence among younger Filaments and public audiences through a human voice | B04 A2 → B04 A2 | M02 → M02:character | OVL; REV | CONFLICT: the 09-26 rulings start Kade's MT voice after Tahl's death, as a grief diary he believes private (KadeEBCI); a B04 public voice must be reconciled with that |
| **M37** | NEW | RULED → `ruled` | — | Tahl learns Baz's name from a news report, and learns why Baz mattered from the protagonists | — → B04-B06, before M20 | — → M10:informational; M12:character | B6B8 1.4 (RULED); WH (name comes late) | Date and outlet of the report; which protagonists |
| **M16** | HOLD | LEAN → `proposed` | The Riot of Light: open civic violence over resonance | A B04 civic conflict may culminate in the Riot of Light; crowd violence is kept separate from verified Resonance effects | B04 A3 → B04 A3 | M13,M14 → M13:institutional; M14:institutional | OVL; GATE #3 (soft lean toward yes as events) | Survival, name and act |
| **M17** | HOLD | LEAN → `proposed` | First manufactured meta deployed publicly | Manufactured-meta deployment becomes consequential; 'first public' B05 use and any operative boost are unverified | B05 A2 → B05 A2 | M13 → M13:institutional | OVL; GATE #3 (lean) | B05 public first against B06 failures; manufactured-meta transfer loop (standing constraint) |
| **M18** | KEEP | REVIEW → `proposed` | The Filaments fracture: 'Connection is survival' against 'Action is survival' | Filaments divide over care, intervention and risk as pressure rises | B05 A2 → B05 A2 | M02,M15 → M02:character; M15:character (needs faction evidence) | OVL; REV; Brightbreak card (some Neon Rebellion splinters join Brightbreak) | B04 first crack against B05 consolidation |
| **M19** | HOLD | LEAN → `proposed` | The Colorstorm: emotional bleedthrough goes global; resonance becomes a weather system | The New Orleans Colorstorm, if kept, is a local event; remote reports and global coupling are separate claims | B05 A3 → B05 A3 | M06 → M06:thematic | OVL; GATE #3 (lean); B6B8 1 (ladder: B05 close = sustained Ghostwave-class instability) | Survival; 'first global' stays retired |
| **M38** | NEW | RECALLED → `proposed` | — | Santa Fe escalates: warnings that originate in VT go unheeded; Fracture at the close of B06 Act I, Rupture in Act II | — → B06 | — → M19:thematic | B6B8 1 (ladder mapping accepted as intent; warnings from VT, RECALLED; the Southwest pull, RECALLED); B06 card | Who relays the VT warnings (VT never broadcasts); CONFLICT to settle: Rupture in A2 against Tahl's death at the end of B06 |
| **M20** | REVISE | RULED → `ruled` | Tahl dies | Tahl dies at the end of B06 at the Santa Fe rupture, in a late fatal VeilThread contact, not a knowingly chosen sacrifice; he glimpses the wound pattern | B06 A3 → B06 A3 | M12 → M12:character; M38:material | ELIAS 4 (end of B06, RULED; glimpses the pattern, RULED); Tier-1 TahlEBCI (fatal late VT contact) | The staging (a task on the list); the injury; supersedes the A2 lean and the old New Orleans transit scene |
| **M21** | REVISE | RECALLED → `proposed` | Silence and Hope make their first choice: two constructs built without agency act | Silence and Hope's first act of agency: Silence collects Tahl's soul, the first crack in the cycle of hard-cap veils | B06 A3 → B06 A3 | M09,M20 → M09:character; M20:chronological | Author 11-23 (NB 89177, 'Saving Tahl's echo is their first act of agency'); B6B8 1 (Silence collects him, RECALLED); MIRA 5 (constructs without a clear beginning) | How; whether M21 and M22 merge; 'constructs built without agency' retired (no builder) |
| **M22** | REVISE | PARTLY RULED → `proposed` | Tahl's Echo is caught in VT: death is not the end of him | Tahl's echo persists after his death, held by Silence; it is not identifiable to the cast | B06 A3 → B06 A3 | M20,M21 → M20:chronological; M21:physical | B6B8 1.2 and 4 (one identifiable appearance, the B09 flare, RULED) | What persists and what it can do; merge candidate with M21 |
| **M39** | NEW | RULED → `ruled` | — | Tahl's last message reaches the group after his death, by mortal means, and gives them the wound pattern | — → B06 EP | — → M20:informational | ELIAS 4 (RULED); CHAIN 1 (the message gives the shape) | Delivery (mortal, not VT); recipients; content; order against M23 |
| **M23** | REVISE | PARTLY RULED → `proposed` | MT passes to Kade; the channel's voice changes permanently | MT passes to Kade: after Tahl's death Kade keeps a grief diary in MT's comments, believing it private | B06 EP → B06 EP | M15,M20 → M15:character; M20:chronological | OVL; KadeEBCI and WOUNDS 2.4 (grief diary believed private, RULED) | Exact first post; the B06 EP / B07 split; order against M39 |
| **M40** | NEW | RULED → `ruled` | — | Book 7 opens at Tahl's funeral with Lacuna prominent; she inspires Kade to post | — → B07 A1 | — → M20:chronological; M23:character | SPINE follow-up (funeral, Lacuna prominent, RULED); ELIAS 5 (Lacuna inspires, RULED); LacunaEBCI | Whether the second line is on the page |
| **M41** | NEW | RULED → `ruled` | — | Elias, in New Orleans for MT, identifies Kade at the funeral and attaches to him | — → B07 A1 | — → M40:chronological | ELIAS (card corrections E1-E4: late-Neon relocation for MT; identifies Kade at the funeral) | Their first contact on the page |
| **M24** | REVISE | REVIEW → `proposed` | Global infrastructure collapse: governments admit there is no containment pathway | Condition, not event: services, transport and institutions degrade unevenly across regions; some persist | B07 A1 → B07 A1 | M19 → M38:material | OVL; LOOM1 6 | A named local failure could give it a face |
| **M25** | REVISE | REVIEW → `proposed` | The diaspora begins: millions move and the world's population map is rewritten | Condition, not event: diaspora and Filament-supported travel expand as routes and supplies come under pressure | B07 A2 → B07 A2 | M24 → M24:material | OVL; LOOM1 6 | Scale ('millions' unproven) |
| **M26** | REVISE | PARTLY RULED → `proposed` | MT becomes the last intact channel | Kade learns he is being read and takes over MT, the last broadly working public channel, maintained through uneven infrastructure | B07 A2 → B07 A2 | M23,M24 → M23:character; M24:material | KadeEBCI ('takes over', RULED); LacunaEBCI and EliasEBCI (MT the only / last broadly working channel, card corrections) | The review's 'last intact' objection against the card wording |
| **M27** | HOLD | REVIEW → `proposed` | Tahl's Echo shows Intent: he is an agent again, not a residue | A VeilThread-side beat: an echo that may or may not be Tahl's reaches toward Silence; not identifiable to the cast | B07 A3 → B07 A3 | M22 → M22:chronological | B6B8 1.2 (not identifiable); LOOM1 6; author 11-13 VT thread | Whether the row survives |
| **M49** | NEW | RULED → `ruled` | — | Seraphine is drawn into becoming the Loom and begins to question the hard cap; Mira, perceived only by her, guides her past recreating it | — → B07  B07 onward, schedule open | — → M03:thematic | WOUNDS 1.2 (RULED); CHAIN 2 (doubt grows from becoming the Loom); MIRA 1 and 5 (RULED) | Mira's appearance schedule is unresolved (author) |
| **M42** | NEW | RULED → `ruled` | — | Kade's post moves people and New Orleans breaks, forcing an accountable departure; Elias begins to subvert Kade | — → B07 A3 | — → M26:character; M41:character | SPINE 2 (C1+C2, RULED); ELIAS 5 (Elias subverts from Act III); B07 card | Post content; what breaks (not a third collapse); civic or scar; post/break order; the act (A3 is a reading) |
| **M28** | REVISE | RULED → `ruled` | Exodus from New Orleans toward the swamp | The crew leaves New Orleans to stabilise the wounds; not toward the swamp | B07 A3 → B07 A3 | M08,M24 → M39:informational; M42:material | SPINE (departure, not exodus toward the swamp); WOUNDS 1.1 (stabilisation, RULED); CHAIN 1 | Route out; who leaves |
| **M43** | NEW | RULED → `ruled` | — | The Lacuna-Kade split is foreshadowed at the end of Book 7, possibly by an argument | — → B07 A3 | — → M42:character | SPINE 4 (RULED; 'argument?' tentative) | The form of the foreshadowing |
| **M44** | NEW | RULED → `ruled` | — | Lacuna and Kade split at the start of Book 8 | — → B08 A1 | — → M43:character | SPINE 4 (RULED) | The cause (11-28 plan: arguing about embracing violence) |
| **M45** | NEW | PARTLY RULED → `proposed` | — | At Santa Fe, where Tahl died, the crew finds something real at the first wound, at a cost, and stabilises it | — → B08 | — → M28:chronological; M39:informational | SPINE 3 and follow-up (A1 at Santa Fe, RULED); WOUNDS 1.3 (stabilises Santa Fe: LEAN); CHAIN 1; B08 card | What is found; the cost; the act |
| **M46** | NEW | RULED → `ruled` | — | Kade's first complicity in his splinter's violence | — → B08 | — → M44:character | SPINE 3 (A2, RULED); B08 card | The form and victims; must not pre-empt the Rex near-kill |
| **M47** | NEW | RULED → `ruled` | — | Mound City (St. Louis), the second wound: the chain's particulars are confirmed | — → B08 | — → M45:chronological | CHAIN 1 (Mound City in B08 after Santa Fe, RULED; discovery beats become confirmation beats); Alignment Chain (author-saved) | The act; what is confirmed and by whom |
| **M29** | RETIRE | REVIEW → `retired` | First Echo Node discovered and stabilised: the Breathable Veil has a working blueprint | Retired: no pre-Mending formal Echo Node; its site function passes to M45 and M47 | B08 A3 → B08 A3 | M03,M28 → none | Packet C; SPINE (M29 retires); Mechanica 7.4 | — |
| **M30** | HOLD | REVIEW → `proposed` | Technarc collapses; its metas fail | Specific Technarc capabilities or manufactured-meta assets may fail or fragment; total collapse needs evidence | B08 A3 → B08 A3 | M17 → M17:institutional | OVL; LOOM1 6 (remnant accountability, POOL-016) | Scale |
| **M48** | NEW | RULED → `ruled` | — | Serpent Mound, the third wound: visited at the end of Book 8; the escape from it opens Book 9 | — → B08 A3 B08 end to B09 A1 | — → M47:chronological | CHAIN 1 (continuous across the break, RULED); SPINE follow-up (B09 escape at Serpent Mound, RULED) | Who is escaped from, and how; sequence against M31 (deferred) |
| **M31** | REPLACE | PARTLY RULED → `proposed` | The swamp convergence: the finale's conditions exist | Book 8 closes on a fleeting storm-wall opening that Elias claims for Kade; the factions conclude it leads back to Louisiana, and the swamp stays secret | B08 A3 → B08 A3 | M28,M29 → M46:character; M48:chronological | B6B8 4 (opening permitted in B08, may be fleeting, RULED); B6B8 2 (Elias claims it: intent); SPINE third follow-up (factions think Louisiana, RULED; via the opening: HYPOTHESIS); GATE #4 (actual opening: LEAN) | Sequence with M48 DEFERRED until milestones are extrapolated; whether Kade caused it; where Elias is |
| **M50** | NEW | RULED → `ruled` | — | The NOLA feint: the factions look for the crew in New Orleans while they are elsewhere | — → B09 A2 | — → M31:informational; M48:chronological | SPINE (11-28 plan; the feint's engine is the factions' Louisiana belief) | Its acts (A1-A2 per the plan); who stages it |
| **M51** | NEW | INTENT → `proposed` | — | The antagonist factions learn the swamp is the Mending site, in Book 9 Act III and not before | — → B09 A3 | — → M50:chronological | B6B8 4 (site secret, author intent with a firm reason; governing constraint) | Which factions; how they learn |
| **M32** | HOLD | REVIEW → `proposed` | Silence and Hope arrive and confess: 'I was afraid.' 'I was alone.' | Silence and Hope face the limits of the old Veil and make a consequential choice before the Mending; the quoted confessions are historical options | B09 A3 → B09 A3 | M21,M31 → M21:character; M51:chronological | OVL; CHAIN 4 (12-07 order wins) | Whether a confession scene survives beside the 12-07 order |
| **M52** | NEW | RULED → `ruled` | — | Elias attacks Rex; Rex knocks him down; Kade, fearing Rex will kill Elias, attacks Rex; Tahl's echo flares and stops him, the echo's one identifiable appearance, known by Rex | — → B09 A3 penultimate chapter | — → M22:physical; M41:character; M46:character; M51:chronological | WOUNDS 2.5 (motive, RULED); CHAIN 4 (choreography, 12-07 wins); B6B8 4 (flare known by Rex, RULED); TahlEBCI (penultimate chapter) | Staging; whether anyone besides Rex recognises it |
| **M33** | REVISE | RULED → `ruled` | The Mending: the hard-cap Veil ends, the Breathable Veil forms, Silence and Hope dissolve into Lucien and Caro | The Mending, the last chapter: Seraphine becomes the Loom; Hope, then Silence (after powering Tahl's echo), give themselves to it; Lucien and Caro become the guides, one at a time, with Elisabet's goodbye to Caro between; Mira's echo is released | B09 A3 E14 → B09 A3 | M03,M05,M27,M29,M32 → M05:character; M32:character; M49:character; M52:physical (Silence's boost) | CHAIN 2 and 4 (cost; 12-07 order; guides and conduit, RULED); MIRA 5 (Mira released; the Loom is powered by a soul, RULED) | The breathing veil's mechanism (D5); what the answer is (reserved for the end) |
| **M34** | REVISE | REVIEW → `proposed` | The Lightfall: resonance storms stop worldwide | Post-Mending storm and service conditions become less hostile over measured regions and intervals | B09 A3 E15 → B09 A3 | M33 → M33:chronological | OVL; REV | Reach and lag; residual hazard |
| **M35** | REVISE | RULED → `ruled` | MT is renamed LT; Kade's stewardship completes | MT continues under a new MT-initialled name with a new role; Elisabet, Rex and Kade stitch society back together, Kade with the rebellion's people | B09 EP → B09 EP | M23,M26,M34 → M23:character; M26:character; M34:chronological | GATE 5 addendum (MT continues, RULED); B6B8 3.2 (the reconstruction, RULED) | The name (MendedThread, MortalThreads are examples); Accord or Concord; the timeskip (lean: a few days) |
| **M53** | NEW | RULED → `ruled` | — | The epilogue's last beat: Lacuna and Kade under the night sky; Seraphine reaches out through LT, and the handshake reaches Kade's device through Tahl's echo; his triangle is implied | — → B09 EP | — → M33:chronological; M35:chronological; M40:character | LTA (scene and Mobius with the B01 prologue, RULED); GATE 5 (LT is the final thing); B6B8 3 (Tahl the conduit, RULED; LT_RULES 6 exception); B6B8 4 (triangle implied, RULED) | What the prompt presents; whether Lacuna perceives it |
| **M36** | HOLD | REVIEW → `proposed` | Tahl's Echo dissolves: 'Be kind for me.' | An identifiable Tahl farewell would be a second appearance; fold into M53's implied triangle, merge into M52's flare, or retire | B09 EP → B09 EP | M22,M33 → M22:chronological; M33:chronological | B6B8 1.2 and 4.3 | Author choice among the three |

## 7. For the author

1. **Approve the copy to replace the live grid?** As a whole, or row by row. On approval the CSV
   replaces `grids/milestones_payoffs.csv` as it stands; it already passes the grid checks.
2. **The 20 `ruled` statuses:** approve them, or keep any row at `proposed`.
3. **The conflicts in §4.** None blocks approval of the wording. Two (M38/M20 and M15) affect Neon
   episode mapping.
4. **Next after approval:** the thread-pressure recalibration pass, then the book, act and episode
   milestones the author named as the condition for B08's end sequence.

## What this does not change

The live grid; any rule, card or registry row; the B01 order; the EBCI hold; the site-secret
constraint; D5 on causal physics. Every `ruled` status in the copy is a proposal until the author
approves it.
