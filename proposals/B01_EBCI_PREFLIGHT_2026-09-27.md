# B01 EBCI preflight

**Date:** 2026-09-27
**Status:** PREFLIGHT / PROPOSAL — NON-CANONICAL, **non-narrative only**. Asked for in
`decisions/PROGRESSIVE_RESOLUTION_SEQUENCE_AUTHOR_INSTRUCTION_2026-09-27.md` item 6: *"template/schema,
causal-card requirements, physics/effects/conflict-code questions, envelope requirements and
production/validation workflow. Do not release the B01 EBCI hold or generate B01 EBCI yet."*

**What it does not change:**

- **The hold stands.** No packet is generated and no pilot runs. There is no `ebci/` directory, and
  no template is installed in `templates/` (the draft is Appendix A).
- No rule, card, envelope, overlay or grid is edited. Every recommendation waits for the author.
- **The release decision comes after the nine-book audit** (the same instruction, item 7).

> **Answered 2026-09-27** (`decisions/NEON_PASS3_MOBIUS_AND_EBCI_PREFLIGHT_AUTHOR_ANSWERS_2026-09-27.md`, ledger §201): *"preflight 1-8 yes"*, approved design. No rule text changes; the hold stands. Pre-release work now approved: the B01 overlay drafts (Q6) and the four causal cards (Q7). The body below is unchanged.

**Sources:** the EBCI readiness report (`reports/B01_INTEGRATED_SYSTEMS_STRESS_AND_EBCI_READINESS_2026-09-23.md`)
and its three reconciliation proposals (physics R1–R8, VFX V1–V7, conflict); the event observation
ruling (`decisions/B01_EVENT_OBSERVATION_AUTHOR_RULING_2026-09-23.md`, D1–D7); the gate ruling
(`decisions/B01_E19_EBCI_GATE_AUTHOR_RULING_2026-09-25.md`); `rules/canon_rules.json`;
`tools/validate_canon.py`; v4.1b; the Veil audit amendments §3–§4.

**Label collisions to keep straight.** D5 is both the causal-physics hold (09-23) and an unrelated
09-27 answer on Kade. B1–B5 are question ids, not books. V1–V7 (VFX) are not V01–V08 (the Veil
refinements). U1–U7 are corridor intensity, not blockers. **In this document D5 always means the
causal-physics hold.**

---

## 1. Where B01 stands

| Area | State |
| --- | --- |
| **Architecture** | v4.1b: prologue, 48 episodes, 6 supplements; narrative order locked; amended for EBCI by the Veil audit (§3, §4 governs) |
| **The gate** | The hold is the only gate (09-25). *"Supersession is not release."* Episodes that may be generated: none |
| **The readiness report's four rulings** (physics; VFX; conflict codes; U1–U7 in metadata) | **None answered.** Two parts are overtaken by later rulings (§3) |
| **Private causal cards** | **None complete.** Every B01 card is a candidate or on hold; the E15, E33 and E48 verdict is *"causal EBCI ready: NO"* |
| **Template** | **None in the repo.** The only one is a Tier D 12-09 source, which the author answered *"Hold until released"*, and which conflicts with current canon (an FX1 default, a retired term) |
| **Envelopes** | A1–A3 bands exist (corridor, weather, FX only). **The prologue envelope (ruled) and the A1 widening (design) are not applied**, as ruled: both apply *at B01 EBCI* |
| **Validator** | Knows nothing of EBCI. It checks ECID fields and vocabulary on any CSV that carries them. **No BID, POV or per-episode band check** |
| **Sudowrite packet** | Only CLAUDE.md §9 step 6 and a 09-19 workflow proposal |

## 2. What an EBCI packet is (working definition)

**EBCI is the episode-level production packet**: the most detailed layer above prose, built from the
episode architecture, which a smaller Sudowrite packet is later derived from. The sources expand the
acronym four ways; the most frequent is ***Episode Beat Content ID***. (The antagonist cards'
*"Environmental / Behavioral / Corridor Interface"* and the Tier-1 *"EBCI CANON"* card suffix are
different uses of the same letters.)

