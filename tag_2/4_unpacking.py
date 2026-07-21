""" 
Entpacken von Sequenzen
"""
values = (1, "name", 43)

# klassisch
id = values[0]
name = values[1]
age = values[2]

# Python (Entpackt)
id, name, age = values

################################################
# mit *rest kann man alle übrigen Werte einer Sequenz abfangen
datensatz = (1, "Bob", 42, 2, 9878, "sys")
id, name, *rest = datensatz
print(id, name, rest)

# zwei Variablen vorne, hinten job und alle anderen mit Rest abfangen
id, name, *rest, job = datensatz
print(id, name, rest, job)

# Entpacken von Rückgaberten von Funktionen
# divmod gibt Floordiv und Modulo zurück
x, y = divmod(4, 2)