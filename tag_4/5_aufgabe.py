"""
Lege eine datei namens data.log an

sensor_id,temperature,status
S1,20.0,OK
S3,19.2,FAIL
S4,21.5,OK

Schreibe ein Python programm, dass die Datei data.log einliest,
alle Zeilen mit Status OK filtert und in eine neue Datei data_ok.log schreibt.

Nutze dazu den CSV Dict Reader (oder alternativ den Reader)

Happy Coding!
"""

import csv
from pathlib import Path

# Hinweis1: data.log mit with open öffnen, und über csvDictreader iterieren.
# alle Zeilen mit key["status"] == "Ok" filtern
# (in eine leere Liste appenden)

FILE_PATH = Path(__file__).parent / "data.log"
OUT_PATH = Path(__file__).parent / "data_ok.log"

# Lesen mit modus r
with open(FILE_PATH, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    ok_sensors = []

    for row in reader:
        # prüfen, ob row status OK und an ok_sensors.append(row)
        if row["status"] == "OK":
            ok_sensors.append(row)


# Schreiben mit modus w
if ok_sensors:
    with open(OUT_PATH, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)  # type: ignore
        writer.writeheader()
        writer.writerows(ok_sensors)


# def f():
#     for i in range(10):
#         yield i


# reader = f()
# for i in reader:
#     print(i)
