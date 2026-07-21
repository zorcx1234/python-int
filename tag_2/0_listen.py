"""
Iteration: enumerate
"""

# Namen und Note ausgeben
students = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 3]

c = 0
for student in students:
    print(f"{student} hat die Note {grades[c]}")
    c += 1

print("*" * 40)

# mit enumerate
for index, student in enumerate(students):
    print(f"{student} hat die Note {grades[index]}")

# Enuemerate erzeugt ein liste von Päärchen (Index, Wert)
values = list(enumerate(students))
print(values)