"""
Aufgabe

Lese die Datei active_volcanos.csv ein und filtere die Einträge
nach einem Land. Das Land soll z. B. über input() oder argparse
angegeben werden.

Speichere die gefilterten Einträge als JSON-Datei im Ordner
datas. Der Dateiname soll aus dem Ländernamen erzeugt werden.

Beispiele:
datas/volcanos_Italy.json
datas/volcanos_United_Kingdom.json  <<< ACHTE auf Leerzeichen im Country Name

Enthält der Ländername Leerzeichen, sollen diese im Dateinamen
durch Unterstriche (_) ersetzt werden.

Berücksichtige nur Vulkane, für die gilt:

risk != "NULL"

Jeder JSON-Eintrag soll folgende Keys enthalten:

name
risk
lat
long
country
region

Beispiel:

[
  {
    "name": "Farallon de Pajaros",
    "risk": "1",
    "lat": "20.538000000000000",
    "long": "144.895999999999000",
    "country": "United States",
    "region": "Japan, Taiwan, Marianas"
  }
]

Lege den Ordner datas an, falls er noch nicht existiert:
data_dir = Path(__file__).parent / "datas"
data_dir.mkdir(parents=True, exist_ok=True)

`parents=True` entspricht dem Verhalten von `mkdir -p` und erstellt bei
Bedarf auch übergeordnete Verzeichnisse. `exist_ok=True` verhindert einen
Fehler, wenn der Ordner bereits existiert.

"""

import json
from pathlib import Path
