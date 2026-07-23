from pathlib import Path

BASE_DIR = Path(__file__).parent

file = open(BASE_DIR / "text.txt", mode="r", encoding="utf-8")
print(file.read())
file.close()
print("*" * 40)

# Best Practice in Python, wie man eine Datei öffnent
with open(BASE_DIR / "text.txt", mode="r", encoding="utf-8") as f:
    print("Datei geöffnent")
    content = f.read()
    print(content.strip())


def handle_line(line: str) -> str:
    return line[:3]


# STreaming über große Dateien (f => Iteratoren, Iteratoren verbrauchen sich)
with open(BASE_DIR / "text.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        line = handle_line(line)
        print("=>", line)  # alternativ line.strip()

    print("*" * 40)

    # setzt FilePointer zurück auf 0
    f.seek(0)

    # Nur wenn der Filepointer nicht am Ende ist, geht das hier (deshalb seek(0))
    for line in f:
        line = handle_line(line)
        print("=>", line)  # alternativ line.strip()
