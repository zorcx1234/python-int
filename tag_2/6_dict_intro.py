""" 
Bad programmers worry about code. Good programmers worry about
data structures and their relationships
linus Torvalds

unordered_map c++
hashmap java
hash perl
array PHP

Datentyp Dict 
"""
from pprint import pprint

d = {} # leeres Dict 
print(f"Datentyp von d: {type(d)}") # <class 'dict'>

# Dict Literale 
player = {
    "name": "Bob", 
    "points": 109
}
# Keys auslesen
print(player["name"])

# Prüfen, ob age in dict player vorhanden ist
if "age" in player:
    print(player["age"]) # falls der key nicht vorhanden ist: KeyError

# neuen Key schreiben ()
player["name"] = "Bobby"
player["weapons"] = ["Sword", "Gun"]

pprint(player, width=40)

# Magiepunkte (wenn keine magic-Key vorhanden ist, dann holt get den defaultwert 0)
magic = player.get("magic", 0)
print(magic)