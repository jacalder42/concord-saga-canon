# B01 redraft: the author's answers to Q-HR1–5, and his notes on the reply

**Date:** 2026-09-30
**Status:** CURRENT AUTHOR RULING. **Approved design for the B01 revision after the author's read,** except where a row
says otherwise.

**The source.** It answers the questions in `reports/B01_REDRAFT_HUMAN_READ_NOTES_E00_E12_CHECK_2026-09-30.md` (§6, as
revised in §7.4). The notes they follow are `decisions/B01_REDRAFT_HUMAN_READ_NOTES_E00_E12_AUTHOR_NOTES_2026-09-30.md`.

**The author held these, then released them:** *"Released."*

**What this does not change:**
- **No manuscript text.** The author's read continues (he is through E12), and nothing is edited until it ends.
- **No card, cast row, overlay or packet yet.** Those changes are listed in §3 and are made when the revision's packets
  are built.
- The one immediate change is the writer profile line in Q-HR1.

## 1. The author's words

> *"Thoughts on previous reply:*
> *1- why would Lucien be involved if his job is city timber stock? Seems unrelated / unclear*
> *2- to be clear, change Mara's first name*
> *3- yes Renee's current reaction is almost unbelievable. Her child dies and she simply walks out of the room without
> reaction.*
> *4- the form doesn't have to be readable, but it doesn't need to be described or it will be missed and confused.*
> *Q-hr5a - yes / Q-hr5b - yes / Q-hr5c - yes*
> *Q-hr5d - it's allowed, especially as he gets more involved with Seraphine*
> *Q-hr2 - they should be (slightly) more engaged in the goings-on. They could be named or perhaps just speak to each
> other. I am open to whichever time fits the revised draft best.*
> *Q-hr3 - agreed / Q-hr1 and q-hr4 - agreed"*

**Earlier in the same exchange,** before the hold:
- *Q-hr2:* the very last beat, or immediately before the last chapter, *"and it shows them intrigued by something
  happening"*;
- *Q-hr3:* Renée is the mother and Odile the grandmother; *"I lean toward the phone call later"*;
- *Q-hr4:* *"something institutional"*, and future confusion with Mara Niht;
- *Q-hr5:* *"the specifics of the lie were not clear when listening. The simple statement of fact works, but there's no
  hint to the reader that it will be important."*

## 2. What is accepted

