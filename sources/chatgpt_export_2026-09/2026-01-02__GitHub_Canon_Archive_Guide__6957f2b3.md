# GitHub Canon Archive Guide

- id: `6957f2b3-7b08-832e-8b72-8f92bb7d5597`
- created: 2026-01-02
- updated: 2026-01-02 (last access, NOT authorship date)
- turns: 14
- words: 5748

---

## USER

github canon archive discussion

## ASSISTANT

Below is a **clean, decision-oriented discussion frame** for the **GitHub Canon Archive**—aligned to how you’re actually using the saga (long-running, system-heavy, art + prose + mechanics, multiple chats).

---

## 1. Purpose of the GitHub Canon Archive (What it *is*)
The GitHub repo is **not a writing workspace**.  
It is a **canonical retrieval engine**.

Its jobs:
- Preserve **locked canon** in stable, diff-able form  
- Act as a **single source of truth** across chats, tools, and collaborators  
- Enable **selective loading** (“only what’s needed right now”)
- Support **art generation, prose writing, and audits** without re-explaining the saga

Think of it as:
> *A spine + organs vault, not muscle or skin.*

---

## 2. What GitHub is *not* used for
Explicit exclusions (important to prevent repo bloat):

- ❌ Draft prose
- ❌ Iterative scene work
- ❌ Exploratory brainstorms
- ❌ Temporary alternates
- ❌ Chat-specific working notes

Those stay in:
- Chat sessions
- Local docs
- Scratch MDs not linked in manifests

Only **canon-locked or reference-stable** material goes in GitHub.

---

## 3. Core Structural Model (Recommended)
### A. Top-Level Repo Structure
```text
/concord-canon
│
├── manifests/
│   ├── saga-load.md
│   ├── book-01-load.md
│   ├── antagonists-load.md
│   ├── art-direction-load.md
│   └── mechanics-load.md
│
├── saga/
│   ├── saga-continuity-spine.md
│   ├── pov-baton-pass.md
│   └── mobius-logic.md
│
├── books/
│   ├── veil/
│   ├── neon/
│   └── loom/
│
├── characters/
│   ├── protagonists/
│   ├── antagonists/
│   └── tertiary/
│
├── factions/
│
├── systems/
│   ├── mechanica.md
│   ├── emotion-systems.md
│   ├── resonance-topology.md
│   └── symbol-engine.md
│
├── art/
│   ├── character-appearance.md
│   ├── vfx-rules.md
│   ├── fashion-materials.md
│   └── prompt-guides/
│
└── governance/
    ├── canon-rules.md
    ├── locking-protocol.md
    └── change-log.md
```

---

## 4. The Manifest System (Critical)
Manifests are the **secret weapon**.

### What a Manifest Is
A manifest is a **curated list of links** that answers:
> “What do I need loaded to do *this* task correctly?”

### Example: `book-07-load.md`
```md
# Loom Book 7 — Canon Load Manifest

## Required
- saga/saga-continuity-spine.md
- books/loom/book-07-structure.md
- characters/protagonists/kade.md
- characters/protagonists/seraphine.md
- factions/choirless.md

## Systems
- systems/mechanica.md
- systems/resonance-topology.md

## Tone & Voice
- systems/voice-systems.md
- systems/fun-layer.md

## Art (Optional)
- art/vfx-rules.md
- art/fashion-materials.md
```

### Why This Matters
- Prevents **overloading memory**
- Enables **task-specific accuracy**
- Allows you to say in chat:
  > “Load Loom Book 7 manifest.”

Even if the model can’t literally fetch files, **the structure trains correct scoping**.

---

## 5. File Granularity Rules
To avoid future pain:

### DO
- One **concept per file**
- Use **compressed canon** where possible
- Prefer **tables, bullets, headers** over prose
- Include **“Purpose” + “Constraints”** at top of each file

### DON’T
- Combine unrelated systems
- Nest lore inside prose examples
- Store chat transcripts
- Store unresolved alternates

Rule of thumb:
> If it changes often → not GitHub  
> If breaking it breaks canon → GitHub

---

## 6. Canon Locking & Change Discipline
You already *intuitively* do this—GitHub just formalizes it.

### Lock States
- **Draft** – not committed
- **Soft-Locked** – committed but noted as adjustable
- **Hard Canon** – requires explicit revision note

### Change Log Pattern
```md
## 2025-12-06
- Locked: Loom Book 9 Act III Structure
- Updated: Choirless faction compression
- Deprecated: Old Veil Shard escalation table
```

This prevents “silent drift.”

---

## 7. Art Pipeline Integration (Very Important)
GitHub should store:
- **Appearance canon**
- **VFX rules**
- **Prompt grammar**
- **Style constraints**

NOT:
- Generated images
- Prompt variants per image
- Iterative aesthetic tests

Those stay local or in art-specific chats.

This lets you say:
> “Generate MJ prompts using canon art stack.”

…and get consistent results.

---

## 8. How This Plays With ChatGPT (Practical Use)
Best practice prompts:
- “Using Concord Saga canon as stored in GitHub, assume full lock.”
- “Assume Loom Trilogy + Mechanica v4 loaded.”
- “This task must not violate canon constraints.”

You don’t paste files every time—you **reference the system**.

---

