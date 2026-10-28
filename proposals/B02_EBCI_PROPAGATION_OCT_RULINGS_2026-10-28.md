# B02 EBCI: propagation map for the October rulings (§615–§626), 2026-10-28

**Status:** PROPOSAL and record. The **MECH** rows are applied to `ebci/B02/` (author: "Agreed proceed", 2026-10-28). The **DESIGN** rows are proposed only: no Story job, Change, Exit state or beat has been rewritten for them. Each affected card carries a `DESIGN pending (propagation map Dn)` line in its Notes so drafters see it. Not committed.

**Governing decisions** (ledger §615–§626):
- `decisions/NYLA_ARC_AND_VISIBLE_MOMENT_2026-10-25.md` (§615)
- `decisions/B01_HOLDS_REVIEW_RULINGS_2026-10-25.md` (§616)
- `decisions/B01_I5_INSTITUTIONS_AUTHOR_RULINGS_2026-10-27.md` (§617, §618)
- `decisions/B01_RESONANCE_DISCOVERY_LADDER_AUTHOR_RULING_2026-10-27.md` (§619)
- `decisions/B01_ELISABET_SIGNATURE_BREACH_LEXICON_AUTHOR_RULING_2026-10-28.md` (§620–§622)
- `decisions/TRILOGY_CONTRACT_AND_QUESTIONS_AUTHOR_RULING_2026-10-28.md` (§624)
- `decisions/NYLA_SAGA_PLACE_AUTHOR_RULING_2026-10-28.md` (§625, §626)

§623 (the I7 brief gate) touches the B01 manuscript only and has no B02 card effect.

**Diagnosis source:** `reports/TRILOGY_SHEET_VEIL_2026-10-28.md` (rows on the forecast engine, the ladder running backwards, Vienna, Hollen, the stale guard and the Nyla gap).

## Counts
- **Cards touched:** 47 of 47.
- **MECH applied:** 71 changes:
  - 47 standing-guard edits;
  - 7 field edits (four *Prohibited* lines, two *Keep* lines, one Event-record citation);
  - 17 card-specific propagation notes.
- **DESIGN proposed:** 15 items (D1–D15), flagged by 27 `DESIGN pending` lines on 21 cards, and 2 proposed new packets (D9, D10).
- `tools/validate_canon.py`: no violations after the edits.

## Part 1. MECH (applied)

### M-1. The P5 standing guard, all 47 cards (§616, §619, §620–§622)
The *Amendments applied* line of every card carried *"physics observed, never explained by the page (characters may ask and theorise, Q-DQ4)"*. That text is struck and kept visible. It is replaced by:
- **Discoverable physics:** resonance's physical behaviour is discoverable. Characters may describe, hypothesise, test and explain it, and argue competing theories.
- **What stays unconfirmed:** nothing confirms its origin, a reserved truth, or that the Veil answers rhythm. Basis: Mechanica §60 as amended, §619; W2 loosened, §616; X1.
- **Lexicon:** a local break is a *breach* (active, escalating) or a *scar* (quiet), never a *Wound*.
- **Reserved word:** *breathing* is reserved (§620–§622).

The rest of the guard (no Tahl, no Kade, Rex or Honey Island, and so on) is unchanged. Each card has a dated Notes line recording the edit.

### M-2. Field edits (struck text kept visible)
| Card | Field | Change | Ruling |
|---|---|---|---|
| E03 | Prohibited on the page | *A mechanism* → a confirmed origin or reserved mechanism (characters may describe and argue how it behaves) | §619 |
| E03 | Event record | the Mechanica §60 citation marked as amended 2026-10-27 | §619 |
| E15 | Prohibited on the page | as E03 | §619 |
| E29 | Prohibited on the page | as E03 | §619 |
| E44 | Prohibited on the page | as E03 | §619 |
| E08 | Keep | *no Dominion exposition* → no **narrated** Dominion exposition; characters may state what the Dominion believes, as its belief | §616 X2, F8 |
| E23 | Keep | as E08 | §616 X2, F8 |

