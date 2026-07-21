""" 
Datentyp tuple: unveränderlich, sequentiell
tritt häufig als Nebenprodukt auf (zb. als Rückgabewert von Funktionen)

Datenbank-Analog:
Liste ist eine Spalte, Tuple ein Datensatz
"""
x = [1, 2, 3] # Liste, sollte immer homogen sein (alle Elemente selber Datentyp)
t = ("Bob", 42, "Sys-Admin") # Tuple, oft heterogen (gemischte Datentypen)

# TypeError: 'tuple' object does not support item assignment
# t[0] = "Alice"

d = 1,  # Tupel mit einem Element
d = (1,)  # Tupel mit einem Element
x = (2) # Integer in der runden Klammer

# konvertieren einer Liste in einen Tuple
x = [1, 2, 3]
tuple_x = tuple(x)
print("Datentyp von tuple_x", type(tuple_x))

# Wann macht tuple Sinn? Wenn man unveränderliche STrukturen benötigt
# Punkte im Koordinantensystem
a = (1, 2)
b = (3, 4)

# 23 Sensor1, Sensor2, Sensor3
config = (34, 25, 12)
print(config[1])