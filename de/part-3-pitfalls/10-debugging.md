---
layout: chapter
title: "Debugging"
chapter: 10
part: 3
part_title: "Probleme"
part_url: "/de/part-3-pitfalls/"
lang: de
dir: ltr
prev: "/de/part-3-pitfalls/09-traps"
prev_title: "Häufige Fallen"
next: "/de/part-3-pitfalls/11-unstuck"
next_title: "Wieder vorankommen"
---

Ihr Code funktioniert nicht. Hier ist der systematische Ansatz zur Behebung.

![Der Debugging-Ablauf](/code-with-ai/assets/images/diagrams/de/10-1-the-debugging.png)
{: .chapter-diagram}
*Abbildung 10.1: Der Debugging-Ablauf — Ein systematischer Ansatz*
{: .diagram-caption}

Debugging folgt einem sechsstufigen Prozess. Erstens, **ERFASSEN** Sie die genaue Fehlermeldung—vollständig, keine Zusammenfassung, den tatsächlichen Text. Zweitens, **LOKALISIEREN** Sie die Problemzeile; Fehlermeldungen sagen Ihnen normalerweise, wo Sie suchen sollen. Drittens, sammeln Sie **KONTEXT**, indem Sie den umgebenden Code einbeziehen; die KI muss sehen, was um den Fehler herum passiert. Viertens, **FRAGEN** Sie die KI mit all diesem zusammengestellten Kontext. Fünftens, **WENDEN** Sie die Lösung an, die die KI liefert. Sechstens, **TESTEN** Sie, indem Sie den Code erneut ausführen, um zu verifizieren, dass er tatsächlich behoben ist.

Der Unterschied zwischen schlechten und guten Debug-Anfragen ist deutlich. Eine schlechte Anfrage sagt „Mein Code funktioniert nicht, reparier ihn"—es fehlen die Fehlermeldung, die fehlerhafte Zeile, der relevante Code und was der Code tun sollte. Die KI wird falsch raten. Eine gute Anfrage sagt „Fehler: TypeError in Zeile 15. Hier sind Zeilen 10-20: [Code]. Eingabe war: [1, 2, None]. Erwartet: Summe der Zahlen. Sollte None-Werte überspringen." Das hat den genauen Fehler, Ort, Code-Kontext, Eingabedaten und erwartetes Verhalten. Die KI kann eine präzise Lösung liefern.

<div class="key-insight">
<strong>Kernaussage:</strong> Bessere Information rein = Bessere Lösung raus. Jedes Detail, das Sie liefern, eliminiert Raten.
</div>

---

## Fehlertypen

Das Verständnis von Fehlertypen hilft Ihnen, sie besser für die KI zu beschreiben.

![Fehlertypen](/code-with-ai/assets/images/diagrams/de/10-2-error-types.png)
{: .chapter-diagram}
*Abbildung 10.2: Fehlertypen — Kennen Sie Ihre Fehler*
{: .diagram-caption}

Syntaxfehler bedeuten, dass der Code nicht einmal laufen kann. Dazu gehören fehlende Klammern, Tippfehler und falsche Einrückung. Wenn Sie diese sehen, sagen Sie der KI „Syntaxfehler in Zeile X: [Fehlermeldung]." Diese sind am einfachsten zu beheben—normalerweise muss ein Zeichen oder eine Zeile korrigiert werden.

Laufzeitfehler bedeuten, dass der Code startet, aber mitten in der Ausführung abstürzt. Beispiele sind Division durch Null, Zugriff auf Null-Werte und Datei nicht gefunden. Sagen Sie der KI „Stürzt ab in Zeile X mit [Fehler]. Eingabe war [Daten]." Diese sind mittelschwer, weil Sie verstehen müssen, was den Absturz ausgelöst hat.

Logikfehler sind am schwierigsten—der Code läuft ohne Absturz, gibt aber falsche Ergebnisse. Beispiele sind falsche Berechnungen, Off-by-One-Fehler und falsche Bedingungen. Sagen Sie der KI „Bekommen [X], erwartet [Y]. Hier ist der Code." Diese sind am schwierigsten, weil es keine Fehlermeldung gibt, die Sie leitet; Sie müssen erkennen, was in Code falsch ist, den Python für völlig in Ordnung hält.

<div class="key-insight">
<strong>Kernaussage:</strong> Den Fehlertyp benennen = Schnellere Lösung. Zu wissen, womit Sie es zu tun haben, formt, wie Sie das Problem beschreiben.
</div>

---

## Probieren Sie es selbst aus

Üben Sie Debugging-Prompts:

- „SyntaxError: unexpected EOF. Hier ist mein Code: [einfügen]. Was fehlt?"
- „TypeError: 'NoneType' has no len() in Zeile 8. Hier sind Zeilen 5-12: [einfügen]. Eingabe war: [Daten]"
- „Der Code läuft, gibt aber 15 statt 120 zurück. Hier ist die Funktion: [einfügen]"
- „IndexError: list index out of range. Die Liste hat 5 Elemente. Hier ist die Schleife: [einfügen]"
- „FileNotFoundError für 'data.csv'. Ich führe das Skript von /home/user/project/ aus. Wo sollte die Datei sein?"
- „Der Code funktioniert für kleine Eingaben, stürzt aber bei 1000 Elementen ab. Wie kann ich das debuggen?"

---

## Kernaussage

Debugging ist ein systematischer Prozess, kein zufälliges Raten. Erfassen Sie den Fehler genau. Lokalisieren Sie, wo er auftritt. Sammeln Sie Kontext um das Problem. Fragen Sie die KI mit all diesen Informationen. Wenden Sie die Lösung an. Testen Sie zur Bestätigung. Je mehr Informationen Sie bei Schritt 4 liefern, desto schneller kommen Sie zu funktionierendem Code.

Im nächsten Kapitel werden wir angehen, was zu tun ist, wenn Sie völlig feststecken und nichts zu funktionieren scheint.
