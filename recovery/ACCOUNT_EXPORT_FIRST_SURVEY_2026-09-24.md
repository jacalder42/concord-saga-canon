# First survey of the committed account export — 2026-09-24

**Scope.** The first search of `sources/chatgpt_export_2026-09/` since it was committed
(ledger §73). It targets the two live recovery items in `CLAUDE.md` §8 item 6 and the
`Archive Veil Book 1` target in item 7. **Nothing is migrated and nothing is ruled** —
findings are observational, per §4.

> **CORRECTED the same day, before anything was built on it.** This document was written
> without accounting for the **2026-09-20 forensic audits** in this same directory
> (`ACCOUNT_EXPORT_B01_ACT1/ACT2/ACT3_EPISODE_FORENSIC_AUDIT_2026-09-20.md`), which had
> already recovered Book 1's episode packets — **E00–E42, all three acts** — from
> `2025-12-08__Episode_expansion_process__6936cb32`.
>
> **§3 as first written claimed the packets as a find. They were already found.** What is
> actually new is narrower and, as it turns out, sharper: `Archive Veil Book 1` is an
> **independent second witness** that no prior pass had used, and **it disagrees with the
> first**. §3 is rewritten below; §4.6 is corrected. §1, §2 and §4.1 stand unchanged.

**The question item 6 was raised to settle** was *"until this runs, 'not exported' and 'does
not exist' cannot be told apart."* For all three targets it can now be told apart, and the
answers are not the ones the queue assumed.

---

## 1. `Spine Architect chat` — **found, and empty**

It is `2025-12-09__Structural_spine_storage__693823f7`. **2 turns, 410 words.**

The conversation consists of the startup prompt and one reply. The prompt appoints the
assistant *"Saga Structural Spine Architect"*, whose *"ONLY responsibilities"* are to store
act-level summaries, episode-level structural shells, continuity anchors, directional
breadcrumbs, transitions, character arc waypoints, antagonist scaffolding, resonance
topology and setting continuity for all nine books. The reply is *"Ready. Paste the first
structural segment…"*.

**The user never pasted anything.** The conversation ends there.

So §8 item 6's description of it — *"named as the owner of saga-wide continuity storage"* —
is accurate about its **charter** and wrong about its **contents**. The claim traces to
`Character Vault Chat`, which routes *"Saga-wide continuity storage (belongs to the Spine
Architect chat)"* away from itself. That is a routing instruction, not a record that
anything arrived.

**This target is closed.** There is nothing in it to recover.

## 2. `Saga Visual Bible Framework` — **found, and a scaffold**

`2025-11-16__Saga_Visual_Bible_Framework__691a2830`. **2 turns, 1,070 words.**

One prompt, one reply: a Workflow / Pipeline / Schema framework for a Visual Bible,
stamped *"(Ready for population after the Faction Bible is completed.)"* It describes the
artifact's structure. **It contains no visual canon.**

**This target is closed too**, in the same sense: the framework is recoverable and is not
the Visual Bible.

**Both live targets of item 6 are now resolved, and neither yields canon.** What item 6
still buys is the inventory itself — 70 conversations, 7,363,532 words — not these two.

---

## 3. `Archive Veil Book 1` — **a second witness, and it disagrees with the first**

`2025-12-09__Archive_Veil_Book_1__6938278b`. **40 turns, 10,121 words.**

The conversation is a paste-and-acknowledge archive: the user pastes a full structured
episode packet, the assistant confirms it archived verbatim and states the running order.
**18 distinct packets, `E00` through `E17`.**

**Work-queue item 7 is already satisfied, and not by this conversation.** Item 7 reads
*"Archive Veil Book 1 first — this is where the E00–E15 packets are expected to be."* The
packets were recovered on **2026-09-20** from a **different** conversation,
`2025-12-08__Episode_expansion_process__6936cb32`, and far more completely: **E00–E42,
Book 1's three acts**, in the three `ACCOUNT_EXPORT_B01_ACT*_EPISODE_FORENSIC_AUDIT`
files. The prediction was right about the material and wrong about its address.

**`CLAUDE.md` §6's *"the repository holds packets for E16–E18 only"* is stale**, and so
are items 7 and 8 as written. §6 warns of exactly this: *"Verify with `git` before trusting
this section; it dates quickly."*

