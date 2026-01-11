---
layout: chapter
title: "Kernkonzepte"
chapter: 13
part: 4
part_title: "Code-Kompetenz"
part_url: "/de/part-4-literacy/"
lang: de
dir: ltr
prev: "/de/part-4-literacy/12-reading"
prev_title: "Code lesen"
next: "/de/part-4-literacy/14-functions"
next_title: "Funktionen und Bibliotheken"
---

Jedes Programm, dem Sie begegnen werden, ist aus denselben grundlegenden Konzepten gebaut: Variablen zum Halten von Daten und Kontrollfluss zum Treffen von Entscheidungen und Wiederholen von Aktionen. Beherrschen Sie diese beiden Ideen und Sie können jeden Code verstehen.

## Variablen

Variablen sind benannte Behälter für Daten. Das ist das gesamte Konzept. Denken Sie an sie als beschriftete Boxen—der Name sagt Ihnen, was drin ist.

![Variablen](/code-with-ai/assets/images/diagrams/13-1-variables.png)
{: .chapter-diagram}
*Abbildung 13.1: Variablen — Benannte Behälter für Daten*
{: .diagram-caption}

Wenn Sie `bolt_diameter = 12.5` schreiben, erstellen Sie eine Box mit der Beschriftung `bolt_diameter` und legen den Wert `12.5` hinein. Später, wenn Sie `bolt_diameter` in einer Berechnung verwenden, holt der Computer diesen Wert aus der Box.

Variablen können verschiedene Datentypen halten. **Zahlen** speichern Mengen wie `count = 42` oder `price = 19.99` oder `stress = 250.5`. **Text** (genannt "Strings") speichert Zeichen wie `name = "M12"` oder `grade = "8.8"` oder `status = "OK"`. **Wahr/Falsch-Werte** (genannt "Booleans") speichern binäre Zustände wie `is_valid = True` oder `has_error = False`. **Listen** speichern mehrere Elemente wie `sizes = [8, 10, 12]`.

Benennung ist enorm wichtig. Verwenden Sie beschreibende Namen ohne Leerzeichen (verwenden Sie stattdessen Unterstriche): `bolt_count` nicht `bolt count`. Beginnen Sie immer mit einem Buchstaben. Gute Namen wie `bolt_count`, `max_stress` und `is_valid` machen Code selbstdokumentierend. Schlechte Namen wie `x`, `bc` und `thing1` zwingen Sie zu raten, welche Daten sie halten.

<div class="key-insight">
<strong>Kernaussage:</strong> Gute Variablennamen machen Code selbstdokumentierend. Wenn Sie <code>if stress > max_allowable_stress</code> lesen, wissen Sie genau, was geprüft wird.
</div>

---

## Kontrollfluss

Kontrollfluss bestimmt, wie Programme Entscheidungen treffen und Aktionen wiederholen. Drei Muster handhaben praktisch alle Programmierlogik.

![Kontrollfluss](/code-with-ai/assets/images/diagrams/13-2-control-flow.png)
{: .chapter-diagram}
*Abbildung 13.2: Kontrollfluss — Entscheidungen und Wiederholung*
{: .diagram-caption}

Das if/else-Muster handhabt Entscheidungen. Der Code prüft eine Bedingung: wenn wahr, macht er eine Sache; wenn falsch, macht er eine andere. Denken Sie daran als Gabelung auf der Straße. Wenn Sie `if stress > 250: print("Fail") else: print("Pass")` sehen, wählt das Programm einen Pfad basierend darauf, ob stress 250 überschreitet.

For-Schleifen wiederholen Aktionen eine bekannte Anzahl von Malen, einmal für jedes Element in einer Sammlung. Wenn Sie `for size in [8, 10, 12]: print(size)` schreiben, macht der Code etwas für jedes Element in der Liste—verarbeite ein Element, gehe zum nächsten, bis alle Elemente behandelt sind.

While-Schleifen wiederholen Aktionen, bis sich eine Bedingung ändert. Wenn Sie `while error > 0.01: refine()` schreiben, läuft der Code weiter, bis der Fehler klein genug ist. Sie wissen nicht im Voraus, wie viele Iterationen es braucht; der Code läuft, bis die Bedingung erfüllt ist.

Diese drei Muster—if/else zum Wählen, for zum Wiederholen durch Elemente, while zum Wiederholen bis fertig—kombinieren sich zu jedem jemals geschriebenen Programm.

<div class="key-insight">
<strong>Kernaussage:</strong> Programme = Daten + Entscheidungen + Wiederholung. Variablen halten die Daten. If/else trifft Entscheidungen. Schleifen handhaben Wiederholung. Das ist alles.
</div>

---

## Probieren Sie es selbst aus

Üben Sie das Verständnis von Kernkonzepten:

- „Erstelle eine Variable, um einen Schraubendurchmesser von 12.5mm zu speichern"
- „Schreibe eine if-Anweisung, die 'Fail' ausgibt, wenn stress über 250 ist"
- „Erstelle eine for-Schleife, die jedes Element in einer Liste von Schraubengrößen ausgibt"
- „Was ist der Unterschied zwischen einer for-Schleife und einer while-Schleife?"
- „Zeig mir ein Beispiel einer Boolean-Variable und wie man sie in einer if-Anweisung verwendet"
- „Erstelle eine Liste von Zahlen und schreibe eine Schleife, die ihre Summe berechnet"

---

## Kernaussage

Variablen und Kontrollfluss sind das Fundament aller Programmierung. Variablen sind nur benannte Behälter—denken Sie an beschriftete Boxen. Kontrollfluss verwendet if/else für Entscheidungen, for-Schleifen zum Verarbeiten von Sammlungen und while-Schleifen zum Wiederholen bis fertig. Jedes komplexe Programm ist aus diesen einfachen Teilen gebaut, die auf verschiedene Weisen kombiniert werden.

Im nächsten Kapitel erkunden wir Funktionen—wie man Code in wiederverwendbare Bausteine verpackt.
