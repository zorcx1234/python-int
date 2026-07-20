"""
Aufgabe:
Ein neuer Benutzer soll auf einem Server angelegt werden.

Gib einen Benutzernamen ein und prüfe ihn anhand der folgenden
Regeln:

1. Beginnt der Benutzername mit "adm", gib aus:
   Administratorkonto erkannt.

2. Endet der Benutzername mit "$", gib aus:
   Dienstkonto erkannt.

3. Andernfalls gib aus:
   Standardbenutzer erkannt.

Verwende dazu:
- startswith()
- endswith()
- if
- elif
- else

Wir gehen von gültigen Eingaben aus.

Beispiel 1:
-----------
Bitte geben Sie den Benutzernamen ein: admmueller

Administratorkonto erkannt.

Beispiel 2:
-----------
Bitte geben Sie den Benutzernamen ein: backup$

Dienstkonto erkannt.

Beispiel 3:
-----------
Bitte geben Sie den Benutzernamen ein: max

Standardbenutzer erkannt.
"""
