"""
Beispiel-Modul aus dem Pythonkurs
"""

print("Name des Moduls:", __name__)


def summe(a: int, b: int) -> int:
    """Addiere zwei Zahlen"""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multipliziere zwei Zahlen"""
    return a * b


if __name__ == "__main__":
    print("Test:", summe(2, 4))
