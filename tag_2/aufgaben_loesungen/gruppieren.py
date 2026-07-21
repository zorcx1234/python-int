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
    "Franz Gans",
]

random.shuffle(personen)

gruppen = [personen[i : i + max_gruppe] for i in range(0, len(personen), max_gruppe)]

print(gruppen)
