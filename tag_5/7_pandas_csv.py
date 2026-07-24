"""
CSV Datei mit Pandas einlesen und Abfragen
"""

from pathlib import Path

import pandas as pd

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)


df = pd.read_csv(Path(__file__).parent / "worldcities.csv")
print(df.head(5))

print("Datentyp von Spalte lat:", df.lat.dtype)
print(df)

# alle Städte in Deutschland filtern: boolsche Maske (boolsche Serie)
# die größer sind als 3000000 Einwohner
df_germany = df[
    (df["country"] == "Germany") & (df["population"] > 3_000_000) & (df["lat"] > 40)
]
print(df_germany)

df_germany_italy = df[df["country"].isin(["Italy", "Germany"])]
print(df_germany_italy)

# Alle Länder, die vorkommen (nach Numpy Array exportieren)
print(list(df["country"].unique().to_numpy()))


print("*" * 40)

# Welche LÄnder haben wieviele Städte (absteigend sortiert)
# Gruppieren nach Land, und dann die Spalte City zählen
# => Anzahl Städte je Land
anzahl_städte = df.groupby("country")["city"].count()
print(anzahl_städte.sort_values(ascending=False))
