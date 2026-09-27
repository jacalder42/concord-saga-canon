# B01 overlay and book-context TODO drafts (pass 1)

**Date:** 2026-09-27
**Status:** PROPOSAL — NON-CANONICAL; drafts of the B01 book-context and act-overlay TODO fields for author approval (preflight Q6); nothing in book_context/ or act_overlays/ is edited

**Asked for in:** `decisions/NEON_PASS3_MOBIUS_AND_EBCI_PREFLIGHT_AUTHOR_ANSWERS_2026-09-27.md` §3, Q6:
*"Before release, Claude drafts the B01 overlay TODO fields as a proposal."* The fields are those the
preflight lists (`proposals/B01_EBCI_PREFLIGHT_2026-09-27.md` §5).

## What it does not change

- **No file in `book_context/` or `act_overlays/` is edited.** Every value below is a draft for
  approval.
- **The title is the author's.** No title is proposed.
- **POV weights are the author's** (Ruling 9, `recovery/GATE_RULINGS_2026-09-20.md`). No number is
  proposed.
- **No envelope change.** The `PR` overlay and the A1 widening are release work (§5 notes them and
  does not do them). No band, exception, `soft_modulation` value or derived block is touched.
- **No pressure number.** Pressure vectors are directions in plain words. No C number, no score, no
  copy into `reader_pressure.csv` (preflight answers Q3; Ruling 7).
- **The B01 EBCI hold stands.** Nothing here writes a packet, a beat, prose or dialogue.
- **Episode numbers are current v4.1b labels.** In file (reading) order, E37 comes before E36 and
  E44 before E43. The relabel to reading order (B3, approved) happens at release; §5 lists what it
  touches.

## Citation keys

| Key | Source |
| --- | --- |
| **v4.1b** | `proposals/B01_REVISED_BEAT_BIBLE_V4_1B_INTEGRATED_2026-09-22.md` (§ = its section; E = its episode; R = its §1 governing rule) |
| **VAA** | `proposals/VEIL_AUDIT_AMENDMENTS_2026-09-27.md` (§3 notes; §4 governs) |
| **D1–D7** | `decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md` |
| **OQA** | `decisions/OPEN_QUESTIONS_AUTHOR_ANSWERS_2026-09-27.md` |
| **MCL** | `decisions/MAIN_CAST_LOCATION_AUTHOR_ANSWERS_2026-09-26.md` |
| **PF** | the preflight and its answers (Q1: R1, R5, R6, R7, R8; Q2: V1–V3, V7, V6 held) |
| **CC** | the companion `proposals/B01_PRIVATE_CAUSAL_CARDS_E15_E33_E45_E48_PASS1_2026-09-27.md` (this pass) |
| **§42A** | `rules/Mechanica-v4.md` §42A (ruled); **Mech §n** other Mechanica sections |
| **BC-…** | `grids/breadcrumbs.csv` rows (16 name a B01 locator) |
| **M01–M03** | `grids/milestones_payoffs.csv` (all `proposed`) |

---

## 0. Proposed shapes

The overlays hold `pressure_vectors: []` and `character_state_deltas: []`, with no documented schema.
**Proposed** (Q-O1):

```json
{"thread": "<canon_rules.json threads value>", "movement": "<from> → <to>, plain words",
 "carriers": ["E07", "E08"], "source": "<citation>"}
```

```json
{"character": "<cast name>", "from": "<state>", "to": "<state>",
 "carriers": ["E13"], "source": "<citation>"}
```

- `thread` uses the controlled vocabulary (`world`, `seraphine`, `baz`, `filaments`, `dominion`,
  `technarc`, `caro_elisabet`, …). **Lucien has no thread value**, so his arc sits in
  `character_state_deltas`.
- A relief entry uses `"thread": "world"` and says *relief* in `movement` (v4.1b §6 ECG pairs
  pressure with relief).
- `act_success_criteria` and `forbidden_shortcuts` stay arrays of strings, as now. The citations in
  the tables below are for review; on approval they can go into a `_source` note or be dropped.

---

## 1. `book_context_B01.json`

### 1.1 `title`

**Author-owned. Not proposed.** The field reads `"TODO: Book B01 Title"`. It stays for the author.

### 1.2 `pov_targets.weights`

**Author-owned (Ruling 9). Not proposed.** One observation for the author, not a recommendation of
numbers: the derived `rotation` holds Seraphine (saga lead) and Baz (trilogy lead). **Lucien is not in
it**, although v4.1b gives him point-of-view episodes (E04, E05, E11, E12, and his side of E45), and
the recovered Act I packets give him 5 of 19 (`recovery/ACCOUNT_EXPORT_FIRST_SURVEY_2026-09-24.md`).
Baz is absent until E18. Whether the rotation should list Lucien is Q-O5.

### 1.3 `entry_state.world`

The block is `"_basis": "authored - not derivable"`: B01 has no predecessor. `tools/derive_book_context.py`
leaves B01's `entry_state` alone (it derives `entry_state` for B02–B09 only), so an authored value is
not overwritten by regeneration.

**Proposed, on the page at entry:**

