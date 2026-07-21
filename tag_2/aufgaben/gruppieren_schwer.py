"""
Aufgabe:

Die 8 Bewohner von Entenhausen sollen zufällig
in Arbeitsgruppen eingeteilt werden.

- Jede Gruppe darf maximal 3 Personen enthalten.
- Mische die Reihenfolge der Personen zufällig.
- Erzeuge anschließend eine Liste von Gruppen.
- Das Ergebnis soll eine Liste von Listen sein.

[
    ['Gustav', 'Donald', 'Tick'],
    ['Track', 'Daisy', 'Trick'],
    ['Dagobert', 'Daniel Düsentrieb']
]
"""

import random

max_gruppe = 3

personen = [
    "Donald",
    "Daisy",
    "Dagobert",
    "Tick",
    "Trick",
    "Track",
    "Gustav",
    "Daniel Düsentrieb",
]

random.shuffle(personen)
