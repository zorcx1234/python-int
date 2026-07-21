"""
List Comprehensions (Listen Abstraktionen): Kurzform zum Erstellen von Listen
List Comprehensions erzeugen immer eine neue Liste!
"""

from pprint import pprint

# AUfgabe: alle Werte einer Liste quadrieren und in neue Liste schreiben
numbers = [
    1,
    2,
    3,
    4,
]

# Klassisch
new_numbers = []
for number in numbers:
    if number >= 2:
        new_numbers.append(number**2)

print(new_numbers)

# als Listcomprehension
new_numbers = [number**2 for number in numbers if number >= 2]
print(new_numbers)

[print("hallo") for _ in range(10)]


p = [
    {
        "a": i,
        "b": i**2,
        "c": i**3,
    }
    for i in range(10)
]

pprint(p, width=40)
