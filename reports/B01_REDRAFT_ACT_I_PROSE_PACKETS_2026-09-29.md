# B01 redraft, Act I prose packets: derivation and self-sweep

**Status:** DERIVATION REPORT
**Date:** 2026-09-29

**What it does not change:**
- No ruling, canon card, grid row, EBCI packet, overlay or book context.
- No manuscript text. The private manuscript was used only as the comparison corpus for the overlap check, never as a source.
- It does not edit `ebci/prose/README.md`, the writer profile, or the superseded packets in `ebci/prose/B01/superseded_2026-09-29/`.
- It does not release Act I drafting. That is the author's call.

## 1. What was derived

There are 16 new prose packets for the ~150k redraft's Act I, `ebci/prose/B01/B01-E00.md` … `B01-E15.md`. There is one per revised EBCI packet, in the new numbering (`ebci/B01/REDRAFT_CONCORDANCE.md`). S02 is specified inside `B01-E07.md`.

- **Source:** the revised Narrative Briefs only (Q-AC2). That means the Header's length, place and time; Story job; Want; the Conflict block; Change; Reader experience; Keep / don't spend; Exit conditions; the Required observable, consequence and prohibitions; and the Beats.
- **Excluded:** the Control layer (ECID, event records, writer options, obligations, engine, sign-off, tracking and notes). No writer option was promoted.
- **Format:** the approved shape. A status line sits above a `---` rule, and what the writer receives sits below it.
- **Headings used:** a title line, then one line for point of view, place, time and length, then these sections:
  - *What this scene is for*
  - *What she / he / they want here*
  - *Who pushes back*
  - *Pressing on … from outside*, omitted where the brief says none: E00, E05, E11, E12 and E13
  - *What happens. Only this is fixed*
  - *What it costs or changes*
  - *Still open*
  - *Keep off the page*
  - *Ends*
- **Reader experience** is folded into *What this scene is for*.
- **Event pieces** (E06, E07, E14): the required observable sits under *What happens*, the required consequence under *What it costs or changes*, and the prohibitions under *Keep off the page*.
- **Order of work:** the overlays were refreshed before derivation (Q-RE8; commit `d2f633d`, ledger §287).

| File | Source | Point of view | Target length | Packet words |
| --- | --- | --- | --- | --- |
| B01-E00 | PR.E00 | the two presences, unnamed | 500 | 176 |
| B01-E01 | A1.E01 | Seraphine | 2,800 | 389 |
| B01-E02 | A1.E02 | Seraphine | 2,600 | 357 |
| B01-E03 | A1.E03 | Seraphine | 2,800 | 271 |
| B01-E04 | A1.E04 | Lucien | 3,600 | 494 |
| B01-E05 | A1.E05 | Seraphine | 2,300 | 236 |
| B01-E06 | A1.E06 | Seraphine | 2,900 | 426 |
| B01-E07 (+ S02) | A1.E07 | Seraphine | 3,000 + 600 | 538 |
| B01-E08 | A1.E08 | Mara | 2,200 | 324 |
| B01-E09 | A1.E09 | Seraphine | 2,600 | 358 |
| B01-E10 | A1.E10 | Lucien | 2,800 | 455 |
| B01-E11 | A1.E11 | Lucien | 2,200 | 193 |
| B01-E12 | A1.E12 | Seraphine, then Lucien | 4,000 | 267 |
| B01-E13 | A1.E13 | Lucien | 2,400 | 202 |
| B01-E14 | A1.E14 | Seraphine and Lucien | 4,500 | 517 |
| B01-E15 | A1.E15 | Lucien | 4,200 | 406 |

**Lengths:**
- **Narrative:** 45,400 words.
- **With S02:** 46,000 words, as expected for Act I.
- **The packets themselves:** 6,108 words below the rule, about 380 each.

## 2. Guards compressed or reworded

Every page-protecting guard in the briefs is kept. These are the places where the wording changed.

- **The clock rule.** *"No clock time in narration unless a character does something with it"* becomes *"No clock time in the narration unless someone acts on it"*. It appears in every packet whose brief carries it. E09 keeps its exception: the evening call is a time she keeps.
- **E00.** *"No promise of a later reach"* becomes *"any promise that they will reach it"*.
- **E01.**
  - *"The camp is linked to nothing later"* becomes *"the camp is a family's home, and nobody calls it special"*.
  - *"Dré … has no guide role and nothing reaches from him"* becomes *"an ordinary boy with a name; nothing of him lingers or reaches out"*.
  - Both guards hold. The forward-role vocabulary is gone.
  - Renée is identified as Dré's mother in the first beat, because the brief first names her only in the Consequence.
- **E02.** *"No site"* becomes *"nothing made of the place"*.
- **E03, the exit.** *"Seraphine keeps six o'clock for her call to Odile"* becomes *"Seraphine is keeping her evening call to Odile"*.
  - No one acts on the clock time inside the piece.
  - E09's brief knows the call only as the evening call.
