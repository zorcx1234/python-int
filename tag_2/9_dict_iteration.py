"""
Über ein Dict iterieren
"""
d = dict([("a", 1), ("b", 2),("c", 3),("d", 4)])

# 1. Iteration über Dict liefert die Keys des Dicts
for element in d:
    print(f"{element} hat den Wert {d[element]}")

print("*" * 40)

# 2. Über die Keys iterieren
for element in d.keys():
    print(element)

print("*" * 40)

# 3. über die Values iterieren
for value in d.values():
    print(value)

print("*" * 40)

# 4 über Key Value Paare iterieren
for key, value in d.items():
    print(key, value)