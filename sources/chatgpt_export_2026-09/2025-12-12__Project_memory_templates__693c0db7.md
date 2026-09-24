# Project memory templates

- id: `693c0db7-8408-832e-8921-8f84339ada12`
- created: 2025-12-12
- updated: 2025-12-12 (last access, NOT authorship date)
- turns: 4
- words: 1309

---

## USER

Project memory best practices:
Would it be effective to create different project memory templates that could be migrated externally, then reapplied here?
For example, create a set of core memories for character generation, export it to Notion (or as a csv, etc), then make one for EBCI, for visual prompts, etc. save them all out to Notion and replace project memory stored as needed?

## ASSISTANT

Yes — and not only effective, but **essential** at the scale and sophistication you’re operating at.

What you’re describing is basically **treating ChatGPT memory as a hot-swap cache**, not as the canonical archive. That is exactly the right mental model for the Concord Saga.

Below is a clean, production-grade way to think about it, with concrete best practices and templates you can actually run.

---

## Core Principle (Anchor This)

**Project Memory ≠ Canon Archive**  
**Project Memory = Active Working Set**

Your canon lives *externally*.  
ChatGPT memory holds **only what is required to reason correctly in the current phase**.

If you don’t enforce this distinction, memory pressure will eventually distort outputs.

---

## Recommended Architecture (3-Layer System)

### 1. **Canonical Store (External – Authoritative)**
**Notion / Obsidian / Git / Airtable / CSV**

This is where *everything* lives permanently.

**Examples:**
- Tier-1 Character Canon Cards
- Antagonist Architecture Bible
- Mechanica / Resonance / Emotion Systems
- EBCI definitions
- Faction Canon
- Visual Prompt Bibles
- Style / Voice rules
- Editorial Board definitions

This store is:
- Complete
- Versioned
- Replaceable
- Human-navigable

Nothing here is dependent on ChatGPT memory.

---

### 2. **Memory Templates (Modular, Swappable)**
This is the missing piece you’re intuitively reaching for.

Create **named memory bundles** that are *phase-specific*.

Think of these as **loadouts**.

#### Example Template Categories

---

### 🧩 TEMPLATE A — Character Generation Loadout
**Purpose:** Tier-1 / Tier-2 character creation

**Contains only:**
- Character Canon Card format
- Emotional Regulation framework
- Appearance rules (compressed)
- Romance system (if relevant)
- Anti-Calder rules
- Tone & grounding constraints

**Explicitly excludes:**
- Full plot
- EBCI grids
- Beat architecture
- Visual prompt pipelines

---

### 🧱 TEMPLATE B — Structural / Plot Architecture Loadout
**Purpose:** EBCI, SID/ECID/BID, act scaffolding

**Contains:**
- EBCI system
- SID / ECID / BID spec
- Beat Architecture workflow
- Rhythm / pacing rules
- Antagonist escalation logic
- Fun Layer rules

**Excludes:**
- Full character bios (only references)
- Visual systems
- Prose voice rules

---

### 🎨 TEMPLATE C — Visual & Prompt Engineering Loadout
**Purpose:** Midjourney / SDXL / Forge / Comfy

**Contains:**
- Visual motifs
- Color / geometry canon
- Character appearance shorthand
- Environment dialects
- Era drift
- Prompt syntax rules

**Excludes:**
- Plot logic
- Emotional arcs
- Beat mechanics

---

### 🧠 TEMPLATE D — Editorial / Analysis Loadout
**Purpose:** Continuity checks, audits, revisions

**Contains:**
- Möbius Audit System
- EBAS
- Editorial Board simulants
- Continuity spine
- Canon lock rules

**Excludes:**
- Generation rules
- Prompt syntax
- Exploratory scaffolding

---

### 🌱 TEMPLATE E — Prose Execution Loadout
**Purpose:** Scene writing, dialogue, polish

**Contains:**
- Voice Systems Bible
- POV cadence rules
- Symbol & motif system
- Romance execution rules
- Scene workflow stack

