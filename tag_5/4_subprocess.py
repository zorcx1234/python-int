"""
Modul subprocess


"""

from pathlib import Path
import subprocess

result = subprocess.run(
    ["dir"],
    shell=True,
    capture_output=True,  # stdout und stderr
    text=True,  # Bytes nach Text
    check=True,
)
print("Output:\n", result.stdout)

###### PING
result = subprocess.run(
    ["ping", "-n", "2", "google.com"],
    shell=True,
    capture_output=True,  # stdout und stderr
    text=True,  # Bytes nach Text
    check=True,
    encoding="cp850",  # MSDOS Encoding
)
print("Returncode:", result.returncode)  # 0 wenn alles in Ordnung
print(result.stdout)

###### Anderes Python Programm aufrufen
#
target = Path(__file__).parent / "destination.py"

import json

d = {"a": 42, "b": 3}

p = subprocess.Popen(
    ["python", target],
    stdin=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
p.communicate(json.dumps(d))
