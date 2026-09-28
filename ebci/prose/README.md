# ebci/prose/ — prose packets

Status: PRODUCTION LAYER. **The pilot passed 09-27; the format is solved.** B01 Act I's packets are derived and swept
(`decisions/B01_ACT_I_PROSE_PACKETS_AND_WRITER_PROFILE_AUTHOR_RULING_2026-09-27.md`). **The calibration passed 09-27, and
sequential B01 drafting has begun** (`decisions/PROSE_CALIBRATION_RESULT_AND_DRAFTING_START_AUTHOR_RULING_2026-09-27.md`).
**Act II (E18–E37, S04, S05) is derived 09-28** (`decisions/B01_ACT_I_REVIEW_ANSWERS_AND_ACT_II_PACKET_RELEASE_AUTHOR_RULING_2026-09-28.md`). **No layer between packets and prose** (no treatments, dialogue plans or beat sheets).

**Manuscript prose is not kept in this repository**, which is public, and manuscript is not canon. Drafts live in a
separate **private** repository, `jacalder42/concord-saga-manuscript` (live 2026-09-28, ledger §233); see *Where prose lives* below.

## The derivation rule

**A prose packet derives from the EBCI Narrative Brief, never from the Control Layer.**

- **Excluded by default:** ECID and U/W/FX codes; SIDs, beat ids, breadcrumb and milestone ids;
  causal-card terminology and observation classes; tracking; provenance; future-book pointers;
  validator language; editorial explanations of why something matters later; **Writer Options**.
- **Writer Options enter a prose packet only by explicit, episode-specific promotion**, recorded in the
  packet's status line.
- **Shapes differ.** A packet omits every field that does not help its scene. A Life/Reward episode may
  be a handful of lines; an event episode carries only the page-safe observational limits it needs.
- **Only what is below the rule** in each file is given to a writer or to Sudowrite. The status line
  above it is repository metadata.

## The drafting stack

Each episode is drafted from these and nothing else:

1. **The approved writer profile**, `WRITER_PROFILE_JA_CALDER.md`, below its rule, unchanged.
2. **The episode's prose packet**, below its rule.
3. **Minimum identity context** (Q-CAL1), only for named characters not already established in the preceding prose.
4. **The actual preceding prose**; or, until it exists, the **context rule** below (Q-CAL3).
5. **From Act II on, one standing instruction** (Q-AR4): *Continue these people and this novel. Do not reproduce Act I's
   successful shapes.*

**Nothing else enters the stack.** The review-side watch-list (`REVIEW_WATCHLIST.md`) never does. No length numbers
(Q-AR5) and no web-serialisation concerns: web installments are derived later from the finished manuscript.

### Minimum identity context (Q-CAL1)

For any named character who appears in the episode, give only the immutable identity facts that stop the scene
contradicting canon. Normally that is:

- name and pronouns;
- the character's scene-relevant role or relationship;
- **at most one** stable physical or presence fact, and only if it is likely to appear.

Example: *Trip (she): Velvet Vein's host; compact, socially effortless, owns the room without dominating it.*

- **Do not import** full cards, histories, future roles or hidden significance.
- **Do not repeat** anything the preceding prose has already established. Once a character is on the page, the prose governs.
- It is **not a character-voice layer.** Q-WP3's one card line about how a POV character notices still applies at their first substantial POV appearance, and only there.
- The facts come from `canon/characters/` and `canon/cast_registry.csv`. They are assembled per episode in the drafting stack, not kept as a new document.

### The context rule (Q-CAL3)

**Until real preceding prose exists,** the context given to the drafting engine is **only** the relevant earlier
prose packets' **Ends** lines, as written, plus the approximate elapsed time. No synthesised connective summary,
no grouping and no characterisation.

**Once actual preceding prose exists, it supersedes this.** Calibration drafts are never preceding prose.

## Where prose lives (Q-CAL4)

- **Manuscript prose stays out of this repository.** The canon repository may record that drafting began and where
  manuscript authority lives; it holds no drafts.
