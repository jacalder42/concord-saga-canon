# LT and the post-Mending end state — audit (D15, D16)

**Date:** 2026-09-27
**Status:** EDITORIAL REPORT / NON-CANONICAL. It is the deferred pass the author approved with
*"Proceed with deferred passes"*, for **D15** (post-Mending `res_states`) and **D16** (LT access
beyond Kade) in `decisions/OPEN_QUESTIONS_AUTHOR_ANSWERS_2026-09-27.md`. It rules nothing and edits
no card, rule, row or ruling. §7 puts the questions, with recommended answers.

> **Answered 2026-09-27** (`decisions/LT_POST_MENDING_END_STATE_AUTHOR_ANSWERS_2026-09-27.md`, ledger §180): *"Proceed as recommended."* All six as recommended, **approved design**. The Q6 fixes are applied; Q1 and Q4 carry pointer notes only, pending a ruling. The body below is unchanged.

**What it does not change:**

- `rules/era_context_post_mending.json` stays unwritten and held.
- `canon_rules.json`, the channel rules, Mechanica, the cards and the grid are untouched.
- The deferral's caution stands: **LT must not become a communications system.**

**Scope, set by the author:** *"Post mending is only the epilogue don't expand it too much"*
(2025-11-27, *Narrative Structure* l. 13573). This audit settles only what the ending, the
envelope and the cards need. It does not design a post-Mending world.

**Method:** a read-only pass over the channel rules, Mechanica §7.4, §33, §36–§44 and §42A,
Resonance §18, the epilogue and LT rulings, the recovery files, the cast cards, M33–M35 and M53,
the B09 A3 overlay, and the two envelope and channel proposals. It also searched the export for
the author's own words on LT. Export paths below are in `sources/chatgpt_export_2026-09/`.
*NS* = `2025-11-27__Narrative_Structure__69286516.md`; *PC* =
`2025-11-10__Prompt_crafting_types__69114878.md`; *WB* = `2025-12-01__Worldbuilding__692dc2fb.md`. The key quotes were re-checked against the
export by line.

---

## 1. The key finding: the author called LT VT's successor

Two author statements say that **LT succeeds VT**. No repository document cites either:

| Date | Where | The author's words |
| --- | --- | --- |
| 2025-11-29 | NS l. 75231 | *"…then Kade with MT, then post Mending VT converted to LT (LuminousThread)"* |
| 2025-12-11 | `2025-12-10__Character_Vault_Chat__6938daf6.md` l. 45843 | *"MT = MissingThread, which is Tahl's public channel / VT = VeilThread which is the metaphysical back channel / LT = LuminousThread the successor to VT"* |

The 12-11 line is a definition the author wrote to correct drift. Two bibles the author pasted say
the same: *"VT becomes LT"* (`2025-11-29__Create_memory_list__692ae65d.md` l. 792;
`2025-12-01__Worldbuilding__692dc2fb.md` l. 5364). Those are assistant documents the author chose,
not his own prose.

**Against them, the current rules:**

- `LT_RULES_POST_MENDING.md` §1: *"LT is not an upgrade to VT. LT is a different channel
  entirely."*
- `VT_RULES.md` §9: *"VT persists as boundary contact … VT does not evolve into LT."*
- Mechanica §36: *"Channels never merge."*

Both channel rule files are assistant-built. `LT_RULES` is headed *"Source: Project Memory … Phase
1A Migration"*. Under the precedence rule in CLAUDE.md §5 (C3, rule 2), **the author's own words
beat accepted assistant text.** That does not make this a choice Claude can make: the rule files
are substrate, and changing them is destructive.

**One reading reconciles both, and it is offered, not chosen.** *Successor* need not mean
*conversion*:

- **VT closes at the Mending.** VT is Silence and Hope's back channel. At the Mending they
  disperse into the veil's laws (§42A.3), so its two parties are gone.
- **LT opens.** It is a new channel, as `LT_RULES` §1 says, and it takes over VT's place as the
  one metaphysical channel.
- **Channels still never merge** (§36). One ends and another begins.

Under this reading, `VT_RULES` §9 (*"VT persists"*) is the line that would change. §7 Q1 asks.

---

