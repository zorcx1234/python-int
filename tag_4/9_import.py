"""
Module importieren
"""

import json
import sys

# import functions
from functions import summe, multiply


def main():
    print("executable:", sys.executable)
    print("Suchpfad Import:", sys.path)

    # print(functions.summe(3, 4))
    # print(functions.multiply(3, 4))
    summe(3, 4)
    multiply(3, 4)

    # Aktuelle geladene Module
    # for value in sys.modules:
    #     print(value)

    # via sys.modules auf jedes geladene
    # Modul zugreifen.
    # print(sys.modules["functions"].summe(3, 4))


if __name__ == "__main__":
    main()
