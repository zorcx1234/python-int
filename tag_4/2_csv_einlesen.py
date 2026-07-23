"""
CSV lesen

csv.reader => Klassische, Rowbasierte Reader (jede Zeile als Liste von Strings)
csv.DictReader => liest jede Zeile in ein Dict
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent


def read_csv(filename: str) -> None:
    with open(BASE_DIR / filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(
            f,
            delimiter=",",
            fieldnames=["id", "name", "age", "city"],
        )
        # per default wird der CSV-Header als Key für das DIct genommen
        for rowdict in reader:
            print(rowdict)


# falls eine DAtei keinen Header hat, muss er via Fieldnames definiert werden
read_csv("persons_ohne_header.csv")
print("*" * 40)
read_csv("persons.csv")
