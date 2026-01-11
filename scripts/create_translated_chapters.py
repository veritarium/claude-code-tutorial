#!/usr/bin/env python3
"""
Create translated chapter files with proper front matter.
The content will be translated separately.
"""

import os
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent

# Chapter structure (part, filename, title_en, title_de)
CHAPTERS = [
    ("part-1-foundations", "01-core", "The Core Partnership", "Die Kernpartnerschaft"),
    ("part-1-foundations", "02-loop", "The Loop", "Die Schleife"),
    ("part-1-foundations", "03-operations", "Six Operations", "Sechs Operationen"),
    ("part-2-skills", "04-decomposition", "Decomposition", "Zerlegung"),
    ("part-2-skills", "05-precision", "Precision", "Präzision"),
    ("part-2-skills", "06-feedback", "Feedback", "Feedback"),
    ("part-2-skills", "07-context", "Context", "Kontext"),
    ("part-2-skills", "08-restart", "When to Restart", "Wann neu starten"),
    ("part-3-pitfalls", "09-traps", "Common Pitfalls", "Häufige Fallen"),
    ("part-3-pitfalls", "10-debugging", "Debugging", "Fehlersuche"),
    ("part-3-pitfalls", "11-unstuck", "Getting Unstuck", "Weiterkommen"),
    ("part-4-literacy", "12-reading", "Reading Code", "Code lesen"),
    ("part-4-literacy", "13-concepts", "Core Concepts", "Kernkonzepte"),
    ("part-4-literacy", "14-functions", "Functions and Libraries", "Funktionen und Bibliotheken"),
    ("part-4-literacy", "15-data", "Data and Files", "Daten und Dateien"),
    ("part-4-literacy", "16-quality", "Quality", "Qualität"),
    ("part-5-building", "17-first-project", "Your First Project", "Ihr erstes Projekt"),
    ("part-5-building", "18-forward", "Moving Forward", "Weiter geht's"),
]

PART_TITLES = {
    "part-1-foundations": ("Foundations", "Grundlagen"),
    "part-2-skills": ("Skills", "Fähigkeiten"),
    "part-3-pitfalls": ("Problems", "Probleme"),
    "part-4-literacy": ("Code Literacy", "Code verstehen"),
    "part-5-building": ("Building", "Bauen"),
}


def get_nav_info(chapter_idx):
    """Get prev/next navigation info for German."""
    prev_url = None
    prev_title = None
    next_url = None
    next_title = None

    lang_prefix = "/de"

    if chapter_idx > 0:
        prev = CHAPTERS[chapter_idx - 1]
        prev_url = f"{lang_prefix}/{prev[0]}/{prev[1]}"
        prev_title = prev[3]  # German title

    if chapter_idx < len(CHAPTERS) - 1:
        next_ch = CHAPTERS[chapter_idx + 1]
        next_url = f"{lang_prefix}/{next_ch[0]}/{next_ch[1]}"
        next_title = next_ch[3]  # German title

    return prev_url, prev_title, next_url, next_title


def create_chapter_file(part, filename, title_en, title_de, chapter_idx):
    """Create chapter file for German."""
    chapter_num = int(filename.split("-")[0])
    part_num = int(part.split("-")[1][0])

    lang_prefix = "/de"
    part_title = PART_TITLES[part][1]  # German part title

    prev_url, prev_title, next_url, next_title = get_nav_info(chapter_idx)

    front_matter = f"""---
layout: chapter
title: "{title_de}"
chapter: {chapter_num}
part: {part_num}
part_title: "{part_title}"
part_url: "{lang_prefix}/{part}/"
lang: de
dir: ltr
"""
    if prev_url:
        front_matter += f'prev: "{prev_url}"\n'
        front_matter += f'prev_title: "{prev_title}"\n'
    else:
        front_matter += 'prev: null\nprev_title: null\n'

    if next_url:
        front_matter += f'next: "{next_url}"\n'
        front_matter += f'next_title: "{next_title}"\n'
    else:
        front_matter += 'next: null\nnext_title: null\n'

    front_matter += "---\n\n"

    # Placeholder content
    content = f"# {title_de}\n\n*Dieses Kapitel wird übersetzt...*\n"

    # Write file
    file_path = PROJECT_DIR / "de" / part / f"{filename}.md"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(front_matter + content)

    print(f"Created: {file_path}")


def main():
    for idx, (part, filename, title_en, title_de) in enumerate(CHAPTERS):
        create_chapter_file(part, filename, title_en, title_de, idx)

    print(f"\nCreated {len(CHAPTERS)} German chapter files")


if __name__ == "__main__":
    main()
