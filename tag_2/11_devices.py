"""
(LEICHT)
Gegeben sind zwei Listen:


geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh

Erstelle ein Dict, wobei der Key der Gerätename ist und der Value der entsprechende Verbrauch.
Konvertiere die Werte aus stromverbrauch dazu in floats.

Das neue Dict soll nur Geräte beinhalten, deren Stromverbrauch >= 0.2 kWh

Ergebnis:
{
'Fernseher': 0.3,
 'Kühlschrank': 1.2,
 'Waschmaschine': 2.0
 }

"""
d = {}
geraete = ["Kühlschrank", "Fernseher", "Waschmaschine", "Laptop"]
stromverbrauch = ["1.2", "0.3", "2.0", "0.05"]  # Angaben in kWh

for geraet, verbrauch in zip(geraete, stromverbrauch):
    verbrauch_float = float(verbrauch)
    # ist der verbrauch >= 0.2, wenn ja
    # füge dict hinzu: d[geraet] = verbrauch_float
    if verbrauch_float >= 0.2:
        d[geraet] = verbrauch_float

print("*" * 40)

# mit Walrus-Operator (:=)
for geraet, verbrauch in zip(geraete, stromverbrauch):
    if (verbrauch := float(verbrauch)) >= 0.2:
        d[geraet] = verbrauch

print(d)