**What is new is that `Archive Veil Book 1` has never been used as a source.** It is cited
as a *target* in the ledger, `NOTION_RECOVERY_2026-09-19.md`,
`NARRATIVE_BUILD_PRIORITIES_2026-09-19.md` and `CLAUDE.md`, and read by none of them. So
Book 1 Act I now has **two independent witnesses one day apart** — and they do not agree.

`EPISODE 3` is pasted **twice**. The two are **not a version conflict**: the packet bodies
are identical and the difference is entirely in the assistant's reply — the first flags a
possible truncation of the `EXIT CONDITION`, the user re-pastes, the second confirms
*"archived verbatim with no truncation."* Recorded because it is also evidence the archive
was checked for truncation at the time.

### The two witnesses disagree on titles, on segmentation, and on where Act I ends

| Slot | `Episode expansion process` — **2025-12-08** | `Archive Veil Book 1` — **2025-12-09** |
| --- | --- | --- |
| E00 | **The Conversation in the Sky** | **PROLOGUE: SILENCE & HOPE** |
| E01 | The Sick Child | THE CHILD IN THE SWAMP (Part I) |
| E02 | Too Late | THE CHILD IN THE SWAMP (Part II) |
| E03 | The First Echo | THE WALK BACK (Aftermath) |
| E04 | A Line Out of Place | LUCIEN'S FIRST FLICKER (Part I) |
| E05 | The Misalignment | LUCIEN'S FIRST FLICKER (Part II) |
| E06 | Crowd on Edge | FIRST CIVIC DISTURBANCE (Part I) |
| E07 | Instability in the Square | FIRST CIVIC DISTURBANCE (Part II) |
| E08 | Whispers of the Filament | FILAMENT FOOTPRINT (Part I) |
| E09 | Rootkeeper's Glance | FILAMENT FOOTPRINT (Part II) |
| E10 | Seraphine Strains | DUAL COLLAPSE BEGINS (Part I) |
| E11 | Lucien Unravels | DUAL COLLAPSE BEGINS (Part II) |
| E12 | The Dual Collapse | DUAL COLLAPSE BEGINS (Part III) |
| E13 | A Pulse Over Jackson Square | ACT I CLOSE (Part I) |
| E14 | Lines Breaking Apart | ACT I CLOSE (Part II) |
| E15 | Baz, We Need You | ACT I CLOSE (Part III) |
| **E16** | **Baz Arrives in NOLA — ACT II** | **ACT I CLOSE (Final) — ACT I** |
| E17 | The Situation Briefing — ACT II | ACT II OPENING (Part I) — `A2` |

**Three distinct disagreements, in rising order of consequence.**

1. **Naming convention.** The 12-08 source gives every episode a dramatic title; the 12-09
   source names them **structurally**, by the event they belong to and their part number.
   Cosmetic on its own.
2. **The prologue title, and it inverts the usual tiebreak.** `CLAUDE.md` §3 rules the
   prologue is **`The Conversation in the Sky`** and that `Silence & Hope` is superseded.
   The ruled title is in the **earlier** artifact; the **later** one carries the retired
   form. Every other dating argument in this project has favoured the later artifact —
   §27.6 declares the `ACT * SUMMARY` pages superseded on exactly that reasoning. **Here
   the ruling and the recency heuristic point opposite ways**, and the ruling has already
   been made, so the heuristic is what fails. Worth recording because it is the first case
   that shows the heuristic is not load-bearing on its own.
3. **The act boundary differs by one episode, and this one matters.** The 12-08 source ends
   Act I at **E15** and opens Act II at **E16 "Baz Arrives in NOLA"**. The 12-09 source
   runs Act I through **E16 "ACT I CLOSE (Final)"** and opens Act II at **E17**. Its SIDs
   say so outright: `S1.T1.B1.A1.E16` against the audit's placement of E16 in Act II.

   Narratively they are compatible — both close Act I on Baz being summoned and open Act II
   on his arrival; they differ on which side of the line the arrival sits. **But the act
   slot is part of the SID**, so the two sources assign `E16` different identifiers, and
   any migration writes one of them into canon. This is the Book 1 Act I analogue of
   *which Veil draft is canon* (§4), at one episode's granularity.

**None of this is resolved here.** Both readings are recorded with their dates and sources.

### The packets carry a full ECID header

