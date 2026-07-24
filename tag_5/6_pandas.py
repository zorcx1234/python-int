"""
Arbeiten mit Tabellen

pip install pandas, matplotlib

TAbelle in Pandas heisst DataFrame
"""

import pandas as pd

d = {
    "Name": ["Anna", "Bob", "Clara"],
    "Alter": [25, 31, 28],
    "Stadt": ["Berlin", "Hamburg", "München"],
}

# DataFrame erstellen
df = pd.DataFrame(d)

# Die Grundinfos wie Datentypen oder Speicherverbrauch ausgegeben
print(df.info())
print("Spalte Alter:", df.Alter, df["Alter"])

## Describe (statistischen Grundwerte)
print("Describe", df.describe())