## 9. Recommended Next Steps (Concrete)
1. **Finalize folder skeleton** (even empty files are fine)
2. Create **5–7 key manifests**:
   - Saga load
   - Veil trilogy
   - Neon trilogy
   - Loom trilogy
   - Antagonists
   - Art direction
   - Mechanics
3. Backfill **compressed canon MDs** (what you already have)
4. Add a **canon rules + locking doc**
5. Only then expand for collaborators or tooling

---

## Bottom Line
You’re building:
- A saga that outlives individual chats
- A system complex enough to *require* modular recall
- A creative engine that spans prose, art, mechanics, and ethics

GitHub is the **spine and memory palace** that makes that sustainable.

If you want, next we can:
- Design the **exact manifest templates**
- Define **naming conventions**
- Or walk through **one full character → GitHub conversion pass**

## USER

{"content_type":"image_asset_pointer","asset_pointer":"sediment://file_0000000087fc722f86ee3030370608b4","size_bytes":28454,"width":280,"height":703,"fovea":null,"metadata":{"dalle":null,"gizmo":null,"generation":null,"segmentation":null,"container_pixel_height":null,"container_pixel_width":null,"emu_omit_glimpse_image":null,"emu_patches_override":null,"lpe_keep_patch_ijhw":null,"lpe_delta_encoding_channel":null,"sanitized":true,"asset_pointer_link":null,"watermarked_asset_pointer":null,"is_no_auth_placeholder":null}}
{"content_type":"image_asset_pointer","asset_pointer":"sediment://file_00000000007c722f8bd82ed0bec8176b","size_bytes":113987,"width":1891,"height":873,"fovea":null,"metadata":{"dalle":null,"gizmo":null,"generation":null,"segmentation":null,"container_pixel_height":null,"container_pixel_width":null,"emu_omit_glimpse_image":null,"emu_patches_override":null,"lpe_keep_patch_ijhw":null,"lpe_delta_encoding_channel":null,"sanitized":true,"asset_pointer_link":null,"watermarked_asset_pointer":null,"is_no_auth_placeholder":null}}
I feel comfortable with characters at the moment. We have migrated final character definition files for the primary characters (Seraphine, Lucien, Caro, Elisabet, Rex, Baz, Tahl, Kade, Lacuna, Trip) and one antagonist (Elias). (see first screenshot) I have most of the info needed for the other antagonists and factions started.  In this chat I was thinking we start migrating some of the source canon and rules info from project memory into git hub. (see second screenshot)

## ASSISTANT

Perfect—this is exactly the *right* moment to pivot from characters to **systems + rules migration**. You’ve already done the hardest human-shaped work; now we lock the physics, constraints, and governance that keep everything from drifting.

Below is a **clear, low-risk migration plan** that fits your current repo state *and* respects your `source_canon` philosophy.

---

## 1. What You’ve Already Done (Sanity Check)
You are in a **strong position**:

- ✅ Primary protagonists fully migrated (definition + appearance + render + POV)
- ✅ One primary antagonist (Elias) migrated
- ✅ POV files cleanly separated (`/pov`)
- ✅ `source_canon/` explicitly marked **NON-AUTHORITATIVE**
- ✅ Lifecycle rules already written (Extract → Reason → Distill)

This means:
> We can safely migrate *high-resolution canon* without risking premature locks.

No rework needed here.

---

## 2. Migration Philosophy for This Phase
For **systems + rules**, the order matters more than the content.

### Prime Rule
> **Migrate constraint systems before lore systems.**

Why:
- Constraints prevent contradictions
- Lore can be reconciled later
- Mechanics, channels, and prohibitions must not drift

So we **do not** start with “cool metaphysics.”
We start with **what is allowed, forbidden, or structurally true**.

---

## 3. Priority Order for Source Canon Migration
Here is the recommended sequence, aligned to your saga’s actual dependency graph.

---

### PHASE 1 — Canon Governance & Boundaries (Highest Priority)
These should land first because *everything else depends on them*.

**Target folder:** `/rules/`

**Files to migrate (from memory → source_canon first):**
1. **Canon Rules**
   - What can *never* happen
   - No resurrection
   - MT ≠ VT ≠ LT
   - Ascension constraints
2. **Locking Protocol**
   - Draft vs Soft vs Hard canon
   - Who/what can change files
3. **Change Discipline**
   - How revisions are recorded
   - Deprecation rules

👉 These become the *immune system* of the repo.

---

### PHASE 2 — Core Systems (Non-Narrative)
These are the **physics of the universe**.

**Target folder:** `/systems/` or `/metaphysics/` (your naming is fine)

Migrate as **separate files**, not a monolith:

1. **Mechanica v4 (Compressed)**
   - RP equation
   - UARS cost model
   - Environment modifiers
   - Boost ceilings
2. **Channel Separation**
   - MT / VT / LT rules
   - Transmission prohibitions
   - Perception limits
3. **Resonance Topology**
   - Corridors U1–U7
   - Resonance weather W0–W4
   - Conductivity hierarchy

👉 These should be almost entirely **bullet/table driven**, minimal prose.

---

### PHASE 3 — Symbol & Expression Systems
These govern *how things look and feel* without being plot.

**Target folder:** `/systems/` or `/art/`

1. **Symbol & Motif System**
   - Geometry, color, sound mappings
   - Era drift rules
2. **VFX / Visual Grammar**
   - What resonance can look like
   - What it must never look like
3. **FUN Layer**
   - Mandatory delight beats
   - Oxygen rules for Loom