## 2. D15: which resonance states exist after the Mending

| State | The sources | Reading |
| --- | --- | --- |
| **CALM** | Mechanica §33; §39 *"Civilians perceive only calm or clarity"* | **Permitted.** Uncontested |
| **BLOOM** | §33 has no era gate; §7.4 *"Resonance still costs"*; Resonance §18 *"escalation halts at NODE"*. Against: the envelope proposal sets escalation to *none*; assistant WB l. 97329 has no Bloom corridors (unratified) | **Permitted, bounded.** M34 leaves *"residual hazard"* open, and §42 says filtration does not *"Guarantee safety"*. A world with no BLOOM would be the utopia the author rejected (*"not utopian"*, WB l. 100136) |
| **NODE** | §33 *"Post-Mending replacement for shards"*; §7.4 *"Only Echo Nodes remain"*; §43; `canon_rules.json` `post_mending.NODE_ECHO` | **Permitted.** Uncontested |
| **SHARD** | Forbidden by §7.4, §41, §44 and Resonance §18 | **Forbidden** |
| **RUPTURE** | Forbidden by §40, §44 and Resonance §18 | **Forbidden** |
| **VT** | For: `VT_RULES` §9 and its header, *"persists post-Mending"*. Against: the author's §1 statements; Silence and Hope's dispersal | **Depends on Q1** |
| **LT** | §33; `LT_RULES` *"Post-Mending World Only"*; M53 (ruled) requires it | **Permitted.** Omitting it makes the ruled ending illegal (ledger §18) |

**The two proposals on file** differ only by the channels:

- `proposals/concord-2026/ENVELOPE_INTERIM_VALUES_V2…` proposes `CALM · BLOOM · NODE`.
- `proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md` proposes
  `CALM · BLOOM · NODE · VT · LT`. It also offers to move the channels out of `RES` into a
  separate contact field. That would dissolve ledger §18's dilemma, but it changes the ECID schema,
  and it is not recommended now.

**A wrinkle for the era file:** the envelope proposal permits corridors U1–U7, which include U6
*Shard-Laced* and U5 *Bloom*, while it forbids SHARD as a state. When the era file is written, the
corridor list needs the same check.

**Weather:** Mechanica §44 says *"Resonance storms are filtered into weather"*. M34's *"measured
regions and intervals"* argues for easing over time rather than an instant W0–W1. The epilogue is
days after the Mending (D10, ruled), so it sits early in that easing.

---

## 3. D16: LT access, candidate by candidate

The ruled ending (`decisions/SAGA_MILESTONE_GATE_AUTHOR_RULING_2026-09-26.md`, answer 5) is
*"Seraphine reaches out to the survivors"*, plural. The author also wrote, hedged and not ruled: *"I
think the protagonist survivors are able to use LT much like Tahl and VT"* (same file).

**The analogy argues for rarity, not routine use.** Tahl's VT contacts are four across the whole
saga (A11, ruled), and VT *"Never broadcasts"* (Mechanica §33). *"Much like Tahl and VT"* reads as
rare, costly, bounded contact. It does not read as a channel people use.

