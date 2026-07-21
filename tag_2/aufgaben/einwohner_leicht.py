"""

Du entwickelst die Weltkarte eines Fantasy-Rollenspiels.

Für jede Stadt ist die Einwohnerzahl gespeichert:

population = {
    "Minas Tirith": 1854000,
    "Edoras": 274000,
    "Hobbingen": 132000,
    "Bruchtal": 486000,
    "Dale": 821000,
}

1. Erstelle ein neues Dictionary, in dem die Einwohnerzahlen in **Millionen**
gespeichert sind.

2. Gib alle Städte formatiert mit **einer Nachkommastelle** aus.
wert = 23.234223
Nutze dazu f-String, zb. f"Wert {wert:.2f}" oder round(wert, 2)
Gib zusätzlich aus, ob es sich um eine **Großstadt** oder **Kleinstadt** handelt.
Eine Stadt mit mindestens **1 Mio. Einwohnern** gilt als Großstadt.

Beispiel:

Minas Tirith hat 1.9 Mio. Einwohner (Großstadt)
Edoras hat 0.3 Mio. Einwohner (Kleinstadt)
Hobbingen hat 0.1 Mio. Einwohner (Kleinstadt)
"""

populations = {
    "Minas Tirith": 1854000,
    "Edoras": 274000,
    "Hobbingen": 132000,
    "Bruchtal": 486000,
    "Dale": 821000,
}
