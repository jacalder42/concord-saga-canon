# Music-project conversations — corpus index

**Status:** PROVENANCE INDEX. Bodies are **not stored here** — every one of these contains
lyrics, and `CLAUDE.md` §1 forbids prose. Same footing as
`MARA_NIHT_RECOVERY_2026-09-21.md` §5, where the §1/§7 conflict is recorded and unresolved.
**Date:** 2026-09-21

Seven music-project conversations have now been supplied. This file exists so the next
session can tell at a glance **which ones touch Concord canon and which do not**, without
re-reading ~200,000 words.

---

## 1. The index

| Conversation | id | Created | Turns | Concord content |
| --- | --- | --- | --- | --- |
| `Bubble Grunge Lyrics` | `6961c2b0` | 2026-01-10 | 429 | **Mara Niht's source.** No saga content; integration is authorial. §66–§67 |
| `Elias Ward Songwriting Prep` | `69865c91` | 2026-02-06 | 62 | **Four Tier-1 Elias blocks — identical to the repo's own files.** §2 below |
| `Artist Identity and Lyrics` | `69869a0b` | 2026-02-07 | 108 | None. Band OS; band named **Loose Change Parade** |
| `Artist Concept Development` | `698b3f74` | 2026-02-10 | 184 | None. `Elias Ward` appears once, as a rejected artist-name candidate |
| `Song Review and Evaluation` | `69f490ab` | 2026-05-01 | 21 | None. Cites a **"Romance System (S4–S6)"** — §4 below |
| `Suno v5.5 Music Prompt` | `69fb4395` | 2026-05-06 | 9 | **None.** Architectural walkthrough score, unrelated to the saga |
| `Develop Singer Style` | `6a982376` | 2026-09-02 | 28 | None. **Eli Stone** project; wrongly cited as Mara Niht's source. §68 |

**Net: one of the seven carries Concord canon, and it carries nothing new.**

## 2. The Elias Ward canon blocks are the repository's own files

`Elias Ward Songwriting Prep` opens with four Tier-1 blocks pasted in as context — POV,
Identity v1.1, EBCI and Appearance. **They are not a recovery.** Compared word-for-word
against the repository:

| Block | Repo file | Result |
| --- | --- | --- |
| POV | `canon/pov/elias_ward_pov.md` | ratio **1.000** |
| Identity v1.1 | `canon/characters/EliasID.md` | ratio **0.999**, 0 of 66 segments missing |
| EBCI | `canon/characters/EliasEBCI.md` | **563 words to 563, zero word-level differences** |
| Appearance | `canon/characters/EliasAppearance.md` | ratio **1.000** |

Sub-1.000 ratios are punctuation and bullet glyphs only; the EBCI diff returned **no
opcodes at all** once markdown was stripped.

**This is a negative finding worth keeping.** It means two things: no Elias canon needs
recovering, and the songwriting work was **grounded in the repository's canon rather than
drifting from it** — the conversation held position until released and then worked from
the pasted blocks.

## 3. What IS new in that conversation — and its canon status

Songwriting development for Elias: genre boundaries, three song archetypes (Reassurance /
Control / Alt-roots), a ruleset for endings, a Kevin Bacon–Bon Jovi *"everyman with
searing vanity"* calibration, and song drafts.

**The author ruled its status inside the conversation itself:**

> *"Music should be narrative adjacent, but not in world. They can stand-alone without the
> story."*

So the songs are **not in-world artifacts** and do not enter canon. This is the opposite
disposition from Mara Niht, who *was* integrated as a character (§66) — and the contrast
is the useful part: **cross-project material can be integrated as a person without its
work becoming canon.**

**Nothing from it is migrated.** The material is derived *from* canon, not a source *for*
it, so migrating it would invert the dependency.

## 4. Two things to flag

**A name collision, considered and passed over.** `Artist Concept Development` lists
**`Elias Ward`** as candidate #2 for a real solo-artist name, beside `Calder Rowe`,
`Jonah Black` and others. It was **not chosen** — one occurrence, no development. Recorded
so it is not revived without noticing that it is a Concord antagonist's name.

**A Concord system this repository does not have.** `Song Review and Evaluation` cites
*"your Romance System (S4–S6 energy)"*. The repository's romance ladder is `HEAT`,
**`H0`–`H4`** — five levels, `H`-prefixed. An `S4`–`S6` scale is **six-plus levels and a
different prefix**, so it is not a rename of `HEAT`.

Either a separate system exists outside this repository, or the reference is loose. Same
shape as the Silence-and-Hope gap (work-queue item 9b): **a system referred to as canon
from outside, with no file here.** Not resolved. Flagged for the author.

## 5. One incidental provenance fact

`Artist Identity and Lyrics` builds its band OS on a **PCM profile of the author** — "The
Calder Base", Thinker base with Harmonizer/Promoter past phases and a Rebel active phase.
It is a document about the author's creative process, **not a character**, and is not
canon. Noted only so it is not mistaken for a character sheet on a later pass.
