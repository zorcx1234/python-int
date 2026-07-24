import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
FILE_IN = BASE_DIR / "active_volcanos.csv"


def read_volcanos(country: str) -> list:
    """
    Liest die CSV-Datei ein und filtert
    Vulkane nach dem angegebenen Land.

    Gibt eine Liste mit Dictionaries zurück.
    """

    volcanos = []

    with open(FILE_IN, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Country"].lower() == country and row["risk"] != "NULL":
                volcanos.append(
                    {
                        "name": row["V_Name"],
                        "risk": row["risk"],
                        "lat": row["Latitude"],
                        "long": row["Longitude"],
                        "country": row["Country"],
                        "region": row["Region"],
                    }
                )

    return volcanos


def write_json(country: str, data: list) -> None:
    """
    Schreibt die Vulkandaten als JSON-Datei.

    Der Dateiname wird aus dem Land erzeugt.
    Beispiel:
    United Kingdom -> volcanos_united_kingdom.json
    """

    filename = f"volcanos_{country.lower().replace(' ', '_')}.json"
    file_out = BASE_DIR / filename

    with open(file_out, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
        )


country = input("Land eingeben: ").lower()

volcanos = read_volcanos(country)
write_json(country, volcanos)

print(volcanos)
