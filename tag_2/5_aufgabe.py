"""
Aufgabe: Linux-Server sammeln

Gegeben ist folgende Liste:

server_liste = [
    ("SRV-DB01", "Linux"),
    ("SRV-WEB01", "Windows"),
    ("SRV-FS01", "Linux"),
    ("SRV-APP01", "Linux"),
    ("SRV-PRINT01", "Windows")
]

Erstelle eine leere Liste namens linux_server.

Aufgaben:

1. Durchlaufe die Liste mit einer Schleife.
2. Entpacke jedes Tupel in die Variablen servername und betriebssystem.
3. Entferne das Präfix "SRV-" mit String-Slicing.
4. Ist das Betriebssystem "Linux", füge den bereinigten Servernamen mit append() 
der Liste linux_server hinzu.
5. Gib zum Schluss alle Linux-Server aus.

Result:
["DB01", "FS01", "APP01"]
"""
server_liste = [
    ("SRV-DB01", "Linux"),
    ("SRV-WEB01", "Windows"),
    ("SRV-FS01", "Linux"),
    ("SRV-APP01", "Linux"),
    ("SRV-PRINT01", "Windows")
]

linux_server = []

for server in server_liste:
    name, os = server
    if os == "Linux":
        cleaned_name = name[4:]
        linux_server.append(cleaned_name)

print(linux_server)