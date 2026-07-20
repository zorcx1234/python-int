"""
Aufgabe 3 (mittel):
Ein Dateiname soll automatisch erweitert werden.

Ist der Dateiname kürzer als 3 Zeichen,
bleibt er unverändert.

Endet der Dateiname bereits auf "log",
füge "1" an.

Andernfalls füge "log" an.

Verwende:
- len()
- endswith()

Beispiel:
----------
Eingabe: ab
Ausgabe: ab

Eingabe: backup
Ausgabe: backuplog

Eingabe: systemlog
Ausgabe: systemlog1
"""
eingabe = "backup"





"""
Aufgabe 4 (schwer):
Ein Lizenzschlüssel soll geprüft werden.

Enthalten die ersten vier Zeichen mindestens zwei Großbuchstaben,
wird der komplette Schlüssel in Großbuchstaben ausgegeben.

Andernfalls bleibt er unverändert.

Verwende:
- Slicing
- isupper() => true, wenn der Buchstabe groß ist
- eine Zählvariable
- if

Beispiel:
----------
Eingabe: PyThon123
Ausgabe: PYTHON123

Eingabe: Python123
Ausgabe: Python123

Eingabe: ABcd-4711
Ausgabe: ABCD-4711
"""
schluessel = "ABcd-4711"
