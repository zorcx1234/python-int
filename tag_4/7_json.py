"""
HTTP Request an eine REST API stellen.

pip install requests
"""

import json
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent
url = "https://jsonplaceholder.typicode.com/todos"


def get_todos(url: str) -> list[dict]:
    """Get Todos from Todos Api."""
    response = requests.get(url)
    return response.json()


todos = get_todos(url=url)


user_id = int(input("Bitte User-ID eingeben:"))
user_todos: list[dict] = []

for todo in todos:
    if todo["userId"] == user_id:
        user_todos.append(todo)

with open(BASE_DIR / f"user_{user_id}_todos.json", mode="w") as f:
    json.dump(user_todos, f, indent=2)
