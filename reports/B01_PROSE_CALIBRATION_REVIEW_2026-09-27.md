# B01 prose calibration: E06, E13, E15, a qualitative review

**Date:** 2026-09-27
**Status:** EDITORIAL REVIEW (production), qualitative and not scored. It is the stop required by
`decisions/WRITER_PROFILE_APPROVAL_AND_PROSE_CALIBRATION_AUTHOR_RULING_2026-09-27.md`.

**The three drafts are calibration drafts, not canonical prose.** They are **not committed**: the
repository is public *"until narrative generation"* (CLAUDE.md §6), and whether prose is published here is
the author's call (Q-CAL4). They were delivered to the author separately.

**What it does not change:** the writer profile, the packets or anything else. Recommendations only.

## 1. How the drafts were made

- **The engine** was a separate Claude agent for each episode, **not Sudowrite**. Each agent was told to
  read only its drafting stack:
  - the approved writer profile;
  - the episode's prose packet;
  - a short note of what came before, written from the POV's side;
  - for a POV character's first appearance, one card line about how they notice.
- **No control layer, writer options, causal card or future architecture reached it.**
- **Length:** E06 2,785 words, E13 3,047, E15 2,558.
- **One caveat:** there is no preceding prose yet, so each stack carried a context note Claude wrote from
  the preceding packets. Real drafting replaces that note with the prose itself.

## 2. The six questions

### 2.1 Does one voice survive all three modes?

**Yes.** Ordinary life (E06), intimacy (E13) and a public event (E15) sound like one writer:
- dry and warm;
- specific about places and people;
- funny from pressure, not performance;
- happy to sit in a silence.

The register shifts correctly: E06 is loose and sociable, E13 close and slow, E15 fast and plural.

### 2.2 Do characters act like people rather than endpoint-delivery systems?

**Yes, with the endpoints reached by behaviour, not announcement.**
- **E06:** *"the room holds her"* arrives because Seraphine starts drying glasses when the host is short
  a pair of hands, and nobody asks her anything.
- **E13:** the After state (each steadies the other with something concrete; each lets the other's way
  of knowing count) arrives through a plumb bob that won't hang still in the wind. She holds the string;
  he turns what she is carrying into a numbered list. Neither fixes the other.
- **E15:** Seraphine reaches individuals: a card reader's cut hand, a lost boy, a man about to be
  blamed. Lucien cannot say *yes* when asked whether he heard it.

### 2.3 Did prose discover worthwhile material the architecture did not prescribe?

**A great deal, and it is the strongest evidence that the packets leave room.**
- **E13:** a plumb bob *"designed for two people"*, and a list of strangers she can't put down, ending
  with her own name at the bottom.
- **E06:** free Monday beans, a rice-fund jar, *"rice on the bottom"*, a card game, a birthday sung in
  three keys.
- **E15:** a guitarist's hand-lettered sign; a police officer's question mark beside *amplifier*.
- **Details that pay forward:**
  - E15's *"You did. On Tuesday."* (the coffee order) pays E13–E14's trust without anyone naming it.
  - E13's *"eleven, not ten"* gives E14 its ordinary decision for free.

### 2.4 Does the strange remain observable rather than explained?

**Yes in E15, which is exact.**
- Some hear a low sound and most don't; the amp cracks and quits.
- Two phones record it.
- Witnesses argue *amp first* against *before the amp*, *earthquake*, *gas main*.
- Nobody wins, and nobody explains it.

**Mostly yes in E13:** the post reads true while the rails still lean. Two small slips are listed in §3.

### 2.5 Does humour come from character and pressure?

**Yes.** Every laugh is local:
- the domino players;
- *"Two-drink minimum"* as the answer to a chemistry question;
- a card reader's *"Don't you dare make the joke"*;
- Seraphine's *"Oh, fuck off"* at being counted.

**Profanity appears twice in three episodes**, both times where it's true. None of it feels like the
profile being satisfied.

### 2.6 Did the profile itself create repeated Calderisms or AI tells?

**Mostly no, but the engine has its own tics, and they recur across all three drafts:**

