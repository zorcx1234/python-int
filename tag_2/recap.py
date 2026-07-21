"""
Recap Montag

if (len(values) > 0) {
}
"""
from copy import deepcopy


# die beiden numerischen Typen (Unverändliche)
x = 10 # int
y = 1.1 # float
values = ["1", "2", "3"]
print(values)

# Truthiness / Falsiness
if len(values) > 0:
    pass

# pythonisch
if values:
    pass

if not values:
    pass

# Prüfen, ob die "1" in values enthalten ist
if "1" in values:
    pass

# mit for schleife
for value in values:
    if value == "1":
        pass

name = "Bob" # unveränderlich
print(id(name))

name = name.replace("B", "N")
print(id(name))

# Einen Satz anhand von Space splitten
satz = "A brown fox"
words = satz.split()

# Liste veränderlicher Datentyp
print(f"Datentyp von words: {type(words)}")
words[0] = 42
print(words)
words.append(99)
print(words)

# Referenz auf Liste wird kopiert
copy_words = words
shallow_copy = words.copy() # flache Kopie
deep_copy = deepcopy(words) # tiefe Kopie

# Über Sequenzen iterieren
for char in "hamburg":
    print(char)

for word in words:
    print(word)