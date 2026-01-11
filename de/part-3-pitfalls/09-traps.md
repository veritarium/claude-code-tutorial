---
layout: chapter
title: "Häufige Fallen"
chapter: 9
part: 3
part_title: "Probleme"
part_url: "/de/part-3-pitfalls/"
lang: de
dir: ltr
prev: "/de/part-2-skills/08-restart"
prev_title: "Wann neu starten"
next: "/de/part-3-pitfalls/10-debugging"
next_title: "Debugging"
---

Sprechen wir über Fehler. Jeder Anfänger macht diese. Jetzt werden Sie es nicht mehr.

![Häufige Fallen](/code-with-ai/assets/images/diagrams/de/09-1-common-traps.png)
{: .chapter-diagram}
*Abbildung 9.1: Häufige Fallen — Fehler, die jeder macht*
{: .diagram-caption}

Es gibt sechs Fallen, die fast jeden Anfänger erwischen. Die erste ist blindes Vertrauen—Code ausführen ohne ihn zu lesen. KI-generierter Code kann Bugs, Sicherheitsprobleme haben oder einfach nicht das tun, was Sie denken. Überprüfen Sie immer vor dem Ausführen, und bitten Sie die KI zu erklären, was der Code tut, wenn Sie unsicher sind.

Die zweite Falle sind vage Prompts. Anfragen wie „mach es besser" oder „reparier das" zwingen die KI zu raten, was Sie meinen, und sie wird normalerweise falsch raten. Seien Sie spezifisch darüber, was falsch ist. Nennen Sie das erwartete Verhalten im Vergleich zum tatsächlichen Verhalten.

Die dritte Falle ist, zu viel auf einmal zu verlangen. Die KI zu bitten „bau mir eine ganze App" gibt ihr zu viel zu bewältigen. Die KI verliert den Fokus, Sie verlieren die Kontrolle, und das Ergebnis befriedigt niemanden. Teilen Sie die Arbeit in kleine Aufgaben auf und bearbeiten Sie ein Feature nach dem anderen.

Die vierte Falle ist, keinen Kontext zu liefern. Fehlermeldungen oder relevanten Code nicht zu teilen lässt die KI blind arbeiten. Sie kann nicht reparieren, was sie nicht sehen kann. Fügen Sie die Fehler ein, schließen Sie den Code ein, teilen Sie den vollständigen Kontext.

Die fünfte Falle ist, zu schnell aufzugeben. Viele Anfänger hören auf, nachdem der erste Versuch scheitert, aber sie könnten eine Iteration vom Erfolg entfernt gewesen sein. Geben Sie 3-5 Versuche, bevor Sie einen anderen Ansatz in Betracht ziehen.

Schließlich ist die sechste Falle, nicht aus dem Code zu lernen, den Sie verwenden. Lösungen kopieren und einfügen ohne sie zu verstehen bedeutet, dass Sie nie Fähigkeiten aufbauen, und Sie werden dieselben Probleme wieder haben. Bitten Sie die KI zu erklären. Lernen Sie aus jeder Lösung. Die wenigen Minuten, die Sie für das Verstehen aufwenden, zahlen sich vielfach aus.

<div class="key-insight">
<strong>Kernaussage:</strong> Die meisten Fallen entstehen, wenn man KI wie Magie behandelt statt wie ein Werkzeug. Bleiben Sie engagiert, bleiben Sie spezifisch, bleiben Sie neugierig.
</div>

---

## Vertrauensstufen

Wie sehr sollten Sie der Ausgabe der KI vertrauen? Es hängt von den Konsequenzen eines Fehlers ab.

![Vertrauensstufen](/code-with-ai/assets/images/diagrams/de/09-2-trust-levels.png)
{: .chapter-diagram}
*Abbildung 9.2: Vertrauensstufen — Wie viel Überprüfung ist nötig*
{: .diagram-caption}

Wenn die Konsequenzen eines Fehlers schwerwiegend sind, brauchen Sie niedriges Vertrauen—überprüfen Sie alles. Das bedeutet sicherheitsrelevanter Code, Finanzberechnungen, sicherheitskritische Systeme und Datenlöschoperationen. Lesen Sie jede Zeile. Testen Sie gründlich. Holen Sie eine zweite Meinung ein, wenn nötig. Verstehen Sie vollständig, bevor Sie deployen.

Für Standardarbeit ist mittleres Vertrauen angemessen—überprüfen Sie den Code und testen Sie ihn. Das umfasst Standardfeatures, Geschäftslogik, API-Integrationen und Datenbankoperationen. Überfliegen Sie den Code, um seine Struktur zu verstehen. Führen Sie grundlegende Tests durch. Prüfen Sie Randfälle. Verifizieren Sie, dass das Verhalten den Erwartungen entspricht.

Wenn wenig auf dem Spiel steht, ist hohes Vertrauen in Ordnung—eine schnelle Prüfung reicht aus. Das gilt für einfache Hilfsprogramme, Formatierungscode, Textmanipulation und Dokumentation. Werfen Sie einen Blick auf die Ausgabe, führen Sie es einmal aus, prüfen Sie, dass es funktioniert, und machen Sie weiter.

Die Kernerkenntnis ist, dass die Vertrauensstufe von den Konsequenzen eines Fehlers abhängt, nicht davon, wie selbstsicher die KI erscheint. Die KI könnte sehr selbstsicher bei Code sein, der Ihre Datenbank löscht. Das bedeutet nicht, dass Sie ihm blind vertrauen sollten. Für einen Schraubenspannungsrechner in einer echten Ingenieuranwendung? Niedriges Vertrauen—alles überprüfen. Für ein Skript, das Dateien in einem Ordner umbenennt? Höheres Vertrauen—eine schnelle Prüfung reicht.

<div class="key-insight">
<strong>Kernaussage:</strong> Höherer Einsatz = Mehr Überprüfung nötig. Vertrauensstufe hängt von Konsequenzen ab, nicht von KI-Selbstsicherheit.
</div>

---

## Probieren Sie es selbst aus

Üben Sie, die Fallen zu vermeiden:

- Statt „Reparier das" → „Die Funktion gibt None in Zeile 12 zurück. Erwartet: eine Liste von Zahlen."
- Statt „Mach es besser" → „Mach die Funktion 50% schneller, indem wiederholte Berechnungen vermieden werden"
- Statt „Bau mir eine App" → „Erstelle eine Funktion, die eine CSV-Datei liest und die Summe von Spalte A zurückgibt"
- „Erkläre, was dieser Code Zeile für Zeile macht: [Code einfügen]"
- „Welche Sicherheitsprobleme könnte dieser Code haben? [Code einfügen]"
- „Ich habe es 5 Mal versucht und bekomme immer denselben Fehler. Hier ist ein frischer Start: [neue Beschreibung]"

---

## Kernaussage

Die sechs Fallen—blindes Vertrauen, vage Prompts, zu große Aufgaben, kein Kontext, zu schnelles Aufgeben und nicht lernen—erwischen die meisten Anfänger. Jetzt, da Sie sie kennen, können Sie sie vermeiden. Bleiben Sie mit dem Code engagiert, seien Sie spezifisch in Ihren Anfragen, teilen Sie Arbeit in kleine Stücke, teilen Sie vollständigen Kontext, halten Sie durch bei Schwierigkeiten, und streben Sie immer danach, zu verstehen, was die KI Ihnen gibt.

Im nächsten Kapitel werden wir Debugging angehen—was zu tun ist, wenn Dinge schiefgehen.