**It must stay optional where the story is.** From the readiness report's entry contract: *"'Optional'
is real: life, pleasure, work and grief scenes may have no Resonance effect or active opposition. EBCI
should not become a machine that inserts an anomaly and a C score in all 48 episodes."*

The draft schema is **Appendix A**. Its shape:

1. **Header**: SID, working title, POV, place, act position.
2. **ECID block**: the nine fields, single end-state values, the original string kept in notes
   (decisions §1.3, §1.5). **Machine-checked.**
3. **Episode contract**: story job; objective; opposition or constraint (or *none*); the turn;
   consequence; unresolved issue; reader reward or relief; chronology guard; exit condition.
4. **Beats**, each with a BID (`{SID}-BTnn`).
5. **Event record**, **only** for an episode with a physical Resonance event: it points to that
   event's private causal card and records the observation class of each sensory claim.
6. **Obligations**: breadcrumbs by `BC-` id; continuity; protected reveals; the audit amendments
   that apply.
7. **Exit state.**

## 3. Physics, effects and conflict codes: what is still open

The readiness report named four ruling groups as **"essential before drafting any packet with a
Resonance event."** Later rulings answered parts of them.

| Item | Proposal | State now |
| --- | --- | --- |
| **R1** | RP = Will × Emotion × Intent as a **qualitative potential model**; load, skill, pressure and environment are separate constraints on realised output | **Open** |
| **R2** | Controlled output vs stored load and leakage | **Answered in substance** by the meta ruling (Mechanica §48, three-part model). Its general statement for B01 events stays with R1 |
| **R3** | The meta battery | **Answered** (ruled 09-27) |
| **R4** | Thread names | **Answered** (C1, C2) |
| **R5** | Corridor *class* and shard *severity* are separate axes; quarantine the old *"safe to dangerous corridor"* definitions | **Open.** Note: U1–U7 **is** the ruled intensity scale in the ECID `CORRIDOR` field (Ruling 2), and the prologue envelope is U7 (B1). Only the old *class* definitions are quarantined |
| **R6** | A private scene record of cause, coupling, effect, limit, cost and residue; **an observation class on each sensory claim**: objective, attuned, subjective, metaphor (`OBJ` · `ATT` · `POV` · `MET`) | **Open** |
| **R7** | Breath, grounding and empathy **contribute to regulation, coordination and consent**; they are never automatic repairs. Bleed and attunement are fallible. No mind reading | **Open.** Consistent with §42A's ruled *"empathy is a responsive medium, not a virtue gate"* |
| **R8** | Colour and geometry tables are conditional tendencies, mediated by light, material and POV | **Open** |
| **V1** | The four VFX pillars are a presentation palette | Open |
| **V2** | Colour is not a detector of emotion, truth or Intent | Open |
| **V3** | Veil geometry is perspective, reflection or optical misregistration; impossible geometry unapproved | Open |
| **V4** | Technology cannot carry VT or LT | **Current** |
| **V5** | FX2 in Veil is a **default**, not a ban | **Current in effect** (trilogy context; the validator does not treat FX as a ceiling). The mapping is open |
| **V6** | Quarantine self-emitting VT light, topological travel and levitation | Open (a hold is acceptable) |
| **V7** | Witnesses may misread | Open |
| **Conflict codes** | **Quarantine both C ladders** (the November C0–C4 and December C0–C5 give the same numbers different meanings). The packet's conflict brief is plain words: *objective · opposition/constraint · decision/turn · consequence · unresolved issue*. Tier 0–5, M1–M5 and Resolution A–E are optional descriptors. Retire "True/False conflict". Never copy a C number into `reader_pressure.csv` | **Open** |
| **U1–U7 in B01 metadata** | Conservative path: ordinary locations; only defined weather, load and FX fields; U category unresolved rather than invented | **Open.** R5's note applies: `CORRIDOR` is a required ECID field, so the packet needs a U value. The recommendation (Q2) is to use the ruled intensity scale and nothing else |

