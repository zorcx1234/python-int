""" 
Aufgabe: Städte aus Bayern in ein Dictionary übernehmen

Gegeben ist folgende Liste:

staedte = [
    ("München", 1490000, "Bayern"),
    ("Hamburg", 1900000, "Hamburg"),
    ("Nürnberg", 526000, "Bayern"),
    ("Köln", 1080000, "Nordrhein-Westfalen"),
    ("Augsburg", 301000, "Bayern")
]

Erstelle ein leeres Dictionary namens bayern.

Aufgaben:

1. Durchlaufe die Liste mit einer Schleife.
2. Entpacke jedes Tupel in die Variablen:
   - stadt
   - einwohner
   - bundesland
3. Überprüfe, ob das Bundesland "Bayern" ist.
4. Falls ja, füge die Stadt dem Dictionary hinzu:
   - Schlüssel: Stadtname
   - Wert: Einwohnerzahl 
5. Gib das fertige Dictionary aus mit pprint
"""
staedte = [
    ("München", 1_490_000, "Bayern"),
    ("Hamburg", 1_900_000, "Hamburg"),
    ("Nürnberg", 526_000, "Bayern"),
    ("Köln", 1_080_000, "Nordrhein-Westfalen"),
    ("Augsburg", 301_000, "Bayern")
]

bayern = {}
for line in staedte:
    name, einwohner, bundesland = line
    if bundesland.lower() == "bayern":
        bayern[name] = einwohner
print(bayern)