- **Drafts live in a private repository, provisionally `concord-saga-manuscript`**, with a simple structure and no
  elaborate governance:

  ```
  B01/act-01/E00.md, E01.md, …
  B02/
  B03/
  draft-notes/
  ```

- **Manuscript is not canon.** Canon is what the substrate says (CLAUDE.md §1). Material that prose discovers
  enters canon only through the usual reconciliation and an author ruling.
- **Calibration drafts are disposable**, not preceding prose, and their invented material is not canon.

## The pilot's five questions

1. Can a competent novelist begin without reopening the canon repo?
2. Does it protect everything whose violation would actually damage canon?
3. Are the best dialogue, imagery, blocking, humour and emotional discovery still unwritten?
4. Is anything present because the database knows it rather than because the novelist needs it?
5. Does reading it make the novelist want to write the scene?

## The workflow

**Act by act, never all 144 at once:** derive B01 Act I's prose packets immediately before drafting Act
I; draft; reconcile what prose discovered with canon and EBCI; then derive Act II. After B01's prose,
reconcile Veil continuity before deriving B02's packets.

**Sequential drafting began 09-27 at E00,** with a checkpoint after E03 or E04: *"One episode can tell us whether a
sentence works; four sequential episodes can tell us whether we have a novel."* No anti-tic rules are added to the
profile yet. After B01 Act I exists as a corpus, a prose-pattern pass separates authorial motif, character habit,
engine tic and AI tell.

## The writer profile

`WRITER_PROFILE_JA_CALDER.md` is the one stable instruction set that accompanies every packet (**approved 09-27** for Veil). **No per-character voice layer:** at a character's first substantial POV appearance only, one card line about how they notice or think may be promoted; after that the preceding prose governs. It is **recovered, not invented**: `recovery/JA_CALDER_WRITER_PROFILE_SOURCE_RECOVERY_2026-09-27.md` registers every source, its provenance and the conflicts. It carries no scores, ratios or required beats.

## Guards for B01 Act II and after

From the Act I checkpoints (`decisions/B01_ACT_I_DRAFTING_CHECKPOINT_AUTHOR_ANSWERS_2026-09-28.md`,
`decisions/B01_ACT_I_REVISION_REPORT_AUTHOR_ANSWERS_2026-09-28.md`), carried into prose-packet derivation.

- **No return to the camp in B01** (Q-DR7).
- **No Vienna scene in B01.** Mentioning that Lucien is from Vienna is fine (Q-DR8).
- **No landmark or compass direction for Lucien's lean** (Q-DR10). E04's *toward the low sun* is the only bearing.
- **Seraphine's entry into an episode does not default to paperwork.** Her life widens as her story widens.
- **Act I is closed for editing.** It is the calibration corpus. Its rhythms and endings are judged later in an
  author-led line edit, not an automated pass.

**From the Act I review** (`decisions/B01_ACT_I_REVIEW_ANSWERS_AND_ACT_II_PACKET_RELEASE_AUTHOR_RULING_2026-09-28.md`).
These describe how narrative behaviour changes; they do not add scenes:

- **Agency (Q-AR7).** Act I happened to them; Act II increasingly happens because of what they decide to do about it.
  They plan, test assumptions, disagree about what things mean, look for witnesses, cause trouble with what they think
  they know, miss ordinary obligations, and choose on incomplete evidence.
- **Seraphine's work (Q-AR8).** Her casework continues, and the investigation begins to cost it. This permits the
  conflict; it is not a scheduled beat.
- **Three methods (Q-AR9).** Baz adds testimony, memory and questioning. He does not replace Lucien's physical
  evidence, measurement and contradiction. Seraphine's method is people, access and care. The investigation is most
  interesting where the methods disagree.
- **Titles are working labels (Q-AR2).** A packet's title is a label for the file, never a cue for the page. Final
  chapter titles are the author's, at publication.
- **Supplement scale (Q-AR6)** is given in words (*a short piece, about a page*), never as a number.

**Drafting reads the manuscript's continuity layer** (`draft-notes/B01_ACT_I_CONTINUITY.md` in the private repository)
for anything later prose must remember.