- **E04.** *"The only bearing he is ever given"* becomes *"the only bearing he gets"*. It is still E04's only bearing. The who-sent-him guard is compressed to a list of what is not named.
- **E06.**
  - *"By any aura"* becomes *"by presence"*.
  - The Unresolved line, *"It will happen again"*, becomes *"Whether it happens again"*. That keeps the forecast from reading as the narrator's certainty.
- **E07.** *"Calming by aura"* becomes *"calming by presence"*.
- **E07, S02.** *"No faction, institution or antagonist named"* becomes *"No organization, group or antagonist named; the city speaks only as the city"*. The brief also requires the city's own procedural answer, so the city itself cannot be excluded.
- **E10.**
  - *"Its cost is deferred"* becomes *"nothing has come of it yet"*.
  - *"Inside his ten days"* becomes *"within a set period"*, matching the brief's own *Pressed by* line.
- **E11.** *"A one-scene child with no later role"* becomes *"belongs to this scene only, and nothing sets her up"*.
- **E12.**
  - *"The first major … rung"* becomes *"the first real step"*.
  - The place marker `[P]` is dropped.
  - The Turn is carried as the third fixed item, because the brief lists only two beats.
- **E14.** *"People across the Square go down"* becomes *"everyone in the Square goes down where they stand"*. The author confirmed the whole-crowd fall (Q-RE2, `decisions/REVISED_EBCI_VEIL_PASS6_AND_TRILOGY_GUIDE_AUTHOR_ANSWERS_2026-09-29.md`).
- **E15.**
  - *"His first bypass"* becomes *"gone from the proper channel to a person for the first time"*.
  - The exit's *"Baz arrives the next day"* becomes a commitment: *"Baz has agreed to come and is due the next day"*. This keeps the next piece's event out of the exit.
- **US spelling throughout** (profile §12): *neighborhood*, *behavior*, *organization*, *color*, *humor*, *labeled*.

## 3. Where the brief was unclear

- **E14, *"a man in a Saints jersey who says the speaker did it."*** *Speaker* could mean the loudspeaker or a person. It is kept as written, since a character's claim may be wrong.
- **E14, Seraphine's own fall.** Under the whole-crowd ruling she goes down too, but the brief says only that Lucien is *"down himself"*. The packet says *everyone* and leaves her fall to prose.
- **E08 and E11 both involve a laundromat.** In E08 it is a neighbor's account of a fight at *the laundromat*; in E11 it is *a laundromat near his lodging*.
  - The briefs don't say whether it is the same place.
  - E11 forbids any clue, so the packets draw no link.
  - The author may want to decide this before drafting.
- **E13's *Still open*** (*"Seraphine's short, easy reply"*) is a pleasant beat, not an open question. It is kept as the brief has it.
- **Title lines.** They follow the instructed format, `# Book 1, Episode {n} — {title}`, with E00 as *Episode 0*.
  - The format has no slot for Q-AR2's *"titles are working labels"*, so that guard is not restated per packet.
  - The author may want *(working label)* added, as in the pre-redraft Act II and III packets.
- **S02's scale** is given in words and as a number: *"a short piece, about a page (about 600 words)"*. Q-AR6 asked for words only; Q-IT2(d) now asks every redraft packet to carry an approximate length.

## 4. Self-sweep

| Check | Result |
| --- | --- |
| Ids or codes below the rule (SIDs, beat, breadcrumb and milestone ids, ECID values, *Resonance*, faction and later-book names, causal-card or observation-class terms, `[P]`) | **None.** One false match on the plain word *observations* (E15) |
| Future pointers | **None.** The remaining *will* forms are volition (*"no will behind it"*) or in-book commitments (an inspector coming, the Vein, what the city will make of it) |
| Required repair | **None.** No packet requires a repair; the words *repair*, *apology*, *forgive* and *reconcile* do not appear |
| Exits are facts only | **Yes:** elapsed time, place, who is present, who holds what, and open commitments. No exit states the next piece's events |
| Clock times nobody acts on | **None.** The remaining time words are durations or agreements someone acts on: the ambulance's half hour, the agreement to tell each other the time, *the same minute*, *midday* |
| Manuscript wording: 7-gram overlap against `concord-saga-manuscript/B01/**/*.md` (55 files, about 225k words), excluding 7-grams also in `ebci/B01/*.md` or `decisions/*.md` | **0 hits, and 0 before the exclusion.** At 6 words there are two raw matches, both the brief's own paraphrase (*a man in a Saints jersey*; *corner post reads out of true*), and both are kept |
| Validator: `python3 tools/validate_canon.py --quiet` | **0 violations** across 469 files |

## 5. Not in the packets, by design

- **Minimum identity context and character pressures** are assembled per episode in the drafting stack (`ebci/prose/README.md`). They are not written into packets.
- **The Q-EN8 sign-off questions** stay control-side.

Nothing is committed.

## Resolved by Claude after derivation (2026-09-29)

- **The two laundromats (E08, E11)** stay unlinked. Neither brief links them, and *silence is permission*.
- **E14's "the speaker"** reads *Clement's amplifier*, the fault theory (D3). It is corrected in the EBCI brief and the
  prose packet.
- **Title lines** use the working-label form of the Act II and III packets (Q-AR2).

