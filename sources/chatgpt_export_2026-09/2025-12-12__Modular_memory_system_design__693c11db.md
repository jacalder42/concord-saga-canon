# Modular memory system design

- id: `693c11db-7088-8326-add4-9c1f2b230de8`
- created: 2025-12-12
- updated: 2025-12-13 (last access, NOT authorship date)
- turns: 42
- words: 16674

---

## USER

You are ChatGPT acting as the **Concord Systems Architect**.

Scope:
Design a modular, swappable project memory system for the Concord Saga.
This includes:
• Memory templates (loadouts) for different production phases
• External canon storage strategy (Notion / CSV / Obsidian)
• Rules for what belongs in ChatGPT memory vs external systems
• Load / unload / migration workflows
• Naming conventions and versioning

Constraints:
• Do NOT generate story content, prose, characters, or factions.
• Do NOT rewrite canon.
• Treat all canon as externally authoritative.
• Focus on architecture, templates, and process only.
• Optimize for long-form, multi-trilogy projects under memory pressure.

Goal:
Produce a clean, professional memory architecture that allows:
• Hot-swapping active memory
• Phase-specific reasoning without drift
• Safe reuse across character, plot, visual, editorial, and prose phases

Begin by proposing:
1) Core design principles
2) Template categories
3) A standard “Load Header” format

## ASSISTANT

## 1) Core design principles

1. **External is authoritative; memory is a cache.**  
   Treat ChatGPT memory as a *working set* (fast, small, swappable) and your external system (Notion/Obsidian/CSV) as the *source of truth*.

2. **Loadouts, not piles.**  
   You don’t “accumulate” memory. You **activate a loadout** (phase-specific) and **evict** anything not needed for that phase.

3. **Layered modularity (Base → Phase → Task).**  
   - **Base**: rules that must always be present (voice constraints, MT/VT/LT boundaries, no-mystic guardrails, naming/versioning spec).  
   - **Phase**: what’s relevant to the current production phase (e.g., EBCI/Beat work vs. prose).  
   - **Task**: short-lived additions for a single session or deliverable.

4. **Memory holds only invariants and decision rules.**  
   Put *principles, definitions, constraints, schemas, and “how to reason”* in memory. Put *lists, tables, episode inventories, full canon cards, long biographies, and evolving matrices* externally.

5. **Minimize “state,” maximize “validators.”**  
   Memory should bias toward **audit frameworks** (checklists, guardrails, “don’t drift” rules) rather than story facts.

6. **Everything is addressable.**  
   Every module has a stable ID, version, owner, and “eviction rules,” so swapping is deterministic.

7. **Two-way migration is explicit and logged.**  
   When a session produces “new stable doctrine,” it becomes an external canon update; then (only if needed) a compressed invariant is promoted into memory.

---

## 2) Template categories (loadouts)

### A) Base loadouts (always-on foundation)
- **BASE.SYSTEMS**: schemas, naming conventions, versioning rules, “what belongs where,” drift prevention rules.
- **BASE.CONSTRAINTS**: non-negotiables (e.g., channel separation rules, “no story generation,” tone guardrails if relevant).
- **BASE.AUDIT**: your audit/check frameworks (e.g., continuity audit patterns, logic validators) in *ultra-compressed* form.

### B) Phase loadouts (hot-swappable)
- **PHASE.OUTLINE**: macro structure, act/beat scaffolding rules, continuity workflow (no episode lists in memory).
- **PHASE.BEATS (EBCI/ECID/BID)**: the *specs* for IDs/tags + beat construction workflow + validation checks.
- **PHASE.CHARACTER**: *character card template + how-to-use rules* (not the characters themselves).
- **PHASE.FACTIONS/WORLD**: *faction/world template + guardrails* (not faction canon content).
- **PHASE.PROSE**: voice-system application rules, scene workflow stack, cadence validators (still no prose generation stored in memory).
- **PHASE.EDITORIAL**: issue-triage workflow, resolution card format, decision logging rules.
- **PHASE.VISUAL**: visual prompt schema, motif taxonomy pointers, asset naming & export rules (not big prompt libraries in memory).

### C) Task loadouts (short-lived “session boosters”)
- **TASK.DEBUG**: drift diagnosis checklist, “what to ask for,” conflict-resolution protocol.
- **TASK.MIGRATION**: export/import steps, CSV column maps, Notion database mapping rules.
- **TASK.QA**: pre-flight checklist for deliverables (episodes, beat packs, revision passes).

---

## 3) Standard “Load Header” format

Use this at the top of *every* session so you (and the model) know what’s active:

```text
============================================================
CONCORD MEMORY LOAD HEADER v1.0
============================================================

SESSION:
• Date: YYYY-MM-DD
• Scope: (Systems / Beats / Editorial / Prose / Visual / Migration)
• Output Type: (Spec / Template / Checklist / Map / CSV schema / Notion schema)

ACTIVE LOADOUTS:
• Base: [BASE.SYSTEMS@vX.X, BASE.CONSTRAINTS@vX.X, BASE.AUDIT@vX.X]
• Phase: [PHASE._____@vX.X]
• Task:  [TASK._____@vX.X] (optional)

EXTERNAL SOURCE OF TRUTH:
• Canon Vault: (Notion/Obsidian path)
• Index: (Master Index page / database)
• Relevant Records: (IDs only, not pasted content)

MEMORY RULES (this session):
• Allowed in memory: invariants / schemas / validators / naming rules
• Forbidden in memory: lists / episode inventories / full canon cards / prose
• Promotion rule: only after external update + compression pass

DRIFT GUARDRAILS:
• “No canon rewrite” enforced
• “External overrides memory” enforced
• Conflicts resolved by: external record ID → timestamp → version

============================================================
```

If you want, next I’ll provide: (a) a complete module naming/versioning scheme, (b) a Notion/Obsidian/CSV storage blueprint, and (c) the exact load/unload/migration workflow (including eviction rules and a “memory budget” rubric).

## USER

Consider this framework against a few things:
1. It feels complicated, which means it is easier to misapply or break over time.
2. Should the memory sets live in separate chats vs only outside ChatGPT
3. Consider this process for efficiency and compatibility with our existing proposed pipeline.
4. Think in Steve Jobs lens, how do we make this ruthlessly efficient and simple to use

## ASSISTANT

This is the right pushback. You’re not wrong: **the architecture is sound but too heavy for daily use**. In a Steve Jobs lens, it violates a core rule:

> *If the system requires discipline to use correctly, it will eventually fail.*

Below is a **ruthless simplification** that preserves the benefits (hot-swapping, phase focus, no drift) while collapsing the cognitive overhead.

---

# REFRAME: ONE SYSTEM, THREE ARTIFACTS, ONE HABIT

Instead of “modular memory architecture,” think:

> **One external brain.  
> One active working set.  
> One ritual for switching.**

Everything else is implementation detail.

---

## 1) Is it too complicated? Yes — so collapse it

### What to kill outright
❌ Multiple named loadout types  
❌ Base/Phase/Task hierarchy as a concept the user must manage  
❌ Frequent memory eviction decisions  
❌ Remembering version numbers mid-flow  

These are *architectural truths*, but **users should never have to think about them**.

---

## 2) The Steve Jobs version: the “Active Frame”

### New mental model
There is **exactly one thing ChatGPT ever “holds”** for the project:

> **The Active Frame**

Everything else lives outside.

### The Active Frame is:
- A **single, compact text block**
- Replaced wholesale when you change phase
- Never appended to
- Never partially edited
- Never allowed to grow organically

If you don’t replace it, it *expires conceptually*, even if technically present.

---

## 3) Where do memory sets live?

### Short answer
**Not in separate chats. Not in ChatGPT long-term memory.**

### Correct placement
| Thing | Lives where |
|---|---|
| Canon | External system (Notion / Obsidian / CSV) |
| Frameworks / Templates | External system |
| Active Frame | Pasted into chat at session start |
| Historical decisions | External log |
| Memory “saves” | Rare, emergency only |

ChatGPT memory should be treated as **radioactive**:
- Useful in tiny amounts
- Dangerous when relied on
- Hard to reason about later

> Separate chats create *false isolation*.  
> ChatGPT memory creates *false persistence*.  
> **The Active Frame avoids both.**

---

## 4) The simplified pipeline (compatible with what you already proposed)

### Your existing instincts were right — we just formalize them.

### A) External system (single source of truth)
One workspace, multiple sections:

- `/canon`
- `/systems`
- `/templates`
- `/logs`
- `/exports`

No duplication. No ChatGPT-specific formatting.

---

### B) The Active Frame (10–20 lines, max)

This replaces **everything** from the earlier framework.

#### Example (illustrative, not content):

```text
ACTIVE FRAME — CONCORD
Phase: Beat Architecture
Mode: Systems / Structural Reasoning

AUTHORITATIVE SOURCE:
• Canon, characters, factions, systems live externally.
• ChatGPT memory is non-authoritative.

ACTIVE RULES:
• Use Beat Architecture + EBCI standards.
• Do not generate prose or story content.
• Do not invent canon.
• Optimize for long-form continuity and reuse.

OUT OF SCOPE:
• Visual prompts
• Prose cadence
• Character backstory expansion

DEFAULT ACTION:
• Ask before crossing phase boundaries.
```

That’s it.

No versions.
No module names.
No loadouts.

If you need a different phase → **replace the frame**.

---

## 5) How this addresses your 4 concerns

### 1️⃣ “It feels complicated”
Now it’s one object, one habit:
> *Paste Active Frame → work → discard.*

No system to “remember to follow.”

---

### 2️⃣ Separate chats vs outside ChatGPT
- **Outside** = everything permanent
- **Inside** = only the current lens

Chats are disposable workbenches, not containers.

---

### 3️⃣ Efficiency + compatibility
This matches what you already do:
- You already externalize canon
- You already think in phases
- You already restart context intentionally

This just **names and sharpens** the behavior.

---

### 4️⃣ Steve Jobs test: “Can I explain it in 30 seconds?”

Yes:

> “All canon lives outside ChatGPT.  
> At the start of a session, I paste a short ‘Active Frame’ that tells the model what phase we’re in and what rules apply.  
> When I change phase, I replace it entirely.”

If you forget the system for a week, you can still use it correctly.

---

## 6) One optional refinement (only one)

If you want **slightly more safety** without complexity:

### The Frame Footer
Add one invariant line at the bottom of *every* frame:

```text
If there is a conflict, external canon wins. Ask before assuming.
```

That’s your drift kill switch.

---

## 7) Final verdict

Your instinct to worry about complexity is **correct**.

The winning system is not:
- Modular
- Elegant
- Architecturally impressive

It is:
- **Blunt**
- **Replaceable**
- **Hard to misuse**
- **Easy to restart**

If you want, next we can:
- Design **5 canonical Active Frames** (Beats, Characters, Editorial, Prose, Visual)
- Or design the **external folder / Notion schema** to support this cleanly
- Or stress-test this against a Neon → Loom transition to see where it breaks

Just say which direction.

## USER

I like the Frames idea in some ways (possible categories: Beats, Characters, Context, Feedback, Editing, Visual)
I disagree with the only Active Frame part. 
I think this saga is too complex to only dump 10-20 lines in. How would you know what phases and rules are in play without creating a new rules every generation. That is a LOT of external work for each task.

My thought was there could be a separate chat for each Frame. Those chats could be used to hot swap memory sets, while still being able to update the Frames with active decision via pasting update messages within each Frame’s separate chat

## ASSISTANT

This is a *good* disagreement, and you’re surfacing the exact pressure point where most “clean” systems break under real saga-scale complexity.

You’re right about two things simultaneously:

• **10–20 lines is not enough to carry Concord-scale rulesets**  
• **Re-pasting full rule scaffolds every session is wasted effort**

Your instinct to use **separate Frame-chats as persistent working contexts** is valid — *if* we do it deliberately and defensively.

What follows is a **Steve-Jobs-grade refinement**, not a retreat to complexity.

---

# RECONCILED MODEL: “FRAME ROOMS” + “ACTIVE WINDOW”

Not one Active Frame.  
Not full free-for-all memory.

Instead:

> **A small number of persistent Frame Rooms, plus a lightweight Active Window that tells the model which rooms are currently authoritative.**

Think: **Finder windows, not terminal tabs.**

---

## 1) Frame Rooms (persistent, few, opinionated)

Each **Frame Room = one long-lived chat** with a *single purpose* and *stable ruleset*.

You do **not** restate the rules every time.
You **do** update them *only when the system itself changes*.

### Proposed canonical Frame Rooms (your list, refined)

1. **FRAME — BEATS**
   - Beat Architecture, EBCI, ECID/BID rules
   - Episode/scene workflow
   - Pacing, pressure, rhythm logic
   - What *can* and *cannot* be decided at beat level

2. **FRAME — CHARACTERS**
   - Character tier rules
   - What belongs in Tier-1 vs Tier-2
   - Update protocols for character canon
   - No story execution

