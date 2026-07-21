"""
Die zip-Funktion (Reißverschluss):

zip nimmt immer die kürzeste Sequenz (als Alternative siehe itertools ziplongest)
"""
students = ["Bob", "Alice", "Grumpy"]
grades = [1, 2, 3]
cities = ["Köln", "Dresden", "Bielefeld"]


for student, grade, city in zip(students, grades, cities):
    print(student, grade, city)