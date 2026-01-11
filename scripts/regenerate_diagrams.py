#!/usr/bin/env python3
"""
Regenerate all tutorial diagrams with:
1. Green for good/success elements, red for bad/error elements
2. Higher quality PNG output (2x resolution)
3. Text overflow checking
"""

import os
import re
import subprocess
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
SOURCE_DIR = PROJECT_DIR / "diagrams" / "source"
OUTPUT_DIR = PROJECT_DIR / "assets" / "images" / "diagrams"

# Color definitions
COLORS = {
    # Good (green)
    "good_primary": "#0a7c42",
    "good_dark": "#065a2f",
    "good_light": "#e8f5ed",

    # Bad (red) - keep existing
    "bad_primary": "#b60002",
    "bad_dark": "#690308",
    "bad_light": "#fff5f5",

    # Neutral (steel blue) - keep existing
    "neutral_primary": "#6882a1",
    "neutral_light": "#7a94b3",

    # User/YOU (deep blue) - keep existing
    "user_primary": "#091358",
    "user_dark": "#0d0829",

    # AI (purple - changed from red to avoid bad semantic)
    "ai_primary": "#6b21a8",
    "ai_dark": "#4c1d6d",

    # Dark navy (for output/software)
    "dark_primary": "#0d0829",
    "dark_secondary": "#091358",
}

# New gradient definitions
NEW_GRADIENTS = '''  <defs>
    <linearGradient id="goodGreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a7c42"/>
      <stop offset="100%" style="stop-color:#065a2f"/>
    </linearGradient>

    <linearGradient id="badRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#b60002"/>
      <stop offset="100%" style="stop-color:#690308"/>
    </linearGradient>

    <linearGradient id="deepBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#091358"/>
      <stop offset="100%" style="stop-color:#0d0829"/>
    </linearGradient>

    <linearGradient id="aiPurple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6b21a8"/>
      <stop offset="100%" style="stop-color:#4c1d6d"/>
    </linearGradient>

    <linearGradient id="steelBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7a94b3"/>
      <stop offset="100%" style="stop-color:#6882a1"/>
    </linearGradient>

    <linearGradient id="darkNavy" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d0829"/>
      <stop offset="100%" style="stop-color:#091358"/>
    </linearGradient>
  </defs>'''


def update_svg_colors(svg_content: str, filename: str) -> str:
    """Update SVG colors based on semantic meaning."""

    # Files that have good/bad semantic colors
    good_bad_files = [
        "05-1-the-spectrum.svg",  # PRECISE = good
        "05-2-five-components.svg",
        "06-1-good-vs-bad.svg",   # GOOD FEEDBACK = good
        "06-2-the-formula.svg",
        "09-1-common-traps.svg",  # Traps = bad
        "09-2-trust-levels.svg",
        "10-1-the-debugging.svg",
        "10-2-error-types.svg",
        "11-1-the-stuck.svg",
        "11-2-escape-routes.svg",
        "16-1-testing.svg",
        "17-2-project-checklist.svg",
    ]

    # Files that use AI color (change red to purple)
    ai_color_files = [
        "01-1-the-core.svg",
        "02-1-the-loop.svg",
        "02-2-the-draft.svg",
        "03-1-six-operations.svg",
        "07-1-the-window.svg",
        "07-2-what-to-share.svg",
    ]

    # Update defs section with new gradients
    defs_pattern = r'<defs>.*?</defs>'
    svg_content = re.sub(defs_pattern, NEW_GRADIENTS, svg_content, flags=re.DOTALL)

    if filename in good_bad_files:
        # Change deep blue (good) to green
        # For "GOOD" sections, change blue to green
        svg_content = svg_content.replace('fill="url(#deepBlue)"', 'fill="url(#goodGreen)"')
        svg_content = svg_content.replace('stroke="#091358"', 'stroke="#0a7c42"')
        svg_content = svg_content.replace('fill="#091358"', 'fill="#0a7c42"')
        svg_content = svg_content.replace('fill="#f0f7ff"', 'fill="#e8f5ed"')

        # Update spectrum gradient if present
        spectrum_old = '''<linearGradient id="spectrumBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#b60002"/>
      <stop offset="50%" style="stop-color:#6882a1"/>
      <stop offset="100%" style="stop-color:#091358"/>
    </linearGradient>'''
        spectrum_new = '''<linearGradient id="spectrumBar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#b60002"/>
      <stop offset="50%" style="stop-color:#6882a1"/>
      <stop offset="100%" style="stop-color:#0a7c42"/>
    </linearGradient>'''
        svg_content = svg_content.replace(spectrum_old, spectrum_new)

    if filename in ai_color_files:
        # Change AI red to purple
        svg_content = svg_content.replace('fill="url(#brightRed)"', 'fill="url(#aiPurple)"')
        svg_content = svg_content.replace('fill="#b60002"', 'fill="#6b21a8"')

    return svg_content


def check_text_overflow(svg_content: str, filename: str) -> list:
    """Check for potential text overflow issues."""
    issues = []

    # Parse text elements and their containers
    text_pattern = r'<text[^>]*x="(\d+)"[^>]*>([^<]+)</text>'
    rect_pattern = r'<rect[^>]*x="(\d+)"[^>]*width="(\d+)"'

    # Check for very long text
    for match in re.finditer(text_pattern, svg_content):
        text = match.group(2)
        if len(text) > 50:
            issues.append(f"{filename}: Long text ({len(text)} chars): '{text[:40]}...'")

    # Check for small font sizes
    small_font_pattern = r'font-size="(\d+)"'
    for match in re.finditer(small_font_pattern, svg_content):
        size = int(match.group(1))
        if size < 12:
            issues.append(f"{filename}: Small font size: {size}px")

    return issues


def convert_to_png(svg_path: Path, png_path: Path, scale: int = 2):
    """Convert SVG to PNG at specified scale."""
    cmd = [
        "rsvg-convert",
        "-z", str(scale),  # Scale factor for higher resolution
        "-o", str(png_path),
        str(svg_path)
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting {svg_path}: {e.stderr.decode()}")
        return False


def process_all_diagrams():
    """Process all SVG diagrams."""
    print("=" * 60)
    print("DIAGRAM REGENERATION")
    print("=" * 60)

    all_issues = []
    processed = 0

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Process each SVG file
    svg_files = sorted(SOURCE_DIR.glob("*.svg"))
    print(f"\nFound {len(svg_files)} SVG files to process\n")

    for svg_path in svg_files:
        filename = svg_path.name
        print(f"Processing: {filename}")

        # Read SVG
        with open(svg_path, 'r') as f:
            svg_content = f.read()

        # Check for issues
        issues = check_text_overflow(svg_content, filename)
        all_issues.extend(issues)

        # Update colors
        updated_svg = update_svg_colors(svg_content, filename)

        # Write updated SVG back
        with open(svg_path, 'w') as f:
            f.write(updated_svg)

        # Convert to PNG
        png_name = filename.replace('.svg', '.png')
        png_path = OUTPUT_DIR / png_name

        if convert_to_png(svg_path, png_path, scale=2):
            processed += 1
            print(f"  ✓ Generated: {png_name}")
        else:
            print(f"  ✗ Failed: {png_name}")

    print("\n" + "=" * 60)
    print(f"SUMMARY: Processed {processed}/{len(svg_files)} diagrams")
    print("=" * 60)

    if all_issues:
        print("\nPOTENTIAL ISSUES FOUND:")
        for issue in all_issues:
            print(f"  - {issue}")
    else:
        print("\nNo text overflow issues detected.")

    return processed, all_issues


if __name__ == "__main__":
    process_all_diagrams()