**D1–D7 of the 09-23 observation ruling still bind:** E15 is undeniable as a many-witness incident,
though its cause may stay disputed (D1); the thrum and the E33 window shudder are **trials only**
(D2, D4); **causal physics is held until each retained effect has a private medium, limits, cost,
residue and a plausible competing explanation** (D5); E48 needs a *"positive, independently checkable
but quiet"* observation (D6); no automatic sorting (D7).

## 4. Causal-card requirements

### What a card must contain

The D5 minimum, extended by the eight-question contract and the docket's row format:

| Field | Question |
| --- | --- |
| Action and baseline | Who does what, with what ordinary skill, before anything happens? |
| Pressure / trigger | What sets it off, here and now? |
| Medium and coupling | Through what material (air, water, glass, metal, structure, bodies, crowds) does it act, and why here? |
| Objective change | What exact, bounded, observable thing changes? |
| Observation class | `OBJ` / `ATT` / `POV` / `MET` for each claim, and who can check it |
| Limit / failure | What it cannot do; where it stops; what fails |
| Ordinary alternative | The plausible competing explanation, and what evidence would disconfirm the leading one |
| Cost | Who pays, and in what kind: ordinary, deliberate action, ambient, social |
| Residue | What trace remains, and how it is independently checked |

**The design fork stays open** (the 09-23 coupling review): ambient pressure with material coupling
(its recommended hypothesis), directed action, ordinary co-occurrence, or metaphor. **Mechanica §42A.2
now rules the ambient case at saga scale**: stored pressure breaking through weak points produces the
shard ladder. No ruling applies it to a specific B01 medium.

### Which B01 episodes need one

The readiness report lists beats needing *"a private mechanics card"*. **Not all of them need a
physics card.** Triage:

