"""
Ausnahmebehandlung bei dem Requests Package

pip install requests
"""

import requests

url = "https://api.github.com/u"

try:
    response = requests.get(url, timeout=20)
    response.raise_for_status()  # statt Status 404 wird ein Http-Fehler ausgelöst
    print(response)
    x = 3
except requests.HTTPError as e:
    print(f"Es ist ein Http Error aufgeterten {e}")
except requests.RequestException as e:
    print(f"es ist ein Fehler aufgetreten im Request: {e}")
finally:
    print("wird immer ausgeführt: Datenbank / Datei schließen, loggen")
