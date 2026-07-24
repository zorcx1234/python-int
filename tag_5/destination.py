"""
wird via POpen aufgerufen
"""

import sys
import json

daten = sys.stdin.read()
daten = json.loads(daten)
print("Datentyp von daten:", type(daten))
print(f"Empfangene Daten: {daten}")