These are critical for:
- Art prompts
- Tone audits
- Avoiding prestige-gloom collapse

---

### PHASE 4 — Saga-Level Structural Canon
Only after systems are stable.

**Target folder:** `/saga/`

1. **Saga Continuity Spine**
2. **POV Baton Pass**
3. **Mobius / Endgame Logic**
4. **Trilogy Escalation Rules**

This ensures:
- No late retcons
- Endgame remains mechanically legal

---

## 4. How to Use `source_canon` Correctly (You’re Doing This Right)
Your README is excellent. Lean into it.

### Recommended Pattern
For each system:

1. **Drop full memory export into**  
   `source_canon/{domain}/{system}_raw.md`
2. Allow:
   - Redundancy
   - Notes
   - Contradictions
3. Then create a **distilled file** in `/systems` or `/rules`

Example:
```text
source_canon/metaphysics/veils_raw.md
systems/veil-system.md   ← distilled, authoritative
```

Never link *into* source canon.  
Only link *out of* it.

---

## 5. What We Should NOT Migrate Yet
To avoid scope creep:

- ❌ Faction lore (except constraints)
- ❌ Antagonist psychology (already handled separately)
- ❌ City-by-city flavor prose
- ❌ Scene workflows (until systems are locked)

Those come **after** systems stabilization.

---

## 6. Suggested Next Action (Concrete)
If you want a clean start **in this chat**, I recommend:

### Option A (Best)
> “Let’s migrate **Canon Rules + Locking Protocol** into `source_canon/rules/`.”

I will:
- Extract from project memory
- Normalize language
- Flag hard vs soft constraints
- Produce a GitHub-ready MD

### Option B
> “Let’s migrate **Mechanica v4 (Compressed)** first.”

Heavier lift, but immediately useful across art + prose.

---

## Bottom Line
You’ve crossed the threshold from *worldbuilding* to *world governance*.

This phase is about:
- Preventing future contradictions
- Enabling collaborators
- Making ChatGPT + art tools reliable without re-explaining the universe

Say the word on **which Phase 1 file you want to migrate first**, and we’ll do it cleanly and canon-safe.

## USER