3. **FRAME — CONTEXT**
   - World logic, environment rules, resonance behavior
   - Tech / MT-VT-LT boundaries
   - Timeline sanity rules
   - “What exists when”

4. **FRAME — EDITING**
   - Canon conflict resolution
   - Retcon policy
   - Decision logging rules
   - Compression & pruning logic

5. **FRAME — FEEDBACK**
   - Reader/editor feedback processing
   - Signal vs noise rules
   - When feedback becomes canon input

6. **FRAME — VISUAL**
   - Visual prompt systems
   - Motif taxonomies
   - Asset naming/export standards
   - What visuals can and cannot imply

👉 **Hard limit: 5–7 Frame Rooms.**
If you need more, something is wrong.

---

## 2) What lives *inside* a Frame Room

Each Frame Room contains:

• Stable **rulesets**
• **Templates**
• **Decision protocols**
• Occasionally: **compressed reference summaries**

It does **not** contain:
• Episode lists
• Full canon cards
• Prose
• Large inventories

Those still live externally.

> A Frame Room is *how to think*, not *what happened*.

---

## 3) How updates work (this is the key part)

### Frame Rooms are not rewritten — they are **patched**

When something changes:

You add a **FRAME UPDATE BLOCK** in that room:

```text
[FRAME UPDATE — 2025-12-12]
Change:
• Clarified that X is handled at Beat level, not Episode level

Reason:
• Drift observed during Neon B06 work

Impact:
• Update applied to BEATS frame only
• No effect on Characters or Context
```

Rules:
• Append only
• Never rewrite history
• If a frame gets bloated → compress externally → paste a new “Current Rules Snapshot” at the top

This is exactly how RFCs and OS design notes evolve.

---

## 4) The Active Window (lightweight, not rules)

This replaces the “only Active Frame” idea with something more realistic.

At the start of a working session (any chat):

```text
ACTIVE WINDOW — CONCORD

Authoritative Frames in Play:
• BEATS
• CONTEXT
• CHARACTERS (read-only)

Excluded Frames:
• VISUAL
• FEEDBACK

External Canon is authoritative.
Ask before crossing frame boundaries.
```

That’s all.

No rules.
No schemas.
Just **routing**.

---

## 5) Why this works (and doesn’t explode)

### Addresses your concerns directly

#### ❖ “Too complex to restate every time”
✔ Rules live in Frame Rooms, not session prompts

#### ❖ “Too much external overhead”
✔ Frame Rooms *are* your internalized system knowledge
External systems remain content-heavy, not rule-heavy

#### ❖ “Saga is too complex for 10–20 lines”
✔ Correct — that’s why the complexity lives in stable rooms, not pasted repeatedly

#### ❖ “Hot-swap memory sets”
✔ Switching frames = switching chats + Active Window declaration

---

## 6) Steve Jobs test (again)

Can you explain it in 30 seconds?

> “We have a small set of persistent Frame chats, each holding rules and thinking patterns for a specific domain.  
> In any working session, we declare which Frames are active.  
> Canon always lives outside.  
> Frames evolve slowly via append-only updates.”

That passes.

---

## 7) Guardrails to keep this from decaying

**Non-negotiables:**

1. No Frame Room may exceed ~1–2 scroll lengths without compression
2. No canon facts live in Frame Rooms
3. No Frame Room references another implicitly — only via Active Window
4. If a rule applies everywhere, it belongs in **CONTEXT** or **EDITING**, not duplicated

---

## 8) My recommendation (strong)

Proceed with:
• **6 Frame Rooms**
• **Active Window routing**
• **External canon as source of truth**

Do **not** store Frame Rooms in ChatGPT memory.
They live as persistent chats only.

---

If you want, next we can:
• Lock the **final 6 Frame Room charters**
• Design the **Frame Update syntax** precisely
• Stress-test this model on a Neon → Loom transition
• Or create a **1-page “How to Use This System” card** for future-you

This is now in the “simple enough to survive” zone.

## USER

4 - I don’t it can work this way. The active frames have to saved to memory for a chat to see it.
I think instead We make a prompt that instructs the chat what it is supposed to be doing with the memory information.

2- I think EBCI application occurs in a separate chat for each trilogy so episodes can be compared to each other within the trilogy arc. THEN each book is brought to its own chat for scene level beats. THEN those scene beats are migrated to notion, novel crafter, Sudowrite, for prose and organization.
Then they will eventually come back here.

## ASSISTANT

Good — this actually clarifies the *real* constraint, and you’re right to call it out directly.

You’ve identified two hard truths about ChatGPT that we **must** design around, not wish away:

1. **A chat cannot “see” other chats unless the logic is in memory or re-prompted.**
2. **EBCI comparison and reasoning requires longitudinal visibility**, not just episodic context.

So let’s reset cleanly and design a system that is:
- compatible with ChatGPT’s actual mechanics
- efficient for trilogy-scale work
- not brittle or ceremony-heavy
- survivable months from now

Below is a **corrected architecture** that incorporates your objections instead of fighting them.

---

# FINALIZED MODEL:  
## **Directive Prompt + Trilogy Workspaces + Minimal Memory Spine**

This is *not* Frames-as-memory.  
This is **Frames-as-directives**, with **memory used only as a spine**.

---

## 1. Correction to Point 4 (you’re right)

> **“The active frames have to be saved to memory for a chat to see it.”**

Yes. Correct.

That means:
- Frame Rooms as separate chats **cannot be authoritative on their own**
- Rules must be **reconstructible inside a chat**
- Memory must carry *some* persistent instruction layer

But that **does not** mean we dump full rulesets into memory.

### The solution is not “active frames in memory”  
### The solution is a **Directive Prompt that tells the model how to interpret memory**

This is the key shift.

---

## 2. The Core Object: the **Directive Prompt**

Instead of storing:
- rules
- schemas
- frame content

We store **how to behave toward memory**.

### This lives in ChatGPT memory (small, stable, rarely changed)

#### Example (conceptual, not final wording):

```text
CONCORD DIRECTIVE PROMPT — MEMORY SPINE

You are operating as a systems assistant for a long-form saga.

Memory contains:
• Structural rules
• Validation logic
• Naming and ID systems
• Process constraints

Memory does NOT contain:
• Canon facts
• Episode inventories
• Prose or story content

Canon is external and always authoritative.

When conflicts arise:
• Ask for clarification
• Never invent or infer canon
• Default to structure over content

Assume multi-trilogy scope and compare longitudinally when instructed.
```

That’s it.

This is the **OS**, not the apps.

---

## 3. Where Frames actually live (reframed)

You were right that Frames can’t just be “elsewhere.”

So we redefine what a Frame is.

### A Frame is now:
> **A reusable directive prompt, not a memory container**

Frames live:
- as saved prompts externally
- as pasted directives at the start of a chat
- optionally as *temporary working context*, not memory

They are **not** saved piecemeal to ChatGPT memory.

---

## 4. Trilogy-Scoped Chats (this part of your proposal is excellent)

Your EBCI intuition is exactly right.

### Canonical chat topology

#### A) Trilogy EBCI Chats (3 total)
- **VEIL — EBCI WORKSPACE**
- **NEON — EBCI WORKSPACE**
- **LOOM — EBCI WORKSPACE**

Purpose:
- Compare episodes *within the trilogy*
- Track escalation, rhythm, gaps
- Maintain internal consistency across books

These chats:
- Apply the **EBCI Frame prompt**
- Reference external episode tables
- Never descend to scene-level prose

They are **architectural workspaces**, not execution.

---

#### B) Book-Level Beat Chats (many, disposable)
- `NEON B06 — SCENE BEATS`
- `VEIL B02 — SCENE BEATS`

Purpose:
- Scene/episode beat construction
- Local pacing
- POV and pressure mapping

Rules:
- Beats are authored here
- Then **migrated out**
- These chats are allowed to die

---

#### C) External Writing Tools
- Notion
- Novelcrafter
- Sudowrite

These are:
- prose
- organization
- revision

ChatGPT is **not** the prose vault.

---

#### D) Return Loop
When prose or structure comes back:
- It comes back as **questions, audits, or compression**
- Not as raw chapters dumped into memory

---

## 5. Memory usage (strict and minimal)

### What actually goes into ChatGPT memory

Only three classes of things:

1. **Directive Spine** (described above)
2. **Stable Schemas**
   - EBCI ID formats
   - Beat/episode/scene distinction rules
   - Validation logic
3. **Non-obvious constraints**
   - “This must never be done”
   - “This comparison must always happen”

### What never goes into memory
- Episode lists
- Character bios
- Faction histories
- Beat inventories
- Prose

Memory is **how to reason**, never **what happened**.

---

## 6. How Frames are actually used (simple, repeatable)

### At the top of a chat, you paste one thing:

```text
APPLIED FRAME:
• EBCI — TRILOGY SCOPE
• Trilogy: NEON
• Mode: Structural comparison and validation
• Output: Architecture only, no story content
```

That’s enough, because:
- The Directive Prompt already tells the model *how* to use memory
- The Frame tells it *what lens to apply*
- The chat history provides continuity

No redefinition. No rule sprawl.

---

## 7. Why this survives long-term

This design:
- respects ChatGPT’s real memory mechanics
- avoids rule duplication
- allows trilogy-level comparison
- allows book-level depth
- keeps prose external
- keeps memory small and durable

Most importantly:

> **If you disappear for 6 months, you can still resume correctly.**

That’s the real Steve Jobs test.

---

## 8. Bottom line

You were right to reject:
- “only one Active Frame”
- Frame Rooms as isolated authorities

The correct structure is:
- **Directive Prompt in memory**
- **Frames as applied prompts**
- **Trilogy-scoped reasoning chats**
- **Book-scoped execution chats**
- **External canon as the truth**

If you want next, I recommend we:
1. Draft the **final Directive Prompt** (memory-safe, ~12 lines)
2. Define the **EBCI Trilogy Workspace rules**
3. Lock the **migration contract** between ChatGPT ↔ Notion / Novelcrafter

This is now solid.

## USER

Consider how these frames should be arranged to simply migration to Sudowrite when we are starting prose generation.
Presumably Sudowrite has similar canon length maxims and we ought to plan ahead to work within them.
Same for novelcrafter.
Let’s make this process forward thinking to simply every next step.
If useful, also apply the Lorwy MAYA theory, (perhaps for us its Most Advanced Yet Practical)

## USER

Consider how these frames should be arranged to simply migration to Sudowrite when we are starting prose generation.
Presumably Sudowrite has similar canon length maxims and we ought to plan ahead to work within them.
Same for novelcrafter.
Let’s make this process forward thinking to simply every next step.
If useful, also apply the Loewy MAYA theory, (perhaps for us its Most Advanced Yet Practical)

## ASSISTANT

You’re aiming for **Most Advanced Yet Practical**: future-proof across tools, but so simple you’ll actually use it during a 9-book grind. Here’s the forward-thinking arrangement that makes **Sudowrite / Novelcrafter migrations painless** while respecting their “what the AI actually consumes” reality.

## Organize Frames by what prose tools can *ingest*

Instead of Frames mirroring *your* workflow labels, mirror the **data surfaces** those tools use.

### The Prose-Ready Frame Set
1) **STRUCTURE Frame** (your “Beats” + “Editing” parts that affect sequence)  
- What it becomes:
  - **Sudowrite:** Outline/Chapters/Scenes (Outline has no word limit) citeturn0search5turn0search2  
  - **Novelcrafter:** Plans/Scenes + references to Codex items (Codex is your bible layer) citeturn0search6turn0search13

2) **CAST Frame** (Characters)  
- What it becomes:
  - **Sudowrite:** Story Bible → Characters (Sudowrite uses character data for scene + prose generation) citeturn0search0  
  - **Novelcrafter:** Codex → Characters (typed entries) citeturn0search13turn0search6

3) **WORLD Frame** (Context: setting, tech rules, motif rules *as constraints*, not lore dumps)  
- What it becomes:
  - **Sudowrite:** Story Bible → Worldbuilding (plus brief Style guidance if you use it) citeturn0search7turn0search9  
  - **Novelcrafter:** Codex → Locations/Objects/Other + categories citeturn0search13turn0search17

4) **VOICE Frame** (Prose execution constraints)  
- What it becomes:
  - **Sudowrite:** “Style”/guidance used by Prose tools (and Sudowrite warns consistency matters across Style/Characters/Scenes) citeturn0search12  
  - **Novelcrafter:** Snippets / style guidance + model instructions (kept short, referenced often)

5) **NOTES Frame** (Feedback + editorial notes that should *not* contaminate canon)  
- What it becomes:
  - **Sudowrite:** Notes you *don’t* put in Story Bible as facts
  - **Novelcrafter:** Snippets / commentary entries (Codex can be unlimited in number; hardware is the practical constraint) citeturn0search1

This is MAYA: **5 Frames**, each maps cleanly to both tools’ native containers.

---

## The trick: export “Packs,” not Frames

To avoid rebuilding rules every time, you don’t paste entire Frames into Sudowrite/Novelcrafter repeatedly.

