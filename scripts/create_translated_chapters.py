#!/usr/bin/env python3
"""
Create translated chapter files with proper front matter.
The content will be translated separately.
"""

import os
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent

# Chapter structure
CHAPTERS = [
    ("part-1-foundations", "01-core", "The Core Partnership", "Die Kernpartnerschaft", "مشارکت اصلی"),
    ("part-1-foundations", "02-loop", "The Loop", "Die Schleife", "حلقه"),
    ("part-1-foundations", "03-operations", "Six Operations", "Sechs Operationen", "شش عملیات"),
    ("part-2-skills", "04-decomposition", "Decomposition", "Zerlegung", "تجزیه"),
    ("part-2-skills", "05-precision", "Precision", "Präzision", "دقت"),
    ("part-2-skills", "06-feedback", "Feedback", "Feedback", "بازخورد"),
    ("part-2-skills", "07-context", "Context", "Kontext", "زمینه"),
    ("part-2-skills", "08-restart", "When to Restart", "Wann neu starten", "چه زمانی از نو شروع کنیم"),
    ("part-3-pitfalls", "09-traps", "Common Pitfalls", "Häufige Fallen", "تله‌های رایج"),
    ("part-3-pitfalls", "10-debugging", "Debugging", "Fehlersuche", "اشکال‌زدایی"),
    ("part-3-pitfalls", "11-unstuck", "Getting Unstuck", "Weiterkommen", "رهایی از بن‌بست"),
    ("part-4-literacy", "12-reading", "Reading Code", "Code lesen", "خواندن کد"),
    ("part-4-literacy", "13-concepts", "Core Concepts", "Kernkonzepte", "مفاهیم اصلی"),
    ("part-4-literacy", "14-functions", "Functions and Libraries", "Funktionen und Bibliotheken", "توابع و کتابخانه‌ها"),
    ("part-4-literacy", "15-data", "Data and Files", "Daten und Dateien", "داده و فایل‌ها"),
    ("part-4-literacy", "16-quality", "Quality", "Qualität", "کیفیت"),
    ("part-5-building", "17-first-project", "Your First Project", "Ihr erstes Projekt", "اولین پروژه شما"),
    ("part-5-building", "18-forward", "Moving Forward", "Weiter geht's", "گام بعدی"),
]

PART_TITLES = {
    "part-1-foundations": ("Foundations", "Grundlagen", "مبانی"),
    "part-2-skills": ("Skills", "Fähigkeiten", "مهارت‌ها"),
    "part-3-pitfalls": ("Problems", "Probleme", "مشکلات"),
    "part-4-literacy": ("Code Literacy", "Code verstehen", "سواد کد"),
    "part-5-building": ("Building", "Bauen", "ساختن"),
}


def get_nav_info(chapter_idx, lang_idx):
    """Get prev/next navigation info."""
    prev_url = None
    prev_title = None
    next_url = None
    next_title = None

    lang_prefix = "/de" if lang_idx == 1 else "/fa" if lang_idx == 2 else ""

    if chapter_idx > 0:
        prev = CHAPTERS[chapter_idx - 1]
        prev_url = f"{lang_prefix}/{prev[0]}/{prev[1]}"
        prev_title = prev[2 + lang_idx]

    if chapter_idx < len(CHAPTERS) - 1:
        next_ch = CHAPTERS[chapter_idx + 1]
        next_url = f"{lang_prefix}/{next_ch[0]}/{next_ch[1]}"
        next_title = next_ch[2 + lang_idx]

    return prev_url, prev_title, next_url, next_title


def create_chapter_file(part, filename, title_en, title_de, title_fa, chapter_idx):
    """Create chapter files for German and Farsi."""
    chapter_num = int(filename.split("-")[0])
    part_num = int(part.split("-")[1][0])

    for lang_idx, (lang, title, dir_attr) in enumerate([
        ("de", title_de, "ltr"),
        ("fa", title_fa, "rtl")
    ], start=1):
        lang_prefix = "/de" if lang == "de" else "/fa"
        part_title = PART_TITLES[part][lang_idx]

        prev_url, prev_title, next_url, next_title = get_nav_info(chapter_idx, lang_idx)

        front_matter = f"""---
layout: chapter
title: "{title}"
chapter: {chapter_num}
part: {part_num}
part_title: "{part_title}"
part_url: "{lang_prefix}/{part}/"
lang: {lang}
dir: {dir_attr}
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
        if lang == "de":
            content = f"# {title}\n\n*Dieses Kapitel wird übersetzt...*\n"
        else:
            content = f"# {title}\n\n*این فصل در حال ترجمه است...*\n"

        # Write file
        file_path = PROJECT_DIR / lang / part / f"{filename}.md"
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(front_matter + content)

        print(f"Created: {file_path}")


def main():
    for idx, (part, filename, title_en, title_de, title_fa) in enumerate(CHAPTERS):
        create_chapter_file(part, filename, title_en, title_de, title_fa, idx)

    print(f"\nCreated {len(CHAPTERS) * 2} chapter files")


if __name__ == "__main__":
    main()
