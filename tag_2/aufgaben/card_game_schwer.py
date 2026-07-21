"""
(SCHWER)

Schreibe ein vereinfachtes Kartenspiel.

Spielregeln:
- Zu Beginn werden zwei Karten gezogen.
- Der Spieler kann anschließend beliebig viele weitere Karten ziehen,
  dazu muss er "J" eingeben.
- Sobald der Spieler "N" eingibt, endet das Spiel.
- Überschreitet die Punktzahl der gezogenen kartenwerte 21, ist das Spiel
  sofort verloren.
- Liegt die Punktzahl am Ende zwischen 17 und 21 (einschließlich),
  hat der Spieler gewonnen.

Aufgaben:
1. Erstelle ein Kartendeck aus vier Kartensätzen
2. Mische das Deck mit random.shuffle().
3. Ziehe Karten vom Stapel mit pop(). Ziehe solange im while() bis der
Spieler "N" eingibt oder die Punktzahl 21 überschreitet.
4. Berechne die Gesamtpunktzahl des Spielers.
5. Gib am Ende aus, ob der Spieler gewonnen oder verloren hat.

Kartenwerte:
2-10 -> Zahlenwert
Bube, Dame, König -> 10
Ass -> 11 (hier zählt Ass immer 11, nicht wie in Black Jack 1 oder 11)

Tipp:
Es zählen nur die Kartenwerte.
"""

import random

MAX_POINTS = 21
MIN_WIN_POINTS = 17
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# Kartendeck erstellen und mischen
deck = VALUES * 4
random.shuffle(deck)

# Let's play the game ...
# Ziehe zwei Startkarten...
