"""
CSV lesen

csv.writer (schreibt Listen von Strings)
csv.DictWriter (schreibt Listen von Dicts)
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

data = [
    [1, "bob", "dev", "42"],
    [2, "alice", "admin", "33"],
    [3, "grumpy", "dev", "41"],
]

# mit dem klasssischen Writer schreiben
# mode=w legt eine Datei an, falls sie nicht exisitiert
with open(BASE_DIR / "data1.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "pos", "age"])
    writer.writerows(data)

# Liste von Dicts

persons = [
    {"id": 1, "name": "bob", "job": "dev", "age": 32},
    {"id": 2, "name": "alice", "job": "admin", "age": 42},
    {"id": 3, "name": "otto", "job": "dev", "age": 12},
]

# der Dict Writer
with open(BASE_DIR / "data2.csv", mode="w", encoding="utf-8", newline="") as f:
    # fieldnames müssen im Dict vorkommen, mit keys() bekommt man alle.
    writer = csv.DictWriter(f, fieldnames=persons[0].keys())
    writer.writeheader()  # basiert auf den Feldnamen
    writer.writerows(persons)


# der Dict Writer (wenn man nur eine Untermenge von Key braucht)
with open(BASE_DIR / "data2.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name"], extrasaction="ignore")
    writer.writeheader()  # basiert auf den Feldnamen
    writer.writerows(persons)
