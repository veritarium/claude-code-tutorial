# Diagram Design System

Professional technical illustration standards for AI coding tutorial.
Corporate style with navy blue, red, and steel accents.

---

## Semantic Color Palette

**Core Elements (consistent across ALL diagrams):**

```
YOU / USER:     Deep Blue gradient
                Primary:  #091358
                Dark:     #0d0829
                Label:    #091358 (on white cards)

AI:             Red gradient
                Primary:  #b60002
                Dark:     #690308
                Label:    #b60002 (on white cards)

PROMPT:         Steel Blue gradient
                Primary:  #6882a1
                Light:    #7a94b3
                Label:    #ffffff (on steel background)

OUTPUT/SOFTWARE: Dark Navy gradient
                Primary:  #0d0829
                Dark:     #091358
                Label:    #ffffff (on dark background)
```

**Neutral Foundation:**

```
Background:     #ffffff (pure white)
Card Fill:      #ffffff (white cards inside colored boxes)
Text Primary:   #0d0829 (dark navy)
Text Secondary: #6882a1 (steel blue - descriptions)
Arrows:         #0d0829 (dark navy)
```

---

## Color Usage Rules

1. **YOU elements** — Deep blue gradient (#091358 → #0d0829)
2. **AI elements** — Red gradient (#b60002 → #690308)
3. **PROMPT elements** — Steel blue gradient (#7a94b3 → #6882a1)
4. **OUTPUT elements** — Dark navy gradient (#0d0829 → #091358)

**Card Style:**
- White fill (#ffffff)
- No borders (flat modern look)
- Sharp corners (no rounded)
- Card labels match parent box color

---

## Typography

**Font Family:** Helvetica, Arial, sans-serif

**Hierarchy:**
```
Title:          42px, Bold, #0d0829, letter-spacing: 3px
Subtitle:       18px, Italic, #6882a1
Box Label:      32px, Bold, #ffffff (on colored backgrounds)
Card Title:     22px, Bold, matching parent color
Card Desc:      17px, Italic, #6882a1
Center Labels:  26px, Bold, #ffffff (PROMPT, SOFTWARE)
Legend:         16px, Regular, #6882a1
```

**Rules:**
- ALL CAPS for diagram titles
- ALL CAPS for main labels (YOU, AI, PROMPT, SOFTWARE)
- Sentence case for descriptions
- Italic for all secondary/descriptive text

---

## Shapes

**Main Boxes (YOU, AI):**
- Sharp corners (no radius)
- Gradient fill
- Contains white cards

**Inner Cards:**
- Sharp corners
- White fill (#ffffff)
- 15px left padding for text
- 10px gaps between cards

**Center Boxes (PROMPT, OUTPUT):**
- Sharp corners
- Gradient fill
- Center-aligned text

---

## Spacing

**Grid:** 8px base unit

```
Page margins:     60px
Box padding:      20px (inner cards from box edge)
Card height:      90px
Card gap:         10px (between cards)
Text padding:     15px (from card left edge)
```

**Alignment:**
- Left-align text within cards
- Center-align main box labels (YOU, AI)
- Center-align standalone boxes (PROMPT, SOFTWARE)

---

## Line & Arrow Styles

**Arrows:**
```
Stroke:          3px, #0d0829
Style:           stroke-linecap: round
Arrowhead:       Triangle polygon, filled #0d0829
```

---

## Visual Effects

**Allowed:**
- Linear gradients on main boxes
- Sharp corners throughout
- Clean white space

**Not Allowed:**
- Rounded corners
- Borders/strokes on cards
- Decorative elements (dots, patterns)
- Drop shadows
- Textures

---

## SVG Gradient Definitions

```svg
<linearGradient id="deepBlue" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#091358"/>
  <stop offset="100%" style="stop-color:#0d0829"/>
</linearGradient>

<linearGradient id="brightRed" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#b60002"/>
  <stop offset="100%" style="stop-color:#690308"/>
</linearGradient>

<linearGradient id="steelBlue" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#7a94b3"/>
  <stop offset="100%" style="stop-color:#6882a1"/>
</linearGradient>

<linearGradient id="darkNavy" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#0d0829"/>
  <stop offset="100%" style="stop-color:#091358"/>
</linearGradient>
```

---

## Quick Reference

| Element | Gradient | Text on Element | Card Label Color |
|---------|----------|-----------------|------------------|
| YOU | deepBlue | #ffffff | #091358 |
| AI | brightRed | #ffffff | #b60002 |
| PROMPT | steelBlue | #ffffff | — |
| OUTPUT | darkNavy | #ffffff | — |
| Cards | #ffffff | — | matches parent |
| Secondary | — | #6882a1 | — |

---

## Layout Principles

1. **Clean & Corporate** — No decorative elements
2. **Instant recognition** — YOU=blue, AI=red across ALL diagrams
3. **Sharp modern look** — No rounded corners
4. **High contrast** — White cards on colored backgrounds
5. **Breathing room** — Consistent padding and gaps

---

## File Format

- Source: SVG (hand-coded)
- Export: PNG via rsvg-convert
- Dimensions: 1169 x 827 (A4 landscape ratio)
- Always self-check PNG output before finalizing
