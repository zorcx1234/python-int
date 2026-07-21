"""
Der Datentyp set: (Menge)
veränderlicher Wert, Hash-Set, kennt keine Ordnung
"""

# eine Menge definieren
x = set()
y = {}  # leeres Dict
z = {1, 2, 3}

print(f"Datentyp von t: {type(z)}")  # <class 'set'>

# Menge von doppelten bereinigen
values = [1, 2, 2, 3, 5, 1, 2, 3]  # gewünschtes Result: [1, 2, 3, 5]

# Dopplete Werte rausschmeissen, indem von der Liste ein Set erstellt wird,
# und daraus wieder eine Liste erstellt wird
unique_values = list(set(values))
print(unique_values)  # [1, 2, 3, 5]

gruppe_a = {"Bob", "Alice", "Grumpy", "Quux"}
gruppe_b = {"Bob", "Quux", "Albert"}
gruppe_c = {"Bob", "Quux"}

# Schnittmenge (&)
print("Folgende Personen sind in beiden Gruppen:", gruppe_a & gruppe_b)

# Vereingungsmenge (|)
print("Folgende Personen sind vorhanden:", gruppe_a | gruppe_b)

# ist Gruppe c eine ECHTE Untermenge von gruppe_a
print("Ist gruppe_c eine echte Untermenge von gruppe_a:", gruppe_c < gruppe_a)
print("Ist gruppe_c eine Untermenge von gruppe_c:", gruppe_c <= gruppe_c)
