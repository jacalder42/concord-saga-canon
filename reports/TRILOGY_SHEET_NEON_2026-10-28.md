# NEON (B04–B06): trilogy resolution sheet

**Date:** 2026-10-28. **Status:** analyst sheet, non-canonical, read-only. No novel prose. Every line carries one tag:
**RULED** (author ruling or rule text) · **DESIGN** (approved design, proposal or EBCI, not ruled) · **GAP** (canon silent) · **CONFLICT** (sources disagree; both quoted).

**Source keys** (canon repo paths; `:n` = file line):
REC `proposals/NEON_RECONCILIATION_FOR_EPISODE_ARCHITECTURE_2026-09-27.md` · A4/A5/A6 `proposals/B0{4,5,6}_EPISODE_ARCHITECTURE_PASS3_2026-09-27.md` · P4 `proposals/NEON_PASS4_SURGICAL_2026-09-27.md` · GRID `grids/milestones_payoffs.csv` · BC `grids/breadcrumbs.csv` · TDS `decisions/TAHL_DEATH_SPECIFICS_AUTHOR_ANSWERS_2026-09-27.md` · LCK `decisions/LOOM_CHAIN_KNOWLEDGE_AND_MENDING_COST_AUTHOR_RULING_2026-09-26.md` · LEX `decisions/B01_ELISABET_SIGNATURE_BREACH_LEXICON_AUTHOR_RULING_2026-10-28.md` · COI `decisions/B01_CANON_OPEN_ITEMS_AUTHOR_ANSWERS_2026-10-18.md` · NPA `decisions/NEON_PASS3_MOBIUS_AND_EBCI_PREFLIGHT_AUTHOR_ANSWERS_2026-09-27.md` · NBA `decisions/NINE_BOOK_AUDIT_AUTHOR_ANSWERS_2026-09-27.md` · QSH `decisions/B01_SHAPE_Q_SH_AUTHOR_ANSWERS_2026-10-14.md` · POV `decisions/POV_DISTRIBUTION_TARGETS_AND_TRILOGY_BATON_AUTHOR_RULING_2026-09-26.md` · GOV `decisions/GOVERNANCE_AND_CIVIC_BREAKDOWN_AUTHOR_ANSWERS_2026-10-02.md` · E689 `decisions/B06_B08_B09_EPILOGUE_AUTHOR_ANSWERS_2026-09-26.md` · FT `decisions/FIRST_TEAR_Q_FT_AUTHOR_ANSWERS_2026-10-13.md` · SIL `decisions/B01_SILENCE_CONFIRMATION_AND_RESONANCE_LIFT_AUTHOR_RULING_2026-10-12.md` · DOM `canon/factions/Dominions.md` · TN `canon/trilogy_neon.md` · SO `canon/saga_overview.md` · TEBCI `canon/characters/TahlEBCI.md` · T2 `rules/trilogy_context_T2_neon.json` · BX4/5/6 `book_context/book_context_B0{4,5,6}.json` · MECH `rules/Mechanica-v4.md` · TGD `proposals/TRILOGY_CONFLICT_GUIDE_2026-09-29.md` · CCA `reports/SAGA_CAST_CONFLICT_AUDIT_NEON_B04_B06_2026-09-29.md` · AFM `reports/ANTAGONIST_FACTION_ARC_MATRIX_PASS1_2026-09-27.md` · LED `recovery/RECOVERY_LEDGER_2026.md`.

**Not read:** the project knowledge base docs (`claude/TAHL_REVEAL_ARCHITECTURE.md`, `claude/SAGA_MILESTONE_TIMELINE.md`, `claude/EPILOGUE_STRUCTURE_RULING.md`, `claude/NOTION_01_SAGA_ARCHITECTURE.md`). No Projects tool was available in this session and no copy exists on disk. **GAP in this sheet's coverage**; recheck §6 and §8 against them.

**Overall authority:** all Neon episode architecture is provisional, approved design, Tier B (A4:13, A5:12, A6:14; NPA:17). The rulings inside it are the M-rows marked `ruled` in GRID.

---

## 1. The trilogy's question