| Kind | Episodes | What the packet needs |
| --- | --- | --- |
| **Physical event: full causal card** | **E15** (the first civic event), **E33** (the predicted pulse), **E45** (the rebound, `B1-45A`), **E48** (the quiet predicted event) | A completed card per §4, before the packet |
| **Perception without physics** | **The prologue** | A card on **whose perception** is presented and what the reader may know; the PR envelope; no LT motif (macro-Möbius card §4) |
| **Evidence and prediction** | E20, E25, E27 | Which independent observations predict a **limited** window, and the error bars. Data, not physics |
| **Observation notes inside the packet** | E01–02, E04–05, E07–08, E13, E29, E32, E34, E43, E44 | An observation class and ordinary sources for each sensory claim. **E44 may stay unverified wonder** (the evidence ledger's B1-E7 recommendation) |
| **Institutional and civic** | E23, E38–E41 | An event card without physics: who decides, what capacity fails, what the consequence is. **E23: Technarc stays ambient** (Veil audit T5) |

**E48 has moved since its observable was proposed.** The E48-OBS candidate (lights at small scale,
re-ranked to a conditional backup) predates *"arrive together, and carry one"* (approved 09-27). D6
still requires a positive, independently checkable, quiet observation. **It should be re-chosen
against the new E48**, where the payoff is a steadied stranger and a bodily cost.

## 5. Envelope requirements

| Requirement | Authority | What release needs |
| --- | --- | --- |
| **The prologue's own envelope**: `S1.T1.B01.PR.E00`, U7/FX3 metaphysical permitted | **Ruled** (B1); *"applied at B01 EBCI"* | **Where it lives.** Recommended: an overlay file for the `PR` position (`act_overlay_S1_T1_B01_PR.json`), checked by `CHK_BANDS`. `PR` is a structural position, not an act (Ruling 6), so the file must not count toward the 27 acts |
| **The A1 band widens** to W3 and FX3 at E13–E14 | Design (B2); *"at B01 EBCI"* | Declared `exceptions` on A1 with SIDs, per Ruling 5 (soft ceilings, declared breaches). **Map the recovered labels first**: E13/E14/E16 in the recovered packets are not v4.1b numbers (B4 ruling) |
| **RES, HEAT, LOAD and MODE** | No band exists for them | **Not required.** They are validated by vocabulary. HEAT's trilogy range is H0–H4. Recommend no new bands for B01 |
| **Overlay fields still `TODO`** (A1–A3): `act_thesis`, `deltas`, `act_success_criteria`, `forbidden_shortcuts`; book title; POV weights; entry state | The book context and overlays | **Before the pilot.** Claude can draft them from v4.1b and the audits **as a proposal** for approval. POV weights stay the author's (Ruling 9) |
| **The trilogy container** | T1: U1–U5, W0–W3, FX2 default, one declared exception (B03 A3 E14 W4) | **B03's exception SID uses old numbering**; re-map it when B03 reaches EBCI |

## 6. Production and validation workflow (proposed)

**Per episode:**

1. **Inputs:** the v4.1b episode; the Veil audit amendments (§3 notes, §4 governs); the breadcrumb
   rows whose locators name it; the B01 notes checklist (Appendix B); the relevant causal card.
2. **Draft the packet** to the template.
3. **Mechanical checks** (the validator, extended, §6.1).
4. **Editorial checks:**
   - the Veil execution tests (discovery accumulates; a variety of pleasure and want; duration);
   - Life/Reward stays ordinary;
   - no mechanics explained in dialogue (Mechanica §60);
   - the five editorial checks in `rules/validation_checks.json`.
5. **Author review** by act, not by episode.
6. **Lock.** Only then is a Sudowrite packet derived, and **never raw EBCI** (CLAUDE.md §9 step 6).

**After release, first:** a **two-packet pilot**, as the readiness report's step 3 asks: **one event
episode** (E33 is the natural choice: its window shudder is already a trial) and **one Life/Reward
episode** (E31, the anticipated night). **The pilot is the diagnostic for the template**, before 48
packets inherit it.

### 6.1 Validator extensions to build before the pilot

| Check | Enforces |
| --- | --- |
| `CHK_BID_FORMAT` | Beat ids are `{SID}-BTnn` and their SID parses |
| `CHK_EPISODE_BAND` | Each packet's CORRIDOR, WEATHER and FX sit inside its act band, **or** are a declared exception (Ruling 5). The overlays hold the bands; nothing checks an episode against them today |
| `CHK_PACKET_LINKS` | Every `BC-` id and milestone id a packet cites resolves; LOCKED breadcrumbs cited by a packet are placed at a matching locator |
| `CHK_POV` | The POV is a known cast member (`canon/cast_registry.csv` or `canon/characters/`) |

They are additive tooling, each with self-tests, and **they are built at release, not now.**

### 6.2 Where packets live (at release)

**Recommended:** one Markdown packet per episode under `ebci/B01/`, created **at release** (the
standing instruction forbids the directory until then), **plus** one row per beat in
`grids/episode_beats.csv`, whose header already carries the ECID fields and BID. The validator
already checks that grid's ECID vocabulary, so the beat rows are machine-checked from the first
packet.

---

## 7. Questions for the author

These do **not** release anything. They are the rulings the readiness report says must come first,
put now so the release decision can be quick when the nine-book audit is done.

| # | Question | Recommended |
| --- | --- | --- |
| **Q1** | **Physics:** approve **R1, R6, R7, R8** as written, and **R5 as clarified** (quarantine the old corridor *class* definitions; keep U1–U7 as the ruled intensity scale in `CORRIDOR`)? R2–R4 are already answered | **Yes** |
| **Q2** | **VFX:** approve **V1, V2, V3, V7**; **hold V6** (no self-emitting VT light, topological travel or levitation); V4 and V5 stand as current | **Yes** |
| **Q3** | **Conflict:** quarantine both C ladders; the packet's conflict brief is plain words (objective · opposition · turn · consequence · unresolved), with *none* allowed; the older descriptors are optional; retire True/False conflict | **Yes** |
| **Q4** | **The template** (Appendix A) as the schema for the pilot, installed in `templates/` at release | **Yes** |
| **Q5** | **Storage at release:** `ebci/B01/` per-episode packets plus beat rows in `grids/episode_beats.csv` | **Yes** |
| **Q6** | **Envelopes at release:** a `PR` overlay for the prologue; A1's widening declared as exceptions after the numbering is mapped; no new RES/HEAT/LOAD/MODE bands. **Before release:** Claude drafts the B01 overlay `TODO` fields as a proposal | **Yes** |
| **Q7** | **Causal cards:** full cards for **E15, E33, E45 and E48**, drafted **before release** (the 09-23 ruling's *"precise next work"* already asks for E15 and E33), after Q1–Q2. Observation notes suffice elsewhere. **E48's quiet observable is re-chosen** against *"arrive together, and carry one"* | **Yes** |
| **Q8** | **The four validator checks** (§6.1) built at release, before the two-packet pilot (E33 and E31) | **Yes** |

**Answer format:** for example *"1–8 yes"*.

---

## Appendix A — draft packet template (not installed)

```
# {SID} — {working title}
Status: EBCI PACKET — {DRAFT | REVIEWED | LOCKED}
Source: v4.1b §{n}; amendments {refs}; causal card {path | none}

## Header
SID:        S1.T1.B01.{A1|A2|A3|PR|EP}.E{nn}
Reading position: {n of 55, file order}
POV:        {cast member}
Place:      {locations_registry id / plain place}

## ECID (single end-state values; original strings in Notes)
POV | ENV | CORRIDOR | WEATHER | MODE | HEAT | FX | RES | LOAD
Band check: {inside A{n} band | declared exception: {axis}={value}, reason}

## Episode contract
Story job:
Objective:                  {or none}
Opposition / constraint:    {or none}
Turn (what changes):
Consequence:
Unresolved:
Reader reward / relief:
Chronology guard:           {what must not be known or shown yet}
Exit condition:

## Beats
{SID}-BT01  {function} | {who acts} | {what changes} | {obs class of any sensory claim}
{SID}-BT02  …

## Event record (only if a physical Resonance event occurs)
Card: {path}   Observation classes: {OBJ/ATT/POV/MET per claim}
Cost payer and kind:   Residue and who can check it:

## Obligations
Breadcrumbs:        {BC-ids planted / reinforced / paid here, with their dependency class}
Continuity:         {inherited state that must hold}
Protected reveals:  {what this episode must not spend}
Amendments applied: {Veil audit §3/§4 items}

## Exit state
World · Knowledge · Relationships · Body/cost

## Notes
{original strings for migrated ECID values; open-but-safe items resolved here (O1–O12)}
```

**Out on purpose:** word-count targets, hue-to-emotion lookups, colour-coded auras, automatic
reader-pressure scores, and numeric conflict codes (the readiness report, and Q3).

## Appendix B — the B01 notes checklist for EBCI

From the Veil audit amendments (§3, as refined by §4) and the 09-27 answers:

| Item | Where | What changes |
| --- | --- | --- |
| **Arrive together, and carry one** | E48 (and E01) | The shared prediction brings them early; one stranger (not a child) steadied; the whole Square declined; a bodily cost; the others taken by the trio and Mara's people |
| **Retitle E29**; *pressure zone* in text | E29 | *Drift* is B02's word. **Keep "swamp wound"**; reword *"conceptual wound"* |
| **Technarc ambient** | E23 | No request to Baz; B02 E13 is the first |
| **One visit** | E23–E30 | Elisabet's is a visit; B02 E05 is where she stays |
| **Lacuna's cameo** | E31; four notes | Reconcile the deferral notes to *"a cameo only"* |
| **v4.1a leftovers** | §12 | Remove |
| **LR02 skipped** | LR numbering | Renumber, or record the skip |
| **Header** | L5 | *"READY FOR CONTROLLED EBCI"* predates the hold |
| **Relabel to reading order** | E36/E37 + S05; E43/E44 | The file order is the reading order (B3, approved) |
| **The site seed** | E01 | A Möbius seed of the Mending site only (O1) |
| **Execution tests** | All | Discovery accumulates (B01: predicting a window); a variety of pleasure and want; duration |
| **The prologue envelope; A1 widening** | E00; E13–E14 (mapped) | §5 |
| **Open-but-safe register O1–O12** | Per scene | Each is resolved when its scene reaches EBCI |
| **Breadcrumbs placed in B01** | 16 ledger rows name a B01 locator | The packet names each `BC-` id it carries |
