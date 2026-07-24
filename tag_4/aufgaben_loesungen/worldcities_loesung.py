import csv
from pathlib import Path


BASE_DIR = Path(__file__).parent
FILE_IN = BASE_DIR / "worldcities.csv"
FILE_OUT = BASE_DIR / "worldcities_sorted.csv"


def normalize_country(country: str) -> str:
    """
    Normalisiert eine Ländereingabe für Vergleiche.
    Entfernt Leerzeichen und ignoriert Groß-/Kleinschreibung.
    """
    return country.strip().casefold()


def load_cities(filename: Path, country: str) -> list[dict]:
    """
    Liest Städte aus einer CSV-Datei ein.

    Filtert die Einträge nach dem angegebenen Land
    und gibt eine Liste von Dictionaries zurück.
    """

    cities = []
    country = normalize_country(country)

    with open(filename, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if normalize_country(row["country"]) == country:
                cities.append(row)

    return cities


def sort_cities_by_ascii_name(cities: list[dict]) -> list[dict]:
    """
    Sortiert Städte alphabetisch nach city_ascii.
    """
    return sorted(
        cities,
        key=lambda city: city["city_ascii"].casefold(),
    )


def save_cities_to_file(filename: Path, cities: list[dict]) -> None:
    """
    Speichert eine Liste von Städten als CSV-Datei.
    """

    if not cities:
        return

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=cities[0].keys(),
        )

        writer.writeheader()
        writer.writerows(cities)


def main() -> None:
    """
    Steuert das Einlesen, Sortieren und Speichern.
    """

    country = input("Land eingeben: ")

    cities = load_cities(FILE_IN, country)
    cities_sorted = sort_cities_by_ascii_name(cities)

    save_cities_to_file(FILE_OUT, cities_sorted)

    print(f"{len(cities_sorted)} Städte gespeichert.")


if __name__ == "__main__":
    main()