| Pattern | E06 | E13 | E15 | Cause |
| --- | --- | --- | --- | --- |
| *"the way…"* as a simile scaffold | 8 | 10 | 8 | engine |
| shoulders dropping or rising as the emotional tell | 3 | 2 | 2 | engine (stock tell) |
| *"It wasn't a question"* and its variants | 1 | 1 | 1 | engine |
| *"a breath she hadn't known she was holding"* | 1 | — | — | engine (a known AI cliché) |
| a short one-line paragraph after a long one | frequent | frequent | frequent | **the profile**, used well so far; watch it |

**The profile's named techniques do not yet read as a checklist.**
- Profanity, white space and *"one precise expletive"* are all restrained.
- The humanising beat after a sharp line appears, but not every time.

**The watch item is the short-punch paragraph.** It is the one profile technique that shows in all three.
It still reads as rhythm, not as a tic.

## 3. Problems, sorted by cause

### Instruction problems

These come from the profile, the packet or the stack, and would recur with any engine.

1. **E06 contradicts canon: Trip is a woman.**
   - The draft made Trip a big, grey-haired man and gave him a teenage relative (*"She had Trip's
     eyebrows"*).
   - Canon (`TripAppearance`, `TripID`): **Trip is she**, 5'6"–5'8", *"owns the room without needing
     to dominate it"*, with a locked family (her mother Tally, her drag parent Birdie).
   - **Cause:** the packet says only *"Trip is hosting"*, and Q-WP3 allows a first-appearance card line
     **only for POV characters**. A non-POV recurring character arrived with no anchor, and the engine
     invented one.
   - **This is the calibration's one canon contradiction** (Q-CAL1).
2. **E13: Seraphine reads content, not pressure.**
   - She knows *"she's leaving him; he doesn't know yet"* and *"somebody's sick, somebody he loves"*.
   - The draft hedges some of it (*"I think"*), but canon attunement reads **intensity and pattern,
     never thoughts or stories**.
   - **Neither the profile nor the packet says so** (Q-CAL2).
3. **The context notes misled twice.** This is Claude's stack, not the profile.
   - **E13:** the note listed *"even a small domestic task went wrong"* among the strange failures, so
     the draft turned E12's shelf into a leaning shelf. E12's packet says that failure *"has nothing to
     do with anything else"*.
   - **E15:** the note gave no elapsed time, so Lucien has carried it *"for a month"*. B01's calendar
     makes it about two weeks.
   - In real drafting the preceding prose replaces these notes (Q-CAL3).

### Engine and draft problems

These are ordinary first-draft matters, not grounds to change the profile.

- **The four recurring tics in §2.6.**
- **E15 invents three earlier incidents** for Lucien (a laundromat, a stairwell, a streetcar stop) that
  the book does not have. The stack gave no account of his earlier moments.
- **E13 names a direction** (*"downhill, toward the river"*). E11 keeps Lucien from naming or mapping
  one.

## 4. Recommendations

- **Q-CAL1: extend the first-appearance line to any recurring character's first on-page appearance, not
  only a POV character's.** For a non-POV character, the line anchors identity: pronoun, and one
  presence or role fact. Example: *Trip (she) owns the room without needing to dominate it.*
  - **Recommended: yes.** It is the only fix here that prevents canon contradictions.
  - It adds no layer: one line, only at first appearance.
- **Q-CAL2: add one line to the profile's *strange on the page*:** *Nobody reads minds. Sensing a room is
  sensing pressure and distress, never thoughts or stories; a guess about someone is a guess.*
  - **Recommended: yes.** It is a standing Veil rule, not an episode fact.
- **Q-CAL3: when preceding prose does not exist yet,** the context note uses the preceding packets'
  *Ends* lines as written, plus the approximate elapsed time, with no grouping or characterisation.
  - **Recommended: yes.** It is a process note for Claude, not a profile change.
- **Q-CAL4: where drafts live.**
  - **Recommended:** keep calibration and draft prose out of the public repository until you decide
    whether the repository goes private at narrative generation, or where prose is kept.
  - `manuscript/` is ready when you say so.
- **The tics stay out of the profile for now.** Recurring *"the way…"* similes and shoulder tells belong
  to a revision pass, or to the real engine's settings. If they persist with Sudowrite, one line in the
  profile's tells list would be the fix.

**Verdict:** the stack works. It produced three alive scenes with real invention, one voice, and the
strange kept observable.
- **Before drafting Act I sequentially:** fix Q-CAL1 and Q-CAL2.
- **Everything else** is ordinary draft revision.
