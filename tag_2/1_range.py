""" 
Das Range Objekt

Return an object that produces a sequence of
integers from start (inclusive)
to stop (exclusive) in einer Schrittweite

analog zum Slicing [von:bis]
"""
for i in range(0, 10, 2):
    print(i)

# Aufgabe: Studenten und Noten ausgeben
# mit range
students = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 3]

for i in range(len(students)):
    print(f"{students[i]} hat die Note {grades[i]}")