# B01 under-120k test: the Sudowrite import report and ChatGPT's self-assessment, reviewed

Status: NON-CANONICAL editorial report, 2026-10-02. It records Claude's review of three things:
- ChatGPT's compressed version of B01 draft 3, made by the author to test Sudowrite's novel import, which is capped at 120k words;
- the manuscript report and story bible that Sudowrite generated from it;
- ChatGPT's own assessment of its version against the reference works.

**It changes nothing.** No manuscript edits are made, and revision is **on hold until the author releases it**. No ruling, card, packet or profile line is changed. The compressed version is not adopted. Under the scope instruction (`decisions/SUDOWRITE_REVIEW_SCOPE_AUTHOR_INSTRUCTION_2026-09-30.md`), Sudowrite's book-level claims are not evidence on their own.

Following the standing rule for this public repository, this report quotes no manuscript text. Passage-level detail is kept in chat and in the private manuscript repository.

---

## 1. The compressed version

- **Baseline:** ChatGPT worked from draft 3 at manuscript commit `8586e9e`, which is before the realism pass. Its version therefore lacks:
  - the E01–E02 transport fix;
  - Lucien's consultancy through the licensed firm;
  - the realism repairs;
  - Guidry's follow-up at E38 and E48.
- **Size:** 116,044 words against the baseline's 132,869. Every scene is kept.
- **Measured changes:**
  - average sentence length fell from 10.2 to 9.0 words;
  - contrast constructions fell from 0.78 to 0.60 per 1,000 words;
  - paragraphs of 80 words or more fell from 316 to 77, while paragraphs of 10 words or fewer stayed at about 2,100;
  - all italics are lost, possibly in the .txt export.
- **Verdict (Claude, three act readers, verified):** worse than its source on balance.
  - **Losses:** about fifteen serious ones across the acts. Dependencies were cut: E04's witness statement, E10, Baz's rule against leading a witness, E21, E22, the coroner-form provenance, and the told/untold rationale.
  - **The ending is weakened:** E46's private *None* scene, E48's signed account, and E49's non-attribution line.
  - **New errors:**
    - E37 conflates two characters;
    - E46 contradicts the book on missing men;
    - E34 pre-empts E41's discovery;
    - E04 ends on an incoherent line;
    - E12 has an orphaned line;
    - E49 mentions a character before his introduction.
  - **A guard breach at E49:** standing water responds to a watcher's attention. That attributes a response to the watchers, which E49 must not do.
  - **Voices:** the characters' speech is flattened toward one clipped register.
  - **Gains:** fewer contrast constructions, some fair trims, an improved E30, and two small new interior beats (E13, E30), which §3 discusses.

## 2. Sudowrite's import report and story bible

**The summaries are accurate.** Sudowrite's synopsis and fifty chapter summaries match the text wherever they were sampled. The employer line, Caro's calendar at E28, and Seraphine seeing the *None* at E44 all check out. Unlike the blind read of 09-30 (ledger §316, §318), this read had the whole book and a story bible behind it. **Its chapter-level reading has earned somewhat more weight; its book-level opinions still do not count on their own** (the 09-30 instruction).

**Where it agrees with independent findings:**
1. **Act II slows during the procedural testing.** This matches the author's note on times (ledger §347) and the times-and-privacy proposal (Q-TM1–3).
2. **The prologue feels disconnected.** This matches the beta panel (ledger §313) and the already approved Q-HR2 (clues to E00's presences, and a reprise). Cutting E00 is not available: it is ruled.

**One risk it exposes.** Sudowrite reads the phenomenon as having a rule: community presence shields people, and isolation exposes them. Its synopsis ends on that theme. The book refutes it (the gathering is struck at E46, and Seraphine concedes her assumption was wrong), and the phenomenon stays unexplained. A whole-book machine reader missed the refutation. **During the author's read, check whether a reader of the current draft would miss it too.** This is something to test, not a defect.

**One continuity check on the current draft, queued.** Lucien mails his correction at E36. At E44 the file Seraphine sees still carries only his *None*, and by E48 the correction is attached. Nothing on the page explains the gap, and a reader can take E44 to mean she is alone on the record. The check comes after the author's read.

**Declined, with reasons:**
- **Reduce the Inez and Caro points of view.** Those POVs are authorised design. Clear scene breaks are fair advice, and the import kept the breaks.
- **Recast the gray cases as bureaucratic neglect.** This conflicts with approved design: unattributed actors who want only the time (Q-EN), and the third pressure (Q-XP). Its useful core is that the watchers should feel ordinary and paperwork-bound. That fits the approved governance frame (Q-GV) and needs no change.
- **Put the anomaly's exact mechanics in the story bible.** Never feed raw canon or an explanation to prose generation (CLAUDE.md §9 step 6). The phenomenon is never explained on the page.
- **Use Rewrite > Shorter.** That is a tool rewrite of the manuscript, and revision is on hold.

**If Sudowrite is used further,** its generated story bible should not stand. It states interpretations as facts, such as the shielding theme and a declared romantic realisation. Replace its contents with a short bible built from the prose packets: characters, places, and the surface rules a reader can see, with no explanation.

## 3. ChatGPT's self-assessment

ChatGPT now describes its version as mainly a compression pass with a few substantive improvements, not a full voice revision. It compares the version with *The Graveyard Book*, *Bride* and *Rivers of London* (by passage) and with the saved craft studies for *Dungeon Crawler Carl* and *He Who Fights with Monsters*.

**Verified:**
- the long-paragraph collapse (316 → 77), with short dialogue paragraphs almost untouched;
- the E42 example: the compression turns a precise injury in Caro's speech into a general one;
- the two new beats in E13 and E30, which are its additions and not in the baseline;
- E48's clipped summary.

Its count of changed paragraphs (387 of 4,799) uses a different method from Claude's. That does not change the finding.

**Its pattern diagnosis agrees with the record:**
- speakers answer the thematic point;
- characters converge on polished formulations;
- gestures receive authoritative interpretations;
- conversations close cleanly.

This is the over-articulacy risk found in the reference-craft review (ledger §353), and it is covered by profile §5A, by *nobody reads minds*, and by the watch-list's recurrence question (ledger §359). The point is not new. It is fresh confirmation that the residue sits in short dialogue, which a compression pass cannot reach.

**Where Claude disagrees:**
1. **"Retain this draft as the working version" is not recommended.** The assessment omits the new errors, the E49 guard breach and the lost dependencies in §1. It also starts from a baseline older than the realism pass, so its version would need those repairs and the realism changes ported in.
2. **Its scene priorities stay valid.** Wherever the next revision happens, it should look at the dialogue and conflict in E21, E35, E42 and E46, at whether discoveries change the next move in E20–E26, E36–E39 and E48, and at action with interiority inside it in E39, E46 and E49. They belong in the post-read revision list, not in a new pass now.
3. **The E13 and E30 beats are worth carrying forward**, subject to the author's approval at revision. They are small and emotionally unfinished, they show a private want through behaviour, and they come from outside the current draft.

## 4. What this leaves for after the author's read

- **For the Sudowrite test:** if a version under 120k is still wanted, a targeted trim of the current realism-pass draft (132,972 words) is the better base. It would keep the measurable gains, protect the dependencies and voices in §1, and export with italics. This is not started, because revision is on hold.
- **Added to the post-read revision list:**
  - the E36 → E44 → E48 correction gap (§2);
  - a check that the E46 refutation reads (§2);
  - ChatGPT's dialogue, mystery and action priorities (§3);
  - the E13 and E30 beats as candidates (§3).

**Next: the author's read.**