I think we can be light on the administrative portions since it is just you and I working on this. (like locking protocols, change discipline, etc. We'll get there, but not until all of the baseline information has been transferred and tested) Should the breadcrumb, mobius, fun layer, and other beat related items go into the rules section to guide the "grids" section?

## ASSISTANT

Yes — **you’re thinking about this exactly right**, and your instinct to stay *light* on admin until the physics are proven is correct.

Short answer first, then the precise structure:

> **Breadcrumbs, Möbius, Fun Layer, and beat-logic should live in `/rules/` as *behavioral constraints***  
> and the **`/grids/` folder should consume them, not define them.**

They are **governing logic**, not data tables.

Below is the clean rationale and a concrete placement map.

---

## 1. Re-classifying These Systems (Important Mental Shift)

The key insight is this:

- **Rules** = “What must be true for the saga to work”
- **Grids** = “Where and how those truths are applied”

Breadcrumbs, Möbius, Fun Layer, EBAS checks, etc. are **NOT structural content** and **NOT planning tools**.

They are **validation logic**.

They answer questions like:
- *Did we earn this payoff?*
- *Are we honoring reader trust?*
- *Is pressure releasing often enough?*
- *Is the saga looping meaningfully or drifting?*

That puts them squarely in **rules**, not grids.

---

## 2. Recommended Placement (High Confidence)

### `/rules/` — Narrative Governance & Validation
These files should exist **before** grids are populated.

#### 1. `breadcrumb-system.md`
**Purpose:**
- Defines how information is seeded, reinforced, recalled, and paid off
- Prevents mystery rot and deus ex payoff

**Why rules, not grids:**
- Breadcrumbs exist *before* you know what episode or act they appear in
- Grids only track *instances*, not logic

---

#### 2. `mobius-logic.md`
**Purpose:**
- Defines the saga’s recursive meaning structure
- Why the ending reframes the beginning
- How thematic loops are allowed to close

**Why rules:**
- Möbius logic governs *interpretation*, not placement
- Grids will reference Möbius points, but must not define them

---

#### 3. `fun-layer.md`
**Purpose:**
- Oxygen guarantee
- Prevents tonal suffocation, especially in Loom
- Codifies delight, warmth, wonder as non-optional

**Why rules:**
- Fun is not a scheduling issue — it’s a **health requirement**
- Grids ensure inclusion; rules define *what counts* as Fun

This is especially important because Fun is often the first thing to get “optimized away.”

---

#### 4. `beat-validation-framework.md`  
(this may later be split, but start unified)

Includes:
- EBAS / Möbius audit
- Emotional circuit audit
- Antagonist pressure check
- Breadcrumb pass
- Reader trust checks

**Why rules:**
- These are *tests*, not planning artifacts
- Grids should be checkable *against* them

---

## 3. What the `/grids/` Folder Should Be (And Should Not Be)

### `/grids/` = Applied Instances
Grids are **maps**, not laws.

They should include:
- Beat matrices
- Act escalation tables
- POV distribution
- Pressure curves
- Fun beat placement (as flags, not definitions)
- Breadcrumb IDs referencing the breadcrumb system

They should **not** contain:
- Philosophy
- Justification
- Narrative ethics
- “Why this matters” prose

If a grid needs to *explain itself*, the rule is missing.

---

## 4. A Clean Dependency Chain (This Matters Later)

Here’s the ideal flow:

```
RULES
│
├─ Breadcrumb System
├─ Möbius Logic
├─ Fun Layer
├─ Beat Validation
│
▼
GRIDS
│
├─ Act / Beat matrices
├─ POV distributions
├─ Pressure curves
├─ Breadcrumb maps
│
▼
BOOK CONTEXT
│
├─ Book-specific plans
├─ Act overlays
```

This ensures:
- You can change a grid without changing meaning
- You can audit a grid against stable rules
- You can scale the saga without losing coherence

---

## 5. What NOT to Worry About Yet (You’re Right)
You are correct to defer:
- Locking protocols
- Version governance
- Editorial workflow
- Collaboration permissions

Right now the priority is:
> **“Does the saga obey its own laws under stress?”**

Admin comes *after* the laws are proven survivable.

---

## 6. Strong Recommendation for Next Migration Step
Given your answer, the **best next file to migrate** is:

> **`rules/breadcrumb-system.md`**

Why:
- It touches *everything*
- It’s already well-formed in your project memory
- It will immediately clarify how grids should be built

After that:
1. Möbius Logic  
2. Fun Layer  
3. Beat Validation Framework  

Once those four exist, the grids will almost build themselves.

If you want, next message you can say:
> “Let’s migrate the Breadcrumb System into source_canon.”

And I’ll extract, normalize, and GitHub-ready it with zero admin overhead.

## USER

fully review information in project memory and verify that is the best next step. Let's consider ideal file list. It seems like Mechanica really ought to break into several smaller targeted files, etc. Our goal is to be robust but manageable

## ASSISTANT

I reviewed what’s already locked in project memory, and with *your* current repo state (characters solid, factions/antags partly staged, `source_canon` scaffolded), the best next step is **not** Breadcrumbs first.

### Why (based on what’s in memory)
Your breadcrumb/Möbius/fun systems are *powerful*, but they **depend on stable underlying physics + channel boundaries** to avoid “beat logic” accidentally implying illegal mechanics (especially around MT/VT/LT separation, resonance costs, corridor/weather behavior, and VFX ceilings). In the memory set you already have:

- **Mechanica v4** is the authoritative mechanics canon (replacing v3) and it governs action costs, environment modifiers, and resonance-state behavior.
- **Veil System Canon v3** governs shard progression, ascension constraints, and the Mending rules.
- **Tech & Comms v2 + MT/VT/LT supplement** is a hard boundary layer that prevents a ton of drift.
- **Resonance Topology + Symbol/Motif + Voice systems** are the “expression” layers that everything else should reference.

So the most robust, manageable path is:

> **Split and migrate the physics/boundary layer first (as small targeted files), then migrate beat-validation layers (breadcrumb/Möbius/fun) to guide grids.**

That gives you robustness without bloat.

---

## Ideal file list (robust but manageable)

I’m proposing a “**thin core**” (authoritative) + “**optional overlays**” (audit and beat logic), with *small files* that are easy to reference and update.

### A) `/rules/` — constraints + audit frameworks (but light admin)
**1. rules/channel-boundaries.md**  
MT ≠ VT ≠ LT, “no digital transmission,” how distortion works, who can perceive what.

**2. rules/forbidden-behaviors.md**  
No resurrection; Tahl = echo only; ascension gating; no “public metaphysics”; no magic-consent shortcuts, etc.

**3. rules/continuity-guards.md**  
Your “hard locks” that matter to writing: Mending final chapter only, Tahl flare penultimate only, etc.

**4. rules/audit-mobius.md**  
Möbius Audit System (humanity-pass, breadcrumb-pass, resonance logic, antagonist-pressure, emotional circuit).

**5. rules/breadcrumb-system.md**  
Breadcrumb definitions + payoff types + “minimum breadcrumb density” guidance.

**6. rules/fun-layer.md**  
FUN mode definition + oxygen rule (1 fun beat per 5–8 episodes) + what counts.

> Light admin means we skip locking protocols for now, but these six are “behavioral rules,” not admin.

---

### B) `/systems/` — mechanics + world physics (split Mechanica)
Mechanica *should* be split. Right now it’s doing too many jobs: equation, costs, corridor ecology, weather, and action routing.

**7. systems/resonance-core.md**  
RP equation (Will×Emotion×Intent), on-page proxy, definitions, ceilings.

**8. systems/uars-costs.md**  
Boost logic, >20% consequences, cost ladders, recovery/strain rules.

**9. systems/environment-modifiers.md**  
Conductivity hierarchy (water/humidity/glass/metal/stone/air/crowds), RO modifiers, how environment changes cost.

**10. systems/corridors-u1-u7.md**  
Corridor tier behaviors (U1–U7), what’s allowed/forbidden per tier, signature tells.

**11. systems/resonance-weather-w0-w4.md**  
Clear→Landfall, comms/travel implications, pacing and risk.

**12. systems/action-routing.md**  
Your Symbolic Action Engine / ActionState routing (baseline→rupture→proto) with permissions.

**13. systems/symbol-motif-taxonomy.md**  
Geometry/light/color/sound/environment motifs + resonance-state iconography (CALM/BLOOM/SHARD/etc).

**14. systems/voice-systems.md**  
POV voice constraints + metaphoric grammars (already canon in memory).

This split makes each file *targeted* and keeps updates low-risk.

---

### C) `/metaphysics/` — veil, shards, ascension, post-mending
Keep this separate from “systems” because it’s saga-specific metaphysical law.

**15. metaphysics/veil-system.md**  
Veil System Canon v3 distilled: shard progression (Flicker→Rupture), Veil cap model, prohibited outcomes.

**16. metaphysics/ascension-and-echo.md**  
Ascendant Trio rules, Intent transfer, Tahl echo interface, “no resurrection.”

**17. metaphysics/mending-and-breathable-veil.md**  
Mending event constraints + Breathable Veil filtration + Echo Node conversion.

**18. metaphysics/post-mending-ecology.md**  
Post-Mending Master Canon v2.0 distilled: what changes, what remains imperfect, LT rules.

---

### D) `/tech/` — tech boundaries (keep small + strict)
**19. tech/tech-comms-rules.md**  
Tech & Comms v2: AR/holochat norms, failure behavior under resonance, resopunk drift.

**20. tech/channels-mt-vt-lt.md**  
Supplement card distilled: MT/VT/LT separation, exceptions, placement rules.

---

### E) `/grids/` — applied maps (only after rules + systems exist)
Not yet—but when ready, grids should *reference* the above.

**21. grids/ecid-schema.md**  
Your ECID fields + allowed enums (U/W/MODE/HEAT/FX/RES).

**22. grids/sid-bid-schema.md**  
SID and BID rules (you already have Content ID spec in memory).

**23. grids/beat-matrix-templates.md**  
Templates that tags FUN, breadcrumb IDs, audit hooks—no prose.

---

## What is the best “next step” now?

Given your goal (“robust but manageable”), the best next step is:

### **1) Create the split skeleton for Mechanica + boundaries**
Start by migrating these three files (small, high-leverage):

1) `rules/channel-boundaries.md`  
2) `systems/resonance-core.md`  
3) `systems/uars-costs.md`

