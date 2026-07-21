# übungsaufabe: filtere alle Zahlen aus der Liste, die 
# durch 2 teilbar
# und größer als 2 sind. Als List-Comprehension

liste = [1, 2, 3, 4, 9, 11, 24, 10, 7]
new_liste = [i for i in liste if i % 2 == 0 and i > 2]
print(new_liste)