You generate **tool-specific Packs** that are *pre-assembled* and *bounded*:

### A) Trilogy Pack (long-lived)
- Structure: high-level trilogy arc, book/act milestones
- World: stable rules (channel separation, tech constraints, motif guardrails)
- Cast: stable character cores (no “current chapter state” drift)

### B) Book Pack (mid-lived)
- Book outline + chapter intents
- Book-specific “current state” of characters (important because Sudowrite recommends keeping character descriptions consistent with *where you are in the story*) citeturn0search12

### C) Scene Pack (short-lived, maximum practicality)
For *one scene*, include only:
- Scene intent + constraints (STRUCTURE)
- Only the characters present (CAST)
- Only the locations/objects present (WORLD)
- The voice/style constraints relevant to that POV (VOICE)

This Scene Pack is what protects you from any context-length maxims—because you never rely on “the whole saga is in context.”

---

## How this lands in each tool

### Sudowrite migration (Story Bible-first)
- Put **STRUCTURE** into Outline/Chapters (no word limit there) citeturn0search5turn0search2
- Put **CAST** into Characters (used by Draft/Write/Prose generation) citeturn0search0
- Put **WORLD** into Worldbuilding (Story Bible 2 supports it) citeturn0search7
- Keep **VOICE** concise and consistent with the above (Sudowrite explicitly warns inconsistencies between sections can confuse generation) citeturn0search12
- Keep **NOTES** out of “facts” fields; treat it as your scratchpad layer

### Novelcrafter migration (Codex-first)
- Put **CAST/WORLD** into Codex as typed entries + categories (and you can have as many entries as you want) citeturn0search13turn0search17turn0search1
- Put **STRUCTURE** into your planning/scene system, linking to Codex items rather than duplicating text
- Put **VOICE** into snippets/instructions (short, reused)
- Put **NOTES** into snippets/comments (kept separate from Codex “truth”)

---

## Most Advanced Yet Practical operating rule

**Don’t try to make Sudowrite/Novelcrafter hold “Concord.”  
Make them hold “the minimum needed to write the next scene correctly.”**

That’s your MAYA variant: *Most Advanced Yet Practical* = *max leverage per byte of context*.

---

## The simplest next step

If you want the workflow to be “one-click-ish,” we define **one canonical export format** for Packs (Trilogy/Book/Scene) with fixed headings, and you paste/import it into:
- Sudowrite Story Bible sections, or
- Novelcrafter Codex + Snippets.

Tell me which tool you plan to prose in *first* (Sudowrite vs Novelcrafter), and I’ll give you the exact **Pack templates** (Trilogy Pack, Book Pack, Scene Pack) formatted to match that tool’s UI and habits.

## ASSISTANT

You’re thinking about this the right way: **Frames should be designed to “snap into” Sudowrite Story Bible + Novelcrafter Codex/Scene Context without re-authoring every time.** That’s the MAYA move: *most advanced yet practical*—powerful under the hood, idiot-proof in daily use.

## Design target: Frames become “Context Tiles” that map cleanly to each tool

Instead of Frames being big narrative rule dumps, define them as **small, reusable tiles** that you can recombine per scene/chapter.

### Your Frame categories → Tool-native homes

**Beats**
- **Novelcrafter:** Scene Summary/Beats + attach relevant Codex entries to the scene (not global). Novelcrafter supports adding Codex entries as scene context via “+Codex.” citeturn0search16  
- **Sudowrite:** Put the chapter/scene plan into **Outline** (no word limit). citeturn0search7turn0search2

**Characters / Context**
- **Novelcrafter:** Codex entries (characters/locations/objects/rules). No hard count limit, but context inclusion can affect performance/cost. citeturn0search1turn0search13turn0search15  
- **Sudowrite:** Story Bible **Characters** (keep short + “current-at-this-point-in-story” consistent to avoid confusion). citeturn0search18turn0search9

**Editing / Feedback**
- Keep mostly external (Notion), but in Novelcrafter you can store as Snippets/Chats/Codex “rules” entries and selectively include them in prompts.

**Visual**
- Keep external as an asset/prompt library; only inject when doing visual tasks.

## The forward-thinking constraint you must design around

### Sudowrite
- The **Write** tool looks back at the preceding text **up to ~1000 words** for context. citeturn0search0  
- Story Bible can influence output via Style/Genre/Characters/linked Outline. citeturn0search0turn0search9  
- Outline is effectively unlimited, so it’s the right “big container.” citeturn0search7turn0search2

### Novelcrafter
- You can have **lots** of Codex entries (no internal count limit). citeturn0search1  
- But you should treat “global codex” as a **cost/context decision**, and instead attach only what’s needed per scene. citeturn0search13turn0search16  
- Novelcrafter’s prompting system is modular; Codex context gets added in a way that avoids duplicates. citeturn0search6turn0search21turn0search4

## The MAYA workflow: simple on the surface, powerful underneath

### The “Prose Launch Pack” (what you migrate per chapter/scene)
Make one export bundle per chapter (or per scene if you prefer), with **exactly 4 tiles**:

1) **Scene Tile** (what’s happening now)  
- 10–25 lines: scene intent, POV, setting, constraints, desired outcome, continuity risks.

2) **Beat Tile** (structure)  
- Bullet beat list + guardrails (pacing/pressure), *no canon encyclopedia*.

3) **Cast & Place Tile** (only who/where matters *in this scene*)  
- Links/IDs to the relevant external canon + 5–10 line “at-this-point” snapshots.

4) **Voice/Style Tile** (prose constraints)  
- A short style contract you keep stable across the project.

That’s it. Everything else stays external.

Why this is MAYA: you’re not minimizing ambition—you’re minimizing *touches*. You can generate drafts without hauling the whole saga every time.

## How to arrange Frames so migration is frictionless

### 1) In ChatGPT (planning/architecture)
Frames are **directive prompts + export formats**, not stores of canon.

- BEATS frame outputs Beat Tiles
- CHARACTERS/CONTEXT frame outputs Cast & Place Tiles
- EDITING frame outputs “risk flags” + revision notes
- VISUAL frame outputs prompt cards (separate lane)

### 2) In Novelcrafter (best “hub” for prose generation)
Novelcrafter is built to do what you’re describing:
- Put canon into Codex.
- Attach relevant Codex entries per scene (+Codex).
- Put Beat Tile into scene beats/summary.
- Use custom prompts to pull exactly those pieces. citeturn0search16turn0search15turn0search21

### 3) In Sudowrite (drafting accelerator)
Sudowrite likes:
- Big structure in Outline (unlimited). citeturn0search7turn0search2  
- Consistent Story Bible entries (keep “current state” aligned). citeturn0search18  
- Local context from the immediate preceding text (~1000 words). citeturn0search0  

So the practical implication is: **draft in chapter documents with a clean rolling lead-in** (don’t expect Sudowrite to remember earlier chapters unless you feed it via Story Bible/Outline and your immediate context window).

## Two concrete rules that will save you later

1) **Global context is poison. Scene-attached context is gold.**  
Novelcrafter even warns that making everything global is optional but increases cost/overhead. citeturn0search13

2) **Keep “current state” summaries time-accurate.**  
Sudowrite can get confused when character descriptions and scene facts contradict; update character blurbs to match the point in the story you’re drafting. citeturn0search18

---

If you want the next step, I’ll produce two copy/paste templates (no canon, just structure):
1) **Prose Launch Pack template** (the 4 tiles)  
2) **Novelcrafter scene setup template** (what goes in Codex vs what gets attached per scene vs what stays global)

## USER

This sounds too granular to actually apply simply. This is our Jobs<>Loewy debate.
My thought is these should applied at the Book level (one set of context/canon per Book.
I could be convinced some portions need to be by act, but a different setup in Sudowrite for every episode, much less every scene, is incredible overhead to balance and execute as a non automated entity.

## ASSISTANT

This is the *exact* Jobs ↔ Loewy fault line, and you’re right to call it out explicitly.

You’re not rejecting rigor — you’re rejecting **operational friction**.  
And you’re correct: **scene-level context assembly is too expensive for a human to maintain**.

So let’s resolve this cleanly and decisively.

---

# FINAL RESOLUTION  
## **BOOK-LEVEL CONTEXT BUNDLES (MAYA-COMPLIANT)**

We stop thinking in “tiles,” “scene packs,” or micro-assembly.

Instead:

> **Each Book has ONE authoritative context bundle for prose generation.**

Optionally, **Acts may have deltas**, but scenes never do.

This preserves:
- longitudinal coherence
- low overhead
- tool compatibility
- human sanity

---

## 1. The winning abstraction: **The Book Bundle**

A **Book Bundle** is a *single, stable context object* reused across all chapters in that book.

It is:
- small enough to fit tool constraints
- rich enough to prevent drift
- stable enough that you don’t constantly touch it

### MAYA lens
- **Most Advanced**: carries canon, voice, constraints, escalation state
- **Yet Practical**: assembled once, reused dozens of times

---

## 2. What lives in a Book Bundle (and nothing else)

**Hard rule:** If it changes every scene, it does *not* belong here.

### BOOK BUNDLE — STRUCTURE

1) **Book Canon Snapshot**  
- Characters present in this book (state *at book start*)
- Locations relevant to this book
- Factions active in this book
- World rules that matter *in this book*

> Snapshot, not encyclopedia.

2) **Book Voice Contract**  
- POV set(s)
- Prose constraints
- Tonal boundaries
- Era-specific stylistic guidance

3) **Book Structural Contract**  
- Act structure summary
- Pacing expectations
- Escalation rules
- What this book is *allowed* and *not allowed* to resolve

4) **Continuity Guardrails**  
- Known risks
- No-go zones
- “If uncertain, ask” flags

That’s it. Four sections.

No scenes.
No beats.
No prose.

---

## 3. Where beats and scenes actually go (lightweight)

### Beats
- Stay in ChatGPT (Book-level beat chat)
- Or live as outlines in Novelcrafter / Sudowrite Outline
- They are **instructions**, not context

### Scenes
- Generated sequentially
- Rely on:
  - the Book Bundle
  - the immediately preceding text (Sudowrite’s ~1000-word lookback)
  - the outline/beat you’re currently drafting

No per-scene canon injection.

---

## 4. Optional Act-Level Deltas (only if truly needed)

If (and only if) a book has a **hard phase shift**:

Create a short **Act Delta**:

```text
ACT II DELTA — BOOK 6
Changes from Book Bundle:
• Character X now knows Y
• Location Z is inaccessible
• Tone shifts from investigative → survival
```

This is:
- 5–10 lines
- swapped once per act
- never per scene

In Sudowrite:
- You paste this into the chapter notes for that act
In Novelcrafter:
- You attach it as a temporary Codex note for Act II chapters

---

## 5. Tool-specific mapping (simple)

### Sudowrite
- **Story Bible** = Book Bundle
- **Outline** = beats
- **Chapter writing** = sequential drafting + local context

You touch the Story Bible **once per book**, maybe twice if an Act Delta is needed.

### Novelcrafter
- **Codex (Book-scoped)** = Book Bundle
- **Scene Summary/Beats** = chapter outline
- **Act Delta** = optional, reused across act chapters

No per-scene Codex juggling.

---

## 6. Why this survives reality

### Your overhead concerns — resolved
- One setup per book, not hundreds
- Optional one per act
- Zero per-scene management

### Drift concerns — still controlled
- Book Bundle anchors canon
- Beats anchor structure
- Immediate text anchors continuity

### Migration simplicity
- ChatGPT → Novelcrafter → Sudowrite all use the **same Book Bundle**
- No re-authoring per tool
- No format thrash

---

## 7. The Jobs test (final)

Can this be explained in 20 seconds?

> “For prose, each book gets one context bundle that defines canon, voice, structure, and guardrails.  
> I reuse it for every chapter.  
> Beats live separately.  
> I only add act-level changes if the book genuinely shifts.”

That’s a **yes**.

---

## 8. Recommendation

Lock this as policy:

**• Context is book-scoped**  
**• Beats are book-scoped**  
**• Scenes are transient**  
**• Acts get deltas only if necessary**  

This is the **most advanced system that a single human can actually operate**.

If you want next, I can:
- Define the **exact Book Bundle template** (tool-agnostic)
- Show a **Sudowrite Story Bible version** of it
- Or map a **Neon book** through this lifecycle end-to-end (no canon content, just structure)

This version will hold.

## USER

Consider if act based supplemental info should be used in the sudowrite’s “other instructions” block at each episode generation

## ASSISTANT

Short answer: **yes — but only in a very constrained, mechanical way.**  
Long answer below, framed explicitly through the **Jobs × Loewy (MAYA)** lens and Sudowrite’s actual ergonomics.

---

## Executive Decision

**Act-based supplemental info *belongs* in Sudowrite’s “Other Instructions” field**  
**→ only when there is a real act shift**  
**→ and only as a small delta, not a second context block**