| # | Statement | Source |
| --- | --- | --- |
| W1 | New Orleans is living ordinary life: work, commerce, tourism, worship, music, heat, transit. Most of the city, most of the time, is normal (the Veil floor of U1/W0) | v4.1b §3, E03, E08; `proposals/concord-2026/ENVELOPE_INTERIM_VALUES_V2_2026-09-19.md` (*"Veil keeps a floor of U1/W0"*) |
| W2 | Veil-era conditions: effects are subtle and low-amplitude; technology is mostly stable; a few people notice faint wrongness, and no one shares a word for it | Mech §7.1; `rules/trilogy_context_T1_veil.json` (`tech_state: mostly_stable`); v4.1b E01, E04 |
| W3 | **No public event has yet happened.** No shared vocabulary, no pattern, no suspicion of anything beyond New Orleans | v4.1b E15 (*"first undeniable civic-scale event"*), §9 handoff (*"global extent suspected at most"* by the end) |
| W4 | **No MissingThread exists in B01.** No anonymous public voice | v4.1b R23; `BC-ANONYMOUS-MT-VOICE` (introduced B02 E07) |
| W5 | Institutions are present as footprint and procedure: the **Dominion** sphere (authority, classification, protection; Lucien's civic/cultural structural-systems bureau works within it) and **Technarc** (measurement: sensors, protocols, access), both ambient | v4.1b R14, R32, E23; VAA §3 T5 |
| W6 | Informal care networks (future Filaments) already exist as ordinary civic and community infrastructure, not an organisation | v4.1b E09, E10, R13 |
| W7 | The **Velvet Vein** is a working nightlife room, not anomaly headquarters | v4.1b R11, E06 |
| W8 | Places in play, by route family: a Honey Island-adjacent south-Louisiana wetland community; Tremé/community routes; St. Charles/Garden District/Uptown; the French Quarter and **Jackson Square**; Marigny/Bywater and the Vein; CBD/civic infrastructure; the riverfront; City Park. District-level specificity unless a venue is recovered and useful | v4.1b §3 |

**Proposed, writer-only and protected** (Q-O3: include as a `_private` sub-block, or omit):

| # | Statement | Source |
| --- | --- | --- |
| P1 | The Veil is a **hard cap**, held by a single soul (Mira's) and tended from outside by Silence and Hope. Blocked pressure is stored and concentrates at thin points | §42A.2 (ruled); `decisions/SERAPHINE_LOOM_HARD_CAP_AND_MIRA_AUTHOR_RULING_2026-09-27.md` |
| P2 | Silence and Hope perceive strain and cannot simply intervene | v4.1b prologue; `BC-SILENCE-HOPE-OBSERVE` |
| P3 | The swamp near Honey Island is the **original Tear**, the cap's first break. It is unexplained and unnamed in Veil; **nobody in Veil knows** it is the Mending site | `decisions/MECHANICA_HARD_CAP_BREATHING_VEIL_AUTHOR_ANSWERS_2026-09-27.md` Q2; VAA §3 O1; `BC-HONEY-ISLAND-SITE`, `BC-SWAMP-WOUND` |
| P4 | Pressure surfaces in New Orleans only at precursor level (flickers, ghostwaves), and Jackson Square recurs as a thin point | Mech §7.1, §34; CC §1.2 (**PROPOSAL**, Q-C2) |
| P5 | A faint southwest lean exists in the disturbances. It is perceptible to Lucien only, unnamed | v4.1b §13 southwest correction; `BC-SOUTHWEST-LADDER` |

**Guard:** none of P1–P5 may appear on the page in B01 as statement, prophecy or image. The prologue
**names nothing** and carries **no LT motif** (`proposals/MACRO_MOBIUS_PROLOGUE_EPILOGUE_DESIGN_2026-09-27.md` §4).

### 1.4 `entry_state.key_character_states`

| Character | State at entry | Source |
| --- | --- | --- |
| **Seraphine Vael** | Lives and works in New Orleans in a care role that takes her to a family in a medical/care crisis (exact role OPEN). Already perceives subtle wrongness, with no word for it and little confidence in it. Belief: ***"If I care enough, I should be able to save/fix this."*** Has a friend (Caro) and a life before the mystery | v4.1b §4, E01, E03, R31 |
| **Lucien** | Already in New Orleans on a **legitimate, bounded professional assignment** from a civic/cultural structural-systems bureau within the Dominion sphere: credentials, a mandate, an expected report. **Sent from Vienna before B01** (ruled); first on the page at E04; no on-page Vienna. Not a field agent; no explicit distrust of Virelli. Belief: ***"If I can structure it, I can contain uncertainty."*** Who sent him, and under what cover, is OPEN | v4.1b R32, E04, §4, v4.1b *Explicit non-decisions*; MCL follow-up 1 |
| **Bastien "Baz" Arnaud** | Outside the crisis and outside New Orleans (where is OPEN). Lucien's close friend and former/adjacent colleague, with witness, documentation, archive and institutional-literacy skills; current employer OPEN. Arrives by personal choice in Act II | v4.1b R33, §4, E17–E18; OQA A12 |
| **Caro** | In New Orleans, Seraphine's friend **before page one**; independently employed in response/care work (employer, credential and hospital OPEN, O2). **Does not leave New Orleans in B01** (ruled) | v4.1b R31, E03; MCL item 9 |
| **Elisabet Arnardóttir** | Not in New Orleans. An independent environmental/geospatial crisis researcher whose own data has flagged a Louisiana anomaly. **Her E23–E30 is one research visit**; she comes back to stay in B02 (E05) | v4.1b R34, E23; MCL follow-up 2; VAA §3 T8 |
| **Mara** | Civilian resource, intake and referral work in a small neighbourhood organisation; a notebook of ordinary tasks. Organisation, neighbourhood and title OPEN | v4.1b R35, E09 |
| **Trip** | Hosts the Velvet Vein | v4.1b E06 |
| **Offstage, with guards** | **Tahl:** exists, itinerant, **not named before the B03 epilogue**; no Tahl trace in B01. **Lacuna:** a human working musician; **a cameo at E31 only**, zero portent. **Rex:** in Detroit; not on the page in B01. **Kade:** not in B01 | `book_context_B01.json` `_ruled_constraints`; v4.1b §9; MCL; VAA §3 T8; `BC-LACUNA-CAMEO` |

---

## 2. Act I — `act_overlay_S1_T1_B01_A1.json` (E01–E17)

### 2.1 `act_thesis`

> **Discovery becomes pattern.** A care failure (E01–E02) and a private misperception (E04–E05)
> recur in public (E07–E08) until a many-witness Square event (E15) makes the problem undeniable in
> fact and disputed in cause. Seraphine and Lucien come to trust each other without fixing each other
> (E13), and Lucien chooses a person over process by calling Baz (E17).

**Source:** v4.1b Act I heading, §13 Act I jobs (7/7), E17 *Act I exit*; D1; M01.

### 2.2 `deltas.pressure_vectors`

| thread | movement | carriers | source |
| --- | --- | --- | --- |
| `world` | private, unshared wrongness → a **public many-witness incident with disputed cause** | E01, E04–E05, E07–E08, E15–E16 | v4.1b E07 (*"from private perception into public behavior"*), E15; D1; M01 |
| `seraphine` | failure to save → responsibility to understand; a private rule forms: *"next time, arrive sooner / move faster / carry more"*; she cannot regulate every room | E01–E02, E10 | v4.1b E01, E10; `BC-ARRIVE-TOGETHER` |
| `filaments` | informal care becomes visible at human scale (seed; M02 lands in A2) | E09–E10, S03 | v4.1b E09–E10; M02 |
| `dominion` | latent: a legitimate bounded mandate becomes pressure on Lucien, and he bypasses process | E04, E11, E17 | v4.1b E11, E17; `BC-DOMINION-LADDER` |
| `baz` | absent → summoned; *"help is coming"* | E17 | v4.1b E17; `BC-ASKED-HIM-HERE` |
| `world` (relief) | ordinary life and the hearth hold: grief in ordinary time, the Vein as an ordinary room, care culture | E03, E06, E12, E14, S01, S03 | v4.1b §6 (*"3–6: ordinary life → Lucien weirdness → hearth"*) |

`caro_elisabet` holds (no movement in A1).

### 2.3 `deltas.character_state_deltas`

| character | from | to | carriers | source |
| --- | --- | --- | --- | --- |
| Seraphine | *"If I care enough, I should be able to save/fix this"* | the same belief, now with a private rule (arrive sooner, move faster, carry more), and her first accepted help | E01–E02, E10, E13 | v4.1b §4, E01, E13 |
| Lucien | *"If I can structure it, I can contain uncertainty"*; a bounded mandate | his own perception unreliable; two faint, unnamed southwest twists; lets Seraphine's read matter; admits the case exceeds his model; calls Baz personally, **the first crack in institutional trust** | E04–E05, E11–E13, E16–E17 | v4.1b E04–E17; v4.1b *Möbius additions*; `BC-SOUTHWEST-LADDER` |
| Seraphine / Lucien | uncertain counterparts | real trust, shown in ordinary behaviour | E13–E14 | v4.1b E13 State, E14 |
| Baz | outside the crisis | agrees to come; hears what Lucien is not saying | E17 | v4.1b E17 |
| Caro | Seraphine's friend | unchanged; recognises Seraphine's baseline and keeps her own obligations | E03, E06 | v4.1b E03 |
| Mara | a notebook of ordinary people and tasks | strange civic observations begin entering it | E09 | v4.1b *Möbius additions* |
| Trip / Velvet Vein | — | **ordinary room** (Möbius state 1) | E06 | v4.1b E06, §4 |

### 2.4 `act_success_criteria`

| # | Criterion | Source |
| --- | --- | --- |
| 1 | E01 gives the mystery human cost before explanation: the child dies, Seraphine stays with the family; no Shard terminology; the swamp is not mythologised; the site is a Möbius seed of the Mending site only, known to no one | v4.1b E01; VAA §3 O1; `BC-HONEY-ISLAND-SITE` |
| 2 | E02 separates grief from anomaly; the residue is unnamed (no formal Echo language) | v4.1b E02 |
| 3 | Seraphine has a life and a friend before the mystery: Caro's friendship predates page one, shown by behaviour, with no introduction | v4.1b E03, R31 |
| 4 | Lucien is introduced through his way of seeing, on a legitimate bounded assignment; the southwest lean appears twice, faint and unnamed | v4.1b E04, E11, §13 southwest ladder |
| 5 | The Vein works as an ordinary room: the scene holds with its anomaly dialogue deleted | v4.1b E06 guardrail; `BC-VELVET-VEIN-ROOM` |
| 6 | Public recurrence precedes the civic event: a brittle crowd with no puppets (E07); a repeat at the Square under different circumstances (E08) | v4.1b E07–E08; `BC-JACKSON-SQUARE-RETURN` |
| 7 | S02 produces *"Was that similar?"*, not *"This is happening globally"* | v4.1b S02; `BC-REMOTE-SIMILAR`, `BC-PULSE-NAMING` |
| 8 | E13: neither fixes the other. E14: trust appears in behaviour; no romance declaration, no clue | v4.1b E13–E14 |
| 9 | **E15 meets its causal card:** a many-witness incident with disputed cause; the amp and the two-recording thrum as trials | D1, D2, D3; CC §2; M01 |
| 10 | E16 traces a specific consequence of E15 (cleanup, commerce, imperfect comparison) and Lucien admits the problem exceeds solitary solution | v4.1b E16 |
| 11 | **Act exit:** help is coming; the problem is larger than the people asking; Lucien calls Baz personally rather than escalating; no death foreshadowing | v4.1b E17; `BC-ASKED-HIM-HERE`, `BC-DOMINION-LADDER` |
| 12 | The Life/Reward units (E03, E12, E14) end on life, not plot | v4.1b §13 Life/Reward checksum |
| 13 | A variety of pleasure and want is visible (amusement, irritation, harmless selfish wants), not only care | VAA §4 execution tests |

### 2.5 `forbidden_shortcuts`

| # | Forbidden | Source |
| --- | --- | --- |
| 1 | Seraphine and Lucien's alignment (E13) causes, calms or triggers the Square event (E15) | `reports/B01_EVENT_MECHANICS_EPISODE_CONTEXT_RECOMMENDATIONS_2026-09-23.md`; CC §2.1 |
| 2 | Grief, feeling or Intent as the cause of the child's death or of any event's onset | evidence ledger (prologue → E01–02 row); PF R1, R7 |
| 3 | Colour, aura or hue as a detector of emotion, truth or Intent | PF V2, R8 |
| 4 | Objective floating or impossible geometry (E05 explicitly) | v4.1b E05; PF V3 |
| 5 | Formal Pulse, Shard, micro-Shard, Node or Echo naming; corridor-class semantics (*"U4 Memory"*) | v4.1b R15, R16, §8; PF R5 |
| 6 | Mechanics explained in dialogue | Mech §60 |
| 7 | Technology as a carrier; a recording as transmission | Mech §23; PF V4 |
| 8 | Seraphine calming a crowd or the Square by aura or *"calm pockets"*; breath or grounding repairing anything | PF R7; `recovery/B01_PULSE_EVENT_FULL_EXPORT_PROVENANCE_PASS_2026-09-23.md` (quarantine) |
| 9 | Lucien naming, mapping or interpreting the southwest lean; *"Everything curves southwest"* | v4.1b §13 |
| 10 | An introduction package for Caro, or Caro on standby for Seraphine | v4.1b E03 |
| 11 | Lacuna required in Act I | v4.1b R12 |
| 12 | A named antagonist; Virelli; Dominion history or a bureau name | v4.1b E04, E11, *Explicit non-decisions* |
| 13 | MissingThread, Tahl, Marrakesh, Elias, Brightbreak; global confirmation | v4.1b R23, R25, S02 ceiling |
| 14 | The prologue as literal preview or prophecy; any LT motif; naming Silence and Hope | v4.1b prologue; macro-Möbius design §4 |
| 15 | Death foreshadowing in the Baz call | v4.1b E17 |
| 16 | Honey Island named or linked to any future site | VAA §3 O1 |

---

## 3. Act II — `act_overlay_S1_T1_B01_A2.json` (E18–E37; E37 read before E36)

### 3.1 `act_thesis`

> **Investigation becomes prediction.** Baz arrives as a person before he is a method; the trio's
> three ways of knowing (feel → structure → verify) turn scattered incidents into a falsifiable local
> window. Restraint is rewarded (E29) and promised pleasure is paid (E31). The predicted pulse (E33)
> proves the system is not random while control fails; bodies and care come before explanation
> (E34–E35); the city begins to adapt as the cycle shortens (E36, the act close).

**Source:** v4.1b Act II heading, §13 Act II jobs, E20 trio grammar, E33 payoff, E36 *Act II exit*.

### 3.2 `deltas.pressure_vectors`

| thread | movement | carriers | source |
| --- | --- | --- | --- |
| `world` | scattered incidents → a working pattern → a falsifiable window → a partial hit with an expressive miss → an accelerating cycle; *"isolated event"* stops being a useful frame. **No global claim** | E20, E25, E27, E33, E35–E36 | v4.1b E25, E27, E33, E36; CC §3 |
| `seraphine` | too late → temptation to act too early → **restraint** (E29); then overreach and saturation (E33) | E27, E29, E33–E34 | v4.1b E29 Möbius turn; VAA §4; CC Q-C5; `BC-BOUNDED-RESPONSIBILITY`, `BC-SWAMP-WOUND` |
| `baz` | arrives → an embedded method → a cautious conclusion: *"the pattern is accelerating"* | E18–E19, E27, E33, E36 | v4.1b E18–E19, E36 |
| `filaments` | recognisable through recurring care and coordination (**M02 lands**) → *"control was never the promise"* | E20, E22, E35 | M02; v4.1b E35; `BC-FILAMENT-ETHIC` |
| `dominion` | authority, classification and protection language, as footprint | E23 | v4.1b E23 |
| `technarc` | **ambient only**: sensors, protocols, access; **no request to Baz** | E23 | VAA §3 T5 (`BC-TECHNARC-KIT` starts at B02 E13) |
| `caro_elisabet` | none → **recognition / instinctive safety** | E28 (option), E30 | v4.1b E30; `BC-CARO-ELISABET-LADDER` |
| `world` (relief) | competence fun, wonder, anticipation, the night paid in full, bodies first, friendship | E21, E26, E28, S04, E31, E34, E37 | v4.1b §6, §13 Life/Reward checksum |

### 3.3 `deltas.character_state_deltas`

| character | from | to | carriers | source |
| --- | --- | --- | --- | --- |
| Seraphine | tempted to treat community knowledge as a hidden answer | chooses restraint in the pressure zone despite the swamp wound's pull; saturates at the pulse; sees that useful care can exist without causal certainty | E22, E29, E33, E35 | v4.1b E22, E29, E35; VAA §4 |
| Lucien | resists withdrawal | accepts it; sees structure and cannot command it; shows a different self off the clock | E29, E33, E37 | v4.1b E29, E33, E37 |
| Seraphine / Lucien | trust | **trust capable of surviving conflict** | E24 | v4.1b E24 State |
| Baz | a friend summoned | a person in New Orleans first; a witness-sequence method (*"what would count as wrong?"*); the act's cautious conclusion; a friendship with Lucien independent of the case | E18–E19, E22, E27, E36–E37 | v4.1b E18–E19, E27, E36–E37 |
| Elisabet | absent | **one research visit** on her own vector; productive friction with Lucien; supplies or contests one inference; creates clarity for Caro; returns to her own work. Not the trio's fourth member | E23, E25 (option), E30 | v4.1b E23, E25 option, E30; VAA §3 T8; MCL follow-up 2 |
| Caro | Seraphine's friend | competent first; accepts help; **safe because seen without being managed**; registers interest in Elisabet's sharp public self | E28 (continuity), E30 | v4.1b E28 continuity, E30 |
| Mara | a notebook with odd entries | a continuity face for the trio's investigation; she does not join the team | E20 | v4.1b E20, *End states* |
| Trip / Velvet Vein | ordinary room | the night is paid (E31); **rumour room** (S05, E36) | E31, S05, E36 | v4.1b §4 Möbius |

### 3.4 `act_success_criteria`

| # | Criterion | Source |
| --- | --- | --- |
| 1 | Baz is a person before a function (arrival pleasure, no clue in the meal, no death shadow), and has a friendship with Lucien independent of the case | v4.1b E18, E37 |
| 2 | Investigation happens while walking, eating and waiting; briefing through disagreement, not exposition | v4.1b E19; v4.1b §11.D (embedded restoration ledger) |
| 3 | E22 is no lore council; Baz asks what would falsify an interpretation | v4.1b E22 |
| 4 | E23: institutions as footprint; Technarc ambient with no request to Baz; Elisabet enters on her own vector, on a visit, not for Caro and not for the Dominion | v4.1b E23; VAA §3 T5, T8 |
| 5 | E24: fear, not misunderstanding, drives the conflict; repair requires changed behaviour | v4.1b E24 |
| 6 | E25: a working model only; the narrator certifies no Corridors or Nodes | v4.1b E25 |
| 7 | E26: wonder without punishment; no new Mechanica | v4.1b E26 |
| 8 | **E27 states in advance** the window, the place, what they will watch for, and what counts as a miss | `reports/B01_E15_E33_CAUSAL_EVIDENCE_FALSIFICATION_PASS_2026-09-23.md`; CC §3.2 |
| 9 | E29 is retitled away from *drift* and uses *pressure zone*; *"swamp wound"* stays an unexplained seed; restraint is chosen and later validated | VAA §3 T6; `BC-SWAMP-WOUND` |
| 10 | E30: recognition / instinctive safety; no romance episode, no mechanics lesson, no Elisabet biography; Leila not required | v4.1b E30 |
| 11 | E31: the night succeeds and is not attacked; Lacuna is a cameo only | v4.1b E31; VAA §3 T8; `BC-LACUNA-CAMEO` |
| 12 | E32 → E33 → E34 run with no supplement; **E33 meets its causal card** (window shudder trial, no lamp); E34 puts bodies before any debrief; E35's care helps people without reversing the event | v4.1b E32–E35, §7; D4; CC §3 |
| 13 | **Act close (E36, read after E37):** the city adapts; the cycle shortens; the pattern accelerates; no global claim; words stay scattered | v4.1b E36; `BC-PULSE-NAMING` |
| 14 | **M02 lands:** Filaments recognisable through recurring care and coordination, with no recruitment and no organisation chart | M02 |
| 15 | Reading order holds: E37 before E36, S05 at its file position; labels corrected only at release | D7; OQA B3 |
| 16 | A variety of pleasure and want is visible, and Caro's interest in Elisabet is more than care | VAA §4 execution tests |

### 3.5 `forbidden_shortcuts`

| # | Forbidden | Source |
| --- | --- | --- |
| 1 | Breath, grounding or the trio's presence controlling or cancelling the pulse | PF R7; readiness report (E32–35 row) |
| 2 | Exposition during acute aftermath; any debrief or clue in E34 | v4.1b E34 |
| 3 | A plot alert inside E31; a threat hidden in S04 | v4.1b E31, S04 |
| 4 | A Technarc request to Baz; Technarc as a named antagonist | VAA §3 T5 |
| 5 | Elisabet as Dominion, as the trio's fourth member, introduced for Caro, or staying in B01 beyond the visit | v4.1b E23, E25; VAA §3 T8 |
| 6 | A C/E romance declaration or full romance episode; an S/L physical romance payoff | v4.1b E30, §4 |
| 7 | *Drift* as ontology or as E29's title | VAA §3 T6 |
| 8 | Exact-second prophecy; a model that becomes authority | v4.1b E33; CC §3 |
| 9 | Community knowledge as the hidden answer; a council of mystical specialists | v4.1b E22 |
| 10 | Glass as an automatic conductor; a citywide mechanical wave; a lamp failure by default | D4; context review (E19–27 → E31–35 row) |
| 11 | Global confirmation, Marrakesh, MissingThread, Tahl | v4.1b §9 |
| 12 | Numeric sorting of E36/E37 | D7; OQA B3 |
| 13 | Death foreshadowing for Baz | v4.1b E18, E37 |
| 14 | Mechanics explained in dialogue | Mech §60 |

---

## 4. Act III — `act_overlay_S1_T1_B01_A3.json` (E38–E48; E44 read before E43)

### 4.1 `act_thesis`

> **Pattern becomes systemic.** Disturbances cross neighbourhoods and systems faster than the city
> can close them out; civic coordination, not spectacle, carries the failure (E40–E41). Care helps
> people without controlling the phenomenon (E43). The rebound breaks Lucien's model and turns shared
> burden into usable behaviour (E45). After the Wide Quiet and the Square's human memory, the trio
> **arrive together** at a predicted quiet pulse and Seraphine **carries one**, at bodily cost:
> understanding without control. The city knows something is happening; nobody knows enough.

**Source:** v4.1b Act III heading, §13 Act III jobs, E48 Möbius inversion and book-end state; VAA §4;
M03.

### 4.2 `deltas.pressure_vectors`

| thread | movement | carriers | source |
| --- | --- | --- | --- |
| `world` | recurrence without one centre → civic coordination failure → human aftermath → **systemic, not global** → a changed baseline | E38–E41, E47–E48 | v4.1b E38–E41, E47–E48 |
| `world` (non-local) | an ambiguous remote similarity becomes an **ethical question**, still not proof; inquiry widens, certainty does not | E39, E45 | v4.1b E39, E45 structural aftermath; `BC-REMOTE-SIMILAR` |
| `seraphine` | the limits of being useful to everyone → overreach at the rebound → **arrive together, and carry one** (**M03 lands**) | E41, E45, E48 | v4.1b E41; VAA §4; M03; `BC-ARRIVE-TOGETHER`, `BC-BOUNDED-RESPONSIBILITY` |
| `filaments` | practice as stabilisation → **practice as human care under instability** | E43 (label), E41 | v4.1b E43 *Filament state*; `BC-FILAMENT-ETHIC` |
| `baz` | embedded → the one who argues investigation must widen, and says *"we don't know"* | E45, E48 | v4.1b E45, E48, §4 |
| `dominion`, `technarc` | watching and collecting stay **footprint, not confrontation** | E48 | v4.1b E48, §9 |
| `world` (relief) | exhausted humour and care; harmless wonder; the continuity room | E42, E44 (label), S06 | v4.1b §6 (*"41–44"*), S06 |

`caro_elisabet` holds at recognition / instinctive safety.

### 4.3 `deltas.character_state_deltas`

| character | from | to | carriers | source |
| --- | --- | --- | --- | --- |
| Seraphine | *"If I care enough, I should be able to save/fix this"* | ***"Care matters even when it cannot control the outcome."*** She has recognised the cost of over-responsibility and experienced restraint as useful, and **has not mastered either**; she carries one at bodily cost | E41, E45, E48 | v4.1b §4; VAA §4; M03 |
| Lucien | *"If I can structure it, I can contain uncertainty"* | ***"A model can be useful without being complete."*** He accepts help sooner, leaves an imperfect line unchecked, and still believes better structure may resolve it | E45, E48 | v4.1b E45, E48, §4 |
| Seraphine / Lucien | trust capable of surviving conflict | **usable shared burden** | E45 | v4.1b E45 Möbius, §4 |
| Baz | embedded | embedded enough to widen the investigation, and still the one most willing to say *"we don't know"*; his warmth and future orientation visible | E45, E48 | v4.1b §4 |
| Lucien (institution) | a legitimate bounded mandate | the assignment is ethically and personally larger than the mandate; Dominion conflict stays **latent** | E45, E48 | v4.1b *End states*, *Möbius additions* |
| Mara / Filaments | care useful; control assumed | care persists; claims of control weaken; the notebook holds **community memory under load**; she does not join the team | E41, E43 | v4.1b §4, *Möbius additions* |
| Caro / Elisabet | recognition / instinctive safety | unchanged: a seed, not yet the romance plot | — | v4.1b §4 |
| Trip / Velvet Vein | rumour room | **continuity room** | S06 | v4.1b S06, §4 |

### 4.4 `act_success_criteria`

| # | Criterion | Source |
| --- | --- | --- |
| 1 | E38 establishes a changed baseline, not an isolated incident; *"hum"* stays ambiguous | v4.1b E38 |
| 2 | E38–E41 use **distinct material failure chains** (routes, dispatch, care capacity), not repeated unnamed surges | evidence ledger (E38–41 row); census cards `B01-40A`/`B01-40B` |
| 3 | E39 is the strongest synthesis; the remote item is suggestive, not confirmatory | v4.1b E39 |
| 4 | E40: cohesion breaks through fear, conflicting information and contagion, never mind control; officials unnamed unless earned | v4.1b E40 |
| 5 | E41 makes aftermath human before any solution; E42 has nothing supernatural in it | v4.1b E41–E42 |
| 6 | The wonder episode (label E44, read first) stays unverified wonder: no mechanic, no danger, no report | v4.1b E44; evidence-ledger item E7 |
| 7 | The grounding episode (label E43): *"care succeeding is not control succeeding"* | v4.1b E43 |
| 8 | **E45 meets its causal card:** Lucien's collapse is point-of-view only, against a negative instrument check; Seraphine anchors him; the narrator never links the practice to the rebound; inquiry widens, certainty does not | CC §4; v4.1b E45; census card `B01-45B` |
| 9 | E45 → E46 → E47 → E48 run with no supplement; E46 is not compressed, has no comedy and is not fully explained | v4.1b E46, §7 |
| 10 | E47: the Square's memory is human (routines, memorial habits, stories); the model is systemic, not global and not controllable, and points to a narrow window | v4.1b E47 |
| 11 | **E48 meets its causal card:** they arrive together by shared prediction; one stranger, not a child, is steadied; the whole Square is declined; the cost is bodily; the stranger walks out whole; a positive, quiet, independently checkable observation | VAA §4; D6; M03; CC §5 |
| 12 | **Book-end state:** the system is patterned; the city knows something is happening; nobody knows enough. Global extent unconfirmed; vocabulary fragmented (B02 owns *pulse*) | v4.1b E48, §9; VAA §1 E03 |
| 13 | S06 comes after the narrative close: the same room, incompatible stories, no reveal, no cliffhanger | v4.1b S06 |
| 14 | Every item of v4.1b's B01 → B02 handoff holds | v4.1b §9 and its handoff additions |
| 15 | Reading order holds: E44 before E43; labels corrected only at release | D7; OQA B3 |
| 16 | **Discovery accumulates:** *predicting a window* still works when B02 opens | VAA §4 execution tests |

### 4.5 `forbidden_shortcuts`

| # | Forbidden | Source |
| --- | --- | --- |
| 1 | The narrator links the grounding practice or the gathering to the rebound; *"it learned"*; a responsive agent | CC §4; `recovery/ACCOUNT_EXPORT_B01_ACT3_EPISODE_FORENSIC_AUDIT_2026-09-20.md` (E38 caution) |
| 2 | Objective impossible geometry at E45; Lucien's instruments confirming a change in geometry | v4.1b E45; PF V3 |
| 3 | Stone or water *memory* as a law; the Square literally remembering | v4.1b E47; evidence ledger |
| 4 | Exact-second prophecy; a complete model; mastery or control; *"falsify random"* as a literal claim | v4.1b E48; CC §5.8 |
| 5 | Global confirmation, Marrakesh, MissingThread, Tahl, Elias, Brightbreak, Choirless, a formal network; Santa Fe or Warehouse breadcrumbs | v4.1b §9 |
| 6 | Seraphine holding the whole Square; a child rescue that restages E01 | VAA §4 |
| 7 | A third escalating device glitch as E48's centrepiece | context review (E38–47 → E48 row); CC §5.1 |
| 8 | A cosmic reveal, a Mending-site hint, or Loom foreshadowing beyond restraint and cost | readiness report (E45–48 row); M03 notes |
| 9 | Shard filtration, a prismatic debut, micro-Shard language, U6/U7 geography | M03; v4.1b §8 |
| 10 | A supplement inside a protected window (E40 → E41; E45 → E46 → E47 → E48) | v4.1b §7 |
| 11 | B02's answers: verified multi-city instability, *"accelerating everywhere"*, a global pulse cluster | v4.1b §13 B1/B2 boundary |
| 12 | *"Everything curves southwest"* in B01 | v4.1b §13 |
| 13 | Breath or care repairing anything; mind reading | PF R7 |
| 14 | Mechanics explained in dialogue | Mech §60 |

---

## 5. Envelope work at release (noted, not done)

1. **A `PR` overlay** for `S1.T1.B01.PR.E00`: U7 / FX3 metaphysical permitted (OQA B1, ruled). The
   recommended file is `act_overlay_S1_T1_B01_PR.json`, checked by `CHK_BANDS`, **not counted among the
   27 acts** (Ruling 6). Its thesis, criteria and forbidden list come from the prologue's perception
   card (preflight §4) and the macro-Möbius guardrails (no LT motif; names nothing). **The
   `silence_hope` thread and the two prologue breadcrumbs** (`BC-MACRO-MOBIUS-SKY`,
   `BC-SILENCE-HOPE-OBSERVE`) belong there, not in A1.
2. **A1's widening (OQA B2, approved design):** W3 and FX3 at **recovered-packet** E13–E14. **Map
   first.** By slot and by title the two witnesses agree that recovered E13 is *A Pulse Over Jackson
   Square* and recovered E14 is *Lines Breaking Apart* (`recovery/ACCOUNT_EXPORT_FIRST_SURVEY_2026-09-24.md`
   §2; the Act I forensic audit), which are v4.1b **E15** and **E16**. If that mapping is confirmed, the
   declarations would take this form (**sketch only, not applied**):

   ```json
   {"sid": "S1.T1.B01.A1.E15", "axis": "weather", "value": "W3", "scope": "brief",
    "reason": "First civic-scale event; recovered-packet E13 (W2->W3), OQA B2"}
   {"sid": "S1.T1.B01.A1.E16", "axis": "weather", "value": "W3", "scope": "brief",
    "reason": "Recovered-packet E14 (W3), OQA B2"}
   {"sid": "S1.T1.B01.A1.E16", "axis": "fx", "value": "FX3", "scope": "brief",
    "reason": "Recovered-packet E14 (FX2->FX3), OQA B2"}
   ```

   **Caution:** recovered E14's W3/FX3 describe the 12-09 witness's *"ACT I CLOSE (Part II)"*, a
   continuation of the event; v4.1b E16 is cleanup and comparison. The E16 exceptions may have nothing
   to attach to. The causal card recommends W3 at E15's peak and **no FX3** (CC §2.6).
3. **The overlays' `basis_note` values use recovered numbering:** A1's *"E16 at U3->U4, W1, FX2"* and
   A2's *"E17/E18 at U2->U3"* are 12-09 packet numbers (Act I closes at recovered E16). Re-note them in
   v4.1b labels at release.
4. **The relabel (OQA B3)** swaps labels E36 ↔ E37 and E43 ↔ E44 to match reading order. It touches
   these drafts (§3, §4), the causal cards, and breadcrumb locators such as `BC-FILAMENT-ETHIC`
   (`S1.T1.B01.A3.E43`) and `BC-PULSE-NAMING` (`S1.T1.B01.A2.E36`).
5. **No new RES, HEAT, LOAD or MODE bands** (preflight Q6).
6. **The book's `escalation_permissions` is a derived union** of the act bands. Regenerate it after the
   A1 exceptions are declared, rather than editing it by hand.
7. **Not TODO, not proposed, flagged:** every B01 act carries `soft_modulation` `fun`, `slice_of_life`
   and `wonder` at `max_intensity: LOW`. v4.1b promotes 12 Life/Reward units, and Act II pays
   *"competence fun"* (E21) and a night that *"succeeds"* with *"someone [having] more fun than
   expected"* (E31). Whether LOW is the intended ceiling is the author's to review.

---

## 6. Questions for the author

**Answer format:** for example *"O1–O4 yes, O5 no"*. Approval makes these approved design (Tier B).

| # | Question | Recommended |
| --- | --- | --- |
| **Q-O1** | **Shapes:** `pressure_vectors` and `character_state_deltas` as arrays of objects (thread or character, movement, carriers, source), with no numeric pressure? | **Yes** |
| **Q-O2** | **Values:** approve §2–§4 and §1.3–§1.4 as drafted, to be **written into the overlay and book-context files when approved**, marked approved design, before the two-packet pilot? | **Yes** |
| **Q-O3** | **Private entry state:** include §1.3's P1–P5 as a writer-only `_private` block, protected from the page? (Alternative: keep `entry_state` to what is on the page, and leave the private truths to the rules and rulings) | **Yes, as `_private`** |
| **Q-O4** | **The title** stays yours; nothing is proposed. (A reminder, not a question) | — |
| **Q-O5** | **Rotation:** add Lucien to B01's derived POV `rotation` as a third entry? Weights stay yours either way | **Yes** (v4.1b gives him point-of-view episodes; the rotation omits him) |

---

## 7. Conflicts and observations

1. **`locations_in_play` names only Bywater**, derived from M01's historical *"Was:"* note
   (*"Notion B1.A1.E1 lantern/Bywater flicker"*). The current M01 is E15's Jackson Square event. The
   derived block is not edited; the entry-state draft uses v4.1b's location grammar instead (§1.3 W8).
   A regeneration will keep deriving Bywater until the grid note changes.
2. **M02's act (A2) and v4.1b's Filament introduction (A1, E09–E10)** are compatible: seeded in A1,
   recognisable in A2. The drafts follow that reading.
3. **The derived POV rotation omits Lucien** (§1.2; Q-O5).
4. **`soft_modulation` LOW** against 12 Life/Reward units (§5.7).
5. **Overlay `basis_note`s use recovered numbering** (§5.3); the A1 widening's target episodes need
   mapping, and recovered E14's FX3 may have no v4.1b content to attach to (§5.2).
6. **v4.1b §6's ECG line** *"41–44: … conceptual wound …"* is to be reworded at EBCI (VAA §3 T6).
   No draft here uses the phrase.
7. **Mechanica §7.1's *"Heavy institutional suppression"*** and v4.1b's *"institutions as footprint"*
   are compatible; the drafts use the footprint reading.