| Candidate | Evidence | Reading |
| --- | --- | --- |
| **Kade** | Access **ruled** (§39). What access is, is not ruled. The author, 11-29: *"Then a simple log prompt for LT left open"* (NS l. 87678). The author, 12-07: *"the epilogue closes with Kade getting a message request for the LT"*. In the accepted 11-30 skeleton, an assistant text, Kade **accepts** (*"Okay. One more thread"*). `KadeEBCI.md` still says *"(no agency)"* | The author's own words are **receipt, with the prompt left open**. The acceptance is accepted assistant text, which the author's words outrank (C3, rule 2). *"(no agency)"* is the assistant's 11-29 framing. The reading that fits both: **Kade can answer; the saga ends before he does** |
| **Elisabet** | No card grants LT. She is the ruled Mending witness (M33). The author's 11-15 design has her and Rex *receiving* an LT notification (PC l. 92969). The assistant's perception tiers (WB l. 99443) are unratified | **Can be reached; off the page.** Being reached by the trio fits *"reaches out to the survivors"*. Nothing requires her to use LT |
| **Rex** | `RexEBCI.md`: *"Rex remains non-metaphysical … reliability, not transcendence"*. Otherwise as Elisabet | **Can be reached; off the page.** Receiving a reach does not make Rex metaphysical, so his card holds |
| **Lacuna** | `LacunaEBCI.md`: *"Not accessible … clarity hum only; no agency"*. The author: she *"shouldn't mention the thread"* (NS l. 87935). M53 leaves *"whether Lacuna perceives it"* open | **Feels the clarity, not the reach**, as the LT access ruling already reads it. Her stars line is the civilian experience of LT |
| **The trio** | Seraphine is the Loom: *"Its reach through LT is invitation, never instruction"* (§42A.4). Lucien and Caro are the guides (§42A.3; M33). The accepted 11-30 skeleton: *"Tahl is the conduit on Kade's side; Seraphine/Lucien/Caro on the other"* | **The reaching side.** They are not survivors in the access question |
| **Tahl's echo** | The conduit (ruled). `TahlEBCI.md`: *"Echo may interface lightly post-death only"* | **The conduit, not a party** |
| **Civilians** | Indirect only: calmer, clearer emotional ground (`LT_RULES` §2; §39) | **Uncontested** |

