---
layout: chapter
title: "Wann neu starten"
chapter: 8
part: 2
part_title: "Fähigkeiten"
part_url: "/de/part-2-skills/"
lang: de
dir: ltr
prev: "/de/part-2-skills/07-context"
prev_title: "Kontext"
next: "/de/part-3-pitfalls/09-traps"
next_title: "Häufige Fallen"
---

Manchmal müssen Sie wissen, wann Sie aufhören sollten zu verfeinern und neu anfangen sollten.

![Die Entscheidung](/code-with-ai/assets/images/diagrams/de/08-1-the-decision.png)
{: .chapter-diagram}
*Abbildung 8.1: Die Entscheidung — Verfeinern oder neu starten?*
{: .diagram-caption}

Hier ist ein einfacher Entscheidungsbaum. Die KI hat Ihnen eine Ausgabe gegeben, die nicht richtig ist. Fragen Sie sich: „Ist es nah an dem, was ich will?"

Wenn ja, **VERFEINERN**. Geben Sie Feedback, iterieren Sie, bauen Sie auf dem auf, was Sie haben. Die Struktur ist korrekt, aber es gibt kleine Bugs oder Tippfehler. Vielleicht fehlt ein Feature. Vielleicht muss der Stil angepasst werden oder die Logik ist korrekt aber unvollständig. Diese Probleme lohnt sich vor Ort zu beheben.

Wenn nein, **NEU STARTEN**. Neue Konversation, neuer Prompt, frischer Start. Der Ansatz ist völlig falsch. Die KI hat den Punkt Ihrer Anfrage verfehlt. Es gibt mehrere grundlegende Probleme, die ein komplettes Neuschreiben erfordern würden. Sie drehen sich im Kreis mit denselben sich wiederholenden Fehlern.

Der Sunk-Cost-Trugschluss ist hier stark. Sie haben Zeit in diese Konversation investiert, und es fühlt sich verschwenderisch an, sie aufzugeben. Aber manchmal ist der schnellste Weg zu funktionierendem Code, mit allem, was Sie gelernt haben, von vorne anzufangen.

<div class="key-insight">
<strong>Kernaussage:</strong> Neu anfangen ist kein Scheitern. Es ist Effizienz.
</div>

---

## Die 5-Versuche-Regel

Hier ist eine praktische Regel: maximal fünf Versuche, dann neu starten.

![Die 5-Versuche-Regel](/code-with-ai/assets/images/diagrams/de/08-2-the-5-attempt-rule.png)
{: .chapter-diagram}
*Abbildung 8.2: Die 5-Versuche-Regel — Wissen, wann man Verluste begrenzt*
{: .diagram-caption}

Versuch 1 ist Ihr initialer Prompt—probieren Sie einfach und sehen Sie, was passiert. Versuch 2 verfeinert durch Hinzufügen von mehr Details und Klärung dessen, was falsch ist. Versuch 3 passt an durch Beheben von Fehlern und Ausprobieren anderer Formulierungen. Versuch 4 formuliert um mit einem anderen Ansatz oder neuem Blickwinkel auf das Problem. Versuch 5 ist Ihr letzter Versuch, der alles einbezieht, was Sie gelernt haben.

Wenn Sie nach fünf Versuchen immer noch nicht am Ziel sind, starten Sie neu. Neue Konversation, besserer Prompt, frischer Kontext.

Warum fünf? Zu wenige Versuche (1-2) bedeutet zu früh aufzugeben—Sie könnten eine Information von der Lösung entfernt sein. Genau richtig (3-5) gibt genug Versuche, um Lösungen zu finden, ohne Zeit zu verschwenden. Zu viele Versuche (6+) bringen abnehmende Erträge—der Kontext wird überladen und Sie beginnen, sich im Kreis zu drehen.

Das Schöne am Neustart ist, dass Sie nicht bei null anfangen. Sie wissen jetzt, was nicht funktioniert. Ihr zweiter Versuch wird besser sein, weil Ihr erster Versuch Ihnen etwas beigebracht hat.

<div class="key-insight">
<strong>Kernaussage:</strong> Maximal 5 Versuche, dann neu anfangen mit dem, was Sie gelernt haben.
</div>

---

## Probieren Sie es selbst aus

Üben Sie zu erkennen, wann neu gestartet werden sollte:

- Nach 3 fehlgeschlagenen Versuchen: „Lass mich einen völlig anderen Ansatz versuchen. Anstatt X, versuchen wir Y."
- „Vergiss den vorherigen Code. Hier ist, was ich eigentlich brauche: [klarere Beschreibung]"
- „Der Schleifen-Ansatz funktioniert nicht. Kannst du das stattdessen mit List Comprehension lösen?"
- „Frischer Start: Ich brauche eine Funktion, die X macht. Hier ist ein Beispiel für Eingabe und erwartete Ausgabe."
- „Neuer Ansatz: anstatt alles auf einmal zu verarbeiten, machen wir es in Stapeln von 100"

---

## Kernaussage

Lassen Sie sich nicht von versunkenen Kosten festhalten. Wenn Sie fünf Versuche gemacht haben und immer noch nicht nah dran sind, starten Sie neu. Nehmen Sie, was Sie gelernt haben—wie die Daten aussehen, was nicht funktioniert, welche Randfälle existieren—und schreiben Sie einen besseren Prompt von Grund auf. Ein frischer Start mit Wissen schlägt endlose Iteration auf einem kaputten Fundament.

In Teil 3 werden wir uns die häufigen Fallen ansehen, über die Anfänger stolpern, und wie man sie vermeidet.
