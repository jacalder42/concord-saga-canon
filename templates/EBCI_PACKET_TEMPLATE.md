# EBCI packet template

Status: TEMPLATE — hand-authored. Installed 2026-09-27 for the B01 two-packet pilot
(`decisions/SAGA_LOCK_AND_B01_EBCI_PILOT_RELEASE_AUTHOR_ANSWERS_2026-09-27.md`), from the approved
draft in `proposals/B01_EBCI_PREFLIGHT_2026-09-27.md` Appendix A (preflight Q4), with one addition:
the **Tracking** line (the author's clarification that fun, slice of life and wonder are tracked for
presence, not capped). **Provisional until the pilot's narrative review.**

What it does not change: no rule, card or overlay. Packets made from it live in `ebci/`, not here,
and are not hand-copied back into this file.

## How to use it

- **Optional means optional.** Life, pleasure, work and grief episodes may have **no Resonance
  effect, no active opposition and no breadcrumb.** Write `none` and move on. A field filled because
  the template has it is a defect.
- **Keep every element; point at none.** A breadcrumb is structurally deliberate and **narratively
  incidental**: the Obligations section is for the writer, never an instruction to make the reader
  notice.
- **Plain words.** No numeric conflict codes (both C ladders are quarantined), no word counts, no
  hue-to-emotion lookups, no reader-pressure scores.
- **Beats are story units, not prose.** No dialogue, no scene text.
- `[P]` marks a provisional choice made in the packet for the author to confirm.

## The skeleton

```
# {SID} — {working title}
Status: EBCI PACKET — {DRAFT | REVIEWED | LOCKED}
Source: v4.1b §{n}; amendments {refs}; causal card {path | none}

## Header
SID:        S1.T{t}.B{bb}.{A1|A2|A3|PR|EP}.E{nn}
Reading position: {n of the book's episodes and supplements, file order}
POV:        {cast member}
Place:      {locations_registry id / plain place}
Season:     {season | [P]}

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
{SID}-BT01  {function} | {who acts} | {what changes} | {obs class of any sensory claim, or —}
{SID}-BT02  …

## Event record (only if a physical Resonance event occurs; otherwise: none)
Card: {path}   Observation classes: {OBJ/ATT/POV/MET per claim}
Cost payer and kind:   Residue and who can check it:

## Obligations
Breadcrumbs:        {BC-ids planted / reinforced / paid here, with their dependency class; or none}
Continuity:         {inherited state that must hold}
Protected reveals:  {what this episode must not spend}
Amendments applied: {audit items}

## Tracking (a record, not an obligation)
Fun: {none | light | strong} · Slice of life: {…} · Wonder: {…}

## Exit state
World · Knowledge · Relationships · Body/cost

## Notes
{original strings for migrated ECID values; open-but-safe items resolved here; [P] choices}
```

## Machine checks

`tools/validate_canon.py` checks every packet in `ebci/` and every row of `grids/episode_beats.csv`:
`CHK_BID_FORMAT` (beat ids are `{SID}-BTnn` and match their packet or row), `CHK_EPISODE_BAND` (CORRIDOR,
WEATHER and FX inside the act band, or a declared exception), `CHK_PACKET_LINKS` (every breadcrumb and
milestone id resolves; a LOCKED breadcrumb carried on the Breadcrumbs line is placed at this SID) and
`CHK_POV` (the POV is a known cast member).
