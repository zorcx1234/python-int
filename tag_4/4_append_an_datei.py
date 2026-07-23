"""
mit modus a kann man an eine Datei text anhängen.
write hat kein newline integriert.

Modi für Textdatei:
r = lesen
w = schreiben
a = append
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent

strings = ["a", "b", "c"]
# write bzw. writelines hat kein Newline am Ende, also muss man ein newline angeben
strings = [f"{s}\n" for s in strings]

with open(BASE_DIR / "data3.txt", mode="a") as f:
    f.write("abcd\n")
    f.writelines(strings)
