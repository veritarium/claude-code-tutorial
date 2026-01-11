---
layout: chapter
title: "Daten und Dateien"
chapter: 15
part: 4
part_title: "Code-Kompetenz"
part_url: "/de/part-4-literacy/"
lang: de
dir: ltr
prev: "/de/part-4-literacy/14-functions"
prev_title: "Funktionen und Bibliotheken"
next: "/de/part-4-literacy/16-quality"
next_title: "Qualität"
---

## Datenstrukturen

Datenstrukturen sind Wege, mehrere Datenstücke zu organisieren. Die Wahl der richtigen Struktur macht Ihren Code sauberer und schneller.

![Datenstrukturen](/code-with-ai/assets/images/diagrams/de/15-1-data-structures.png)
{: .chapter-diagram}
*Abbildung 15.1: Datenstrukturen — Daten organisieren*
{: .diagram-caption}

Eine **LISTE** ist eine geordnete Sammlung. Wenn Sie `bolt_sizes = [8, 10, 12, 16]` schreiben, erstellen Sie eine Sequenz, bei der die Reihenfolge wichtig ist. Greifen Sie auf Elemente nach Position zu: `bolt_sizes[0]` gibt Ihnen `8` (Positionen beginnen bei 0). Sie können Elemente hinzufügen, entfernen und der Reihe nach verarbeiten. Denken Sie daran wie an eine Einkaufsliste.

Ein **DICTIONARY** speichert Schlüssel-Wert-Paare. Wenn Sie `bolt = {"name": "M12", "grade": "8.8", "diameter": 12.0}` schreiben, erstellen Sie benannte Eigenschaften. Greifen Sie auf Elemente nach Namen zu: `bolt["grade"]` gibt Ihnen `"8.8"`. Denken Sie daran wie an ein echtes Wörterbuch, wo Wörter auf Definitionen abgebildet werden.

Ein **TUPLE** ist eine feste, unveränderliche Liste. Wenn Sie `coords = (100.0, 200.5, 50.2)` schreiben, erstellen Sie eine Sequenz, die nach der Erstellung nie geändert werden kann. Gut für Koordinaten, Konstanten und Daten, die sich nie ändern sollten. Denken Sie daran wie an einen versiegelten Umschlag.

Verwenden Sie eine Liste, wenn Sie eine Sammlung ähnlicher Elemente haben und hinzufügen oder entfernen müssen. Verwenden Sie ein Dictionary, wenn Sie benannte Eigenschaften haben und nach Namen suchen müssen. Verwenden Sie ein Tuple, wenn Sie eine feste Gruppe von Werten haben, die sich nie ändern sollten.

<div class="key-insight">
<strong>Kernaussage:</strong> Richtige Struktur = Saubererer, schnellerer Code. Fragen Sie KI: „Welche Datenstruktur sollte ich für [Beschreibung] verwenden?"
</div>

---

## Dateien und I/O

Dateien sind permanenter Speicher. Wenn Ihr Programm endet, verschwinden Variablen, aber Dateien bleiben bestehen. So speichern Sie Ergebnisse und laden Daten.

![Dateien und I/O](/code-with-ai/assets/images/diagrams/de/15-2-files-io.png)
{: .chapter-diagram}
*Abbildung 15.2: Dateien und I/O — Permanenter Speicher*
{: .diagram-caption}

Um eine Datei zu lesen, öffnen Sie sie und laden ihren Inhalt in den Speicher: `with open("data.csv") as file: content = file.read()`. Die Daten fließen von der Festplatte in Ihr Programm, wo Sie sie verarbeiten können.

Um eine Datei zu schreiben, öffnen Sie sie zum Schreiben und senden Daten dorthin: `with open("results.txt", "w") as file: file.write("Spannung: 250 MPa")`. Die Daten fließen von Ihrem Programm zur Festplatte, wo sie nach Programmende bestehen bleiben.

Gängige Dateitypen fallen in zwei Kategorien. Textdateien sind menschenlesbar: `.txt` für reinen Text, `.csv` für Tabellendaten, `.json` für strukturierte Daten. Datendateien benötigen Bibliotheken zum Lesen: `.xlsx` für Excel-Dateien, `.xml` für strukturiertes Format, `.db` für Datenbanken.

<div class="key-insight">
<strong>Kernaussage:</strong> Dateien = Permanente Daten, die Programmneustarts überleben. KI übernimmt die Details des Dateilesens/-schreibens—Sie beschreiben, was Sie brauchen.
</div>

---

## Probieren Sie es selbst aus

Üben Sie mit Datenstrukturen und Dateien:

- „Erstelle eine Liste von Schraubengrößen: 8, 10, 12, 16"
- „Erstelle ein Dictionary für eine Schraube mit Name, Güte und Durchmesser"
- „Wie greife ich auf das dritte Element in einer Liste zu?"
- „Zeig mir, wie ich eine CSV-Datei lese und jede Zeile ausgebe"
- „Wie schreibe ich Ergebnisse in eine Textdatei?"
- „Was ist der Unterschied zwischen einer Liste und einem Tuple?"
- „Erstelle ein Dictionary und iteriere durch alle seine Schlüssel und Werte"

---

## Kernaussage

Datenstrukturen organisieren Ihre Daten: Listen für geordnete Sammlungen, Dictionaries für benannte Eigenschaften, Tuples für feste Werte. Dateien machen Daten permanent: Textdateien für einfachen Inhalt, CSV für tabellarische Daten, JSON für strukturierte Daten. Der typische Arbeitsablauf ist: Daten aus Dateien laden, mit Ihrem Code verarbeiten und Ergebnisse zurück in Dateien speichern. KI übernimmt die Syntaxdetails—Sie konzentrieren sich auf welche Daten Sie brauchen und wie Sie sie organisieren.

Im nächsten Kapitel behandeln wir Qualität—wie Sie Ihren Code testen und Ihre Projekte organisieren.