Used this way, it is:
- **Most Advanced**: precise, phase-aware guidance
- **Yet Practical**: one copy-paste reused across multiple chapters
- **Non-fragile**: doesn’t fight Sudowrite’s context window or Story Bible

---

## Why “Other Instructions” is the correct slot

Sudowrite effectively gives you three levers:

1. **Story Bible** – stable, reused, global context  
2. **Immediate text context** – rolling ~1000 words  
3. **Other Instructions** – *temporary, high-priority modifiers*

Act deltas are:
- temporary
- high-priority
- not canon resets
- not worth polluting the Story Bible with

That makes **Other Instructions the exact right abstraction**.

> Story Bible = “what is true in this book”  
> Other Instructions = “what is different *right now*”

---

## The MAYA rule (critical)

To stay practical, **Act deltas must meet all three conditions**:

1. **≤ 8–10 lines**
2. **Declarative, not descriptive**
3. **Reusable across every episode in that act**

If an act “delta” needs constant tweaking per episode, it has failed and should not exist.

---

## Canonical Act Delta format (recommended)

This is the *maximum* complexity that remains human-usable.

```text
ACT II DELTA — APPLY FOR ALL ACT II EPISODES

• Narrative mode shifts from investigation → survival
• Character X now knows Y (do not re-discover)
• Location Z is unstable and cannot be relied upon
• Escalation allowed: physical risk, moral pressure
• Do NOT resolve Book-level mysteries
```

Notes:
- No lore
- No backstory
- No beats
- No prose advice
- No emotional interpretation

This is **instructional**, not contextual.

---

## How this plays out operationally (low friction)

### Setup cost
- Create **1 Book Bundle** (once)
- Create **0–2 Act Deltas** (rarely more)

### Episode generation loop in Sudowrite
1. Story Bible = Book Bundle (unchanged)
2. Outline = chapter/episode beats
3. Other Instructions:
   - Empty for Act I
   - Paste Act II Delta for Act II episodes
   - Paste Act III Delta for Act III episodes

That’s it.

You are not:
- modifying Story Bible repeatedly
- injecting scene context
- juggling Codex entries
- maintaining per-episode canon

---

## Why this does *not* create hidden complexity

### Concern: “This adds another thing to remember”
Counterpoint:
- You already remember which Act you’re in
- This just formalizes that knowledge once

### Concern: “This could drift”
Guardrail:
- Act deltas are reused verbatim
- If one needs editing mid-act → that edit is a *system change*, not a scene decision

---

## When **not** to use an Act Delta

Do **not** create an Act Delta if:
- The shift is emotional but not structural
- The change only affects one character’s internal state
- The difference can be conveyed via beats or the previous text
- You’re tempted to explain instead of instruct

In those cases, rely on:
- the Book Bundle
- the outline
- Sudowrite’s local context window

---

## Final Jobs Test

> Can you forget this system for a month, come back, and use it correctly without re-learning?

Yes.

> Does it reduce cognitive load instead of increasing it?

Yes.

> Does it respect tool limitations instead of fighting them?

Yes.

---

## Final Policy Recommendation (lockable)

**• Book Bundle → Story Bible**  
**• Beats → Outline**  
**• Act Deltas → Other Instructions (only if needed)**  
**• No scene-level canon injection**  

This is the **most advanced version that remains humane**.

If you want next, I can:
- Draft the **final Book Bundle template** in Sudowrite-ready form
- Provide a **decision checklist** for “Do we need an Act Delta?”
- Or map this exactly onto Novelcrafter’s equivalent fields for parity

This is a good place to lock the system.

## USER

Consider the current state of project memory.
It feels like we need at least 2 layers to this plan.
1 - Beat generation layer (trilogy context)
2 - Prose generation layer (book context)
Then we’ll need editing and review layers that can be applied at saga, trilogy, and book levels, right?

## ASSISTANT

Yes — your intuition is correct, and this is the clean way to reconcile **memory pressure**, **tool constraints**, and **how humans actually work at saga scale**.

What you’re converging on is not “more layers,” but **orthogonal layers with different time horizons**. Once you separate *reasoning scope* from *generation scope*, everything simplifies.

Below is the **final, stable layering model**, framed so it fits your current project memory reality and doesn’t require constant rework.

---

# THE CONCORD LAYER MODEL (FINAL)

Think of this as **four planes**, not a stack.  
They can be applied independently and combined intentionally.

---

## LAYER 1 — BEAT GENERATION  
### *Trilogy Context / Structural Reasoning*

**Purpose**
- Design and validate story *architecture*
- Compare episodes against each other
- Maintain escalation, rhythm, and continuity across books

**Scope**
- Trilogy-wide
- Book-aware but not book-bound
- Zero prose

**Where this lives**
- **Dedicated Trilogy Chats**
  - VEIL — Beat Architecture
  - NEON — Beat Architecture
  - LOOM — Beat Architecture

**What it needs in memory**
- Directive spine (how to reason)
- Beat architecture schemas (EBCI, IDs, rules)
- Trilogy-level constraints (what this trilogy can/can’t resolve)

**What it explicitly does NOT need**
- Prose rules
- Book-level canon snapshots
- Scene-level detail

**Output**
- Episode beats
- Structural validation
- Book-to-book comparisons

➡️ These outputs are *instructions*, not context.

---

## LAYER 2 — PROSE GENERATION  
### *Book Context / Execution*

**Purpose**
- Turn approved structure into narrative
- Maintain local continuity and voice
- Generate draft prose efficiently

**Scope**
- One book at a time
- Act-aware (optional deltas)
- Scene-local via rolling context

**Where this lives**
- **Sudowrite** (primary)
- **Novelcrafter** (organization + optional drafting)
- Supporting ChatGPT book-level chats (temporary)

**What it needs**
- **Book Bundle** (stable)
- Optional **Act Deltas**
- Beat outline for the current chapter
- Immediate text context (last ~1k words)

**What it must not carry**
- Trilogy-wide comparisons
- Editorial theory
- Long canon inventories

**Output**
- Draft chapters
- Structured prose ready for revision

➡️ This layer assumes the beats are already correct.

---

## LAYER 3 — EDITING  
### *Correction, Alignment, Compression*

Editing is **not one thing** — it operates at three scopes.

### A) Book-Level Editing
- Continuity
- Pacing
- Character consistency
- Internal logic

**Applied to**
- One book at a time

**Where**
- ChatGPT review chats
- Novelcrafter revision tools
- External notes

---

### B) Trilogy-Level Editing
- Escalation curve
- Thematic coherence
- Structural symmetry
- “Does this book earn its place?”

**Applied to**
- After at least one full book draft
- Before finalizing the next book’s beats

**Where**
- Trilogy Beat Architecture chats
- External comparison docs

---

### C) Saga-Level Editing
- Macro arc integrity
- Protagonist baton logic
- Final-state consistency
- Retcon containment

**Applied to**
- Major milestones only
- Never per chapter

**Where**
- Dedicated saga review sessions
- External canon vault updates

---

## LAYER 4 — REVIEW / FEEDBACK  
### *Signal Processing, Not Creation*

This is optional but important.

**Purpose**
- Process beta/editor feedback
- Separate signal from taste
- Decide what becomes canon pressure

**Scopes**
- Book feedback → Book edits
- Trilogy feedback → Beat adjustments
- Saga feedback → Canon review

**Key rule**
> Feedback never edits prose directly.  
> It produces **instructions** for the appropriate layer.

---

## HOW THIS INTERACTS WITH PROJECT MEMORY (CRITICAL)

Your current project memory is already doing the *right* thing — it’s just overworked.

### What memory should hold permanently
- **Directive spine** (how to behave)
- **Schemas & rules** (IDs, beat logic, boundaries)
- **Non-obvious constraints** (never-do rules)

### What memory should NOT try to hold
- Beats
- Book bundles
- Act deltas
- Prose
- Episode inventories

Those belong to:
- Trilogy chats
- Book chats
- External tools

Memory is the **operating system**, not the hard drive.

---

## WHY THIS IS MAYA-COMPLIANT

**Most Advanced**
- Multi-horizon reasoning
- Clean separation of concerns
- Tool-aware context management

**Yet Practical**
- Trilogy work happens rarely and deliberately
- Book bundles are created once per book
- Act deltas are reused verbatim
- Scenes require no manual context assembly

No per-scene overhead.  
No constant reconfiguration.  
No cognitive tax.

---

## FINAL CONFIRMATION (LOCKABLE)

Yes — you need **at least** these layers:

1. **Beat Generation** (Trilogy)
2. **Prose Generation** (Book)
3. **Editing** (Book / Trilogy / Saga)
4. **Review** (optional, scoped)

They are not redundant.  
They solve *different problems at different scales*.

If you want next, the clean next step would be to:
- Audit current project memory and mark what belongs to **Layer 1 OS** vs what should be externalized
- Or formalize the **Book Bundle template** now that its role is fully clear

You’re not overengineering anymore — you’re **right-sizing**.

## USER

