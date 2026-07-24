import json
import csv
from pathlib import Path
from pprint import pprint

BASE_DIR = Path(__file__).parent
DATA_DIR = Path(__file__).parent / "datas"


def read_csv(filename: str):
    volcanos = []
    with open(BASE_DIR / filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            volcanos.append(row)
    return volcanos


volcanos = read_csv("active_volcanos.csv")
country = input("Land: ")
country_volcanos = []

for row in volcanos:
    if row["Country"] == country and row["risk"] != "NULL":
        vol = {
            "name": row["V_Name"],
            "risk": row["risk"],
            "lat": row["Latitude"],
            "long": row["Longitude"],
            "country": country,
            "region": row["Region"],
        }
        country_volcanos.append(vol)

pprint(country_volcanos, width=40)
print(f"Insgesamt {len(country_volcanos)} Vulkane in {country} mit bewertetem Risiko")

filename = country.replace(" ", "_") + ".json"
with open(DATA_DIR / filename, mode="w", encoding="utf-8") as f:
    json.dump(country_volcanos, f, indent=2)
