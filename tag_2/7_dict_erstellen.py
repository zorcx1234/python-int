"""
Alternative Wege, ein Dict zu estellen
"""

import os
from pprint import pprint

server_liste = [
    ("SRV-DB01", "Linux"),
    ("SRV-WEB01", "Windows"),
    ("SRV-FS01", "Linux"),
    ("SRV-APP01", "Linux"),
    ("SRV-PRINT01", "Windows"),
]

# 1. neues Dict via Iteration aus einer Liste erstellen
d = {}
for name, os_ in server_liste:
    print(f"{name}, {os_}")
    d[name] = os_

# Zugriff auf dict via Key (konstanter Laufzeit)
print(d["SRV-FS01"])
pprint(server_liste, width=40)

print()
# 2. neues Dict via dict
d2 = dict(server_liste)
pprint(d2, width=40, sort_dicts=False)
