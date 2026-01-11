# Method: Restructuring the Tutorial

## The Problem

We have 16 chapters. Most drawings are too tall for A4 landscape. The text doesn't read like presentation narration. We need to restructure everything, but we need a systematic way to do it.

## The Method: LASSO

Five steps. Do them in order.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   L ─── LIST        What concepts must be taught?               │
│                                                                 │
│   A ─── ARRANGE     What order? What depends on what?           │
│                                                                 │
│   S ─── SPLIT       Break into A4-sized visual units            │
│                                                                 │
│   S ─── SKETCH      Draw each unit (max 35 lines)               │
│                                                                 │
│   O ─── ORATE       Write presentation narration                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Step 1: LIST

Write down every concept the tutorial must teach. One concept per line. Don't organize yet—just dump everything.

**Questions to answer:**
- What must someone know to code with AI?
- What mental models do they need?
- What skills do they need?
- What patterns will they use repeatedly?

**Output:** A flat list of concepts (maybe 30-50 items)

---

## Step 2: ARRANGE

Take the list. Find dependencies. Order by dependency.

```
Concept A
    └── requires: nothing (foundational)

Concept B
    └── requires: Concept A

Concept C
    └── requires: Concept A, Concept B
```

**Rules:**
- If B requires A, A comes first
- Group related concepts into chapters
- Each chapter = one theme

**Output:** Ordered list with chapter groupings

---

## Step 3: SPLIT

For each concept, ask: Can this be drawn in ≤35 lines on A4 landscape?

- **Yes** → One drawing
- **No** → Split into multiple drawings

**Splitting rules:**
- Each drawing = ONE idea
- If you need "and" to describe it, split it
- Better too small than too big

**Output:** List of drawings with titles (e.g., "03a: Breaking Down - The Tree", "03b: Breaking Down - The Rule")

---

## Step 4: SKETCH

Draw each unit in **Draw.io**.

```
┌─────────────────────────────────────────────────────────────────┐
│  TOOL:       Draw.io (app.diagrams.net)                         │
│  PAGE SIZE:  A4 Landscape                                       │
│  OUTPUT:     SVG (web) + PDF (print)                            │
│  SOURCE:     .drawio files in diagrams/source/                  │
└─────────────────────────────────────────────────────────────────┘
```

See `diagrams/WORKFLOW.md` for details.

**Output:** .drawio source files + exported SVG/PDF

---

## Step 5: ORATE

Write narration for each drawing. Style: presenter explaining a slide.

**The voice:**
- Direct ("See this box here...")
- Pointing ("Notice how the arrow goes from...")
- Explaining why ("This matters because...")
- Connecting ("Remember the loop from before? This is where...")

**Structure for each drawing:**
```
[DRAWING]

---

[NARRATION - as if presenting to someone looking at the drawing]
```

**Output:** Complete chapter files with drawing + narration

---

## Applying the Method

### Current State
- 16 chapters
- Drawings too tall
- Text not presentation-style

### Target State
- ? chapters (determined by Step 2)
- All drawings ≤35 lines
- All text reads like presentation

### Next Action
Start with Step 1: LIST all concepts.

---

## Checklist

- [ ] Step 1: LIST - concepts dumped
- [ ] Step 2: ARRANGE - dependencies mapped, chapters defined
- [ ] Step 3: SPLIT - drawings identified and sized
- [ ] Step 4: SKETCH - all drawings created
- [ ] Step 5: ORATE - all narration written
- [ ] Final: Verify A4 fit, test comprehension flow