### M-3. Card-specific notes (control layer; nothing in the brief changes)
| Card | Note | Ruling |
|---|---|---|
| E01 | The Institute is the Hollen Institute, a Dominion front. Q-GV2 is answered in part. **Funder guard:** Baz knows the Hollen front from Vienna, and nothing in B02 reveals his Houston funder is a Dominion faction. The Veil questions and the never-reset ladder are cited. | §617, §619, §624, §626 |
| E03 | The first pulse **the city** names, not the protagonists' first. | §619, §624 rule 4 |
| E05 | Vienna = the Regional Review = Hollen. Signature limits (coarse; no count, place or out-forecast). *Why do the wells stop following the tide?* *Breathing* is reserved. C44's method and cone are the floor. | §617, §620–§622 |
| E06 | *He has no forecast* fits the re-scope. | §619 |
| E08 | The naming lock is off; Lucien's Institute is Hollen; Line 8 is Dominion's wrong belief; funder guard on Helena. | §616, §617, §624 §5, §626 |
| E13 | *Not their models* is superseded in part: Baz knows the Hollen front, and that Dominion forecasts the window, not how. | §617, §619 |
| E15 | *Prohibited* edit recorded. | §619 |
| E22 | As E13; the naming lock no longer backs the occlusion (see D13). | §617, §619 |
| E23 | *Keep* edit recorded. | §616, §617 |
| E26 | The occlusion is approved design, no longer a naming rule (see D13). | §617 |
| E27 | Q-GV2's *hidden nature* is superseded in part; *Keep* is unchanged. | §616, §617, §619 |
| E29 | *Prohibited* edit recorded. | §619 |
| E30 | **Guard:** the signature gives no size, pulse count or place. | §620 §3 |
| E34 | Lucien's notebook went to Vienna without Nyla's page (B01 C44). Dominion's grounds are the Pontalba footage (control only). | §615 §2 |
| E44 | *Prohibited* edit. The stretch is a **breach** in the control record; never a *Wound*. | §619, §620 |
| E46 | *No decay* is breach behaviour; escalation is B01 knowledge, and persistence is B02's finding. | §619 §6.1, §620 |
| E47 | The Act III close serves the Veil dramatic question; funder guard. | §624, §626 |

### Rulings with no B02 card effect
- **D04 (Doucet early, §618):** no B02 card names Doucet; Odile Doucet's B02 recurrence (cast B12) is not carded.
- **Joanne Pryor (§618):** absent from B02 cards. Her backers and buyer stay unexplained if she is added.
- **Caldas's B03 defeat (§624 §4):** B03 only. E27's restraint-made-visible note is unaffected.

### Upstream rows outside this scope (not touched; for the canon pass)
- `canon/cast_registry.csv`, rows B23 and B24 (Lanette, Nyla) and C06 (Strobl): *"have lost Nyla for good"* and *"Dominion plans to observe her, not take her"* are superseded by §615 (lost **at the Square**; taken in B02).
- `grids/episode_beats.csv`: the B02 rows need the DESIGN beats once ruled.

## Part 2. DESIGN (proposed; not applied)

Each item says what a card's Story job, Change or Exit state would need to make true. `[P]` marks a placement or choice for the author. No prose and no dialogue.

### D1. The ladder never resets: B02 starts from B01's ceiling (§619, §624 rule 4)
B01's ceiling has four parts:
- a working forecast, Dominion's, partly reverse-engineered;
- the Square protocol (preparation, position, a trusted signal, a repeat-pulse signal);
- three pulses and the false all-clear;
- a seated, connected crowd that changed the event, observed and unexplained.

| Card | Must make true |
|---|---|
| E01 | *Keep*: what still works is B01's ceiling, not *the window method, a bet that paid once*. |
| E10, E17 | Recurrence and repeat pulses are known going in; the version steps add to them (see D2). |
| E32 | *Keep*: *wait an hour, it passes* is the city's rule; the people who were at the Square do not share it. |
| E44 | *Want*: Seraphine does not wait by the city's hour, because she knows a repeat can follow a calm. What exceeds everyone's assumptions, hers included, is that it does not end. |