**"More tangible than VT"** (the author, 09-26: *"Tahl becomes the conduit which enables LT to be
more tangible than VT was"*) conflicts with `LT_RULES` §8 (*"VT remains sharper. LT remains
softer."*) only if it describes LT in general. **The author ties it to Tahl as conduit.** The one
ruled tangible event is the device-borne handshake, through the §6 exception. The narrow reading:
**LT is soft; the echo-borne reach is tangible.**

---

## 4. The post-Mending world, as far as the epilogue needs it

- **Stable, not utopian** (Mechanica §7.4; the author, WB l. 100136). Filtration does not
  *"Guarantee safety / Resolve trauma"* (§42). LT does not prevent *"conflict / grief / human
  error"* (`LT_RULES` §9).
- **Humans slowly adapt**, and the cycle of caps ends (§42A.5; M34).
- **MT continues** under a new MT-initialled name (ruled; the name is deferred, D12). Kade's first
  post-Mending post is on MT.
- **Reconstruction:** Elisabet, Rex and Kade (ruled), with Kade on the rebellion's people. The name
  is deferred (D11).
- **Factions:** Brightbreak dissolves; Elias survives, never unmasked, with at most one epilogue glimpse; the Dominion is
  *"outgrown"*; Technarc is obsolete; the Choirless ideology does not recover; the Filaments
  persist, relieved. The remnant's and the Choirless's end states stay with B09 architecture (D18).
- **Not recommended:** the assistant's *"POST-MENDING CANON v1"* (WB l. ~96782–109420). It is
  unratified, and the author said it *"will not be needed for a long time"* (WB l. 127629).
  `canon/saga_overview.md`'s *"Post-Mending Snapshot"* can stay TODO.

---

## 5. Defects and loose ends found

These are recorded, not fixed. Fixing any of them edits substrate, so each waits for the author.

1. **A stale note in `rules/canon_rules.json`.** `_thread_note` still describes the MT channel as
   *"passed to Kade, renamed LT"*. That was the author's 11-22 idea (*"Originally MT I thought was
   converted to LT"*), and M35 supersedes it: *"A rename, not a channel conversion."* **Fix:** a
   dated supersession note beside it, keeping the original.
2. **A wrong citation in Mechanica §42A.5.** *"Humans exposed to filtered resonance slowly adapt
   (§44)"*: §44 says nothing about adaptation. The source is M34 and the Mechanica Q5 answer
   (`decisions/MECHANICA_HARD_CAP_BREATHING_VEIL_AUTHOR_ANSWERS_2026-09-27.md`). **Fix:** change
   the pointer. §42A is ruled rule text, so even a pointer change is put to the author.
3. **Who enforces the safeguards.** `LT_RULES` §9 says *"LT enforces: no new shards / no rupture
   events"*. §42A.3 says the veil's laws *"apply themselves"*, and `LT_RULES` §4 says *"LT is not a
   system"*. **Fix:** reword §9 to *"After the Mending, the veil's laws prevent …"*, with a dated
   note.
4. **"Post-Mending anchors"** in `LT_RULES` §2 is undefined, and the file flags it. The locked
   Finale Phase Map calls Lucien and Caro the *"Two Anchors"*. **Reading:** it means the guides,
   not the survivors.
5. **Lucien's and Caro's post-Mending card lines.** `LucienID.md` (*"discipline remains
   human-rooted, not mystical"*) and `CaroID.md` describe ordinary human lives after the Mending.
   That sits uneasily with their becoming the guides (ruled). **Flagged for a later card pass**,
   not fixed here.
6. **The entity's name and `Concord-Limits.md`.** The author finds *Concord* plausible for what the
   reconstruction becomes. `Concord-Limits.md` says *"Concord dissolves / no successor organization
   forms"*. **This belongs to D11, which stays deferred.** It is recorded so D11 is answered with
   it in view.

---

## 6. What was checked and is consistent

- The Möbius close, the night sky, Lacuna's stars line and the triangle (ruled, M53).
- Tahl's echo as conduit (ruled) and the §6 handshake exception (accepted).
- The timeskip of a few days (D10, ruled). It matches every author statement from 11-30 on.
- Kade's reconstruction role (ruled) is an MT and civic role. It does not need LT agency.

---

## 7. Questions for the author, with recommended answers

1. **Does VT continue after the Mending?**
   - **(a)** VT persists beside LT, as `VT_RULES` §9 says now.
   - **(b) Recommended: VT closes at the Mending, and LT succeeds it as a new channel.** Channels
     still never merge. This follows your 11-29 and 12-11 words (§1). It would amend `VT_RULES` §9
     and the *"persists post-Mending"* header, with dated notes keeping the old text.
   - (c) LT is VT converted. **Not recommended:** it breaks Mechanica §36.
2. **Post-Mending `res_states` (D15).**
   - **Recommended, if Q1 is (b): `CALM · BLOOM · NODE · LT`.** SHARD and RUPTURE are forbidden,
     not merely unlikely. BLOOM stays, bounded: escalation halts at NODE.
   - If Q1 is (a): `CALM · BLOOM · NODE · VT · LT`.
   - **Recommended in either case:** the era file stays held until B09 episode work, and its
     weather eases over time (M34) rather than starting at W0–W1.
3. **LT access beyond Kade (D16).**
   - **Recommended: the survivors can be reached, and none uses LT routinely.** Kade (ruled),
     Elisabet and Rex can **receive** the trio's reach, rarely, through Tahl's echo. It is felt, not
     read: no information passes beyond the §6 handshake. **Only Kade's is on the page.**
   - **Lacuna feels the clarity, not the reach.** Her card stands, and M53's open point closes that
     way.
   - Not recommended: routine two-way use, which makes LT a communications system; or no access
     beyond Kade, which narrows *"reaches out to the survivors"* to one.
4. **What Kade's access consists of.**
   - **Recommended: he can answer, and the saga ends before he does.** The prompt is left open, as
     you wrote on 11-29 (*"a simple log prompt for LT left open"*) and 12-07. The accepted 11-30
     acceptance beat (*"Okay. One more thread"*) is not used.
   - `KadeEBCI.md`'s *"(no agency)"* would be replaced by *"can answer; the prompt is left open"*,
     with a dated note keeping the old text.
5. **"More tangible than VT."**
   - **Recommended: it describes the echo-borne reach, not LT in general.** LT stays softer than VT
     (`LT_RULES` §8). The handshake is the tangible exception, because Tahl is the conduit.
6. **The loose ends in §5.**
   - **Recommended: yes to 1–4** (the `_thread_note` supersession note; the §42A.5 pointer; the
     `LT_RULES` §9 rewording; *"post-Mending anchors"* read as the guides).
   - **Items 5 and 6 wait:** the Lucien and Caro card lines for a card pass, and the Concord name
     for D11.

**Answer format:** for example *"1b, 2 yes, 3 yes, 4 yes, 5 yes, 6 yes"*. The answers are
**approved design** unless you say *ruled*. Q1 and Q4 change rule and card text, so for those a
*"ruled"* is what lets the edits go in.