| # | Accepted | Status |
| --- | --- | --- |
| **Q-HR1** | **The contrast-construction family** (*she X, not Y*, *not X but Y*, *Not X.*, *not because*, *not quite*) is kept only where the rejected alternative is what a reader would expect, or where the contrast changes the meaning | **Applied now:** writer profile §12, widening its existing line. The watch-list question stands |
| **Q-HR2** | **E00's two presences get behavioural clues** (him, silence; her, hope). **They return slightly more engaged in what is happening:** intrigued by something, not only watching. **They may be named, or may simply speak to each other.** Placement: the book's very last beat, or just before the last chapter, whichever fits the revised draft | Approved design. **It amends the prologue prose packet's *"never named"* / *"keep off the page: names"* guard,** by the author's direction. The rest of that guard stands: no cosmology, no prophecy, no preview |
| **Q-HR3** | **Renée is the mother and Odile the grandmother.** Renée's grief becomes specific and believable. The author: her current reaction is *"almost unbelievable"*, walking out of the room without reaction. **The renewal is forgotten in the emergency.** Odile's line during the resuscitation reminds Seraphine. **She first raises it with Odile in a later phone call** (E09's calls). The E01 porch-step telling goes; E03's telling to Caro becomes the first | Approved design |
| **Q-HR4** | **Seraphine's workplace gets an institutional name,** shortened in use to *the center*. **Trip's E03 line is fixed**, so Mara no longer reads as the boss. **Mara's first name changes** (cast row A01), because of the later clash with Mara Niht (G08) and Mira (L01). Her introduction and role are made clear at her entrance | Approved design. **The rename is a ruling on A01's name. The new name is not yet chosen** (Q-HR7). The registry and packets change when it is |
| **Q-HR5a** | **Lucien is with the Dominion, in New Orleans on its assignment, under a Dominion-supplied cover organization** | Approved design. **It amends A4** (`decisions/OPEN_QUESTIONS_AUTHOR_ANSWERS_2026-09-27.md`), where the cover was *a legitimate bureau*. B1's *"the cover's exact form is open"* is now answered. Lucien knows. The Dominion is still first named on the page at B02 E08 |
| **Q-HR5b** | **Both tensions, in separate places on the form.** The employer or commissioning line carries the cover name. The observation line carries his false denial of what happened to him in the room | Approved design |
| **Q-HR5c** | **The *None* is made legible.** The observation question is unmistakable, E10's shortened reference is fixed, and **the reader gets a hint that it matters** | Approved design. See note 4 in §4 |
| **Q-HR5d** | **Lucien's point of view may think about the cover**, more as he becomes involved with Seraphine | Approved design. **It amends** B01's entry state (*"not a field agent"*) and the B01 overlays' ban on him voicing distrust of his office, as far as the cover requires |

## 3. What changes when the revision's packets are built

The build needs Q-HR6 and Q-HR7 answered first.

**Canon and substrate:**
- `canon/cast_registry.csv` row A01: Mara's new name. Her retired first name goes into `cast_retired_aliases.csv`.
- **A01 is B01's pantry Mara, not G08 Mara Niht.**
- `book_context/book_context_B01.json` entry state: who sent Lucien (the Dominion, under cover). This replaces the stale
  *"OPEN"* line.
- **The B01 act overlays' forbidden shortcuts.** The cover organization's name becomes allowed. *"Who sent Lucien"* stays
  off the page as the Dominion until B02 E08.

**The revised EBCI and prose packets:**
- E00 and the book's last beat or last chapter (Q-HR2);
- E01, E02, E03 and E09 (Q-HR3);
- E03, E08 and every Mara packet (Q-HR4);
- E04, E10, E14 and E24, and the *None*'s later uses (Q-HR5).

**Carried as a dependency:** A1, Seraphine's discovery of the *None*. It stays as designed, because Q-HR5c's hint comes
from Lucien and the page, not from her.

## 4. The author's notes on the reply, and what they raise

| # | Note | What it means for the revision |
| --- | --- | --- |
| **1** | **Why would Lucien be involved if his job is the city's timber stock?** | On the page, the link is one line in E04: he joined the coroner's contract list as part of a brief on how the city records its buildings. **The author finds it unrelated and unclear.** With Q-HR5a there is a stronger answer, but it decides what the Dominion sent him to do, so it is a question (Q-HR6) |
| **2** | **Change Mara's first name** | Accepted in Q-HR4. The name is Q-HR7 |
| **3** | **Renée walks out without reaction** | Accepted in Q-HR3 |
| **4** | *"the form doesn't have to be readable, but it doesn't need to be described or it will be missed and confused"* | **Read as:** the form need not be reproduced, but what it asks and what he writes must be **described clearly enough** to be followed, or it is missed. **If the author meant the opposite, this row is corrected** |

## 5. New questions

| # | Question | Recommended |
| --- | --- | --- |
| **Q-HR6** | **Why is Lucien on the coroner's contract list?** | **The timber brief is his cover. The contract list is his real assignment's doing.** The Dominion's observation posting has him put his name where the city's unusual incidents are recorded, which is where a coroner's contract inspector gets sent. This makes the inspection at the house where Dré died the assignment working, not a coincidence. It also gives the *None* a second motive: writing down his own episode would put him on record at exactly the kind of incident he was sent to watch quietly. That connects to E38's *keep a low profile*. **It decides what the Dominion sent him to observe**, within B1's *"observation posting"* and *"Virelli knows NOLA only as a case file"* |
| **Q-HR7** | **Names.** (a) The center's institutional name. (b) Mara's new first name | **The author's to choose.** Options can be offered on request. Both should be fictional and checked against the cast registry for clashes |

## 6. Addendum: the *None*'s hint (author, 2026-09-30)

> *"In response to your 'one thing to weigh' - I think Lucien could have hitched in his breathing, hinting at his
> discomfort with the falsehood."*

**Accepted as the Q-HR5c hint (approved design).** When he writes the *None*, or confirms it, **Lucien's breath hitches.**
It is a small physical sign of his discomfort with the falsehood.

**It resolves "the one thing to weigh":**
- **Seraphine does not react aloud and does not learn of the *None* early.**
- **A1's later discovery stands.**

**Placement, at the revision:**
- **E04**, where he writes it alone in the truck; or
- **E10**, where he signs it a second time at Guidry's counter, in front of a witness who could notice.

**It works as a hint, not as the whole of the moment.** Profile §12 warns against stock physical tells doing all the
emotional work. The form's question must still be clear (Q-HR5c) for the hitch to point at something.

## 7. Addendum: the hint in two steps, and Q-HR6 (author, 2026-09-30)

> *"I think the hitch or sigh alone could make it clear he's uncomfortable with something. E10 could give a further hint
> letting the reader what Lucien is uncomfortable with.*
> *Q-hr6 - it seems difficult to resolve a timber study and the coroner's report. Unless Renee home is included in the
> area of study and he is reviewing all municipal costs associated with the timber area (which help link in swamp stuff
> later), but that still feels like a tenuous link. Perhaps his cover is helping the Parish review unexpected costs /
> events, which makes a more plausible connection to the death, and the timber can still be woven in…?"*

**The hint, in two steps (approved design; refines §6):**
- **E04:** a hitch or a sigh as he writes the *None*. It says only that he is uncomfortable with something.
- **E10:** a further hint that tells the reader **what** he is uncomfortable with, when he confirms it at Guidry's
  counter.

**Q-HR6: the author's direction, as a lean.**
- **The cover is work helping the parish review unexpected costs and events.** That gives him a plausible reason to
  inspect the house where a child died, for the coroner. The timber study stops being his brief.
- **The timber is woven in instead:**
  - as his professional expertise, which is why the review sends a structural engineer;
  - through his hands-on work with Sal.
- **What it replaces:** the recommendation in §5, which kept the timber brief as the cover and tied the coroner list to
  the Dominion. That recommendation is withdrawn.
- **What it fits:**
  - the page's own phrase for his brief, *the relation between what was recorded and what was done*, which reads
    naturally as a review of costs against events;
  - Lucien's canon card (*a structural analyst within a civic … systems bureau*);
  - the Dominion's observation posting (B1). A review of a parish's unexpected events is a legitimate way to see every
    unusual incident, which is what the Dominion wants watched.

**One check for the revision: which authority commissions the review.**
- **The camp is past the parish line.** Guidry is a neighbouring parish's coroner (E04, E10).
- **Lucien's other institutional contacts in B01 are the city's:**
  - the city's line and letters;
  - the city's table (E21);
  - the pump station (E24).
- **So there are two possible commissioners:**
  - **the neighbouring parish alone**, which puts his city contacts outside his cover;
  - **a regional review across the parishes around the city**, which covers both.

**This is left to the author** (Q-HR6a). The cover organization's name stays Q-HR7.

## 8. Addendum: Q-HR6a answered (author, 2026-09-30)

> *"Regional gives us more flexibility and better cover for him."*

**Answered (approved design).** Lucien's cover is a **regional** review of unexpected costs and events across the
parishes around the city. **It covers both of his official contacts:**
- the neighboring parish's coroner (the camp);
- the city (the line, the table, the pump station).

**The names are drafted** as options for Q-HR7 in `proposals/B01_NAMES_OPTIONS_Q_HR7_2026-09-30.md`.
