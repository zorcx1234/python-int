import random

VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
MAX_POINTS = 21
MIN_WIN_POINTS = 17

# Kartendeck erstellen und mischen
deck = VALUES * 4
random.shuffle(deck)

print("Willkommen beim Kartenspiel!")

# Zwei Startkarten ziehen
points = deck.pop() + deck.pop()

while True:
    print(f"Aktuelle Punkte: {points}")

    if points > MAX_POINTS:
        print("Du hast verloren! Game Over.")
        break

    choice = input("Weitere Karte ziehen? (J/N): ").strip().upper()

    if choice == "J":
        card = deck.pop()
        print(f"Du hast eine {card} gezogen.")
        points += card

    elif choice == "N":
        if points >= MIN_WIN_POINTS:
            print("Du hast gewonnen!")
        else:
            print("Du hast verloren!")
        break

    else:
        print("Ungültige Eingabe. Bitte J oder N eingeben.")