| Item | Tag | Finding |
| --- | --- | --- |
| Stated dramatic question | **GAP** | None. TN:1–16 has no question; SO:35 reads *"Neon (T2): TODO"*. No B04–B06 file states one (searched REC, A4–A6, P4, the NEON_* proposals). |
| Stated mystery question | **GAP** | None. |
| Trilogy identity (nearest thing to a premise) | **DESIGN** | QSH:23, 27–30: *Neon is the trilogy in which resonance is "embraced and exploited"*. Veil teaches what resonance is and how it works; Loom is the aftermath. |
| Per-book grammar | **DESIGN** | REC:104–110: B04 *"Grief becomes public argument"*; B05 *"Different systems fail differently, and people choose separate work"*; B06 *"Knowledge does not guarantee prevention."* |
| Lead's thematic function | **RULED** (Tier-1 card) | TEBCI:180–185: Tahl is *"the proof that clarity alone is insufficient"*; *"truth travels — even when the carrier cannot."* |

**Candidates** (analyst's, for the author; built only from the lines above):

| # | Kind | Candidate | Answered where | Grounding |
| --- | --- | --- | --- | --- |
| D1 | Dramatic | Once resonance is public and being exploited, can people who know the truth make the world act on it in time? | **No**, at B06 A3; partial yes by mortal means at B06 EP | A6:26; TEBCI:180; GRID:22 (M38), 26 (M39) |
| D2 | Dramatic (lead) | Can the man who posted the coordinates answer for it? | B06 E18 *"the Warehouse mirror"*; E43 the fragment | GRID:13 (M12 *"B04 opens his remorse arc"*); TDS:26 |
| M1 | Mystery (book-level) | Who or what is altering the people in the public meta incidents? | B05 E08 (an institution); B06 E07 (M17) | A5:53; A6:57; BC:39 |
| M2 | Mystery (trilogy) | What is breaking in the Southwest, and is it linked to the other breaks? | B06 EP E47: linked, several, closed in order, the first one last | BC:12 (southwest ladder from B01); A6:120; GRID:26 |

D1 + M2 fit the material best: both run the full B04→B06 span and both close inside Neon.

## 2. Lead, POV baton, antagonists, theatre, time span

| Item | Tag | Finding |
| --- | --- | --- |
| Trilogy lead | **RULED** | Tahl (SO:25; POV:10, 25; TN:16). Seraphine stays saga lead. |
| POV band | **RULED** (as diagnostic) | ~30/30/30/10, *"diagnostic bands, not quotas"* (POV:10–13, 29–38). |
| POV counts | **DESIGN** | Tahl 10/13/16 episodes, rising across the trilogy; Seraphine 12/12/10 after pass 4 (25% of Neon) (P4:36–42; A4:36, A5:35, A6:36). Seraphine is below the band, accepted as provisional (NPA:35). |
| The baton into Loom | **RULED / DESIGN** | Kade has no public rise before Tahl's death (REC:57; GRID:16 M15 retired). He is introduced as a listener (A4 E12, E43) and takes the baton at the B06 EP grief post (GRID:27, M23 *proposed*; TDS:32). |
| The "link" role in Neon | **DESIGN** (direction) | Rex, Elisabet and Lacuna carry the link that Lucien carries in Veil (`decisions/B01_STANDALONE_BRAID_AND_OPPOSITION_DIRECTION_AUTHOR_NOTES_2026-10-12.md`:13–17). |
| Antagonist pressure, trilogy file | **DESIGN** | *"Technarc hardliners, Choirless emergence, manufactured meta failures"* (TN:10). |
| Dominion | **RULED** M05 / **DESIGN** arc | Caldas delivers Virelli's last direct act, the demand (GRID:6). The Dominion is an arc: a *"rise into overt prominence early in Neon"*, then it *"wane[s] by Neon's end"* (DOM:109–112; GOV:22–25). |
| Technarc / Han Wei | **RULED** names / **DESIGN** rows | Protocol 9 in B04 A2 (GRID:14, M13); the model fails in Singapore in B06 A1 (GRID:19, M17). |
| Choirless (Ito, Saeko) | **RULED** names / **DESIGN** rows | The quieting doctrine in B04 A2 (GRID:15, M14); first overt violence in B06 A2, NOLA (GRID:59, M58; NPA N7). |
| Neon Rebellion / Filaments | **DESIGN** | The crack becomes irreversible in B04 A3 and the networks divide in B05 A2 (GRID:20, M18). *Neon Rebellion* is the officials' and press's word (GOV:32–33). There is no faction card (AFM:52–53). |
| Co-opting "Concord" faction | **RULED** (existence, Neon co-option) | The internal Dominion faction *"co-opts the name 'Concord', when resonance goes public in Neon, and drifts into insincerity … collapses in Loom"* (COI:151–153). See §10. |
| Theatres | **DESIGN** | B04: NOLA anchor, plus Vienna, Chicago and short Detroit/Bristol scenes. B05: parallel theatres (NOLA, Chicago, Reykjavík, briefly Vienna, the Southwest, late Singapore). B06: distributed, with Santa Fe for Tahl alone (REC:106–110). Chicago, Detroit and Bristol are not in the registry (A4:18–19). TN:13 *"Key Locations: TODO"* (**GAP**). |
| Time span | **DESIGN** | B03→B04 is days; B04 runs 2–3 months, B05 3–4 months, B06 1–2 months, B06→B07 several days (NBA:23). Roughly 6–9 months in all. |
| Envelope | **DESIGN** (derived from interim values) | Trilogy: U2–U6, W1–W4, FX1–FX3 (T2:17–30). By book: B04 U2–U5/W1–W3; B05 U2–U6/W1–W4; B06 U3–U6/W2–W4 (BX4:78–89; BX5:73–84; BX6:87–97). |

## 3. Entry load

### 3a. What a reader entering B04 must know from Veil

| Fact carried in | Tag | Re-delivered on the B04 page? |
| --- | --- | --- |
| Baz died rescuing a child at the Warehouse; the cast learns of it at B04's start | **RULED** (GRID:12 M10; BX4:21) | **Yes:** E01 the recovery, S01 the corrected notice (A4:47–48) |
| Tahl's anonymous post of the coordinates (M11) and his private rule | **RULED** (GRID:9, 13) | **Partly:** E07 the public record fight, *"the post drew crowds"*; E13 the rule in action (A4:54, 60). The full confession comes in B05 (N2) |
| Who Baz was to each person (Lucien, Seraphine, Caro, Trip, the sister) | **DESIGN** | **Partly:** E02, E04, E05, E08 (A4:49–55) |
| Seraphine's B03 choice and the household | **DESIGN** | Yes, E09 (A4:56) |
| Helena's favour; Rieux's log; Holt | **DESIGN** | Named, not explained (E01, E23) |
| Rex's Detroit history (B03 E43) | **DESIGN** | Compressed into E06 (A4:53) |
| Caro and Elisabet's first kiss (B03) | **DESIGN** (GRID:8 note) | Shown as *"openly together"* (E14) |
| Seraphine's stabilising ability and its limits | **DESIGN** | Demonstrated by failing (E21, E37) |
| What resonance is and how it works (Veil's job) | **DESIGN** (QSH:27–30) | **GAP:** no B04 episode re-teaches it |
| The circle has split from Baz's funder; Baz was still paid by Dominion | **RULED** cause / leaning B03→B04 (COI:29–32, 154–155) | **GAP:** absent from A4 |

**Could a new reader start at B04?** **GAP:** canon never asks. No Neon standalone evaluation exists; Veil has one (`reports/VEIL_TRILOGY_AUDIT_AND_STANDALONE_EVALUATION_2026-09-27.md`:212–216, whose test is *"a dramatic question early, … a decisive act at the climax, answer the question, … satisfaction rather than only a hook"*).

Analyst reading: B04 is **enterable**. It opens on a death and its fallout (the mourning-opening pattern, `decisions/SAGA_TITLES_WORKING_MAP_AUTHOR_DIRECTION_2026-10-17.md`:58). Tahl is new even to Veil readers, because he has no named POV before the B03 EP (GRID:13). B04 also has its own climax (the Riot). The cost is affective: Baz has to matter to someone who never met him.

### 3b. "Previously" for B05 and B06 (DESIGN; A4:126–136, A5:128–135)

| Entering | Must know |
| --- | --- |
| **B05** | The Filament split is irreversible. Protocol 9 is in force. The quieting movement has a caring face and a loud amplifier. Seraphine is publicly filmed and listed. Lucien is in Vienna with Rieux's log. Tahl is remorseful and has asked to meet. Rex is in the cast as MT's verified source. Kade is in NOLA and has seen the triangle. |
| **B06** | The private channel (Seraphine, Lucien, Caro, Elisabet, Rex, Tahl). The Colorstorm is now weather. The Filaments are divided, and the Choirless hold blocks. Technarc's hardliners are ascendant in Singapore. Santa Fe is credible and ignored. The cast is scattered: Caro in Chicago, Elisabet in Reykjavík, Rex in Singapore, Tahl in the Southwest. Tahl is paying for the Last Clear Act. |

### 3c. Does each book stand alone? (analyst verdict on DESIGN material; canon silent, **GAP**)

| Book | Own climax | Own answer | Verdict |
| --- | --- | --- | --- |
| B04 | The Riot (M16, **RULED**; A4:101) | The grief has become public argument (A4:111). Seraphine *"holds neither yet"* of her two lessons (A4:131) | **Mostly.** The climax is strong; the protagonist's resolution is deferred |
| B05 | **By design no Act III set-piece**; the peak is Act II Chicago (A5:27–29, 126) | M56 and M57 close; Santa Fe becomes credible (E42) | **Weakest standalone.** It ends *"no one can make anyone act"* (A5:110), which is a middle book's hook |
| B06 | Tahl's death (M20, **RULED**) | Tahl's arc closes; the shape is delivered (M39, **RULED**) | **Yes as a culmination.** The Rupture *"persists"* (A6:8–9) and closes in Loom |

## 4. Discovery ladder B04→B06 (Mechanica §7.2)

Rule text, **RULED** (MECH:157–163): *fracture and instability increase; shards emerge; tech disruption becomes common; emotional amplification is visible; extremist misuse escalates consequences; cost curves steepen.*

| Axis | B04 | B05 | B06 |
| --- | --- | --- | --- |
| Phenomenon | **DESIGN:** a bounded aftershock at the sealed site (E15); the first public meta incident (E11); metas stay rumour until B04 (`decisions/NYLA_ARC_AND_VISIBLE_MOMENT_2026-10-25.md`:9) | **DESIGN:** the Colorstorm runs apparition → normalisation → changed meaning and *"gates nothing"* (A5:31–32; GRID:21); the Chicago storm (E22) | **DESIGN:** distributed failure in three theatres (A6 A1). **RULED:** the Fracture, then a persisting Rupture (GRID:22–23) |
| The Veil / VT | **RULED:** no Tahl VT contact in B04–B05 (REC:53) | **DESIGN:** memory only; the Filaments' "wrong" pressure matches his B03 brush (E34; NPA N1) | **RULED:** a late fatal slip; he glimpses the pattern; Silence collects the echo (GRID:23–24) |
| The Wounds | **GAP:** nothing (Santa Fe at most a direction, A4:121) | **DESIGN:** Santa Fe becomes credible through converging data (E42, M38) | **RULED** (M39): the shape (linked, several, ordered, *"the first one has to be last"*). **DESIGN:** Seraphine reads "first" as the swamp (TDS:31) |
| Antagonists | **RULED/DESIGN:** M05, Protocol 9 (M13), the quieting doctrine (M14), the Riot (M16) | **DESIGN:** metas are *"people altered by an institution"* (E08); the hardliners push (E37); the Filaments divide (M18) | **DESIGN:** Technarc's authority breaks (M17); the Choirless use force (M58); a legitimacy break (A6:156–158) |
| Cost curve | **DESIGN:** Seraphine hurts someone (E21) and collapses on film (E37); an elder is injured (E38) | **DESIGN:** smear, burned sources, a throttled channel (E39; GOV:34–37) | **RULED:** Tahl dies |
| §7.2 "shards emerge" | **GAP** | **GAP** | **GAP:** 0 hits for "shard" in REC and A4–A6 |
| §7.2 "tech disruption common" | **DESIGN:** partial (MT throttled) | **DESIGN:** MT throttled (E11) | **DESIGN:** AR failures (REC:87); MT goes black (E40) |

## 5. Per-book resolution

| Book | Question it closes | Tag | Hook it opens | Tag |
| --- | --- | --- | --- | --- |
| **B04** | What will Baz's death turn into in public? Answer: the Riot makes the split material and irreversible (M16; crack E39) | **RULED** M16 / **DESIGN** crack | Tahl asks to meet the people Baz belonged to (E44). Lucien is *"coming back, not yet"* (E45). Kade arrives (E43) | **DESIGN** |
| **B05** | Can commitment survive distance? Answer: yes. M56 (E23), M54 (E26), M57 (E35) | **DESIGN** (rows *proposed*: GRID:55, 57, 58) | Santa Fe is credible and *"no one can make anyone act"* (E45). Tahl carries a warning he cannot source | **DESIGN** |
| **B06** | Will the warning be heeded, and will Tahl make it out? Answer: no and no. M55 → M20 | **RULED** M20 / **DESIGN** M55 | The shape of the chain (E47). The body goes east to the funeral (E46). Kade's voice is read (E48). The official account fails (A6:156–161) | **RULED** M39 / **DESIGN** rest |

## 6. Trilogy resolution at the end of B06

| Thread | Tag | End state |
| --- | --- | --- |
| Tahl's arc | **RULED** M20/M21 / **DESIGN** staging | Remorse (B04) → confession and the Last Clear Act (B05) → he goes *"against the warning"* because *"he will not send others where he will not go himself"*; *"not a chosen sacrifice"* (TDS:26; A6 E18). A live broadcast, then MT goes black (TDS:27). The slip, the glimpse, the fragment by mortal means, death with no principal witness (TDS:28–33). Silence collects his echo (GRID:24). This closes TEBCI:183–185, *"truth travels."* |
| Epilogue | **RULED** M39 / **DESIGN** M23 | Three episodes, E46–E48: the news staggered → the fragment to all five recipients → Kade's grief post, which is read and *"closes Book 6"* (A6:115–121; TDS:29–32; P4:96–111). |
| Faction states | **DESIGN** | Technarc's authority is broken in Singapore and its hardliners are a remnant. The Choirless have used force. The Rebellion is leaderless. Officials' credibility breaks in public (A6:147–148, 163–164). |
| Relationships | **DESIGN** | Seraphine–Lucien together (M57); Caro–Elisabet committed across distance (M56) (A5:133). |
| D1 / M2 (§1) | **GAP** as stated / **DESIGN** answered | D1 is answered "no" by the death; M2 is answered at shape level by the fragment. |

## 7. Left open for Loom or the saga

| Item | Tag | Fair thread or dependency? |
| --- | --- | --- |
| The funeral, opening B07 | **RULED** (REC:93) | **Fair.** The body on the road is a closing image. |
| Kade's succession and the first deliberate post (M40) | **RULED** M41 / **DESIGN** | **Fair.** M23 gives Neon a partial payoff. |
| The particulars of the chain (four Wounds, the order) | **RULED** (LCK:21–33) | **Fair.** Neon delivers the shape; Loom delivers *"confirmation beats"* (LCK:24). |
| The Santa Fe Rupture persists; stabilised only in B08 | **RULED** (A6:8–9; LCK:31) | **Dependency risk.** Neon's central catastrophe ends unclosed. It is defensible only if D1 is the trilogy's stated question. |
| Silence holds the echo → the B09 flare (M52) | **RULED** (GRID:24) | **Fair.** M21 is staged on the page. |
| Hope–Caro (BC:40), Lucien–Silence (BC:41) | **DESIGN** | **Dependency.** Planted in Neon, paid only at the B09 Mending, with no Neon partial payoff. |
| The elders' corridor (BC:43) | **DESIGN** | **Dependency.** It *"sets up Loom's stabilisation"* (A4:104), with no Neon payoff. |
| Lacuna and Kade in the same room (BC:38) | **RULED** cameo only | **Fair** as texture. |
| The co-opting Concord faction's collapse | **RULED** (COI:79–81) | **Dependency, and unplanted.** See §10. |
| The Choirless unresolved | **RULED** (LCK:142) | **Fair.** M58 gives Neon a peak. |

## 8. Saga milestones Neon delivers

| Row | Grid status | Book/act | Episode (DESIGN) |
| --- | --- | --- | --- |
| M05 (GRID:6) | ruled | B04 A2 | E16, E19; return B05 E17 |
| M13 (GRID:14) | proposed (names ruled) | B04 A2 | E17 |
| M14 (GRID:15) | proposed (names ruled) | B04 A2 | E20 |
| M16 (GRID:18) | ruled | B04 A3 | E35 |
| M37 (GRID:17) | ruled | B04, before M20 | B04 E03 name; B05 E05 why |
| M18 (GRID:20) | proposed | B05 A2 | E21 |
| M54 (GRID:55) | proposed | B05 A2 | E26 |
| M56 (GRID:57) | proposed | B05 A2 | E23 |
| M57 (GRID:58) | proposed | B05 A3 | E35 |
| M38 (GRID:22) | proposed (ladder ruled in note, Q7) | B05 credibility → B06 A1/A2 | E42; E15; E16 |
| M17 (GRID:19) | proposed | B06 A1 | E07 |
| M55 (GRID:56) | proposed | B06 A1 | E09 |
| M58 (GRID:59) | proposed | B06 (A2 per N7) | E22 |
| M20 (GRID:23) | ruled | B06 A3 | E42–E45 |
| M21 (GRID:24) | ruled | B06 A3 | E45 |
| M39 (GRID:26) | ruled | B06 EP | E43, E47 |
| M23 (GRID:27) | proposed | B06 EP | E48 |
| Retired: M15, M19, M22 (GRID:16, 21, 25) | retired | — | — |

Owed forward from Neon: 12 hooks out of B06 alone (BX6 continuity_hooks: M40, M24, M26, M27, M28, M45, M30, M32, M52, M35, M59).

## 9. Dependency check

### 9a. Neon payoffs that need Veil setups a Neon-first reader lacks

| Payoff | Veil setup | Severity |
| --- | --- | --- |
| B06 E47: Seraphine recognises "the first one" as the swamp | BC-SWAMP-WOUND, planted at the B01 camp (BC:7) | **High.** The recognition is the trilogy's last private revelation and it is invisible to a Neon-first reader. B06 E05 re-plants the ache *"unnamed and unexplained"* (A6:55), which helps only partly. |
| B05 E34 / B06 E42: the pressure *"matches what he felt in B03"* | BC-VT-BRUSH-LADDER, B02–B03 brushes (BC:5) | **Medium.** It is memory only, and Neon has to show the B03 brush again. |
| The triangle (B04 E33, E43; B06 E39) | Every MT post from B02 (BC:3; NBA:25) | **Low.** Neon re-introduces it. |
| Tahl's remorse and the B05 meeting | M11, the post (GRID:9) | **Medium.** B04 E07 re-delivers the public version. |
| B04 E05's missing second line; chorba | BC-SECOND-LINE-INVITE, BC-CHORBA (BC:30, 33) | **Low.** It is grace notes. |
| B04 E01: Helena's favour; E23: Rieux's log | B03 E44, Warehouse record (BC:18) | **Medium** for B04 A1 clarity. |

### 9b. Neon setups that pay off only in Loom, with no Neon partial payoff

BC-HOPE-CARO (B05 E26 → B09) · BC-LUCIEN-SILENCE (B06 E08 → B09) · BC-ELDERS-CORRIDOR (B04 E38 → B08) · BC-TAHL-PARENTS (B04 E22 → B07 funeral; Neon has E35's call as a partial) · BC-FIRST-ONE-LAST (B06 E47 → B09; the plant is itself a Neon payoff of the channel) · the persisting Rupture (→ B08). All **DESIGN** except the Rupture (**RULED**).

## 10. Gaps and conflicts

| # | Tag | Item |
| --- | --- | --- |
| 1 | **GAP** | No trilogy dramatic or mystery question (TN:1–16; SO:35). |
| 2 | **GAP** (stale vs Oct) | **The Concord co-option is missing from Neon.** COI:151–153 rules that the faction *"co-opts the name … when resonance goes public in Neon"*, and that the network and the faction *"collide"*. "Concord" appears 0 times in A4–A6 or REC. The Neon book of the first co-opted use is OPEN (COI:184–185). This is also the missing TGD:49 middle (*"Factions offer things the characters actually want"*). |
| 3 | **GAP** (stale vs Oct) | **The split at Baz's death is not staged.** COI:154–155: *"The circle learning this around his death (end of B03) is the cause of the split"*, with the exact book OPEN (COI:31; BX4:212). A4's entry state (A4:29–32) and E01 (A4:47: *"a debt to the Dominion"*) predate it. Helena is a possible faction member (COI:161–162). |
| 4 | **CONFLICT** (soft) | **Elisabet's open money vs her route.** COI:197–205 (**provisional**): *"Elisabet brings in open, public money … It gives Elisabet a reason to stay in New Orleans."* A5:55, 74 (**DESIGN**): she leaves for Reykjavík in B05 and stays there through B06 (A6 E41). The money arrival book (B04 by leaning) and terms are not ruled (COI:213–215). The architecture has no funding beat. |
| 5 | **CONFLICT** | **The Dominion arc vs the architecture.** DOM:109–111: *"rise into overt prominence early in Neon … then wane by Neon's end."* The architecture puts the Dominion in B04 E01, E16 and E23 only; after M05 Virelli is *"outgrown"* (GRID:6 note). CCA:222 (B04-8) flags *"Currently the ladder stops after one demand."* |
| 6 | **CONFLICT** | **How many Wounds the message gives.** LCK:24 (**RULED**): *"Tahl's B06-epilogue message gives the crew the shape (four wounds, Honey Island last)."* TDS:31 (**DESIGN**) and A6:120: *"there is more than one … No place is named except where he stands."* Either the count of four is stated, or LCK:24's "four" is the crew's later inference. |
| 7 | **CONFLICT** (stale vocabulary) | LEX:17 reserves **Wound** (capital) for the four (also MECH:891). Neon texts say *"tears"* (A6:120; BC:42) and *"wound pattern"* (GRID:23, 26). The lexicon has to be applied before Neon EBCI. Santa Fe is Wound 1. Fracture and Rupture stay M38's terms. |
| 8 | **CONFLICT** | **What Seraphine recognises.** BC:7 plants the swamp wound *"at the camp (B01 E01-E02)"*. LEX:15 classes the camp as a **breach**, not a Wound, and LEX:48 says *"the camp is not the origin"*. FT:22 says the camp's link to Honey Island is *"allowed later"*, OPEN. TDS:31's *"recognises 'the first one' as the swamp"* therefore lacks a ruled B01–B03 referent. |
| 9 | **GAP** (risk) | SIL:36–39 lets Caldas say *"the first one"* in B01, with no guard. That can collide with Tahl's line. |
| 10 | **GAP** (stale vs Oct) | MECH:153 now makes Veil *"escalating, physically consequential, increasingly measurable"*. Neon's §7.2 escalation has to clear a louder Veil, yet Neon has no shards (§4) and B05 A3 has no set-piece by design (A5:27–29). B05's envelope maxima equal B06's (BX5:73–84; BX6:87–97). |
| 11 | **CONFLICT** (resolved, stale doc) | E689:57 leaned toward *"the very end of Act II"* for M20; GRID:23 (Q7) rules the end of A3. Only the older doc is stale. |
| 12 | **CONFLICT** (record) | Who originates the warning: TDS:46 *"still open"* and GRID:22 note (Q7) *"stays OPEN"* vs NPA N1 (**DESIGN**, same day, later): the Filaments originate it and Tahl relays it. |
| 13 | **GAP** | The Brightbreak handle is due in late Neon (`canon/factions/Brightbreak.md`:91–95; AFM:105) and has no episode (REC:59, *"at most"*). |
| 14 | **GAP** | The Neon Rebellion has no faction card, and its B06 state is *"?"* (AFM:52–53, 106). A6:148 calls it *"leaderless"*. |
| 15 | **GAP** (pending pass) | CCA:23–50 finds *"The protagonists are always right"* and *"Separation is used as friction avoidance"*. It proposes 24 Neon fixes (e.g. B05-1 the room splits; B06-1 the collision over Tahl's going: CCA:228, 246). These are allowed by Q-CE4 (`decisions/SAGA_CAST_CONFLICT_PASS_AUTHOR_ANSWERS_2026-09-29.md`:22) and none is applied. |
| 16 | **GAP** | TN:7 (escalation) and TN:13 (locations) read TODO. The book titles are TODO (BX4–BX6:5); *Neon Wake* and *Neon Riot* are open. |
| 17 | **DESIGN** (accepted deviation) | Seraphine is at 25% of Neon against the ~30% band (P4:38; NPA:35). |
| 18 | **GAP** | There is no Neon standalone audit (cf. the Veil audit, §3). |
