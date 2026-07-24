"""
Aufgabe: Webserver-Loganalyse mit Pandas

Gegeben ist eine CSV-Datei "pseudo.log" mit folgenden Spalten:

ip,timestamp,url,status,bytes

Die Datei enthält Zugriffe von verschiedenen IP-Adressen auf einen Webserver.

Lese die Logdatei mit Pandas ein und ermittle den gesamten Datenverbrauch
(Bytes) pro IP-Adresse.

Anforderungen:
- Gruppiere die Daten nach der Spalte "ip". statt .count => .sum()
- Summiere die Werte der Spalte "bytes" je IP-Adresse.
- Gib das Ergebnis aus.

Erwartetes Ergebnis:
Eine Series mit der IP-Adresse als Index und der Summe der übertragenen
Bytes als Wert.

Beispiel:
192.168.1.10    24000
192.168.1.20    30600
192.168.1.30    14900
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "pseudo.log")
print(df.head(5))
anzahl_bytes = df.groupby("ip")["bytes"].sum()
print(anzahl_bytes.sort_values(ascending=False))

anzahl_bytes.plot(kind="barh")
plt.title("Datenvolumen pro IP")
plt.xlabel("Anzahl Bytes")
plt.ylabel("IP Addressen")
plt.tight_layout()  # passt den Plot besser in den Rahmen
plt.show()