`SID`, `Title`, `Function`, `POV`, `ENV`, `U-Level`, `Weather`, `Mode`, `Heat`, `FX`,
`Resonance State`, `Audience`, then `PRESSURE MAP`, `EPISODE JAZZ`, `BEATS` and
`EXIT CONDITION`.

| EP | SID | U-Level | Weather | FX | Resonance State | POV |
| --- | --- | --- | --- | --- | --- | --- |
| E00 | `S1.T1.B1.A0.E00` | **U7** (Quiet Veil) | W0 | **FX3** | VT-adjacent symbolic field | None |
| E01 | `…A1.E01` | U2 → U3 | W1 | FX1 | CALM → STRAIN | Seraphine |
| E02 | `…A1.E02` | U3 | W1 | FX1 | STRAIN → BLOOM → COLLAPSE | Seraphine |
| E03 | `…A1.E03` | U2 → U3 | W1 | FX1 | STRAIN | Seraphine |
| E04 | `…A1.E04` | U2 | W0 | FX1 | CALM → STRAIN | Lucien |
| E05 | `…A1.E05` | U1 → U2 | W0 | FX1 | CALM → STRAIN | Lucien |
| E06 | `…A1.E06` | U3 | W1 → W2 | FX1–FX2 | STRAIN → BLOOM | Seraphine |
| E07 | `…A1.E07` | U3 → U4 | W2 | FX2 | BLOOM → SHARD-LACED | Seraphine |
| E08 | `…A1.E08` | U2 | W1 → W0 | FX1 | STRAIN → CALM | Seraphine |
| E09 | `…A1.E09` | U1 → U2 | W0 | FX0–FX1 | CALM | Seraphine |
| E10 | `…A1.E10` | U2 → U3 | W0 | FX1 → FX2 | CALM → STRAIN → BLOOM → SHARD-TINT | Seraphine |
| E11 | `…A1.E11` | U2 → U3 | W0 | FX1 → FX2 | CALM → STRAIN → FRACTURE-TINT | Lucien |
| E12 | `…A1.E12` | U3 (both spaces) | W1 → W2 | FX2 → FX1 | STRAIN → SHARD-TINT → CALM | Split |
| E13 | `…A1.E13` | U3 → U4 | W2 → **W3** | FX2 | BLOOM → SHARD-LACED | Seraphine |
| E14 | `…A1.E14` | U4 | **W3** (Gale) | FX2 → FX3 | BLOOM → SHARD-LACED → COLLAPSE-TINT | Seraphine |
| E15 | `…A1.E15` | U2 → U3 | W1 | FX1 | CALM → STRAIN | Lucien |
| E16 | `…A1.E16` | U3 → U4 | W1 | FX2 | STRAIN → BLOOM → SHARD-EDGE | Seraphine |
| E17 | `…A2.E17` | U2 → U3 | W1 | FX0 → FX1 | CALM → STRAIN | Baz |

POV distribution: **Seraphine 12, Lucien 5, Baz 1**, plus one metaphysical and one split.
`Heat` is **H0 on all 19 blocks** — no romance ladder movement anywhere in Book 1 Act I.

---

## 4. What the packets bear on — recorded, not resolved

### 4.1 The prologue uses `A0`, which is in no ruled vocabulary

`S1.T1.B1.A0.E00`. Ruling 6 (2026-09-20) made `PR` and `EP` **structural positions
alongside** `A1`–`A3`, and `SID_format` carries `PR`. **This source uses `A0` instead** and
predates the ruling by ten months.

Both readings are on file and neither is adopted here. `A0` is a **fourth** form for the
prologue's slot, after `A1`-with-`E00`, `PR`, and the export layer's beat-1-inside-ACT-I.
It is the only one that implies a *zeroth act*, which the three-act cap (§4) rules out —
so it most likely reads as a position marker, exactly as Ruling 6 describes, under a
different letter. **That is an inference, and it is the author's to make.**

### 4.2 The prologue title is the superseded one

`Prologue — Silence & Hope`. `CLAUDE.md` §3 rules the prologue is `E00`, titled
**`The Conversation in the Sky`**, and that `Silence & Hope` is superseded. This packet is
consistent with the **numbering** ruling (prologue at `E00`, not offset by one) and carries
the **retired title**. Both facts sit in one artifact.

### 4.3 Episode numbering runs continuously across the act boundary — corroborated

`E16` is `A1` and `E17` is `A2`. Numbering does **not** restart. This is direct source
corroboration of §3's ruling, from a source that predates it, and it is the opposite of the
per-act restart §3 flags as pervasive in the recovered material.