Reason: this creates the **physics anchor** that every later file can safely reference—especially breadcrumb and grids.

### **2) Then migrate the audit/beat logic**
After the above, migrate:

- `rules/audit-mobius.md`
- `rules/breadcrumb-system.md`
- `rules/fun-layer.md`

Now grids can be built without accidentally inventing mechanics.

---

## Practical note on “source_canon” vs “authoritative”
To keep this manageable:

- Put the **raw memory dumps** into `source_canon/.../*_raw.md`
- Put the **distilled, reference-safe** versions into `/rules`, `/systems`, `/metaphysics`, `/tech`

That way you don’t lose nuance, but you keep the active surface area small.

---

## If you want to proceed immediately
Tell me which one you want first, and I’ll output a GitHub-ready MD (clean headings, bullets, minimal prose):

- `rules/channel-boundaries.md` (MT/VT/LT + perception + distortion rules) **← best first**
- OR `systems/resonance-core.md` (RP equation + definitions + ceilings)
- OR `systems/uars-costs.md` (boosts, cost ladders, consequences)

If you pick the first, the rest of the stack becomes much easier to distill without drift.

## USER

consider the proposed system with our production pipeline (beat generation here, prose generation in sudowrite, etc)

## ASSISTANT

Totally—if your pipeline is **beat generation here → prose generation in Sudowrite**, then the repo structure should optimize for two things:

1) **Fast, reliable beat authoring** (small, loadable rule modules)  
2) **Prose safety rails** for Sudowrite (short “style + constraints packs” you can paste in)

That changes the “ideal” architecture slightly: we should prioritize **promptable bundles** and **audit checkpoints**, not just encyclopedic canon.

---

## 1) What the pipeline actually needs from GitHub

### For beat generation (ChatGPT)
You need:
- **Hard constraints** (what is illegal)
- **Physics** (what can happen and what it costs)
- **Beat tagging schema** (SID/ECID/BID + modes)
- **Audit passes** (Möbius, breadcrumb, antagonist pressure, emotional circuit)
- **Tone valves** (FUN layer + romance ladder + horror permissions)

Key trait: **modular retrieval**.
You don’t want to “load Mechanica,” you want to load:
- “Action costs”
- “Corridor behavior”
- “Channel boundaries”
…depending on the scene.

### For prose generation (Sudowrite)
You need:
- **Voice packs** per POV (metaphor domain, cadence, forbidden language)
- **VFX lexicon** (what resonance looks/sounds like)
- **Content permissions** (heat ladder, no-magic phrasing, no resurrection)
- **Sensory constraints** (1–2 motif channels per beat; corridor/weather impacts cadence)

Key trait: **pasteable**.
Sudowrite likes concise, directive “style sheets,” not huge bibles.

---

## 2) Therefore: two-layer output model
Keep your canon files, but add **production packs** designed for the tools.

### Layer A — Canon (authoritative reference)
Lives in `/rules`, `/systems`, `/metaphysics`, `/tech`, `/art`.

### Layer B — Production Packs (tool-facing bundles)
Lives in `/templates` (or `/production_packs` if you prefer).

These are *curated subsets* that map to your workflow.

---

## 3) Recommended Production Packs (high leverage)

### A) Beat Generation Packs (ChatGPT)
**templates/beat-pack_core.md**  
Contains only what beats need every time:
- MT/VT/LT boundaries
- RP equation + cost logic summary
- Corridor tiers summary
- Weather ladder summary
- ActionState routing (baseline→proto)
- “never do” list (resurrection, etc.)
- Beat tag schema reminders (SID/ECID/BID)

