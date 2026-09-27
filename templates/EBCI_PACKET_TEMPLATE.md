# EBCI packet template

Status: TEMPLATE — hand-authored. Installed 2026-09-27 for the B01 pilot from the approved draft in
`proposals/B01_EBCI_PREFLIGHT_2026-09-27.md` Appendix A (preflight Q4). Revised twice on 2026-09-27:
**two layers** after the pilot review (`decisions/B01_EBCI_PILOT_REVIEW_AND_ACT_I_RELEASE_AUTHOR_RULING_2026-09-27.md`,
R3), and **compressed** after the full-B01 audit
(`decisions/B01_FULL_AUDIT_COMPRESSION_AND_CALENDAR_AUTHOR_RULING_2026-09-27.md`, Q-FB1). Each revision
supersedes the earlier skeleton; the fields survive, regrouped and lighter.

What it does not change: no rule, card or overlay. Packets made from it live in `ebci/`.

## Silence is permission

**Anything the Narrative Brief does not constrain remains available to prose.** A packet does not need
to account for the episode's full runtime, every character want, incidental objects, conversation,
humour, mistakes, detours or texture. **Do not schedule spontaneity:** no packet says *"room for a
digression"*, *"one joke here"* or *"someone laughs at the wrong time"*. It simply leaves room.

**Unredeemed specificity.** The world is larger than the plot. Some notebooks stay notebooks; some
drinks only get drunk; some musicians never matter again; some people walk through one episode and
back into their own lives. **Do not create receipts** for incidental objects, people, jokes or details
because they exist. (A prose and design principle; never a validator or a quota.)

## The two layers

**Narrative brief: what the writer uses.** A prose-facing (Sudowrite) packet is built from it. It
says what the episode is for, what must be true when it ends, and what the page must never do. **It
does not stage the scene.**

**Control layer: what the machine and the ledger use.** ECID, the event record, **writer options**
(secondary images a writer may take or leave), breadcrumbs, tracking and provenance. **Not passed to
prose generation by default.**

**Prose packets state constraints positively and compactly**, keeping every page-protecting
prohibition. The author's example, for the prologue: *brief, abstract, beautiful; two unnamed presences
perceive strain but cannot intervene; reveal no cosmology or future.*

## Compression rules (Q-FB1)

1. **State, don't script; say each thing once.** Exit states are plain states, not epigrams. No *"X before
   Y"* formulas, no roll calls of who-knows-how. Each idea appears once, in the field it belongs to: an
   idea repeated across Want, Change, Keep and a beat reads as a verdict, not a question.
2. **Events keep only what is required:** the **required observable**, the **required consequence**
   and the **page-protecting prohibitions**. Every other image is a writer option in the control layer.
   The causal card stays authoritative behind the packet.
3. **Relationships name the rung:** the state **before** and **after**. Never the emotional mechanism,
   never the choreography of the change.
   **A relationship packet needs no beat describing the transition** between Before and After: sometimes
   the whole scene is the transition (guidance, not a check; Q-V2).
4. **Register, not schedule.** A Life/Reward brief names its register (fun, rest, wonder, friendship)
   and leaves the moments to prose.
5. **Beats are few and loose:** the story units that must happen, in order, and nothing that merely
   decorates. Protected beats from the architecture stay; everything else is optional.
6. **No scaffolding in the brief:** no cast ids, relabel notes, supplement rules, ledger ids or
   production constraints. They belong to the control layer.
7. **Point-of-view discipline.** A beat carries only what the POV can perceive or be told.
8. **Differentiate, don't merge.** Where two episodes share a function, each brief names what makes it
   different; prose decides whether both survive.
9. **Cut staging, not guards.** Compression removes how a scene plays out. It keeps what later episodes
   rely on (a carry-forward, a state another brief cites) and every line that guards against a likely
   mistake, including what characters *may* do where a prohibition could be over-read (added after the
   five-packet verification, 2026-09-27).

## Other rules

- `[P]` marks a provisional choice for the author to confirm.
- **`ENV`** is `NONE` unless the episode occupies a Mechanica-relevant environmental state.
- **Tracking** (fun, slice of life, wonder) is a descriptive record of presence: no targets, no
  minimums. It observes; it does not manufacture.
- **Cast discipline:** an episode introduces no new named recurring face unless its brief names one; a
  recurring infrastructure, medical, data or care face appears only if one is already active.
- **Identity hygiene:** where a name is ambiguous in the cast registry, the control layer records the
  cast id (for example A01, the Filament Mara, not G08 Mara Niht).
- **The calendar is approximate.** The header gives a rough *when*; exact dates are not set unless
  continuity requires them.

## The skeleton

```
# {SID} — {working title}
Status: EBCI PACKET — {DRAFT | REVIEWED | LOCKED}
Source: {architecture §; amendments; causal card or none}

## Header
SID:        S1.T{t}.B{bb}.{A1|A2|A3|PR|EP}.E{nn}
Reading position: {n of the book's episodes and supplements, file order}
POV:        {an authorised POV-capable narrative entity}
Place:      {plain place}
When:       {approximate: "early March"; "between the Square and the pulse"}

## Narrative brief
Story job:
Want:                               {optional; the immediate objective; use a human want only where the architecture gives one}
Change:                             {or, for a relationship episode: Before: … / After: …}
Reader experience:
Keep / don't spend:                 {compact; page-protecting only}
Exit state:                         {a plain state}
Required observable:                {event episodes only}
Required consequence:               {event episodes only}
Prohibited on the page:             {event episodes only}

### Beats
{SID}-BT01  {a loose story unit}

### Supplement {Snn}                 (only when a supplement follows this episode: function and guardrails, no prose)

## Control layer

### ECID (single end-state values)
POV | ENV | CORRIDOR | WEATHER | MODE | HEAT | FX | RES | LOAD
Band check:

### Event record                     (event episodes only; otherwise: none)
### Writer options                   (secondary images and possibilities; optional; event and set-piece episodes)
### Obligations
Breadcrumbs:        {BC-ids with dependency class; or none}
Amendments applied:
### Tracking (a record, not an obligation)
Fun: {none | light | strong} · Slice of life: {…} · Wonder: {…}
### Notes
```

## Machine checks

`tools/validate_canon.py` checks every packet in `ebci/` and every row of `grids/episode_beats.csv`:
`CHK_BID_FORMAT`, `CHK_EPISODE_BAND`, `CHK_PACKET_LINKS` and `CHK_POV` (an authorised POV-capable
narrative entity: a cast member, or `canon_rules.json` `pov_entities`).
