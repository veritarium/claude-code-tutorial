---
layout: chapter
title: "Wieder vorankommen"
chapter: 11
part: 3
part_title: "Probleme"
part_url: "/de/part-3-pitfalls/"
lang: de
dir: ltr
prev: "/de/part-3-pitfalls/10-debugging"
prev_title: "Debugging"
next: "/de/part-4-literacy/12-reading"
next_title: "Code lesen"
---

Feststecken ist normal. Es früh zu erkennen spart Zeit.

![Feststecken](/code-with-ai/assets/images/diagrams/de/11-1-the-stuck.png)
{: .chapter-diagram}
*Abbildung 11.1: Die Feststeck-Schleife — Früh erkennen*
{: .diagram-caption}

Die Warnzeichen sind klar: derselbe Fehler kommt immer wieder, eine Sache zu beheben bricht eine andere, die KI gibt wiederholt dieselbe Antwort, Sie haben mehr als fünf Versuche ohne Fortschritt gemacht, und Sie fühlen sich frustriert oder verwirrt. Das sind keine zufälligen Probleme—das sind Symptome des Feststeckens.

Was darunter tatsächlich passiert, variiert. Sie könnten das falsche mentale Modell des Problems haben. Ihnen könnte entscheidende Information fehlen. Die Aufgabe könnte zu komplex für einen einzelnen Prompt sein. Sie könnten das völlig falsche Problem lösen. Oder das Kontextfenster der KI könnte durch zu viel Hin und Her erschöpft sein.

Die Feststeck-Schleife sieht so aus: VERSUCHEN → SCHEITERN → WIEDER VERSUCHEN → GLEICHES SCHEITERN → zurück zu VERSUCHEN. Sie drehen sich im Kreis. Jeder Versuch sieht leicht anders aus, aber Sie machen tatsächlich keinen Fortschritt. Der Schlüssel ist, dieses Muster früh zu erkennen, anstatt sich durchzuquälen.

<div class="key-insight">
<strong>Kernaussage:</strong> Feststecken ist Information. Es sagt Ihnen, dass Ihr Ansatz sich ändern muss—nicht Ihr Code, Ihr Ansatz.
</div>

---

## Auswege

Es gibt sechs Wege, wieder voranzukommen. Wählen Sie einen basierend auf Ihrer Situation.

![Auswege](/code-with-ai/assets/images/diagrams/de/11-2-escape-routes.png)
{: .chapter-diagram}
*Abbildung 11.2: Auswege — Sechs Wege heraus*
{: .diagram-caption}

Neu anfangen bedeutet, eine neue Konversation mit einem neuen Prompt zu beginnen. Das räumt Kontext-Unordnung auf und gibt Ihnen eine frische Perspektive. Verwenden Sie dies, wenn derselbe Fehler sich trotz mehrerer Reparaturversuche wiederholt.

Kleiner aufteilen bedeutet, die Aufgabe in kleinere Stücke zu teilen. Wenn die Aufgabe unmöglich erscheint, ist sie vielleicht tatsächlich mehrere Aufgaben, die sich als eine ausgeben. Lösen Sie jedes Stück unabhängig, dann kombinieren Sie sie, wenn sie funktionieren.

Kontext hinzufügen bedeutet, mehr Informationen mit der KI zu teilen. Schließen Sie vollständige Fehlermeldungen, verwandte Dateien und Beispiele des erwarteten Verhaltens ein. Verwenden Sie dies, wenn die KI über Ihre Situation verwirrt scheint oder irrelevante Vorschläge macht.

Umformulieren bedeutet, Ihr Problem anders zu erklären. Verwenden Sie andere Worte oder fokussieren Sie auf einen anderen Aspekt des Problems. Manchmal versteht die KI Ihre erste Erklärung falsch und eine neue Art es zu sagen klickt sofort.

Nach dem Warum fragen bedeutet, die KI den Fehler erklären zu lassen, anstatt ihn nur zu beheben. Fragen wie „warum passiert das?" und „was verursacht das?" können Verständnis offenbaren, das Ihnen fehlt. Verwenden Sie dies, wenn Sie den Fehler selbst nicht verstehen.

Vereinfachen bedeutet, ein minimales Beispiel zu erstellen, das das Problem reproduziert. Reduzieren Sie das Problem auf seinen Kern—entfernen Sie alles, was nicht wesentlich ist. Wenn die minimale Version funktioniert, fügen Sie Komplexität Stück für Stück zurück, bis Sie finden, was kaputt geht.

<div class="key-insight">
<strong>Kernaussage:</strong> Jedes Problem hat einen Ausweg. Feststecken bedeutet nicht besiegt—es bedeutet, dass Sie einen anderen Ansatz brauchen.
</div>

---

## Probieren Sie es selbst aus

Üben Sie Auswege:

- **Neu anfangen:** „Neuer Ansatz: Ich muss [Ziel beschreiben]. Vergiss vorherige Versuche."
- **Kleiner aufteilen:** „Nur der erste Schritt: die Datei lesen. Noch nicht verarbeiten."
- **Kontext hinzufügen:** „Hier ist der vollständige Fehler, der Code und Beispiel-Eingabe: [alle drei einfügen]"
- **Umformulieren:** „Lass mich anders erklären: Ich habe X, ich will Y, das Problem ist Z."
- **Nach dem Warum fragen:** „Warum passiert dieser Fehler? Was verursacht 'NoneType'-Fehler generell?"
- **Vereinfachen:** „Hier ist ein minimales Beispiel, das fehlschlägt: [3 Zeilen Code]. Warum funktioniert das nicht?"

---

## Kernaussage

Feststecken passiert jedem. Die Fähigkeit ist, es früh zu erkennen und einen Ausweg zu wählen. Wenn Sie fünf Mal ohne Fortschritt versucht haben, stoppen Sie. Fragen Sie sich: Sollte ich neu anfangen? Kleiner aufteilen? Kontext hinzufügen? Umformulieren? Nach dem Warum fragen? Vereinfachen? Einer davon wird Sie wieder in Bewegung bringen. Feststecken ist temporär, wenn Sie Strategien zum Entkommen haben.

In Teil 4 werden wir Ihre Code-Lesefähigkeit entwickeln—die Fähigkeit, Code zu lesen und zu verstehen, auch wenn Sie ihn nicht geschrieben haben.