### 4.4 The B01.A1 band is breached on all three axes

`act_overlay_S1_T1_B01_A1.json` carries `corridor U1–U4`, `weather W0–W2`, `fx FX0–FX2`,
and is one of only **three** bands in the repository marked `basis: observed` (ledger §18,
corrected §57). Against these packets:

| Axis | Band | Recovered | Where |
| --- | --- | --- | --- |
| corridor | U1–U4 | **U7** | E00 |
| weather | W0–W2 | **W3** | E13 (micro-Gale), E14 (Gale) |
| fx | FX0–FX2 | **FX3** | E00; E14 reads `FX2 approaching FX3 (Act-level limit)` |

**The band was observed from an incomplete sample.** It was derived when the repository
held E16–E18 only; sixteen further episodes of the same act were unexported at the time.
E14's own note calls **FX3** the *"Act-level limit"*, which contradicts the `FX2` ceiling
the repository derived — and the FX ceiling has already moved once on exactly this kind of
evidence (Veil FX1 → FX2, ledger §18, because the recovered E16 packet was right and the
ceiling was wrong).

Whether the prologue's `U7`/`FX3` are a breach or are outside the act's envelope by
construction depends on §4.1 — a prologue at `A0`/`PR` may not be inside `A1` at all. **The
two questions are entangled and are put together.**

### 4.5 The controlled-vocabulary findings of §4.1 are confirmed at source

Every form `CANON_DECISIONS_2026-09-18.md` §1.5 mapped is here, in volume:

- **Arrow forms throughout** — `CALM → STRAIN`, `FX1 → FX2`, `W2 (Squall) → W3 micro-Gale`.
  §4.1 already rules an ECID field holds a single value and the transition is recoverable
  from the previous episode. **The mapping applies unchanged; this is its input data.**
- **`Mode` carries two to four values per episode** — `CIV / ACT / INT / HORP`,
  `INT / HOR (light) / LORE`. Tokens seen: `CIV`, `ACT`, `INT`, `SCI`, `HOR`, `HORP`,
  `LORE`. §4.1 rules `LORE` is a `supplement_type`, not a mode; `HOR`/`HORP` and the
  multi-value shape are **not** covered by that ruling.
- **Resonance states beyond the vocabulary** — `SHARD-LACED`, `SHARD-TINT`,
  `FRACTURE-TINT`, `COLLAPSE-TINT`, `COLLAPSE`, `SHARD-EDGE`, `VT-adjacent symbolic field`.
  §4.1 rules `STRAIN`, `EDGE` and `BRUSH` are not states; the `-TINT` and `-LACED` family
  is larger than the three it adjudicated.
- **Beat IDs use the retired `B01`–`B06` form**, which `BT` replaced (§3). Converts on
  migration, as §3 anticipates.
- **One-digit book throughout** (`B1`), as §3's scope warning describes.

### 4.6 Silence and Hope — the first substantive material for item 9b

Work-queue item 9b records that **neither Silence nor Hope appears in any of the 62 files
in `canon/characters/`**, and that the 21 sanitized exports hold *"essentially nothing."*

The `E00` packet is not nothing. It gives them a contrast pair — Silence as **containment**,
Hope as **warm modulation** — states they are *"metaphysical roles, not beings"*, has them
name resonance as a consequence of human feeling, and has them **choose not to intervene
directly**, which the packet calls the saga's moral architecture.

**This is a beat outline, not a character file**, and it is Tier D. It does not close item
9b, whose located source is still Notion's `08.10` and `08.11`.

**Corrected:** this is **not** the first Silence-and-Hope material found in an export. The
2026-09-20 Act I audit covers the same prologue from the 12-08 source, and §22's *"the 21
exports hold essentially nothing"* was a finding about the **sanitized derivative**, not
about the account export. What this adds is a **second** rendering of the prologue, under
the retired title, with the same containment/modulation contrast — corroboration, not
discovery.

---

## 5. What was not done

**No migration.** Items 5, 5a and 8 are gated on decisions that have not been made, and
item 4 is gated on *which Veil draft is canon* — which this conversation bears on and does
not settle. The packets are recorded here and remain in `sources/` verbatim.

**No ruling.** §4.1–§4.6 each record what the source says against what the repository says.
Where they differ, both readings stand.
