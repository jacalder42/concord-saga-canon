# The prose calibration passes; the drafting rules; sequential drafting begins — author ruling

**Date:** 2026-09-27
**Status:** CURRENT AUTHOR INSTRUCTION (production).

**Provenance.** This is the author's message to Claude answering Q-CAL1–Q-CAL4 of
`reports/B01_PROSE_CALIBRATION_REVIEW_2026-09-27.md`. It closes with a block headed *"Direction for Claude"*. It has
no *"From ChatGPT"* prefix.

**What it does not change:** no canon ruling, card, grid, EBCI packet or Mechanica text. The drafting stack, the
writer profile's §9 and the prose README change. **No prose enters this repository.**

## 1. Decided

| # | Decided |
| --- | --- |
| **Result** | **The three-episode calibration passes.** *"Do not run another calibration round."* |
| **Q-CAL1** | **Yes, generalised as MINIMUM IDENTITY CONTEXT, not a character-voice layer.** For **any named character** appearing in a prose packet, give only the immutable identity facts that prevent contradiction in that scene: normally **name + pronouns + scene-relevant role or relationship + at most one stable physical or presence fact, if likely to appear**. Do not import full cards, histories, future roles or hidden significance. Do not repeat what the preceding prose has already established; once a character is on the page, the prose is the source. Example: *"Trip (she): Velvet Vein's host; compact, socially effortless, owns the room without dominating it."* |
| **Q-CAL2** | **Yes, in the profile's strange/Mechanica section:** *"Nobody reads minds. Sensing a room means sensing pressure, distress or other permitted effects—not thoughts, memories or stories. Any conclusion about what someone feels, wants or has experienced remains observation, inference or guess."* The underlying principle: *"Resonance may provide information; it does not provide narration."* *"Characters still have to interpret people."* |
| **Q-CAL3** | **Yes.** Until real preceding prose exists, the context given to a drafting engine is **only** the relevant earlier prose-packet *Ends* plus elapsed time. No synthesised connective summaries (*"summarization quietly performs interpretation"*). Actual preceding prose supersedes this once it exists |
| **Q-CAL4** | **Manuscript prose stays out of this public repository.** The calibration drafts are not committed. When real sequential drafting begins, use a **separate private manuscript repository**, provisionally **`concord-saga-manuscript`**, with a simple book/act/episode structure (`B01/act-01/E01.md …`, `B02/`, `B03/`, `draft-notes/`) and **no elaborate governance**. This repository may record that drafting began and where manuscript authority lives. **Manuscript is not canon:** *"canon → constrains manuscript; manuscript → may propose discoveries back to canon; but manuscript ≠ canon."* |
| **Calibration drafts** | **Disposable.** Do not revise or polish E06, E13 or E15. Their inventions (the drying glasses, the plumb bob, the list) are **not promoted into canon**. They are not preceding prose. **E06, E13 and E15 are drafted fresh in sequence** |
| **No anti-tic rules yet** | *"the way…"*, shoulders, *"It wasn't a question"*, held breath and punch paragraphs stay out of the profile. After B01 Act I exists as a corpus, a **prose-pattern pass** separates **authorial motif** (keep), **character habit** (perhaps keep), **engine tic** (edit) and **AI tell** (remove) |
| **Next** | Apply CAL1–3; establish the private manuscript repository when prose preservation begins; **draft B01 sequentially from E00**, each episode from the approved profile + its prose packet + minimum identity context not already established + the actual preceding prose; **stop at a checkpoint after E03 or E04**: *"One episode can tell us whether a sentence works; four sequential episodes can tell us whether we have a novel."* No new planning layer. **No Act II prose packets yet** |

## 2. How it is applied

- **Q-CAL2:** `ebci/prose/WRITER_PROFILE_JA_CALDER.md` §9 carries the author's sentence verbatim. **The principle is
  reworded** there as *"What a character senses may give them information; it never gives them the narration,"*
  because the profile goes to the drafting engine and *Resonance* stays out of Veil's page language
  (`decisions/VEIL_PROSE_PREPARATION_AND_PROSE_PACKET_PILOT_AUTHOR_RULING_2026-09-27.md`). The author's wording is
  recorded here; the substitution reverts if he prefers his own.
- **Q-CAL1 and Q-CAL3:** `ebci/prose/README.md` now sets out the drafting stack, minimum identity context, the
  context rule and where prose lives. Identity facts come from `canon/characters/` and `canon/cast_registry.csv`
  and are assembled per episode in the drafting stack, not kept as a new document. Q-WP3's one card line for a
  POV character's first substantial appearance still stands.
- **Q-CAL4, the private repository.** Claude tried to create `jacalder42/concord-saga-manuscript` (private) on
  2026-09-27. GitHub refused it: the session's integration may not create repositories (HTTP 403). **The author
  creates it.** Until then the drafts are kept in a local git repository with the ruled structure, outside this
  one, and handed over at the checkpoint.