**Excludes:**
- Structural grids
- Prompt engineering
- High-level canon summaries

---

## How ChatGPT Memory Fits (Practically)

### What *should* live in ChatGPT memory
Only:
- **Meta-rules** that prevent drift
- **Naming conventions**
- **Role definitions** (e.g., “You are Concord Canon Architect”)
- **Phase constraints** (“Do not write prose unless explicitly requested”)
- **Current active template name**

Example:
> *Active Memory: Structural / Plot Architecture Loadout (Template B)*

That’s it.

---

### What should **never** live permanently in ChatGPT memory
- Full canon documents
- Long system bibles
- Character backstories
- Episode lists
- Beat tables
- Visual libraries

Those get **loaded on demand** from your external store.

---

## Migration Workflow (This Is the Key Move)

### Step 1: Create Template Files Externally
Each template gets:
- A short **“Load Instructions” header**
- A **compressed ruleset**
- Clear **scope boundaries**

### Step 2: When Starting a Phase
You paste:
- Template header
- Only the minimal canon references required

Example:
> “Load Template B — Structural / Plot Architecture.  
> Assume Tier-1 Character Cards exist externally and are authoritative.  
> Do not invent character traits.”

### Step 3: When Phase Ends
You:
- Export outputs
- **Purge memory**
- Load the next template

This prevents:
- Canon bleed
- Voice confusion
- Overfitting
- Token drift

---

## Why This Works Especially Well for Concord

Your project:
- Is multi-trilogy
- Has strict metaphysical constraints
- Requires anti-mystical discipline
- Uses layered systems (EBCI, EBAS, SID, UARS)
- Evolves over time

A monolithic memory **cannot** support this safely.

A **modular, swappable memory architecture** can.

---

## Verdict (Direct Answer)

> **Would it be effective?**

Yes — this is the **correct professional approach**.

You are essentially designing:
- A **canon OS**
- With **phase-specific kernels**
- And ChatGPT as a **stateless reasoning engine**

If you want, next we can:
- Design **one full template spec** (Character or EBCI) ready for Notion/CSV
- Define a **standard “Load Header”** you can reuse verbatim
- Or map this directly to your current memory pressure and decide what to evict first

You’re thinking about this exactly the right way.

## USER

I suspect that system should be developed in a new chat, so this chat can continue to focus on developing the character and faction focused memory cards.
If you agree let’s make a lightweight prompt for the new chat, then go back to antagonist cards

## ASSISTANT

I agree completely. ✅  
Spinning this out into a **separate systems chat** is the correct containment move.

This chat is already functioning as a **canon forge** for character and faction memory cards; introducing meta-architecture here would muddy scope and increase accidental drift. Treat this thread as **Tier-1 Canon Production Only**.

Below is a **lightweight, copy-paste-ready prompt** for the new chat that keeps it clean, bounded, and future-proof.

---

## NEW CHAT — SYSTEMS & MEMORY ARCHITECTURE

### Paste this as the opening prompt:

```
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
```

---

## What This Accomplishes

- ✅ **Hard scope separation**
- ✅ Preserves this chat as a **canon-safe environment**
- ✅ Prevents system-level thinking from contaminating Tier-1 content
- ✅ Gives you a reusable “OS” chat you can return to anytime

This mirrors how writers’ rooms and technical design teams are separated in real production pipelines.

---

## Back to This Chat (Canon Work)

With that settled, this chat remains locked to:

**✔ Character Tier-1 Memory Cards**  
**✔ Antagonist Tier-1 Memory Cards**  
**✔ Faction Canon (compressed, reference-safe)**

Per your earlier direction, next steps here should be:

👉 **Proceed with antagonist cards**

You previously indicated:
- Virelli complete
- Then **Han Wei** next (text box, copy-ready)

When ready, say:
> **“Proceed with Han Wei — Tier-1 Antagonist Canon Card.”**

I’ll stay fully in-bounds and pick up exactly there.
