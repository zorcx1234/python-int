"""
configparser: Teil der Python der Standardbilbiothek
"""

import configparser
from pathlib import Path

BASE_DIR = Path(__file__).parent
filename = "config.ini"

config = configparser.ConfigParser()
config.read(BASE_DIR / filename)

# Auslesen via Dict-ähnlichem zugriff
print(config["database"]["host"])

# Datenbank host ändern
config["database"]["host"] = "otherhost"

# oder neue Sektion schreiben
section = {
    "host": "127.0.0.1",
    "port": 8080,
}
config["server"] = section

# Dauerhaft speichern
with open(BASE_DIR / filename, mode="w") as f:
    config.write(f)

# Datentyp ist string (Hilfsfunktionen getint und getboolean konvertieren
# gleich in den entsprechenden Datentyp)
print(type(config["server"]["port"]))  # str
print(type(config.getint("server", "port")))  # int
print(type(config.getboolean("application", "debug")))  # bool

print(config["database"]["host"])

# Über die Sectionen iterieren
for section in config.sections():
    print("-" * 40)
    # über Optionen jeder Section als Key-Value-Päärchen iterieren
    for key, value in config[section].items():
        print(f"{key} => {value}")
