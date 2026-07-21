"""(Schwer)

netzwerkdaten = [
    ["192.168.1.10", "192.168.1.20", 8, "TCP"],
    ["192.168.1.15", "192.168.1.30", 3, "UDP"],
    ["192.168.1.20", "192.168.1.10", 12, "TCP"],
    ["192.168.1.30", "192.168.1.25", 5, "UDP"],
    ["192.168.1.10", "192.168.1.25", 15, "TCP"],
    ["192.168.1.25", "192.168.1.20", 4, "UDP"],
    ["192.168.1.20", "192.168.1.15", 10, "TCP"],
    ["192.168.1.25", "192.168.1.10", 7, "UDP"]
]
```

### Aufgabe: Analyse von Netzwerkdaten

Du arbeitest als Netzwerkadministrator und möchtest den Netzwerkverkehr auswerten.

Jeder Eintrag in der Liste `netzwerkdaten` enthält:

1. Absender-IP
2. Ziel-IP
3. Paketgröße in Kilobyte
4. Protokoll (TCP oder UDP)

Führe folgende Analysen durch:

1. Bestimme die Gesamtanzahl der Datenpakete.
2. Berechne die durchschnittliche Paketgröße.
3. Zähle, wie viele TCP- und UDP-Pakete vorhanden sind.
4. Ermittle die IP-Adresse, die am häufigsten als Absender vorkommt.
5. Erstelle eine Liste `grosse_pakete`, die nur Pakete mit
einer Größe von mindestens 10 KB enthält.
6. Prüfe, ob es Selbstsendungen gibt (Absender = Ziel).

### Erwartete Ausgabe

Gesamtanzahl der Datenpakete: 8
Durchschnittliche Paketgröße: 8.0 KB
Anzahl TCP-Pakete: 4
Anzahl UDP-Pakete: 4
Häufigster Absender: 192.168.1.10
Große Pakete: [...]
Selbstsendungen vorhanden: 1
"""
