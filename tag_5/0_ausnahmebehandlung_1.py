"""
Ausnahmebehandlung
"""

import math

# Ausnahme sollten immer spezifiziert werden
# zahl = int(input("bitte zahl eingeben:"))
zahl = 1
try:
    # kritischer Code
    x = 3 / zahl
except ZeroDivisionError as e:
    print(f"Es ist ein Fehler aufgetreten: {type(e)}")
except Exception as e:
    print(f"es ist ein Fehler aufgetretet: {type(e)}")

# löst ValueError aus, weil Fakultät von -1 nicht definiert
# print(math.factorial(-1))