**templates/beat-pack_romance.md**  
- Romance system canon (H0–H4, S0–S8)
- Scene permission triggers + forbidden contexts (U6/combat/collapse cores)
- Resonance–intimacy overlay tells + risks

**templates/beat-pack_fun.md**  
- FUN rules + what counts
- Placement heuristic (1 per 5–8 episodes)

**templates/beat-pack_antagonist-pressure.md**  
- Antagonist escalation rules (institution→extremist→collapse)
- “human-led, emotionally grounded” constraints
- Pressure vectors checklist for beats

**templates/beat-pack_audit.md**  
- Möbius Audit System (the five passes)
- Quick “pass/fail” questions per pass

**Why this helps:**  
When you start a beat session, you paste **one pack** (core + optional) and you’re off.

---

### B) Prose Generation Packs (Sudowrite)
Sudowrite is happiest with ~300–800 words of constraints. So we create paste-sized sheets.

**templates/prose-pack_global.md**
- Prose guardrails: “sensory-first, no prophecy, no magic lexicon”
- Motif rule: pick 1–2 channels max
- Corridor/weather impacts cadence + distortion
- Tech distortion rules (resonance disrupts, never transmits)
- VFX ceilings (FX0–FX3 guidance)

**templates/prose-pack_[POV].md** (Seraphine, Lucien, etc.)
- Metaphor domains + cadence
- Emotional syntax
- Forbidden behaviors/phrases
- Intimacy language permissions for that POV
- Signature tells (light/geometry/sound)

**templates/prose-pack_resonance-visuals.md**
- Color/geometry/sound lexicon
- State iconography (CALM/BLOOM/SHARD/RUPTURE/NODE/VT/LT)

**Why this helps:**  
You can attach a beat plus the relevant **prose pack** and Sudowrite will stay canon-consistent.

---

## 4) How this changes the “Mechanica split” decision
Yes—split Mechanica, but split it along **production use-cases**, not academic categories.

Best splits for your pipeline:

1) `systems/resonance-core.md` (equation + definitions)  
2) `systems/uars-costs.md` (boosts + consequences)  
3) `systems/corridors-u1-u7.md` (scene legality + tells)  
4) `systems/weather-w0-w4.md` (travel/comms/pacing effects)  
5) `rules/channel-boundaries.md` (MT/VT/LT + distortion)  

These five become the backbone of:
- `templates/beat-pack_core.md`
- `templates/prose-pack_global.md`

Everything else can come later without blocking production.

---

## 5) Where breadcrumb/Möbius/fun should go in *this* pipeline
You asked earlier whether these should live in rules to guide grids.

With the pipeline lens:

- **Yes, put them in `/rules/`** (they are validation logic)
- Also create **a distilled checklist version** in `/templates/beat-pack_audit.md`

Because in practice you won’t open `/rules/mobius.md` mid-session.  
You’ll paste the audit checklist at the end of beat generation.

---

## 6) Minimal viable file list to unblock production (robust + manageable)
If you want the smallest set that makes beats + Sudowrite reliable:

### Canon
- `rules/channel-boundaries.md`
- `systems/resonance-core.md`
- `systems/uars-costs.md`
- `systems/corridors-u1-u7.md`
- `systems/weather-w0-w4.md`
- `rules/fun-layer.md`
- `rules/breadcrumb-system.md`
- `rules/audit-mobius.md`
- `systems/voice-systems.md` (already in memory)

### Production packs
- `templates/beat-pack_core.md`
- `templates/beat-pack_audit.md`
- `templates/prose-pack_global.md`
- `templates/prose-pack_[POV].md` (start with your top 3 POVs used most)

This keeps the repo **manageable** while making your production loop **fast**.

---

## 7) Best next step (pipeline-optimized)
Given all that, the best next step is:

### Create the **Beat Pack Core** and **Prose Pack Global** *after* we distill 3 canon files:
1) `rules/channel-boundaries.md`  
2) `systems/resonance-core.md`  
3) `systems/corridors-u1-u7.md`

Those three prevent 80% of drift in both tools.

---

If you want, I can draft the **exact initial file contents** for those three (GitHub-ready markdown), then immediately assemble:

- `templates/beat-pack_core.md`
- `templates/prose-pack_global.md`

…so you can test the full pipeline right away (beats here → paste pack into Sudowrite → prose stays legal).

## USER

review for how we keep this manageable

## ASSISTANT

To keep this manageable, the trick is **controlling surface area**: only a small number of files should be “hot” (used daily), and everything else should be either (a) cold reference, or (b) source_canon dumps you rarely open.

Here’s the tight system I recommend for your pipeline.

---

## 1) Adopt a 3-tier “temperature” model
### Hot (daily production)
- Short, stable, pasteable, used every session.
- Lives in `/templates/`
- Goal: **You never have to open the big canon files mid-session.**

### Warm (authoritative canon modules)
- Small, targeted files you update occasionally.
- Lives in `/rules`, `/systems`, `/metaphysics`, `/tech`, `/art`
- Goal: **One concept per file.**

### Cold (full dumps / exploratory)
- Long, redundant, contradictory allowed.
- Lives in `/source_canon`
- Goal: **Archive and retrieval, not daily use.**

If you enforce this temperature split, the repo stays sane.

---