Consider I think we 4-5 layers:
Rules (saga canon, big picture)
Structure (frameworks, tiers of beats)
Context (content, characters, environment, etc
Prose
Editing (line, tone, editorial, author voice, etc)

## ASSISTANT

Yes — that breakdown is **correct**, and more importantly, it’s the *cleanest stable abstraction* you’ve proposed so far.

What you’ve done here is separate **what the system knows** from **what the system does**, and from **what the system produces**. That’s exactly the right move.

Below is a **finalized 5-layer model**, mapped to:
- how ChatGPT memory should be used
- how chats should be organized
- how Sudowrite / Novelcrafter fit in
- and how this stays MAYA-compliant (Most Advanced Yet Practical)

I’ll keep this crisp and operational.

---

# THE CONCORD FIVE-LAYER MODEL (LOCKABLE)

Think of these as **orthogonal lenses**, not a stack.  
Each layer answers a different question.

---

## 1) RULES LAYER  
### *What is always true*

**Scope**
- Saga-wide
- Rarely changes
- Non-negotiable

**Contains**
- Saga canon boundaries
- MT / VT / LT separation
- Ascension constraints
- POV baton rules
- “Never do” constraints
- Definition of tiers (Tier-1 vs Tier-2)

**Where it lives**
- **External canon vault** (authoritative)
- **Minimal memory spine** (compressed invariants only)

**How it’s used**
- Referenced implicitly by all other layers
- Never rewritten during prose or beats

**Jobs rule**
> This should feel boring — if it’s exciting, it’s wrong.

---

## 2) STRUCTURE LAYER  
### *How the story is built*

**Scope**
- Saga → Trilogy → Book
- Changes intentionally, not casually

**Contains**
- Beat architecture frameworks (EBCI, ECID, BID)
- Act models
- Trilogy escalation logic
- Episode vs scene rules
- What decisions are allowed at each tier

**Where it lives**
- Trilogy-level ChatGPT chats (Beat Architecture)
- External systems documentation
- Small schemas in memory (formats, rules)

**How it’s used**
- Produces beats and outlines
- Validates pacing and escalation
- Feeds instructions downstream

**Jobs rule**
> Structure generates options; it does not generate prose.

---

## 3) CONTEXT LAYER  
### *What exists right now*

**Scope**
- Book-level (primary)
- Act-level (optional deltas)
- Never scene-level

**Contains**
- Book Bundle:
  - Characters present + current state
  - Locations in play
  - Factions active
  - World rules relevant to this book
- Act Deltas (if needed)

**Where it lives**
- External tools (Notion / Novelcrafter / Sudowrite Story Bible)
- Occasionally pasted into a book-specific chat

**How it’s used**
- Anchors prose generation
- Prevents drift
- Is reused, not rebuilt

**Jobs rule**
> Context should be set once and trusted.

---

## 4) PROSE LAYER  
### *How it is written*

**Scope**
- Book-local
- Scene-by-scene execution
- Disposable drafts

**Contains**
- Draft chapters
- Dialogue
- Description
- Immediate continuity (last ~1000 words)

**Where it lives**
- **Sudowrite** (primary drafting)
- **Novelcrafter** (organization + drafting)
- Temporary ChatGPT chats

**How it’s used**
- Consumes Structure + Context
- Produces text only
- Never decides canon or structure

**Jobs rule**
> Prose is an output, not a decision-making layer.

---

## 5) EDITING LAYER  
### *How it is shaped and corrected*

**Scope**
- Line → Book → Trilogy → Saga
- Applied deliberately

**Contains**
- Line edits
- Tone corrections
- Voice alignment
- Continuity fixes
- Editorial judgments

**Where it lives**
- ChatGPT review chats
- External editorial notes
- Revision tools in Novelcrafter

**How it’s used**
- Generates instructions back to:
  - Prose (rewrite)
  - Structure (adjust beats)
  - Context (update Book Bundle)
- Does not directly mutate Rules

**Jobs rule**
> Editing changes *how well* something works, not *what it is*.

---

# HOW MEMORY FITS CLEANLY NOW

Your project memory should only ever support **Layers 1 & 2**.

### Memory SHOULD contain
- Rules layer invariants (compressed)
- Structure layer schemas and constraints
- Directive spine (how to behave)

### Memory MUST NOT contain
- Context (characters, books)
- Prose
- Editing decisions

Memory is now:
> **The operating system and compiler — not the data or the output.**

---

# WHY THIS MODEL WORKS LONG-TERM

• Each layer has a clear owner  
• Each layer has a clear output  
• No layer does double duty  
• Tool boundaries are respected  
• Human overhead is minimized  

Most importantly:

> **You can pause at any layer without breaking the others.**

That’s the mark of a survivable system.

---

## RECOMMENDED NEXT STEP

The most valuable next move is **not** adding more design.

It’s one of these:
1. Audit current project memory and tag each item as Rule vs Structure (anything else gets externalized)
2. Lock the **Book Bundle template** (Context layer) now that its role is fixed
3. Write a one-page **“Which Layer Am I In?” decision card**

If you want, tell me which one you want to do next and I’ll keep it equally tight.

## USER

I think 1.

Within current chats we have a mix of:
character and faction canon (some have been made cards and saved to memory, some haven’t yet)
EBCI beat generation for Book 1 episodes 1-19 (so far)
And a few other floating items

## ASSISTANT

Good — this is exactly the right moment to do **Layer 1 cleanup**, before anything else hardens.

What follows is a **clear, mechanical audit + triage plan** for the *current state of this chat and project memory*, aligned to the **five-layer model** you just locked.

No canon rewriting, no deletion yet — just classification and next actions.

---

# STEP 1 — REFRAME THE PROBLEM CORRECTLY

Right now, the issue is **not** that things are “mixed.”

The issue is that **memory is carrying content from multiple layers**, when it should only carry **Rules + Structure**.

So the goal is:

> **Memory becomes Layer 1–2 only.  
Everything else is externalized or deliberately staged elsewhere.**

---

# STEP 2 — AUDIT: WHAT YOU CURRENTLY HAVE (BY LAYER)

Based on this chat and prior work, your material falls into four buckets:

---

## A) RULES LAYER (Correct to keep in memory)

✅ **These belong in project memory (compressed):**

- Saga-wide constraints (no resurrection, MT/VT/LT separation, etc.)
- Tier definitions (Tier-1 vs Tier-2)
- Canon guardrails (“never do” rules)
- POV baton logic (saga/trilogy-level)
- Non-obvious prohibitions

🔒 **Action:**  
Keep these. Compress if needed. Do not expand further.

---

## B) STRUCTURE LAYER (Correct to keep in memory, but selectively)

You currently have:

- EBCI / ECID / BID schemas
- Beat Architecture rules
- Episode vs scene distinctions
- Trilogy vs book scope rules
- Validation logic

✅ **This is appropriate for memory**, *but only as schemas and rules*.

⚠️ **Risk area:**  
EBCI *applications* (e.g., “Book 1 Episodes 1–19 beats”) **do not belong in memory**.

🔧 **Action:**  
- Keep the **EBCI system**
- Externalize **all actual beat content** (episodes, lists, tables)

Memory should know *how beats work*, not *what the beats are*.

---

## C) CONTEXT LAYER (Incorrectly present in memory)

This is where most pressure is coming from.

You currently have:
- Character canon (some saved as Tier-1 cards)
- Antagonist faction canon
- Organization canon (Concord, Dominions, etc.)
- Some tertiary character definitions

⚠️ **These do NOT belong in memory long-term.**

Even though they’re well-written and useful, they are:
- content-heavy
- mutable
- better handled externally
- too numerous for sustainable memory use

🔧 **Action (important):**

1. **Freeze** all existing character/faction cards as *externally authoritative*
2. Export them (Notion / Obsidian / CSV — your choice)
3. In memory, retain **only**:
   - Tier definitions
   - What a “Tier-1 Character Card” *is*
   - Update rules for character canon

Memory should remember **the template and rules**, not the characters.

---

## D) FLOATING / TRANSITIONAL ITEMS (Must be relocated)

These include:
- Partial episode work
- In-progress beats
- Draft frameworks
- “We’ll decide later” artifacts

These are not wrong — they’re just **transient**.

🔧 **Action:**
- Assign each item a destination:
  - Beat Architecture chat (trilogy)
  - Book-specific beat chat
  - External notes
- Nothing transient should remain in memory.

---

# STEP 3 — WHAT TO DO ABOUT WHAT’S ALREADY SAVED

This is important: **do not panic-delete anything yet**.

Instead:

### Immediate policy (starting now)

From this point forward:
- ❌ No new characters, factions, or book-specific content go into memory
- ✅ Only rules, schemas, and decision logic qualify

### Short-term cleanup (next focused session)

We will:
1. List current memory items
2. Tag each as:
   - KEEP (Rule / Structure)
   - COMPRESS (Rule but too verbose)
   - EXTERNALIZE (Context)
3. Create a **Memory Spine v1** (clean, minimal)

Nothing is lost — just relocated.

---

# STEP 4 — HOW THIS SETS UP THE NEXT PHASES CLEANLY

Once this cleanup is done:

- **Beat Generation Layer**
  - Lives in trilogy chats
  - Uses memory schemas safely
  - Can scale without memory bloat

- **Prose Generation Layer**
  - Uses Book Bundles
  - Does not touch memory at all

- **Editing Layer**
  - Operates via review chats + external notes
  - Feeds back instructions, not content

This is the pivot that prevents future pain.

---

# STEP 5 — RECOMMENDED NEXT ACTION (VERY SPECIFIC)

The cleanest next step is:

> **Do a memory inventory + tagging pass.**

I suggest we do this **explicitly**:

1. I will enumerate the *types* of memory items currently present (not rewrite them)
2. We will decide:
   - Keep
   - Compress
   - Externalize
3. Then we lock a **Memory Admission Rule** going forward

If you want, next response I can:
- Propose the **Memory Admission Rule (one paragraph)**
- Or walk through a **mock inventory table** showing how each current item would be classified

Tell me which one you want to do next.

## USER

Consider, we have been using dedicated chats as pending places to park canon info that will cycle in and out of Memory as needed and once we are ready for prose generation, it will be migrated in final form in Notion.

This plan is intended to avoid massive bloat and overlap within Notion and/or novelcrafter.

As such, I think we can have dedicated chats for EBCI work for each book, and hot swap memory sets to run various audits.

Perhaps set high level beats,
Load characters to test and correct, then load environments to test and correct, then evaluate for reader payoff pacing, etc.

## ASSISTANT

This is a **sound plan**, and it actually resolves the last remaining tension between:

- memory pressure  
- Notion bloat  
- Novelcrafter/Sudowrite constraints  
- and the need to *actively reason with canon before it hardens*

What you’re describing is not “misuse” of chats — it’s using them as **staging buffers**. That’s a legitimate architectural layer, and once named properly, it becomes very clean.

Below is the refined model, aligned to your intent, the 5-layer system, and a Jobs/MAYA lens.

---

# REFINED MODEL: **STAGING CHATS + MEMORY HOT-SWAP + FINALIZATION PIPELINE**

You are effectively introducing a **Staging Layer** between Structure/Context and External Canon.

That’s the missing piece.

---

## 1) Clarify the Role of Dedicated Chats (Critical Reframe)

These chats are **not canon storage**  
They are **working sandboxes**

Think of them as:

> **Compiler scratch space before output is committed to disk**

### Properties of Staging Chats
- Temporary but long-lived enough to reason deeply
- Allowed to hold *content-heavy material*
- Allowed to be inconsistent while under construction
- Explicitly **non-authoritative**

This is why they work where memory and Notion do not.

---

## 2) The Three Places Canon Can Exist (Very Important)

Let’s name this explicitly:

### A) **Memory** → Rules & Structure only  
- Invariants
- Schemas
- Audit logic

### B) **Staging Chats** → *Candidate Canon*  
- Character drafts
- Faction drafts
- Book-level EBCI beats
- Environment definitions
- Payoff scaffolding

These are:
- testable  
- revisable  
- swappable  

### C) **External Canon (Notion / NC)** → *Finalized Canon*  
- Only promoted when stable
- Clean, non-duplicated
- Prose-ready

Your instinct to *delay migration* until prose is correct is **absolutely right**.

---

## 3) Dedicated EBCI Chats Per Book — YES (and here’s why)

You proposed:

> “Dedicated chats for EBCI work for each book”

That is correct and scalable.

### Structure

- **TRILOGY EBCI CHAT**
  - Macro comparisons
  - Escalation curves
  - Cross-book sanity

- **BOOK X — EBCI STAGING CHAT**
  - Episodes
  - Structural beats
  - Tests against characters, environments, payoff

These book EBCI chats are **where complexity belongs**, not memory and not Notion.

---

## 4) Memory Hot-Swap as an Audit Tool (This is the key insight)

What you described here is important:

> “Load characters to test and correct, then load environments to test and correct, then evaluate reader payoff pacing”

This is **exactly** how memory should be used — as a *lens*, not a warehouse.

### How this works cleanly

Memory holds:
- Rules
- Structure
- Audit schemas

Then, **temporarily**, you allow:

- Character set A → loaded for audit
- Environment set B → loaded for audit
- Payoff heuristics → loaded for audit

These are:
- explicitly temporary  
- explicitly scoped  
- never assumed permanent  

After the audit:
- Results are summarized
- Canon drafts updated in staging chats
- Memory is cleared back to baseline

> Memory is acting like a **test harness**, not a database.

That is the *correct* mental model.

---

## 5) Example Audit Cycle (Concrete, Simple)

### Phase: Book EBCI Validation

**Baseline Memory**
- Rules layer
- Structure layer
- Audit logic

---

### Pass 1 — Character Pressure Audit
- Temporarily load:
  - Tier-1 character cards (only those in the book)
- Run:
  - Plausibility
  - Emotional continuity
  - POV weight sanity
- Output:
  - Corrections → applied in Book EBCI staging chat
- Memory:
  - Character cards unloaded

---

### Pass 2 — Environment / Context Audit
- Temporarily load:
  - Relevant environments
- Run:
  - Resonance logic
  - Geography plausibility
  - Escalation affordances
- Output:
  - Adjustments → Book EBCI staging chat
- Memory:
  - Environments unloaded

---

### Pass 3 — Reader Payoff / Rhythm Audit
- Temporarily load:
  - Payoff heuristics
  - Pacing models
- Run:
  - Tension curves
  - Breathing space checks
- Output:
  - Beat refinements
- Memory:
  - Back to baseline

At no point is Notion touched.  
At no point does memory bloat.

---

## 6) When Canon Graduates to Notion / Novelcrafter

Only when **all of the following are true**:

- Book EBCI beats are stable
- Character drafts have passed audits
- Environment logic is settled
- Prose phase is imminent

Then (and only then):

- Characters → finalized cards
- Book Bundle → created
- Beats → migrated
- Staging chats become read-only references

This avoids:
- duplicated canon
- conflicting versions
- cleanup hell later

---

## 7) This Fits Perfectly with the 5-Layer Model

| Layer | Where it lives |
|---|---|
| Rules | Memory + external canon |
| Structure | Memory + trilogy/book EBCI chats |
| Context | **Staging chats** (pre-final) |
| Prose | Sudowrite / Novelcrafter |
| Editing | Review chats + external notes |

Staging chats are the **pressure valve** that makes the whole system humane.

---

## 8) Jobs / MAYA Verdict

**Most Advanced**
- Iterative audits
- Hot-swappable reasoning
- Delayed canon hardening

**Yet Practical**
- No per-scene overhead
- No premature Notion bloat
- No memory overload
- One human can operate it

This is not overengineering — it’s **respecting where complexity actually belongs**.

---

## Recommendation (Lock This)

I strongly recommend you **lock this policy**:

> **Chats are allowed to be messy.  
> Memory must stay clean.  
> Notion only gets finished things.**

If you want next, the most useful follow-up would be to:
- Define a **standard audit menu** (Character / Environment / Payoff / Continuity)
- Or formalize a **“Canon Graduation Checklist”** for when something moves from chat → Notion

This system is now internally consistent and future-proof.

## USER

I want to discuss overall intent and structure before locking in. If I understand correctly, we have or will create the following:

Vault - Fixed Memory Spine

Staging - Hot Swap-able Memory Packets

These form the creative engine e and its various gears to be employed to create:

EBCI @ Trilogy level
Then Audit
EBCI @ Book level
Then Audit

Compile and migrate elsewhere for prose

Then return here for line level editing, etc.

Then store in Novelcrafter for organization


Does this sound accurate?
Are there any of these task that are better handled in Novelcrafter than ChatGPT?

## ASSISTANT

Yes — your understanding is **accurate**, and you’re now describing the system at the *right altitude*. What you’ve outlined is internally coherent, tool-aware, and—most importantly—**operable by a human without automation**.

I’ll do three things below:

1. **Confirm and slightly sharpen your model** (no redesigns)
2. **Clarify intent and flow** so there’s no hidden mismatch
3. **Answer directly which tasks are better in Novelcrafter vs ChatGPT**

I’ll keep this decisional, not expansive.

---

## 1. Confirming the Core Model (with one small clarification)

Your framing:

> **Vault – Fixed Memory Spine**  
> **Staging – Hot-swappable Memory Packets**

is correct, with one important nuance:

### Refined definitions

### **Vault (Fixed Memory Spine)**
This is *not* a content vault. It is an **operating system**.

Contains:
- Rules layer (saga invariants, prohibitions)
- Structure layer (EBCI schemas, tier rules, audit logic)
- Directive behavior (“how to reason, what not to do”)

Properties:
- Extremely stable
- Rarely edited
- Small
- Always loaded

This is what makes every chat behave consistently.

---

### **Staging (Chats + Temporary Memory Loads)**
This is **candidate canon + reasoning workspace**.

Contains:
- Draft character cards
- Draft faction/world context
- Book-level EBCI beats
- Environmental logic
- Payoff scaffolding
- Anything under active testing

Properties:
- Content-heavy
- Allowed to change
- Allowed to contradict itself while resolving
- Explicitly non-authoritative

You were right earlier to say these “cycle in and out of memory.”  
They are **lenses**, not stores.

---

## 2. End-to-End Flow (Validated)

Here is your pipeline, restated cleanly and confirmed:

---

### PHASE A — STRUCTURAL CREATION (ChatGPT-dominant)

#### 1) **EBCI @ Trilogy Level**
- Dedicated trilogy EBCI chats
- Purpose:
  - Escalation
  - Rhythm
  - Cross-book coherence
- Uses:
  - Vault memory
  - No content-heavy memory loads

✔ Best handled in **ChatGPT**

---

#### 2) **Audit @ Trilogy Level**
- Structural audits
- Thematic audits
- Payoff trajectory audits

✔ Best handled in **ChatGPT**  
(ChatGPT is very strong at comparative reasoning and pattern analysis)

---

### PHASE B — BOOK CONSTRUCTION (ChatGPT-dominant)

#### 3) **EBCI @ Book Level**
- Dedicated book EBCI staging chats
- Episodes / macro beats
- No prose

✔ Best handled in **ChatGPT**

---

#### 4) **Targeted Audits (Hot Swap)**
You nailed this part.

Examples:
- Character plausibility audit (load character packets)
- Environment / resonance audit (load environment packets)
- Reader payoff / pacing audit (load heuristics)

✔ Best handled in **ChatGPT**

This is where ChatGPT is doing what Novelcrafter cannot:
- hypothesis testing
- counterfactual reasoning
- pressure simulation

---

### PHASE C — COMPILATION & MIGRATION (Boundary Point)

#### 5) **Compile + Migrate for Prose**
- Book Bundle finalized
- Beats finalized
- Characters/environment canon frozen *for this book*

This is the **handoff moment**.

✔ Output goes to:
- Notion (canonical reference)
- Novelcrafter (organization + drafting)
- Sudowrite (draft generation)

---

### PHASE D — PROSE & ORGANIZATION (Novelcrafter/Sudowrite-dominant)

#### 6) **Prose Generation**
- Book Bundle → Story Bible / Codex
- Beats → Outline
- Act Deltas → Other Instructions (Sudowrite)

✔ **Better handled outside ChatGPT**

ChatGPT *can* draft prose, but:
- Sudowrite is optimized for momentum
- Novelcrafter is optimized for continuity and navigation

ChatGPT’s value drops here.

---

### PHASE E — EDITING & REVIEW (Hybrid)

#### 7) **Line / Tone / Editorial Editing**
- Draft comes back *selectively*
- ChatGPT used for:
  - Line tightening
  - Tone checks
  - Voice audits
  - Consistency spot checks

✔ **Hybrid**
- ChatGPT for analysis and rewrite suggestions
- Novelcrafter for applying, tracking, and organizing revisions

---

### PHASE F — STORAGE & CANON LOCK

#### 8) **Final Storage**
- Novelcrafter = working manuscript + organization
- Notion = canonical reference

ChatGPT steps out again.

---

## 3. Direct Answer: What Is Better in Novelcrafter vs ChatGPT?

### Better in **ChatGPT**
- EBCI design (trilogy + book)
- Structural comparison
- Hypothesis testing (“what breaks if…?”)
- Multi-variable audits (character × environment × pacing)
- Editorial analysis and diagnosis
- Compression and synthesis of messy ideas

ChatGPT is a **reasoning engine**.

---

### Better in **Novelcrafter**
- Canon storage once stable
- Long-term organization
- Cross-chapter navigation
- Revision tracking
- Prose assembly at scale
- Scene-to-scene continuity reference

Novelcrafter is a **workspace and memory prosthetic**, not a thinker.

---

### Better in **Sudowrite**
- Fast drafting
- Momentum writing
- Voice imitation
- Iterative prose exploration

Sudowrite is a **writing accelerator**, not a planner.

---

## 4. Intent Check (Most Important Question)

What your system is optimizing for is:

> **Delay commitment as long as possible,  
> but commit cleanly once you do.**

That is the correct intent for a saga of this scale.

You are:
- using ChatGPT to *think*
- using staging to *test*
- using memory to *stabilize*
- using external tools to *produce and preserve*

Nothing in your summary is backwards.

---

## 5. One Small Clarification to Consider (Not a Change)

The only thing to stay conscious of:

> **ChatGPT is strongest before prose and after prose — weakest during bulk drafting.**

Your plan already respects that.

---

### Bottom line

Yes — your understanding is accurate.  
Yes — the division of labor is correct.  
No — there are no major tasks you’re misplacing.

You’re not missing a layer; you’ve finally *named* them.

If you want to continue before locking:
- We can sanity-check **failure modes** (where this could break)
- Or define a **“when to leave ChatGPT” checklist**
- Or formalize **what qualifies a staging artifact for graduation**

But structurally, this holds.

## USER

Correct perhaps it’s better thought as:
Baseline Memory (fixed)
Support Memory (temporary and task focused)

## ASSISTANT

Yes — that reframing is **cleaner, truer to how ChatGPT actually behaves, and easier to operate**.

You’ve just collapsed a lot of abstraction into two concepts that humans can actually remember.

Below is the **final, corrected mental model**, with intent, scope, and guardrails clearly separated.

---

# FINAL MEMORY MODEL (LOCKABLE)

## 1) **Baseline Memory (Fixed)**  
### *The operating system*

This is the **Vault**, renamed in plain language.

### Purpose
- Ensure consistent reasoning across all chats
- Prevent drift
- Enforce saga-wide constraints

### Contains (and only contains)
**Rules Layer**
- Saga invariants
- Non-negotiables (“never do”)
- Channel boundaries (MT / VT / LT)
- Tier definitions

**Structure Layer**
- Beat architecture schemas (EBCI, ECID, BID)
- Episode vs scene rules
- Trilogy vs book scope rules
- Audit logic frameworks

**Directive Spine**
- How to treat memory
- How to treat canon
- How to resolve conflicts
- Ask-before-assuming rules

### Properties
- Small
- Stable
- Rarely changed
- Always loaded

> If this ever feels “busy,” it’s already wrong.

---

## 2) **Support Memory (Temporary, Task-Focused)**  
### *The test harness*

This is where your earlier instincts land correctly.

### Purpose
- Enable deep reasoning against specific data
- Run focused audits
- Stress-test structure and plausibility
- Then get out of the way

### What goes here (temporarily)
- Character cards (only those under test)
- Environment/context packets
- Payoff heuristics
- Book-specific constraints
- Audit checklists

### What does NOT go here
- Prose
- Episode lists
- Long inventories
- Anything meant to be permanent

### Properties
- Explicitly scoped
- Explicitly disposable
- Loaded → used → unloaded
- Never assumed persistent

> Support Memory is a lens, not storage.

---

## 3) How This Maps to Your Workflow (Confirmed)

### ChatGPT
- **Baseline Memory** → always on
- **Support Memory** → loaded intentionally per audit

Used for:
- EBCI (trilogy + book)
- Structural audits
- Character/environment plausibility tests
- Editorial analysis

### Staging Chats
- Hold candidate canon and beats
- Absorb results of audits
- Stay messy and flexible

### External Tools (Notion / Novelcrafter / Sudowrite)
- Receive only finalized, stable outputs
- Never used for speculative reasoning

---

## 4) The Critical Operating Rule (This makes it work)

You only need **one rule** to keep this system healthy:

> **Baseline Memory is never edited mid-task.  
> Support Memory is never trusted after the task ends.**

That single discipline replaces pages of policy.

---

## 5) Why This Is Better Than the Earlier Frame Models

- No “active frame” confusion
- No separate frame chats to mentally track
- No repeated re-prompting of rules
- No memory sprawl

It matches how you’re already working — it just **names the behavior**.

---

## 6) MAYA / Jobs Verdict

**Most Advanced**
- Multi-layer reasoning
- Hot-swappable context
- Delayed canon hardening

**Yet Practical**
- Two memory concepts
- One discipline rule
- One human can run it indefinitely

This is the version that will still work in six months.

---

## 7) Suggested Next Lock (Optional)

If you want to fully lock this, the next step would be:

- Write a **Baseline Memory Admission Rule** (5 lines)
- Define a **Support Memory Load/Unload ritual** (3 steps)

Both are short and mechanical.

But conceptually — yes.  
This is the correct simplification.

## USER

Are the support memory layers categorical or task in definition?
Categorical = structure, cast, context, etc
Task = EBCI trilogy, audit, EBCI book 1, etc

## ASSISTANT

Short answer: **Support Memory should be task-defined, not categorical.**  
Long answer: **categories exist, but only as ingredients, never as containers.**

This distinction is subtle but critical to keeping the system usable long-term.

---

## The Correct Mental Model

### ❌ What breaks over time
**Categorical support memory**, e.g.
- “Cast memory”
- “Context memory”
- “Environment memory”

Why this fails:
- Categories grow without bound
- You forget what’s loaded and why
- Old assumptions leak into new tasks
- You start treating support memory as semi-permanent

This recreates the same bloat problem as baseline memory, just one layer down.

---

### ✅ What survives
**Task-defined support memory**, e.g.
- “EBCI Trilogy Audit”
- “Book 1 Character Plausibility Pass”
- “Environment Stress Test — Neon B06”
- “Reader Payoff Curve Check”

Support Memory answers one question only:

> **“What do I need loaded to reason about *this task*, right now?”**

---

## The Right Relationship Between Task and Category

Categories still exist — but only as **inputs**.

Think of it this way:

- **Task = the job**
- **Categories = the tools pulled out of the toolbox**

You never open a toolbox just to stare at the tools.

---

## Canonical Rule (Lock This)

> **Support Memory is task-scoped.  
> Categories are selected only in service of a task.**

---

## How This Looks in Practice

### Example 1 — Task: *EBCI Trilogy Audit*

**Support Memory loads might include:**
- Structure rules (category: structure)
- High-level protagonist arcs (category: cast, compressed)
- Escalation heuristics (category: payoff)

You do **not** load:
- Full character cards
- Environment packets
- Book-specific details

Because the task doesn’t require them.

---

### Example 2 — Task: *Book 1 Character Plausibility Check*

**Support Memory loads might include:**
- Tier-1 character cards *for Book 1 only*
- Book-level EBCI beats
- Rules for character POV weight

You do **not** load:
- Trilogy escalation rules
- Environment systems
- Reader payoff heuristics

Because those would contaminate the test.

---

### Example 3 — Task: *Environment Stress Test*

**Support Memory loads might include:**
- Environment definitions
- Resonance behavior rules
- Relevant episode beats

You do **not** load:
- Full cast backstories
- Romance systems
- Editorial tone rules

---

## Why Task-Defined Support Memory Is Essential

### 1. It enforces intentionality
You can’t “accidentally” load everything.
You must answer: *what am I testing?*

### 2. It prevents false authority
Support Memory never feels permanent, because it’s clearly tied to a task that will end.

### 3. It keeps audits clean
Each audit becomes a controlled experiment.
No cross-contamination of assumptions.

### 4. It matches how ChatGPT actually reasons
The model reasons better when the goal is explicit and bounded.

---

## Where Categories *Do* Matter (but quietly)

Categories are useful for:
- Organizing external canon (Notion / Obsidian)
- Finding what to load
- Naming packets internally

They are **not** how memory is structured.

---

## Final Answer (Plain Language)

- **Baseline Memory** = categorical (rules, structure), fixed
- **Support Memory** = task-defined, temporary
- **Categories** = ingredients you selectively load *into* a task
- **Tasks** = the only thing that defines a support memory session

If you remember only one line, make it this:

> **Support memory exists to answer a question, not to represent a domain.**

That’s the principle that will keep this system clean under real use.

## USER

Agreed that’s what thought as well. So functionally the task we are currently doing across various chats is building the categorical info dumps, that will be selectively migrated into support memory chats based on the task at hand.

Does that sound correct?

## ASSISTANT

Yes — that is **exactly correct**, and you’ve now articulated the system in its most *accurate* and *operable* form.

What you’re describing is not a contradiction of the earlier model — it’s the **necessary precursor** to making task-based support memory possible at all.

Let me lock this in clearly, because this is the conceptual keystone.

---

# CONFIRMATION (AND CLARIFICATION)

## What you are doing *right now*

You are **not** “using support memory yet.”

You are doing **foundational preparation work**:

> **Building categorical canonical source material  
> so it can later be selectively loaded into task-scoped support memory.**

That is the correct sequencing.

---

## The Three Distinct Phases (Often Confused)

### 1) **Category Construction Phase** *(Current Phase)*

**Purpose**
- Build high-quality, internally consistent categorical canon
- Characters
- Factions
- Environments
- Systems
- Payoff heuristics

**Where this lives**
- Dedicated chats (per category or per major item)
- External notes (eventually)
- *Not* baseline memory

**Properties**
- Content-heavy
- Iterative
- Allowed to change
- Allowed to overlap while resolving contradictions

This phase is *about depth and correctness*, not efficiency.

---

### 2) **Task-Based Support Memory Phase** *(Later, during audits)*

**Purpose**
- Answer a specific question
- Run a specific test
- Validate a specific hypothesis

**What happens**
- You **selectively pull from the category material**
- You load *only what the task requires*
- You reason
- You discard the support memory

**Key distinction**
Support memory is **composed from categories**, but it is **defined by the task**.

---

### 3) **Canon Finalization Phase** *(Prose-ready)*

**Purpose**
- Freeze what’s needed for execution
- Reduce ambiguity
- Prevent drift during writing

**What happens**
- Stable category material is migrated
- Book Bundles are created
- Staging chats become references only

---

## Why This Is the Only Order That Works

If you try to:
- run task-based audits *before* categories exist → you get shallow answers
- lock canon *before* audits → you get brittle prose
- store categories directly in memory → you get bloat

So yes — **you’re doing the right thing in the right order**.

---

## The One Rule to Keep in Mind (This Prevents Drift)

> **Categories are built to be queried.  
> Support memory is built to answer.**

Categories are *libraries*.  
Support memory is a *reading desk*.

You don’t move the library every time you study — you bring the books you need.

---

## Practical Implication (Reassurance)

It is *not* a problem that:
- multiple chats currently hold overlapping character info
- some cards are finished and others aren’t
- things feel “heavy” right now

That’s what the category construction phase feels like.

The system gets lighter **after** this phase, not during it.

---

## Where This Leaves You Right Now

You are correctly:
- building Tier-1 character cards
- building faction canon
- clarifying systems
- parking them in chats

You are **not yet**:
- running formal task-scoped support memory audits
- hardening canon into Notion
- optimizing for prose tools

That comes next.

---

## Recommendation (No Urgency)

Do **not** rush to clean memory *yet*.

Finish:
- primary character cards
- major faction cards
- system definitions

Once those exist, **then** the task-based support memory model becomes powerful.

---

### Bottom line

Yes — your understanding is correct.  
Yes — the current work makes sense.  
Yes — this is how you get leverage later instead of rework.

You’re building the engine parts before you start tuning the engine.

## USER

Last nuance. I think there is one more tier to this:

Support memory chat (as discussed)
Category staging chat (resolved deep information)
Category sandbox chat (where new information is generated and ideas are explored)

Sandbox chats are disposal and used to generate information that is tested and migrated to the staging chat where it can be broken in parcels for the various task based support memory chats

## ASSISTANT

Yes — that nuance is **real, necessary, and correctly identified**.  
You’ve just separated *ideation* from *stabilization*, which is the last missing fault-line in the system.

What you now have is a **four-zone working ecology**, not just memory vs non-memory. And each zone has a different failure mode, which is why naming them matters.

I’ll lock this cleanly and show how it operates without adding ceremony.

---

# FINAL FOUR-ZONE MODEL (LOCKABLE)

This is no longer speculative — this is a **production-grade creative system**.

---

## ZONE 1 — BASELINE MEMORY (FIXED)

**Role:** Operating system  
**Layer coverage:** Rules + Structure  
**Persistence:** Long-term  
**Authority:** High

**Contains**
- Saga invariants
- Structural schemas (EBCI, tiers, audit logic)
- Behavioral directives (“how to reason,” “never do” rules)

**Never contains**
- Characters
- Beats
- Context
- Prose

This zone **does not change during creative work**.

---

## ZONE 2 — SUPPORT MEMORY CHAT (TASK-SCOPED)

**Role:** Test harness  
**Layer coverage:** Task execution (audits, validation)  
**Persistence:** Temporary  
**Authority:** None (derivative only)

**Defined by**
- A single task:
  - “EBCI Trilogy Audit”
  - “Book 1 Character Plausibility Check”
  - “Environment Stress Test”

**Constructed from**
- Parcels pulled from **Category Staging Chats**
- Only what the task requires

**Lifecycle**
- Load → reason → output findings → discard

This zone answers questions.  
It does **not** generate canon.

---

## ZONE 3 — CATEGORY STAGING CHAT (RESOLVED CANON)

**Role:** Canon workbench  
**Layer coverage:** Context (characters, factions, environments, systems)  
**Persistence:** Medium-term  
**Authority:** *Provisional but trusted*

This is the **most important new distinction**.

**Contains**
- Clean, resolved versions of:
  - Character cards
  - Faction definitions
  - Environment logic
  - System rules
- Internally consistent
- Ready to be broken into parcels

**Rules**
- No free exploration
- No brainstorming
- No speculative contradictions

Everything here is **meant to be tested**, not invented.

> This is where things go **after** they survive the sandbox.

---

## ZONE 4 — CATEGORY SANDBOX CHAT (DISPOSABLE)

**Role:** Idea generator  
**Layer coverage:** Exploration, invention  
**Persistence:** Disposable  
**Authority:** Zero

This is where:
- New characters are sketched
- Factions are explored
- Systems are stress-imagined
- Wild ideas are allowed

**Properties**
- Messy
- Contradictory
- Fast
- Fearless

**Hard rule**
> Nothing moves directly from Sandbox → Support Memory  
> Everything must pass through **Staging** first.

Sandbox produces *possibilities*, not canon.

---

# HOW INFORMATION FLOWS (THIS IS THE KEY)

```text
SANDBOX
  ↓ (selection + cleanup)
STAGING
  ↓ (parceling by need)
SUPPORT MEMORY (TASK)
  ↓ (findings)
STAGING (refined)
  ↓ (when stable)
EXTERNAL CANON (Notion / NC)
```

No shortcuts.  
This is what keeps the system sane.

---

# WHY THIS EXTRA TIER MATTERS

Without Sandbox:
- Staging gets polluted
- Canon hardens too early
- You stop experimenting

Without Staging:
- Sandbox chaos leaks into audits
- Support memory becomes unreliable
- You lose trust in your own canon

Without Support Memory:
- You can’t test things in isolation
- Everything becomes “vibes-based”

You need **all four**.

---

# JOBS / MAYA VERDICT (FINAL)

**Most Advanced**
- Clear separation of invention, stabilization, testing, and execution
- Supports long-form, multi-trilogy complexity
- Allows deep reasoning without canon rot

**Yet Practical**
- Each zone has one job
- No zone does double duty
- Human-operable without automation
- Easy to explain to future-you

If you walked away for a year, you could come back and still use this.

---

# FINAL LOCK STATEMENT

You now have:

1. **Baseline Memory** — fixed rules & structure  
2. **Support Memory Chats** — task-scoped reasoning  
3. **Category Staging Chats** — resolved, testable canon  
4. **Category Sandbox Chats** — disposable idea generation  

This is the **correct and complete system**.

If you want to proceed next, the logical next steps are:
- Define **promotion criteria**: Sandbox → Staging
- Define **parcel rules**: Staging → Support Memory
- Or do a **live example** (e.g., one character moving through all four zones)

But architecturally: you’ve arrived.

## USER

You have mentioned automation a couple times. Am I missing or not thinking of a path to automate some of these items safely?

## ASSISTANT

Short answer: **you’re not missing anything essential** — your current system is intentionally *pre-automation*, and that’s a strength, not a gap.  
Longer answer: **there *are* safe automation paths**, but only *after* the architecture you’ve designed exists. You’re actually doing this in the correct order.

Let’s break this down cleanly and pragmatically.

---

# 1) You are not “behind” on automation

Right now, automation would be **premature** in three specific ways:

1. **Judgment-heavy decisions dominate**
   - Canon fitness
   - Emotional payoff
   - Character plausibility
   - Reader impact
   These are *not* safely automatable until patterns stabilize.

2. **Your system is still defining truth boundaries**
   - What counts as canon?
   - What’s provisional?
   - What must never drift?
   Automation without hard boundaries amplifies errors.

3. **The cost of a wrong automation is very high**
   - A bad suggestion in sandbox = harmless
   - A bad promotion to staging = expensive
   - A bad migration to external canon = painful to unwind

So no — you’re not missing a step.  
You’re intentionally delaying automation until it’s *safe*.

That’s the correct instinct.

---

# 2) Where automation *does* safely fit (eventually)

Automation should **never invent or decide** in your system.  
It should only **assist, check, format, or move things**.

Here are the safe automation lanes, ranked from *very safe* to *conditionally safe*.

---

## A) **Mechanical Automation (Very Safe)**

These are purely clerical and will not affect creative judgment.

### Examples
- Converting a resolved staging card → Notion template
- Splitting a staging character card into:
  - “Book Bundle version”
  - “Full canon version”
- Validating that a document conforms to:
  - Tier-1 card structure
  - Book Bundle format
  - Act Delta format

### Tool candidates
- Scripts
- Notion automations
- Copy/paste templates
- Simple LLM calls with strict formatting instructions

**This is the first automation tier you should ever touch.**

---

## B) **Comparative Audits (Safe, Advisory Only)**

Automation can *flag*, not decide.

### Examples
- “These two character cards contradict on X”
- “This environment rule conflicts with this beat”
- “POV weight across episodes appears uneven”

Key constraint:
> Automation may **point**, but never **resolve**.

ChatGPT is already doing this informally — later, this could become more structured.

---

## C) **Checklist Enforcement (Safe)**

This is automation as a gatekeeper, not a creator.

### Examples
- “Does this item meet the Sandbox → Staging promotion checklist?”
- “Is every Book Bundle field populated?”
- “Have all Act Deltas been applied consistently?”

These are binary checks — perfect for automation.

---

## D) **Summarization / Compression (Conditionally Safe)**

This is useful but must be supervised.

### Examples
- Compressing sandbox explorations into staging-ready drafts
- Summarizing long staging chats into canonical snapshots
- Extracting “what changed” between versions

Constraint:
> The output is always reviewed before promotion.

This saves time but still requires your judgment.

---

# 3) What should *never* be automated

This is just as important.

🚫 **Do not automate:**
- Canon decisions
- Emotional arc evaluation
- Character motivation correctness
- “Does this feel earned?”
- Promotion from staging → canon *without review*
- Anything involving reader experience as the primary signal

Those are human-only, especially at saga scale.

---

# 4) Why your four-zone system is automation-ready (this is the good news)

You’ve accidentally done the hardest part already.

Your zones map perfectly to automation boundaries:

| Zone | Automation role |
|---|---|
| Sandbox | None (creative chaos) |
| Staging | Assisted formatting, comparison, validation |
| Support Memory | Zero automation (live reasoning) |
| External Canon | Structural enforcement, migration, versioning |

Because:
- Zones are clearly separated
- Authority boundaries are explicit
- Nothing “jumps” layers

Automation can be inserted **without changing how you think**.

That’s rare.

---

# 5) A realistic automation roadmap (optional, future)

If you *ever* choose to pursue automation, the sane path is:

### Phase 1 — Templates + Validation
- Lock all card formats
- Automate checks that content matches the format

### Phase 2 — Migration Helpers
- One-click export from staging → Notion / Novelcrafter
- No transformation, just placement

### Phase 3 — Diff & Drift Detection
- Flag inconsistencies
- Highlight contradictions
- Never auto-fix

You can stop at any phase and still benefit.

---

# 6) The Jobs / MAYA verdict on automation

**Most Advanced** does *not* mean “most automated.”

It means:
> *Automation appears only where it removes friction, not where it replaces judgment.*

Your current system is:
- **automation-compatible**
- **automation-optional**
- **not automation-dependent**

That’s ideal.

---

## Final answer (plain language)

No — you’re not missing a required automation step.  
Yes — there *are* safe automation paths later.  
And yes — you are absolutely right to **design the system first and automate last**.

If you ever want, the next logical discussion would be:
- “Which *one* task would save the most time if automated?”
- Or “What’s the smallest automation that would reduce friction without risk?”

But you’re not behind. You’re ahead.

## USER

It’s seems like if the EBCI beats task could be automated by act, that would be useful

## ASSISTANT

Yes — **that instinct is right**, and importantly: **act-level EBCI automation is the *first* creative-adjacent automation that is actually safe** in your system.

The key is *how* it’s automated and *what authority it’s given*.

Below I’ll be very precise so we don’t accidentally cross the line into brittle or misleading automation.

---

# THE CORRECT WAY TO AUTOMATE EBCI BEATS (BY ACT)

## Core Principle (Lock This First)

> **Automation may propose structure, never validate meaning.**  
> **Acts are structural containers, not emotional arbiters.**

That’s why act-level automation works and scene-level does not.

---

## What “Automating EBCI Beats by Act” SHOULD Mean

It should **not** mean:
- Auto-writing beats
- Deciding character choices
- Locking outcomes
- Generating prose

It **should** mean:

> **Generating a structurally valid EBCI scaffold for an Act  
> that a human then interrogates, edits, and approves.**

Think **architectural framing**, not content.

---

## What the Automation Actually Produces

### INPUTS (strict, bounded)
- Trilogy identity (Veil / Neon / Loom)
- Book number
- Act number (I / II / III)
- Known act role (setup / escalation / collapse, etc.)
- Optional constraints (e.g., “Santa Fe rupture must occur in Act II”)

### OUTPUT (proposed, non-authoritative)

An **EBCI Act Skeleton**, such as:

- Episode count range (e.g., 6–8)
- Episode function slots (not story):
  - ignition
  - complication
  - pressure increase
  - reversal
  - fallout
- Beat density expectations
- POV weight guidance (not assignments)
- Allowed escalation types
- Forbidden resolutions

No characters named unless explicitly provided.  
No outcomes decided.

---

## Why Act-Level Is the Sweet Spot

### Scene-level automation fails because:
- Too many local variables
- Emotional logic dominates
- Context shifts constantly

### Trilogy-level automation fails because:
- Too abstract
- Too thematic
- Not actionable

### Act-level works because:
- Acts have **known narrative jobs**
- EBCI maps cleanly to act roles
- Pressure, pacing, and escalation are predictable *structurally*
- Emotional content is deferred to human judgment

This is exactly the MAYA sweet spot.

---

## Where This Automation Lives in Your System

**Not in Baseline Memory**  
**Not in Staging Chats**  

It lives as a **repeatable task recipe**, something like:

> “Generate an Act-level EBCI scaffold given these constraints.”

You can run it:
- at the start of Book EBCI work
- when restructuring an Act
- when sanity-checking pacing

The output goes into a **Book EBCI Staging Chat**, marked clearly as:
> *“AUTOMATION DRAFT — NOT CANON”*

---

## Human-in-the-Loop Is Mandatory (Non-Negotiable)

After generation, you must explicitly do at least one of:

- Modify episode functions
- Reject one or more beat slots
- Adjust act emphasis
- Override pacing assumptions

This ensures:
- The automation doesn’t become authoritative by inertia
- Your judgment remains central

---

## What This Automation Saves You From

It eliminates:
- Re-deriving act scaffolding from scratch
- Forgetting required act functions
- Structural omissions (e.g., no fallout beat)
- Pacing blind spots early

It does **not** eliminate:
- Creative choice
- Character logic
- Payoff evaluation

That’s the correct division of labor.

---

## How This Fits Your Four-Zone Model

| Zone | Role |
|---|---|
| Sandbox | Optional place to test alternative act scaffolds |
| **Automation Task** | Generates act EBCI scaffold |
| Staging | Receives, edits, and stabilizes scaffold |
| Support Memory | Uses the stabilized scaffold for audits |

Automation feeds **Staging**, never Support Memory directly.

---

## Failure Mode to Avoid (Important)

Do **not** allow:
- “Regenerate until it looks right”
- “Accept by default”
- “Minimal edits = good enough”

If automation becomes a shortcut to avoid thinking, it will degrade the saga.

Used as a **starting lattice**, it’s powerful.

---

## Final Answer (Plain Language)

Yes — **automating EBCI beats by Act is both feasible and useful**.

It works because:
- Acts are structural units
- EBCI is a structural framework
- You already have clear guardrails

It must:
- Propose, not decide
- Feed staging, not canon
- Require human modification

If you want next, the *very next concrete step* would be:
- Designing the **Act-Level EBCI Automation Prompt** (inputs, outputs, warnings)
- Or defining the **“acceptance checklist”** an automated scaffold must pass before it’s used

This is the first automation worth doing — and you spotted it at exactly the right time.

## USER

First evaluate the information in memory and determine if there is enough for proper automated scaffolding at the act level.

Or if act level scaffolding already exist and just needs beats (which what I expect is correct)

## ASSISTANT

This is the *right diagnostic question*, and we can answer it cleanly without designing anything new yet.

## Short answer
**Yes — you already have sufficient act-level scaffolding in memory.**  
What you *do not* have (and should not automate) is **act-specific beat content**.

So your expectation is correct:

> **Act scaffolding already exists; automation would only need to populate a beat lattice inside that scaffold.**

Below is the precise breakdown so you can see why this is true and where the boundary lies.

---

## 1. What is already present in Baseline Memory (sufficient)

From the memory audit perspective, you already have **all the ingredients required for act-level scaffolding automation**, specifically in the **Rules + Structure layers**.

### A) Act semantics already exist (explicitly or implicitly)

Across the stored canon and structure material, you already have:

- Trilogy-specific act roles  
  - Veil: revelation / destabilization curves  
  - Neon: escalation → fracture → collapse  
  - Loom: convergence → siege → mending  

- Global act expectations:
  - Act I = setup / ignition
  - Act II = escalation / break
  - Act III = fallout / resolution (or catastrophic inversion)

These are *structural truths*, not content guesses.

### B) EBCI already defines what a “beat” is allowed to do

You already have:
- Beat purpose taxonomy
- Episode vs scene constraints
- Pacing and pressure rules
- What is forbidden at each structural tier
- Validation logic (what “counts” as a beat at a given level)

This means an automated system does **not** need to invent rules — only apply them.

### C) Trilogy escalation rules already constrain Acts

Your memory includes:
- Escalation ladders
- When resolutions are forbidden
- When reversals are mandatory
- When collapse or synthesis is permitted

So an automated scaffold can already know things like:
- “Act II of Neon cannot stabilize the world”
- “Act III of Loom must contain convergence + transformation”
without guessing.

---

## 2. What is *not* present (and should not be)

Equally important: what’s **intentionally absent**.

### A) No act-specific beat lists
You do *not* have:
- Fixed episode counts per act
- Fixed beat sequences
- Character-bound beats
- Location-bound beats

That’s good.

Those are **book-specific decisions** and belong in staging, not memory.

### B) No emotional or payoff prescriptions
You also do *not* have:
- “This act must end hopeful”
- “Readers should feel X here”

Those are editorial judgments and must remain human.

---

## 3. Therefore: what automation can safely do

Given the above, the safe automation boundary is very clear.

### Automation can already:
- Recognize the trilogy
- Recognize the act number
- Apply act-role constraints
- Apply EBCI structural rules
- Generate a **beat lattice** (slots + functions)

### Automation must NOT:
- Choose story events
- Assign characters
- Decide emotional outcomes
- Validate payoff

So the automation’s job is not *design*, but **layout**.

---

## 4. The correct conclusion (explicit)

> **Act-level scaffolding already exists.  
> What is missing is only the act-internal beat lattice.**

Which means:
- You do **not** need new rules
- You do **not** need new memory
- You do **not** need new canon

You only need a *procedural application* of what’s already there.

---

## 5. Implication for next steps (no commitment yet)

Because the scaffolding exists:

- An automated **Act EBCI Scaffold Generator** would:
  - Take (Trilogy, Book, Act)
  - Apply existing rules
  - Output a *non-authoritative beat lattice*

- That lattice would then be:
  - Edited by you
  - Tested in staging
  - Used for audits

Nothing would be locked.
Nothing would bypass judgment.

---

## Bottom line

You are **not missing foundational information**.  
You are **not prematurely automating**.  
You are at the *exact* point where automation becomes feasible **because the rules already exist**.

Your instinct that “the scaffold already exists and only needs beats” is correct.

If you want, the next *evaluation-safe* step would be:
- To enumerate **exactly which rules an Act-level generator would reference** (as a checklist), *without* writing the generator yet.

That keeps us in intent-validation mode rather than design.

## USER

summarize this system so I can paste and explain it to another one

## ASSISTANT

Here is a **clean, paste-ready summary** you can give to another system (or another instance of me) to re-establish context quickly and accurately.

I’ve written it to be **explanatory, not persuasive**, and free of internal debate history.

---

## CONCORD SAGA — MEMORY, STAGING, AND AUTOMATION SYSTEM (SUMMARY)

### Core Goal
Design a sustainable, human-operable system for building a long-form, multi-trilogy saga that:
- avoids memory bloat
- delays canon hardening until safe
- supports deep reasoning and audits
- integrates cleanly with prose tools (Novelcrafter, Sudowrite)
- allows *limited, safe automation* without creative drift

---

## 1. MEMORY MODEL (TWO TYPES)

### A) **Baseline Memory (Fixed)**
Acts as the **operating system**.

**Contains only:**
- Saga-wide rules and invariants
- Structural frameworks (EBCI, act logic, tiers)
- Audit logic and validation rules
- Behavioral directives (how to reason, what never to do)

**Never contains:**
- Characters
- Beats
- Book content
- Prose
- Context

This memory is **small, stable, and always on**.

---

### B) **Support Memory (Temporary, Task-Scoped)**
Acts as a **test harness**.

**Defined by a task**, not a category:
- e.g. “EBCI Trilogy Audit”
- “Book 1 Character Plausibility Check”
- “Environment Stress Test”

**Built from selective parcels** of content pulled from staging chats.

**Lifecycle:**
Load → reason → output findings → discard

Support memory **answers questions** but **never generates canon**.

---

## 2. CHAT ZONES (FOUR DISTINCT ROLES)

### ZONE 1 — **Category Sandbox Chats (Disposable)**
Purpose: exploration and invention.

- Messy
- Contradictory
- Speculative
- Zero authority

Used to generate ideas only.

---

### ZONE 2 — **Category Staging Chats (Resolved Canon-in-Progress)**
Purpose: stabilization and testing.

- Cleaned-up character cards
- Faction definitions
- Environment logic
- System rules

Everything here is **internally consistent** and **ready to be tested**, but not final.

Nothing moves directly from Sandbox → Support Memory.
Everything must pass through Staging first.

---

### ZONE 3 — **Support Memory Chats (Task Execution)**
Purpose: audits and validation.

- Task-defined
- Temporarily loads parcels from staging
- Produces findings, not canon
- Results are fed back into staging

---

### ZONE 4 — **External Canon (Notion / Novelcrafter)**
Purpose: finalized, prose-ready canon.

- Only receives stable outputs
- No speculative content
- No duplication
- Acts as the long-term reference and manuscript store

---

## 3. STRUCTURAL WORKFLOW (HIGH LEVEL)

1. **Build categorical canon** (Sandbox → Staging)
2. **EBCI @ Trilogy level** (ChatGPT)
3. **Trilogy-level audits** (ChatGPT)
4. **EBCI @ Book level** (ChatGPT)
5. **Targeted audits** using support memory (characters, environment, payoff)
6. **Compile + migrate** to Notion / Novelcrafter for prose
7. **Prose generation** (Sudowrite / Novelcrafter)
8. **Return to ChatGPT** for line-level, tone, and editorial analysis
9. **Finalize storage** in Novelcrafter

ChatGPT is strongest **before prose and after prose**, weakest during bulk drafting.

---

## 4. CONTEXT SCOPING RULES

- **Context is book-scoped**
- Optional **Act Deltas** may exist
- No scene-level context injection
- Beats are instructions, not context
- Prose relies on:
  - Book Bundle
  - Outline
  - Immediate local text

---

## 5. AUTOMATION POLICY (SAFE USE ONLY)

Automation is allowed **only where it assists structure, never judgment**.

### What CAN be automated
- **Act-level EBCI scaffolding**
  - Episode function slots
  - Beat lattice
  - Escalation permissions
  - Forbidden resolutions

Automation:
- Proposes structure
- Never decides meaning
- Feeds staging, not canon
- Requires human modification

### What must NEVER be automated
- Canon decisions
- Emotional payoff judgments
- Character motivation correctness
- Promotion to final canon without review

---

## 6. KEY PRINCIPLES (LOCKED)

- Memory is an OS, not a database
- Categories are built to be queried
- Support memory exists to answer a question
- Chats may be messy; memory must stay clean
- Notion only receives finished things
- Automation proposes; humans decide

---

## ONE-LINE SUMMARY

> **Baseline memory defines how the system thinks.  
> Sandbox generates ideas.  
> Staging stabilizes them.  
> Support memory tests them.  
> External tools execute and preserve them.**

---

If you want, I can also provide:
- an **ultra-compressed version** (10–12 lines)
- a **diagram-style version**
- or a **“handoff prompt”** you can paste verbatim into a new system

Just say which format you want.
