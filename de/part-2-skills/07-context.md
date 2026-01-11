---
layout: chapter
title: "Kontext"
chapter: 7
part: 2
part_title: "Fähigkeiten"
part_url: "/de/part-2-skills/"
lang: de
dir: ltr
prev: "/de/part-2-skills/06-feedback"
prev_title: "Feedback"
next: "/de/part-2-skills/08-restart"
next_title: "Wann neu starten"
---

Dieses Konzept wird verändern, wie Sie mit KI arbeiten.

![Das Fenster](/code-with-ai/assets/images/diagrams/de/07-1-the-window.png)
{: .chapter-diagram}
*Abbildung 7.1: Das Fenster — KI sieht nur, was im Prompt steht*
{: .diagram-caption}

Schauen Sie sich dieses Diagramm an. Die große Box repräsentiert IHRE WELT—alles, was Sie über Ihr Projekt wissen, Ihre Geschichte, Ihre Anforderungen, Ihre Präferenzen. Die kleine Box darin repräsentiert das FENSTER DER KI—was die KI tatsächlich sehen kann.

KI kann Ihren Bildschirm nicht sehen. Sie kann nicht auf Ihre Dateien zugreifen. Sie erinnert sich nicht an Ihre vergangenen Gespräche. Sie kennt Ihr Projekt nicht. Sie kann Ihre Gedanken nicht lesen. Sofern Sie es ihr nicht sagen, hat KI keinen Zugang zu dem Kontext, den Sie für selbstverständlich halten.

All diese Informationen, die außerhalb des Fensters schweben—Ihre Projektgeschichte, andere Dateien, Geschäftsanforderungen, Team-Coding-Standards, vergangene Gespräche, Ihre Präferenzen, warum Sie das tun—nichts davon existiert für die KI, bis Sie es teilen.

Deshalb scheitern vage Prompts. Wenn Sie sagen „repariere die Funktion", nehmen Sie an, dass die KI weiß, welche Funktion, was damit nicht stimmt und wie Sie sie repariert haben wollen. Die KI weiß nichts davon. Sie müssen explizit relevanten Code, Fehlermeldungen, Einschränkungen und Anforderungen teilen. Machen Sie das Fenster größer. Je mehr Kontext Sie teilen, desto besser versteht die KI.

<div class="key-insight">
<strong>Kernaussage:</strong> KI sieht nur, was im Prompt steht. Alles andere ist unsichtbar.
</div>

---

## Was Sie teilen sollten

Es gibt fünf Arten von Kontext, die KI-Ergebnisse dramatisch verbessern.

![Was teilen](/code-with-ai/assets/images/diagrams/de/07-2-what-to-share.png)
{: .chapter-diagram}
*Abbildung 7.2: Was teilen — Fünf Arten von Kontext*
{: .diagram-caption}

Einschränkungen sind die Limitierungen und Anforderungen, die Ihre Lösung begrenzen. „Muss in Python 3.8 funktionieren" eliminiert Lösungen mit neueren Features. „Keine externen Bibliotheken" fokussiert die KI auf Standardbibliothek-Lösungen. „Maximal 100 Zeilen Code" gibt ein Größenziel vor. Ohne Kenntnis Ihrer Einschränkungen könnte die KI Ihnen etwas technisch Korrektes geben, das in Ihrer tatsächlichen Situation unbrauchbar ist.

Präferenzen sind Ihre Stil- und Vorgehenswahlentscheidungen. Die Bitte um „beschreibende Variablennamen" formt, wie die KI Code schreibt. Die Anforderung „Kommentare für komplexe Logik" bestimmt das Dokumentationsniveau. „Bevorzuge einfach gegenüber clever" leitet die KI zu wartbaren Lösungen. Wenn Sie Präferenzen teilen, erhalten Sie Code, der Ihren Standards entspricht, anstatt den Standardeinstellungen der KI.

Geschichte ist das, was zu diesem Punkt in Ihrem Projekt geführt hat. Die Erwähnung „wir haben X versucht, aber es ist gescheitert wegen Y" verhindert, dass die KI denselben gescheiterten Ansatz vorschlägt. Der Hinweis „dies ist Teil eines größeren Systems" hilft der KI, den Umfang zu verstehen. Das Teilen von „die vorherige Version hatte diesen Bug" gibt der KI Kontext darüber, was zu vermeiden ist. Geschichte verhindert, dass Sie im Kreis laufen.

Fehler sind die genauen Meldungen und Symptome, die Sie sehen. Das Einfügen von „TypeError: 'NoneType' has no len()" gibt der KI den spezifischen Fehler zur Diagnose. Die Beschreibung „passiert wenn Eingabe eine leere Liste ist" identifiziert den Auslöser. „Zeile 42 in der process_data-Funktion" lokalisiert den Ort genau. Je präziser Ihre Fehlerbeschreibung, desto schneller kann die KI es beheben.

Dateien sind der relevante Code und die Daten für Ihre Aufgabe. Das Einbeziehen von „hier ist die aktuelle Funktion: [Code]" zeigt der KI, woran Sie arbeiten. Das Bereitstellen von „Beispiel-Eingabedaten: [Daten]" hilft der KI, das Format zu verstehen. Das Anhängen von „zugehörige Konfigurationsdatei: [Config]" gibt Systemkontext. KI kann bei Code, den sie nicht sehen kann, nicht helfen.

<div class="key-insight">
<strong>Kernaussage:</strong> Mehr Kontext = Weniger Iterationen = Bessere Ergebnisse.
</div>

---

## Probieren Sie es selbst aus

Üben Sie, Kontext bereitzustellen:

- „Hier ist meine Funktion [Code einfügen]. Sie sollte X zurückgeben, gibt aber Y zurück. Die Eingabedaten sehen so aus: [Beispiel]."
- „Ich verwende Python 3.8 ohne externe Bibliotheken. Erstelle eine Funktion, die..."
- „Dieser Code muss in unter 1 Sekunde für 10.000 Elemente laufen. Optimiere diese Funktion: [einfügen]"
- „Wir haben Rekursion versucht, aber das Stack-Limit erreicht. Schlage einen iterativen Ansatz vor."
- „Hier ist der Fehler: [vollständigen Fehler einfügen]. Hier ist der Code: [einfügen]. Hier ist die Eingabe: [einfügen]."
- „Passe diesen Codestil an: [Beispiel einfügen]. Schreibe jetzt eine neue Funktion, die..."

---

## Kernaussage

Jedes Mal, wenn Sie die KI prompten, denken Sie an das Fenster. KI sieht nur, was Sie ihr vorlegen. Bevor Sie absenden, fragen Sie sich: Habe ich die Einschränkungen geteilt? Die Präferenzen? Die Geschichte? Die Fehler? Den relevanten Code? Je mehr Kontext Sie bereitstellen, desto näher kommt die KI beim ersten Versuch an genau das, was Sie brauchen.

Im nächsten Kapitel lernen wir, wann man aufhören sollte zu iterieren und stattdessen neu anfangen sollte.