## 2) Cap the number of “hot” files (hard limit)
If you do nothing else, do this:

> Keep **Hot files ≤ 10 total**.

Suggested hot set (max 8 to start):
1. `templates/beat-pack_core.md`
2. `templates/beat-pack_audit.md`
3. `templates/beat-pack_romance.md` *(optional)*
4. `templates/beat-pack_fun.md`
5. `templates/prose-pack_global.md`
6. `templates/prose-pack_seraphine.md`
7. `templates/prose-pack_kade.md`
8. `templates/prose-pack_lucien.md`

Everything else is warm/cold.

This prevents “where is the rule?” chaos.

---

## 3) Split canon only where production needs it
Yes, Mechanica should split—but don’t over-split.

**Rule:** only split when it:
- is referenced independently in prompts, or
- changes at a different rate than the rest.

### Minimal practical split (5 files)
1. `systems/resonance-core.md` (RP equation, terms)
2. `systems/uars-costs.md` (boosts + consequences)
3. `systems/corridors-u1-u7.md` (scene legality + tells)
4. `systems/weather-w0-w4.md` (pacing/comms/travel effects)
5. `rules/channel-boundaries.md` (MT/VT/LT constraints)

That’s enough to make beats + Sudowrite consistent without spawning 20 microfiles.

---

## 4) Keep “grids” dumb on purpose
Grids should be **applied maps**, not rulebooks.

**Rule:** a grid can only contain:
- IDs (SID/ECID/BID)
- tags (MODE/HEAT/FX/RES)
- references to rule modules
- placement counts (e.g., FUN beat every 5–8 eps)

If a grid needs paragraphs to explain itself, move that prose into `/rules`.

This keeps grids from turning into another canon layer.

---

## 5) Use “packs” as your interface layer (so canon can stay modular)
The packs are your production UI.

- Packs pull from warm files
- Packs stay stable even if canon grows
- Packs are what you paste into sessions/tools

This means you can keep expanding canon without increasing cognitive load.

---

## 6) Enforce a “one-page rule” for anything used in prompts
Anything that you will paste into ChatGPT or Sudowrite should be:

> **≤ 1 page** (roughly 400–800 words)

If it can’t fit, it’s not a pack. It’s a warm file.
And if a warm file is too big, it belongs in source_canon + distilled summary.

---

## 7) Don’t migrate everything—migrate only what prevents drift
Manageability comes from **prioritizing drift-prevention**.

### Drift-preventers (move early)
- MT/VT/LT boundaries
- No resurrection / echo rules
- Resonance costs and ceilings
- Corridor/weather effects
- VFX permissions (what resonance can look like)
- Voice constraints per POV

### Drift-tolerant (move later)
- Long faction histories
- City flavor prose
- Deep tertiary character rosters
- Extended examples

---

## 8) Use a “manifest light” approach (without heavy admin)
You said you want to be light on admin—agreed.

Do only this minimal navigation aid:

Create **three** manifests, no more (for now):
1. `manifests/hot-packs.md` (links to templates)
2. `manifests/core-rules.md` (channels, forbidden, costs, corridors, weather)
3. `manifests/metaphysics.md` (veil/ascension/mending/post)

That’s enough to stay oriented.

---

## 9) Concrete “manageable” initial file list
If you want an MVP that won’t explode:

### Warm (authoritative)
- `rules/channel-boundaries.md`
- `rules/forbidden-behaviors.md`
- `rules/audit-mobius.md`
- `rules/breadcrumb-system.md`
- `rules/fun-layer.md`
- `systems/resonance-core.md`
- `systems/uars-costs.md`
- `systems/corridors-u1-u7.md`
- `systems/weather-w0-w4.md`
- `systems/symbol-motif-taxonomy.md`
- `systems/voice-systems.md`
- `tech/tech-comms-rules.md`

### Hot (packs)
- `templates/beat-pack_core.md`
- `templates/beat-pack_audit.md`
- `templates/prose-pack_global.md`
- `templates/prose-pack_[top POVs].md`

### Cold
- `source_canon/...` dumps as needed

That’s robust and still small.

---

## 10) The simplest rule that keeps everything sane
If you want one governing principle:

> **If you can’t imagine pasting it into a prompt, it shouldn’t be in /templates.**  
> **If you need it weekly, it shouldn’t be in /source_canon.**  
> Everything else lives in warm canon modules.

---

If you want to proceed right now, the most manageable first move is to create the **three warm anchor modules** that everything else depends on, then generate the packs from them:

1) `rules/channel-boundaries.md`  
2) `systems/resonance-core.md`  
3) `systems/corridors-u1-u7.md`

Once those exist, I can assemble your first `templates/beat-pack_core.md` and `templates/prose-pack_global.md` so you can immediately test “beats here → prose in Sudowrite” with minimal overhead.

## USER

beat pack and prose pack makes sense to me, I presume those are what goes to sudowrite, and should be based on Act level information. The rules and systems are referenced primarily referenced here to create the episode level beats and narrative structure? I presume there needs to be a third level for rules and systems to be effectively described to sudowrite as well.

## ASSISTANT

Yes — your understanding is **exactly right**, and your intuition about a *third level* is the key to keeping this both **powerful and manageable**.

Let me lock this cleanly, because what you’re describing is a **three-layer translation stack**, not just “rules vs packs.”

---

## 1. The Correct Mental Model (This Is the Breakthrough)

