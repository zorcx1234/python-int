"""
yaml

Muss installiert werden:

pip install pyyaml

Zum Lesen eine Yaml-Datei immer(!) safe_load benutzen, da in yaml-Dateien
Extra TAgs enthalten sein können, die Schadcode/Schadcommandos beinhalten.

Idealwerweise nutzt man auch safe_dump() zum Schreiben von yaml dateien.
"""

from pprint import pprint
from pathlib import Path


import yaml


def read_config(filename: str) -> dict:
    """Lese config.yaml aus dem selben Verzeichnis."""
    with open(Path(__file__).parent / filename, mode="r") as f:
        return yaml.safe_load(f)


def write_config(filename: str, data: dict) -> None:
    """SChreibe config.yaml."""
    with open(Path(__file__).parent / filename, mode="w") as f:
        yaml.safe_dump(data, f)


config_data: dict = read_config("config.yaml")
pprint(config_data, width=50)

config_data["users"] = ["Bob", "Alice", "Grumpy"]
write_config(filename="config_neu.yaml", data=config_data)

# Zusatzaufgabe
# Gebe den Datenbank-Host aus
print("Database Host:", config_data["database"]["host"])