### D2. The forecast re-scope: "Dominion's model sees the window; Baz's method sees the people" (§619 §5.1)
| Card | Must make true |
|---|---|
| E10 | **Story job:** the first half of Baz's method, aimed at **people**. **Change:** version 1 reads which reports mark who in a window is exposed, and how they fare. The recurring blocks are expected (breaches escalate), not the find. **Exit:** the signs of who is exposed. |
| E14 | **Change:** the miss is the group's own window, reverse-engineered from B01's evidence, and it proves cruder than Dominion's. **Exit:** the model has failed once, and he stops competing on the window and works on the people. |
| E17 | **Change:** version 2 adds, from Shirin's logs, where people are when repeats come (who goes back in too soon after the first calm). **Exit:** the signs, and who is still exposed in the interval. |
| E22 | **Story job:** inside a Bywater window that is Dominion's (how the group knows it is [P]: through Lucien and Helena, or from Dominion's positioning), Baz's method names who on one block is exposed: Rosette's. The vote is unchanged. |
| E23 | **Change:** Dominion has the window and not the people. Helena's price stays the grounds (the method) and a list. Drop *will not clear a block on a number*. |
| E26 | **Change:** what is sent is the window, the place, the margin and the grounds, now the method's signs for who is exposed. No names, no list. |
| E29 | **Required consequence** and **Exit:** the window held (Dominion's), and Baz's reading of who was exposed was usefully right. *Before the extra cycle Baz argued for* stays. |
| E34 | **Change:** the Bywater rule is Baz's people-method joined to Dominion's window and applied elsewhere, so Dominion now holds both halves. **Guard:** the method is not how Nyla was found (her grounds are the footage, §615 §2). |
| E47 | Check only: Helena's drift request stands, because direction is Baz's and not in Dominion's window model. |

### D3. The seated-crowd follow-up: one beat, shown and argued, never confirmed (§619 §6.2–§6.3) — E38
- **Beat:** Rosette's book, set against Shirin's outside logs, shows that inside the room where two people kept the book together the minutes ran differently from the street around it.
- **The argument:** Baz and Shirin (Seraphine present [P]) argue whether it is what the Square's seated crowd showed. Nothing confirms it.
- **Guards:**
  - nobody tries to reproduce or use it (§619 §6.3);
  - nothing assigns it to Seraphine's gift;
  - nothing confirms rhythm (X1).
- **Exit adds:** a resemblance to the Square, argued and unconfirmed.
- E29 needs no change: the book is already the only record from inside.

### D4. Elisabet's Vienna outcome (§620 §6) — E05
- **Story job adds:** she returns from the Regional Review's consultation.
- **Change / Exit must state an outcome** (author's choice [P]):
  - **(a)** the Review showed her records like hers, unplaced and uncounted on the page, and wanted her home records at full resolution; she gave district and day only (C44);
  - **(b)** she was shown nothing she could use and asked for everything.
- **In both:** the price on the table is her northern series, and why they showed her now stays open.
- **Guards:**
  - nothing counts, orders or links sites;
  - no four Wounds;
  - whether she knows the Review is a Dominion front is not ruled [P].
- How this sits with the university's re-filing (Q-VB3) is [P].

### D5. Lucien's repair (§620 §6, §621) — E05
- **Before:** C39's admission was cut off, and C44 gave the apology in full.
- **After:** the repair is made: the cost to her, why he did it, and what he has done since. Whether she accepts it stays hers.
- Lucien must be on the page in E05, which is in Elisabet's POV.

### D6. The stopped readings (§620 §6, §621)
| Card | Exit fact |
|---|---|
| E05 | Her processed season feed has stopped producing readings. |
| E11 | The logger Lucien kept recording through the quiet stops producing readings on his rounds. |

Why stays open in both. The control choice is among tampering, total suppression, a fault and a step (§621). Nothing on the page confirms the cause.

### D7. E05's Caro beat starts after C44 (§620 §6, M07)
- **Before:** Caro has shown Elisabet her method; home records go out as district and day; the cone is back by the door.
- The release argument stays, built on that footing rather than on first terms.
- **Guards:** no declaration (M07); the kiss is B03.

### D8. P12, the 15 May place, as an early-B02 beat (§615) — E02 [P] (alternative: E09)
- **Beat:** 15 May passes, and the Hollen Foundation's held place for Nyla lapses unclaimed. Lanette's relief is shared at the neighbour's party.
- **Guards:**
  - nothing on the page marks the relief as false;
  - E02 still ends on the pleasure.
- **Exit adds:** the place has lapsed; Lanette believes it is over.
- **Cast:** Lanette (B23) and Nyla (B24) are active.

### D9. The taking (§615, §625) — a new packet after E29 [P]; POV Lanette [P]
- **Story job:** Dominion takes Nyla.
- **Must be true:**
  - she is taken **in person, by people, at a place**: the Foundation's people, with a public authority beside them [P];
  - any paper justification (a welfare referral or a placement) stays offstage or is mentioned in passing (§615 §1 amendment);
  - the grounds are Dominion's and are not stated on the page (control: the Pontalba footage of C42);
  - Seraphine is inside the line with Rosette (E28–E29) and not there [P].
- **Exit:** Nyla is gone, and Lanette knows who has her and not where.
- **Guards:**
  - no procedure on a child;
  - characters may voice Dominion's *Emitter* belief, as its belief, and nothing confirms it (X2, F8);
  - no funder–Dominion link (§626);
  - no new catastrophe.
- **E31 [P]:** Seraphine knows Nyla was taken while she was inside the line; the civic reckoning stays the episode's job.
- **Why a new packet:** folding the taking into an existing card would put it off the page.

### D10. The recovery, Lanette-led (§615)
| Placement | Must make true |
|---|---|
| **A new packet after E37 [P], POV Lanette** | She finds where Nyla is held, through the Filaments' reach and through Baz, who knows from Vienna that the Foundation is Dominion's front (§617). Asking officially fails. **Exit:** she knows where, and that asking will not get Nyla out. |
| E34 | Lucien learns that the camera footage grounded the taking, so the page he cut protected nothing. What he does with it is [P]. *Keep*'s no-refusal-until-B03 stands. |
| E37 (option [P]) | Arianna sees Lanette come to Seraphine. |
| E43 (option [P]) | Lanette is one of Ramon's night riders near where Nyla is held; he does not know why. |

### D11. The escape on the E44 pulse (§615, §625) — E44
- **Change adds:** on the night of the pulse that does not subside, the place where Nyla is held is inside or at the edge of the stretch [P]. The disruption opens a way, and Nyla gets out and reaches Lanette, who is there because she led the recovery.
- **POV:** Seraphine, out looking for unlisted households, is on the page for it [P]. A Lanette section or packet is [P].
- **Guards:**
  - nothing shows Nyla causing or steering anything: no directed power, and her conversion is provisional (§619 §5.3);
  - X1 holds;
  - the Required consequence is unchanged: no casualties, no new catastrophe.
- **Exit adds:** Nyla is out, with Lanette.

### D12. Aftermath and the Act III close (§615, §625)
| Card | Must make true |
|---|---|
| E45 (option [P]) | Lanette and Nyla may be at the night. There is no required clue. |
| E47 | **Exit adds:** Dominion has lost Nyla for now; she and Lanette are out of sight; nobody calls it over (no second false relief). |

**Control only:** the B03 retaking by coercion. Nothing in B02 foreshadows the conversion or the funder.

### D13. The occlusion of Baz's reference (E22 note, E26 Keep; §617)
The 10-03 D2 occlusion was approved design and is no longer backed by a naming lock. Whether Baz's objection names Dominion is the author's choice [P].

### D14. The E01 plot seed (§619 §6.1, §620)
The intake's pre-17 March question about similar episodes is now usable as Dominion's map of old breaches and scars. Using it in B02 is optional. Guard: no Wound chain.

### D15. E30's *her data underestimated the cluster* (§620 §3)
The water signature gives no size, so the line implies an estimate it cannot make. Restate it as: her data gave no sign of its size.
