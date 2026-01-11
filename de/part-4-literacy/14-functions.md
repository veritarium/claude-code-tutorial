---
layout: chapter
title: "Funktionen und Bibliotheken"
chapter: 14
part: 4
part_title: "Code-Kompetenz"
part_url: "/de/part-4-literacy/"
lang: de
dir: ltr
prev: "/de/part-4-literacy/13-concepts"
prev_title: "Kernkonzepte"
next: "/de/part-4-literacy/15-data"
next_title: "Daten und Dateien"
---

## Funktionen

Eine Funktion ist wie eine Maschine: etwas hineingeben, etwas herausbekommen. Funktionen lassen Sie Code in wiederverwendbare Bausteine verpacken, die Sie immer wieder verwenden können.

![Funktionen](/code-with-ai/assets/images/diagrams/de/14-1-functions.png)
{: .chapter-diagram}
*Abbildung 14.1: Funktionen — Wiederverwendbare Bausteine*
{: .diagram-caption}

Wenn Sie `def calculate_stress(force, area): return force / area` schreiben, erstellen Sie eine Maschine namens `calculate_stress`, die zwei Eingaben nimmt (`force` und `area`), Arbeit verrichtet (sie dividiert) und das Ergebnis zurückgibt. Später können Sie diese Maschine überall verwenden: `result = calculate_stress(1000, 4)` gibt Ihnen 250.

Jede Funktion hat vier Teile. Der **Name** beschreibt, was sie tut (`calculate_stress`). Die **Parameter** sind die Eingaben, die sie braucht (`force`, `area`). Der **Körper** ist die Arbeit, die sie ausführt (`return force / area`). Die **Rückgabe** ist die Ausgabe, die sie produziert (der berechnete Spannungswert).

Funktionen sind wichtig, weil sie Code wiederverwenden lassen—einmal schreiben, viele Male verwenden. Sie organisieren Logik mit klaren Namen für klare Operationen. Sie machen Testen einfach, weil Sie isolierte Einheiten verifizieren können. Und sie zentralisieren Korrekturen—ändern Sie die Funktion einmal und alle Verwendungen werden aktualisiert.

<div class="key-insight">
<strong>Kernaussage:</strong> Funktionen = Wiederverwendbare Codebausteine. Einmal schreiben, überall verwenden.
</div>

---

## Bibliotheken

Bibliotheken sind vorgefertigter Code, den Sie verwenden können. Sie sind Sammlungen von Funktionen, die andere geschrieben und getestet haben, damit Sie das Rad nicht neu erfinden müssen.

![Bibliotheken](/code-with-ai/assets/images/diagrams/de/14-2-libraries.png)
{: .chapter-diagram}
*Abbildung 14.2: Bibliotheken — Auf den Schultern von Riesen stehen*
{: .diagram-caption}

Ohne Bibliotheken braucht das Berechnen eines Durchschnitts fünf Zeilen manuellen Code: eine Summe initialisieren, durch Zahlen schleifen, die Summe akkumulieren, durch die Anzahl teilen. Mit Bibliotheken braucht es eine Zeile: `import statistics` dann `statistics.mean(numbers)`. Eine Zeile, getestet, zuverlässig, korrekt.

Für Ingenieure sind bestimmte Bibliotheken unverzichtbar. Für Mathematik und Wissenschaft: `numpy` handhabt Arrays und Matrizen, `scipy` bietet Ingenieurberechnungen, `pandas` arbeitet mit Datentabellen, und `math` bietet grundlegende Operationen. Für Visualisierung: `matplotlib` erstellt Diagramme und Plots, `plotly` macht interaktive Visualisierungen, `seaborn` produziert statistische Grafiken. Für Dateien und Automatisierung: `os` verwaltet Dateioperationen, `json` liest und schreibt JSON-Daten, `csv` handhabt Tabellenformate, und `datetime` arbeitet mit Daten und Zeiten.

Wenn Sie etwas Spezifisches brauchen, fragen Sie KI: „Welche Bibliothek sollte ich für [Aufgabe] verwenden?" oder „Zeig mir, wie ich [Bibliothek] für [Ziel] verwende."

<div class="key-insight">
<strong>Kernaussage:</strong> Stehen Sie auf den Schultern von Riesen—verwenden Sie Bibliotheken! Jemand hat die meisten gängigen Probleme bereits gelöst.
</div>

---

## Probieren Sie es selbst aus

Üben Sie mit Funktionen und Bibliotheken:

- „Erstelle eine Funktion namens calculate_area, die Breite und Höhe nimmt und die Fläche zurückgibt"
- „Welche Bibliothek sollte ich verwenden, um den Mittelwert einer Zahlenliste zu berechnen?"
- „Zeig mir, wie ich pandas verwende, um eine CSV-Datei zu lesen"
- „Erstelle eine Funktion, die eine Liste nimmt und nur Zahlen größer als 10 zurückgibt"
- „Was macht numpy.array() und wann würde ich es verwenden?"
- „Zeig mir, wie ich die math-Bibliothek importiere und verwende, um eine Quadratwurzel zu berechnen"

---

## Kernaussage

Funktionen verpacken Code in wiederverwendbare Bausteine—einmal definieren, überall verwenden. Bibliotheken sind Sammlungen von Funktionen, die andere bereits geschrieben und getestet haben. Zusammen lassen sie Sie schnell leistungsfähige Programme bauen. Wenn Sie eine Fähigkeit brauchen, prüfen Sie zuerst, ob eine Bibliothek existiert. Wenn Sie Code schreiben, den Sie mehr als einmal verwenden werden, machen Sie eine Funktion daraus.

Im nächsten Kapitel erkunden wir, wie man mit Datenstrukturen und Dateien arbeitet.
