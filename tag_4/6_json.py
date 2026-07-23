"""
JSON

Python                  JSON
-----------------------------------------
dict                =>  object
list, tuple         =>  array
str                 =>  string
int, float          =>  number
True                =>  true
False               =>  false
None                =>  null
Set                 =>  Fehler


dumps => erzeugt einen Json-String aus einem Python-Objekt
dump => speichert ein Python objekt in eine Datei als JSON
"""

from pathlib import Path
import json

BASE_DIR = Path(__file__).parent

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian",
        "hobbies": ("Sport", "Coding"),
    },
}

print(data)
print("*" * 40)
print(json.dumps(data))

# Json in eine Datei schreiben
with open(BASE_DIR / "beeblebrox.json", mode="w") as f:
    json.dump(data, f, indent=2)

# JSON lesen
with open(BASE_DIR / "beeblebrox.json", mode="r") as f:
    content = json.load(f)

print(content)
