# Channel Names — Ruling and Change Scope

**Ruled by:** James, 2026-09-19 · **Recorded by:** Claude (Cowork)

> MissingThread, VeilThread and LuminousThread are correct.
> **MT** is the public mortal channel (early Tahl).
> **VT** is the private channel between Silence and Hope that Tahl discovers.
> **LT** is the post-Mending channel.

This resolves the `Veil-Touch` / `VeilThread` question, and settles it against the
repository. It supersedes `Veil-Touch` in `Mechanica-v4.md` and the channel rules.

---

## 1. What the ruling restores

The three channels are three Threads — a coherent naming system the Phase 1A migration
broke in two places out of three. Notion carries the original consistently across five
independent pages: `THE CONCORD SAGA — OVERVIEW`, `01.01 • Master Summary`,
`05.05 • Tech & Communications Bible` §1.3, `05.02 • Metaphysics & Ascension Bible` §4,
and Tahl's character sheet.

The repo file that introduced both renamings, `rules/Channels/CHANNELS_OVERVIEW.md`,
declares its own source as **"Project Memory (inflated)"** — the same inflation flag
raised against Mechanica in the 2026-09-15 handoff. `MT_RULES.md` and `VT_RULES.md` do
not carry it.

---

## 2. This is not a find-and-replace — `MT` is a concept conflict

`VT` is a clean rename: `Veil-Touch` → `VeilThread`, same referent.

`MT` is not. `rules/Channels/MT_RULES.md` §1 defines MT as:

> MT (Mortal Technology) is the **human-built information and communication layer**.
> It includes: phones · AR overlays · holochat · broadcast media · recording and
> storage systems · data networks and relays.

That is infrastructure. The ruling says MT is **the public mortal channel (early
Tahl)** — a publication, the thing Tahl launches. A phone network and a feed Tahl
writes are not the same object, and renaming the file's title does not reconcile them.

**Three ways to resolve it, and this needs your ruling:**

- **A. The Missing Thread is the channel; mortal technology is the substrate it runs
  on.** `MT_RULES.md` keeps most of its content but is retitled and reframed — it
  describes the medium, and the channel is what travels on it. The infrastructure keeps
  no three-letter token.
- **B. `MT` covers both, as the mortal tier.** The Missing Thread is its flagship and
  the rules file describes the tier's properties. Closest to what the file already
  says, and closest to Notion's "MT: Missing Thread (public mortal channel)".
- **C. Split them.** `MT` = Missing Thread; the infrastructure layer gets its own name
  and its own rules file. Cleanest conceptually, most work, and it adds a fourth token
  to a model whose whole point is that there are three.

I would take **B** — it needs the fewest edits, it matches Notion, and the channel
separation law (`MT ≠ VT ≠ LT`) still reads correctly with it. But it is a canon act.

---

## 3. One consequence: the `MT` token collision dissolves

`rules/canon_rules.json` currently carries:

> "MT appears in two vocabularies: as a channel it is Mortal Technology (channels.MT);
> as a supplement vehicle it is The Missing Thread."

Under the ruling those are **the same thing**. There is no `MT` collision to
disambiguate — the note was written to reconcile a drift that has now been ruled away.
It should be removed rather than reworded, and `canon/supplements/SUPPLEMENT_VEHICLES.md`
carries the same note.

`VT` still has a genuine multiplicity — channel, resonance state, supplement vehicle —
and that part of the note stands.

---

## 4. `VT`'s definition sharpens

"The private channel between Silence and Hope that Tahl discovers" is more specific than
anything in the repository. Notion corroborates and extends it:

- `05.02 • Metaphysics & Ascension Bible`: "A private back-channel between
  metaphysicals: originally only Silence + Hope"
- `05.05 • Tech & Communications Bible`: access is "ONLY Silence, Hope, Tahl Echo, and
  ascended trio"

This also explains the `RES: VT` state cleanly. `VT` as a resonance state is the field
registering contact with a channel that was never meant to admit a mortal — which is
why `E14` is anchored "FIRST AND ONLY VT BRUSH IN VEIL TRILOGY."

---

## 5. A gap this exposed: Silence and Hope are not in the repository

`canon/characters/` holds 14 characters across 60 files. **Neither Silence nor Hope
appears in any of them**, nor in `source_canon/`. Two metaphysical entities who are
each half of the Old Veil, whose existence defines `VT`, and whose break drives the
endgame, have no canon file at all.

Notion has at least `08.10 • Silence — Metaphysical`, describing Silence as "half of
the Old Veil — a metaphysical construct built to suppress resonance flux and maintain
boundary containment. Emotionless by design, but over centuries grew brittle."

**Recommend adding this to the work queue as a Tier-1 recovery item.** It is not a
naming cleanup — it is a hole where two principals should be.

---

## 6. Change scope

Counts exclude `recovery/source_exports/`, which is never altered in place.

**`Veil-Touch` → `VeilThread`** — 6 occurrences in 5 files, plus ledger entries:

| File | Count | Note |
| --- | --- | --- |
| `rules/Mechanica-v4.md` | 2 | lines 723, 1137 — **amends Mechanica**, so it needs a ledger entry under §5.2 |
| `rules/Channels/VT_RULES.md` | 1 | line 11 |
| `rules/Channels/CHANNELS_OVERVIEW.md` | 1 | line 14 |
| `CLAUDE.md` | 2 | working agreement |
| `recovery/RECOVERY_LEDGER_2026.md` | 8 | records both readings; update to record the ruling, do not rewrite the history |
| `proposals/concord-2026/CHANNELS_AND_RESONANCE_STATES_2026-09-19.md` | 2 | superseded by this document |

**`Mortal Technology` → per §2's ruling** — 6 occurrences in 5 files:
`rules/canon_rules.json` (1), `MT_RULES.md` (1), `CHANNELS_OVERVIEW.md` (1),
`Mechanica-v4.md` (2), `canon/supplements/SUPPLEMENT_VEHICLES.md` (1).

**`mortal_media_channel`** — `rules/canon_rules.json:8`. Becomes
`"MT": "Missing Thread — public mortal channel"`. The earlier "media narrows it"
finding is moot: the gloss was closer to right than the file it contradicted.

**`VeilThread` already correct** and needs no change: `KadeEBCI.md`,
`LacunaEBCI.md`, `TahlEBCI.md`, and `recovery/CANON_DECISIONS_2026-09-18.md` §1.2.
Those three character cards were not drift — they preserved the original while the
rules files drifted around them.

---

## 7. Open

1. **§2 — how `MT` reconciles** (A, B or C). Blocks the `MT` half of the rename.
2. **Silence and Hope recovery** (§5) — add to the queue?
3. Whether amending Mechanica here needs anything beyond a ledger entry, given §5.2
   makes it authoritative until the line-by-line review.
