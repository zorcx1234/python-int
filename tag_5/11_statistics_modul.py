"""
statistics Modul: Teil der Stdlib
"""

import statistics

# print(dir(statistics))
values = [23, 5, 2, 4, 234, 23, 23, 534]

print("Mittelwert:", statistics.mean(values))

daten = {
    "temperatur": [18, 20, 22, 24, 26],
    "feuchtigkeit": [40, 45, 50, 55, 60, 60],
    "druck": [1010, 1012, 1015, 1018, 1020],
}

for key, value in daten.items():
    print(f"======{key}=======")
    print(f"Mittelwert von {key}", statistics.mean(value))
    print(f"Median von {key}", statistics.median(value))
    print(f"Modus von {key}", statistics.mode(value))
    print(f"Standardabweichung von {key}", statistics.stdev(value))
