---
layout: chapter
title: "Qualität"
chapter: 16
part: 4
part_title: "Code-Kompetenz"
part_url: "/de/part-4-literacy/"
lang: de
dir: ltr
prev: "/de/part-4-literacy/15-data"
prev_title: "Daten und Dateien"
next: "/de/part-5-building/17-first-project"
next_title: "Ihr erstes Projekt"
---

## Testen

Testen ist Qualitätskontrolle für Code. Genauso wie Sie keine Schraube versenden würden, ohne ihre Maße zu überprüfen, sollten Sie keinen Code verwenden, ohne zu überprüfen, dass er funktioniert.

![Testen](/code-with-ai/assets/images/diagrams/de/16-1-testing.png)
{: .chapter-diagram}
*Abbildung 16.1: Testen — Überprüfen, dass es funktioniert*
{: .diagram-caption}

Manuelles Testen ist der einfachste Ansatz: den Code ausführen, die Ausgabe prüfen, verschiedene Eingaben ausprobieren. Das ist gut für schnelle Überprüfungen und das Erkunden von Verhalten. Sie tun dies bereits natürlich, immer wenn Sie Code ausführen und sich die Ergebnisse ansehen.

Automatisiertes Testen bedeutet, Testcode zu schreiben, der automatisch und wiederholt läuft. Sie definieren Eingaben und erwartete Ausgaben, und das Test-Framework überprüft, ob sie übereinstimmen. Das ist gut für Zuverlässigkeit, weil Tests Regressionen erkennen, wenn Sie Code ändern—wenn Sie versehentlich etwas kaputt machen, sagen Ihnen die Tests das sofort.

Grenzfall-Testen untersucht Randbedingungen: leere Eingaben, Extremwerte, ungültige Daten. Das ist gut für Robustheit, weil Grenzfälle dort sind, wo die meisten Bugs sich verstecken. Was passiert bei Null? Bei negativen Zahlen? Bei leeren Listen? Wenn Sie diese nicht getestet haben, wissen Sie nicht wirklich, ob Ihr Code funktioniert.

Der einfachste Test ist eine Assertion: `assert result == expected, "Test fehlgeschlagen!"` Wenn das Ergebnis nicht mit dem erwarteten Wert übereinstimmt, wissen Sie es sofort. Bitten Sie KI, Tests für Ihre Funktionen zu schreiben—sie ist ausgezeichnet im Generieren von Testfällen.

<div class="key-insight">
<strong>Kernaussage:</strong> Testen vor Vertrauen. Bekannte Eingabe + erwartete Ausgabe = Verifizierung. Getesteter Code = Vertrauenswürdiger Code.
</div>

---

## Projektstruktur

Wenn Projekte über eine einzelne Datei hinauswachsen, wird Organisation wichtig. Ein gut strukturiertes Projekt ist einfacher zu verstehen, zu warten und zu teilen.

![Projektstruktur](/code-with-ai/assets/images/diagrams/de/16-2-project-structure.png)
{: .chapter-diagram}
*Abbildung 16.2: Projektstruktur — Organisierte Dateien*
{: .diagram-caption}

Eine typische Projektstruktur trennt Zuständigkeiten. Der Einstiegspunkt `main.py` ist, wo die Ausführung beginnt. Kernfunktionen leben in `calculations.py`. Hilfs-Utilities gehen in `utils.py`. Eingabedateien leben in einem `data/`-Ordner. Ausgabedateien gehen nach `output/`. Testdateien leben in `tests/`. Dokumentation geht in `README.md`.

Diese Organisation hilft Ihnen, Dateien schnell zu finden, trennt verschiedene Zuständigkeiten (Logik vs. Daten vs. Tests), macht Teilen und Zusammenarbeit einfach und folgt professionellen Standards, die andere erwarten.

Für Dateinamen verwenden Sie Kleinbuchstaben (`calculations.py` nicht `Calculations.py`), verwenden Sie Unterstriche (`bolt_stress.py` nicht `bolt-stress.py`) und seien Sie beschreibend (`test_calculations.py` nicht `test1.py`). Namen sollten den Inhalt beschreiben.

<div class="key-insight">
<strong>Kernaussage:</strong> Organisiertes Projekt = Wartbares Projekt. Fragen Sie KI: „Erstelle eine Projektstruktur für [Beschreibung]" und sie wird alles einrichten.
</div>

---

## Probieren Sie es selbst aus

Üben Sie Testen und Organisieren:

- „Schreibe einen Test, der prüft, ob calculate_stress(1000, 4) 250 zurückgibt"
- „Welche Grenzfälle sollte ich für eine Funktion testen, die zwei Zahlen dividiert?"
- „Füge eine Assertion hinzu, um zu überprüfen, dass das Ergebnis nicht negativ ist"
- „Erstelle eine Projektstruktur für eine Taschenrechner-App"
- „Was ist eine gute Namenskonvention für Testdateien?"
- „Zeig mir, wie ich teste, was passiert, wenn die Eingabe eine leere Liste ist"

---

## Kernaussage

Qualität kommt von Testen und Organisation. Testen Sie manuell für schnelle Überprüfungen, schreiben Sie automatisierte Tests für Zuverlässigkeit und testen Sie immer Grenzfälle. Organisieren Sie Ihr Projekt mit separaten Dateien für verschiedene Zuständigkeiten, halten Sie Daten und Ausgabe getrennt vom Code und fügen Sie Tests und Dokumentation hinzu. Getesteter Code ist vertrauenswürdiger Code, und organisierter Code ist wartbarer Code.

In Teil 5 werden Sie alles zusammenfügen und Ihr erstes vollständiges Projekt bauen.