You do **not** have:
- Rules → Beats → Prose

You actually have:

> **Canon → Planning Translation → Prose Translation**

That middle layer is what you just identified.

Sudowrite cannot “reason” about systems.  
It needs **behavioral constraints expressed as prose instructions**.

---

## 2. The Three-Level Stack (Final, Recommended)

### LEVEL 1 — Canon & Systems (Authoritative, Non-Pasteable)
**Lives in:** `/rules`, `/systems`, `/metaphysics`, `/tech`, `/art`

**Used by:** *You + ChatGPT during planning*

**Purpose:**
- Truth
- Constraints
- Physics
- Audit logic

These files answer:
- *What is allowed?*
- *What is forbidden?*
- *What does it cost?*
- *What does it look like?*

They are **never pasted into Sudowrite** directly.

---

### LEVEL 2 — Planning Packs (Beat-Level Translation)
**Lives in:** `/templates/beat-packs/`

**Used by:** *ChatGPT when generating beats*

These packs translate Level 1 into **actionable beat guidance**.

They are:
- Concise
- Directive
- Tagged
- System-aware

They answer:
- *What can happen in this act?*
- *What kind of beats are legal here?*
- *What must be checked before moving on?*

Examples:
- `beat-pack_core.md`
- `beat-pack_act-ii_loom.md`
- `beat-pack_romance.md`
- `beat-pack_fun.md`
- `beat-pack_audit.md`

These are what *shape episode and scene beats*.

---

### LEVEL 3 — Prose Translation Packs (Sudowrite-Facing)
**Lives in:** `/templates/prose-packs/`

**Used by:** *Sudowrite only*

These do **not explain systems**.  
They express **how prose should behave** *as if the systems already exist*.

They answer:
- *How should this scene feel?*
- *What sensory channels are allowed?*
- *What language should be avoided?*
- *What is the emotional temperature?*

They are:
- Short
- Stylistic
- Behavioral
- Act-aware

---

## 3. Why Act-Level Prose Packs Are the Right Call
You are correct that **Sudowrite packs should be Act-scoped**, not saga- or book-wide.

Reason:
- Acts have different pressure ceilings
- VFX amplitude changes by act
- Emotional syntax shifts by act
- Permission sets widen or narrow

So prose packs should look like:

- `prose-pack_global.md` (always included)
- `prose-pack_act-i.md`
- `prose-pack_act-ii.md`
- `prose-pack_act-iii.md`
- `prose-pack_pov-seraphine.md`
- `prose-pack_pov-kade.md`

Sudowrite prompt = **Global + Act + POV (+ optional Romance/Fun)**

---

## 4. The Missing Third Layer (You Called It)
You are right: rules/systems are **too abstract** to go straight to Sudowrite, but beat packs are **too structural**.

The missing layer is:

> **Prose Constraint Summaries derived from rules & systems**

These live in `/templates/prose-packs/` and are *written as if they were creative directives*, not technical specs.

---

## 5. Example: One Rule, Three Translations

### Level 1 — Canon (systems)
```md
Corridor U6: shard-laced
- Severe resonance fracture
- Prohibited: romance, humor, prolonged dialogue
- Visuals: cold light, hard geometry, sound distortion
```

### Level 2 — Beat Pack
```md
U6 beats:
- Action-forward only
- Dialogue minimal and functional
- Emotional expression through physical strain
- No FUN or ROM beats allowed
```

### Level 3 — Prose Pack (Sudowrite)
```md
This scene occurs under extreme environmental strain.
Language should be clipped and physical.
Emotion is expressed through breath, impact, and effort.
Avoid humor, softness, or extended dialogue.
Light is harsh; sound is distorted.
```

Same rule. Three different languages.

---

## 6. What Goes to Sudowrite (Clear Answer)
Sudowrite gets **only Level 3**:

- Prose Pack Global
- Prose Pack Act-Level
- Prose Pack POV-Level
- Optional Prose Pack Romance/Fun

It never sees:
- RP equations
- Corridor tables
- MT/VT/LT explanations
- Audit logic

Those are already “baked in” by the time prose is generated.

---

## 7. Keep This Manageable (Critical Guardrails)

### A. Hard Limits
- Prose packs: **≤ 600–800 words each**
- Beat packs: **≤ 800 words**
- Canon modules: unlimited, but split by concept

### B. No Duplication Rule
- Rules describe *truth*
- Beat packs describe *allowed planning moves*
- Prose packs describe *how it should feel*

If a sentence appears in two layers, one of them is wrong.

---

## 8. Final Confirmation of Your Assumptions
You asked three implicit questions. All answers are **yes**:

✔ Beat packs guide episode- and scene-level beats  
✔ Rules/systems live primarily here for planning and validation  
✔ A third prose-translation layer is necessary for Sudowrite  
✔ Prose packs should be Act-aware and POV-aware  

You’ve correctly identified the architecture.

---

## 9. Best Next Step (Pipeline-True)
To move forward without sprawl:

1. Distill **one Act** (e.g. Loom Act II) into:
   - `beat-pack_act-ii.md`
   - `prose-pack_act-ii.md`
2. Use it end-to-end:
   - Generate beats here
   - Generate prose in Sudowrite
3. Adjust pack density *before* scaling to other acts

If you want, next we can:
- Draft the **exact template** for an Act-level prose pack
- Or do a **full example**: one scene, all three layers side-by-side
