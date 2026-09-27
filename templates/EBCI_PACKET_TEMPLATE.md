# EBCI packet template

Status: TEMPLATE — hand-authored. Installed 2026-09-27 for the B01 two-packet pilot
(`decisions/SAGA_LOCK_AND_B01_EBCI_PILOT_RELEASE_AUTHOR_ANSWERS_2026-09-27.md`), from the approved
draft in `proposals/B01_EBCI_PREFLIGHT_2026-09-27.md` Appendix A (preflight Q4). **Revised 2026-09-27
after the pilot review** (`decisions/B01_EBCI_PILOT_REVIEW_AND_ACT_I_RELEASE_AUTHOR_RULING_2026-09-27.md`,
R3): each packet now has a **Narrative brief** and a **Control layer**, in the same file. The
pilot-era skeleton (one undivided list) is superseded; its fields all survive, regrouped.

What it does not change: no rule, card or overlay. Packets made from it live in `ebci/`.

## The two layers

**Narrative brief: what the writer uses.** A prose-facing (Sudowrite) packet is built **from the
narrative brief**, importing from the control layer **only what the writer actually needs**. For an
event episode that is the brief's **page-safe causal constraints**, never the causal card itself.

**Prose packets state constraints positively and compactly** (Q-AI2, `decisions/B01_ACT_I_AUDIT_AND_FULL_B01_RELEASE_AUTHOR_RULING_2026-09-27.md`): what the scene is
and must keep, in a line or two, plus every genuinely page-protecting prohibition. The full "must not
spend" list stays in the packet as QA. The author's example, for the prologue: *brief, abstract,
beautiful; two unnamed presences perceive strain but cannot intervene; reveal no cosmology or future.*

**Control layer: what the machine and the ledger use.** ECID, the event record, breadcrumb
administration, tracking, provenance and validation. **It is not passed to prose generation by
default.**

## How to use it

- **Optional means optional.** Opposition, consequence and unresolved are filled only when the episode
  has them. A Life/Reward, work or grief episode may have no Resonance effect, no opposition and no
  breadcrumb. A field filled because the template has it is a defect.
- **Leave discovery to prose.** Name what the episode is for and what must change; do not prescribe
  the emotional discovery, the exact behaviour or the line that shows it. Mark a likely carrier `[P]`
  and leave the rest open.
- **Keep every element; point at none.** Breadcrumbs are structurally deliberate and **narratively
  incidental**. They live in the control layer; the brief never asks the reader to notice them.
- **Point-of-view discipline.** A beat carries only what the POV character can perceive or be told.
  What another character experiences is shown by behaviour until it is reported.
- **Plain words.** No numeric conflict codes, no word counts, no hue-to-emotion lookups, no
  reader-pressure scores. **Beats are story units, not prose**: no dialogue, no scene text.
- `[P]` marks a provisional choice for the author to confirm.
- **`ENV`** is `NONE` unless the episode occupies a Mechanica-relevant environmental state. No
  ordinary-environment category exists, on purpose.
- **Tracking** (fun, slice of life, wonder) is a descriptive record of presence. No targets or
  minimums. **It observes; it does not manufacture:** light wonder found naturally in prose needs no
  architectural beat (Q-AI2).
- **Identity hygiene.** Where a name is ambiguous in the cast registry, the control layer records the
  cast id (for example A01, the Filament Mara, not G08 Mara Niht). The page is not burdened with it.

## The skeleton

```
# {SID} — {working title}
Status: EBCI PACKET — {DRAFT | REVIEWED | LOCKED}
Source: v4.1b §{n}; amendments {refs}; causal card {path | none}

## Header
SID:        S1.T{t}.B{bb}.{A1|A2|A3|PR|EP}.E{nn}
Reading position: {n of the book's episodes and supplements, file order}
POV:        {an authorised POV-capable narrative entity}
Place:      {locations_registry id / plain place}
Season:     {season | [P]}

## Narrative brief
Story job:
Want / objective:                   {or none}
Turn / change:
Reader experience / reward:
Must preserve / must not spend:     {continuity that must hold on the page; what must not be shown or known yet}
Exit state:
Opposition / constraint:            {optional; omit or none}
Consequence:                        {optional}
Unresolved:                         {optional}
Page-safe causal constraints:       {event episodes only: what the page may and may not show}

### Beats
{SID}-BT01  {a loose story unit: who, and what changes}
{SID}-BT02  …

### Supplement {Snn}                 (only when a supplement follows this episode)
Function, vehicle, placement, guardrails. No final supplement prose (v4.1b rule 29).

## Control layer

### ECID (single end-state values; original strings in Notes)
POV | ENV | CORRIDOR | WEATHER | MODE | HEAT | FX | RES | LOAD
Band check: {inside A{n} band | declared exception: {axis}={value}, reason}

### Event record                     (event episodes only; otherwise: none)
Card: {path}
Observation classes: {beat: OBJ / ATT / POV / MET, and who can check it}
Cost payer and kind:
Residue and who can check it:

### Obligations
Breadcrumbs:        {BC-ids planted / reinforced / paid here, with their dependency class; or none}
Amendments applied: {audit items}

### Tracking (a record, not an obligation)
Fun: {none | light | strong} · Slice of life: {…} · Wonder: {…}

### Notes
{provenance; original strings for migrated values; open-but-safe items resolved; [P] choices}
```

## Machine checks

`tools/validate_canon.py` checks every packet in `ebci/` and every row of `grids/episode_beats.csv`:
`CHK_BID_FORMAT` (beat ids are `{SID}-BTnn` and match their packet or row), `CHK_EPISODE_BAND`
(CORRIDOR, WEATHER and FX inside the act or position band, or a declared exception), `CHK_PACKET_LINKS`
(every breadcrumb and milestone id resolves; a LOCKED breadcrumb on the Breadcrumbs line is placed at
this SID) and `CHK_POV` (the POV resolves to an authorised POV-capable narrative entity: a cast member,
or an entity declared in `rules/canon_rules.json` `pov_entities`).
