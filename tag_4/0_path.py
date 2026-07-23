"""
Arbeiten mit Pfaden
"""

from pathlib import Path

# 1. Vom absoluten Pfad der Datei ausgehend ein Pfad-Objekt erstellen
BASE_DIR = Path(__file__).parent
BASE_DIR = Path(__file__).resolve().parent  # Symlinks auflösen bzw. normalisieren

print("Aktuelles Arbeitsverzeichnis:", Path.cwd())
print("absoluter Pfad zur Python Datei:", __file__)

path = Path(__file__)
print("Pfadobjekt:", path.parent / "data")  # tag_4/data

# 2. eigenen Pfad angeben (raw string)
DATA_DIR = Path(r"c:\python_kurs\tag_4")
print("DATA DIR:", DATA_DIR)

# Prüfen, ob Datei existiert
if (DATA_DIR / "text.txt").exists():
    print("ja, text.txt existiert")

if DATA_DIR.exists():
    print("DATA DIR exists")

# Recursives Globbing (alle Python Dateien im Pythonkurs auflisten)
print("Alle Python DAteien im Kurs:")
for file in DATA_DIR.parent.rglob("*.py"):
    print(">", file)

# Immer Encoding uft-8 angeben! Unter Windows ist default CP1252
path = DATA_DIR / "text.txt"
inhalt = path.read_text(encoding="utf-8")
print(inhalt)
