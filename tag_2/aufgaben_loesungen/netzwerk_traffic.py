netzwerkdaten = [
    ["192.168.1.10", "192.168.1.20", 8, "TCP"],
    ["192.168.1.15", "192.168.1.30", 3, "UDP"],
    ["192.168.1.20", "192.168.1.10", 12, "TCP"],
    ["192.168.1.30", "192.168.1.25", 5, "UDP"],
    ["192.168.1.10", "192.168.1.25", 15, "TCP"],
    ["192.168.1.25", "192.168.1.20", 4, "UDP"],
    ["192.168.1.20", "192.168.1.15", 10, "TCP"],
    ["192.168.1.25", "192.168.1.10", 7, "UDP"],
    ["192.168.1.25", "192.168.1.25", 7, "UDP"],
]

# 1. Gesamtanzahl
anzahl_pakete = len(netzwerkdaten)

# 2. Durchschnittliche Paketgröße
summe = 0

for paket in netzwerkdaten:
    summe += paket[2]

durchschnitt = summe / anzahl_pakete

# 3. TCP und UDP zählen
tcp = 0
udp = 0

for paket in netzwerkdaten:
    if paket[3] == "TCP":
        tcp += 1
    else:
        udp += 1

# 4. Häufigsten Absender bestimmen
absender_zaehler = {}

for paket in netzwerkdaten:
    absender = paket[0]

    if absender in absender_zaehler:
        absender_zaehler[absender] += 1
    else:
        absender_zaehler[absender] = 1

haeufigster_absender_alternativ = max(
    absender_zaehler, key=lambda ip: absender_zaehler[ip]
)

haeufigster_absender = ""
max_anzahl = 0

for ip, anzahl in absender_zaehler.items():
    if anzahl > max_anzahl:
        max_anzahl = anzahl
        haeufigster_absender = ip

# 5. Große Pakete (mindestens 10 KB)
grosse_pakete = []

for paket in netzwerkdaten:
    if paket[2] >= 10:
        grosse_pakete.append(paket)

# 6. Selbstsendungen prüfen
selbstsendungen = 0

for paket in netzwerkdaten:
    if paket[0] == paket[1]:
        selbstsendungen += 1

# Ausgabe
print("Gesamtanzahl der Datenpakete:", anzahl_pakete)
print("Durchschnittliche Paketgröße:", round(durchschnitt, 2), "KB")
print("Anzahl TCP-Pakete:", tcp)
print("Anzahl UDP-Pakete:", udp)
print("Häufigster Absender:", haeufigster_absender)
print("Häufigster Absender alt:", haeufigster_absender_alternativ)
print("Große Pakete:", grosse_pakete)
print("Selbstsendungen vorhanden:", selbstsendungen)
