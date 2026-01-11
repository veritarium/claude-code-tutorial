# Diagram Workflow

## Tool: Draw.io (diagrams.net)

### Folder Structure
```
diagrams/
├── source/          ← .drawio files (editable source)
├── export/          ← .svg and .pdf files (for web and print)
└── WORKFLOW.md      ← this file
```

### Creating Diagrams

1. **Open Draw.io**
   - Web: https://app.diagrams.net/
   - Desktop: https://github.com/jgraph/drawio-desktop/releases

2. **Page Setup for A4 Landscape**
   - File → Page Setup
   - Size: A4
   - Orientation: Landscape
   - This ensures all diagrams fit when printed

3. **Save Source File**
   - Save as `.drawio` in `diagrams/source/`
   - Naming: `01-the-core.drawio`, `02-the-loop.drawio`, etc.

4. **Export for Web**
   - File → Export as → SVG
   - Save to `diagrams/export/`
   - Naming: `01-the-core.svg`

5. **Export for Print**
   - File → Export as → PDF
   - Save to `diagrams/export/`
   - Naming: `01-the-core.pdf`

### Embedding in Markdown

```markdown
![The Core](diagrams/export/01-the-core.svg)
```

### Style Guide

**Colors:**
- YOU box: Blue (`#dae8fc`)
- AI box: Green (`#d5e8d4`)
- PROMPT: Red/Pink (`#f8cecc`)
- Your items: Yellow (`#fff2cc`)
- AI items: Purple (`#e1d5e7`)
- Output: Gray (`#f5f5f5`)

**Fonts:**
- Titles: 28px bold
- Box labels: 24px bold
- Content: 14px

**Stroke:**
- Width: 2px
- Rounded corners for main boxes

### Version Control

- `.drawio` files are XML (text-based)
- Git tracks changes
- Can diff between versions
- Store source files, regenerate exports as needed

### GitHub Integration

GitHub can preview `.drawio` files directly in the repository when using the Draw.io integration, but for reliable display, always export to SVG.
