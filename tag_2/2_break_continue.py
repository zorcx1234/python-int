"""
Die Keywords break und continue

break: bricht die Iteration ab
continue: bricht den aktuellen Durchlauf ab
"""
students = ["Bob", "Alice", "Grumpy"]

found = False

# um eine Iteration zu beenden, wenn die Aufgabe erledigt wurde, nutzt man break
for student in students:
    if student.startswith("Al"):
        print("Word mit Ad gefunden")
        print(student)
        found = True
        break

# Wenn der Name nicht gefunden wurde, wurde found nicht auf True gesetzt 
# und damit ist folgende Aussage wahr:
if not found:
    print("Wurde nicht gefuden")



# Pythonische Variante (for-else: else wird ausgeführt, wenn der Loop nicht mit break
# abgebrochen ist)
print("*" * 40)  # 40 mal * 

for student in students:
    if student.startswith("Ad"):
        print("Word mit Ad gefunden")
        break
else:
    # wird ausgeführt, wenn der Loop NICHT mit break abgebrochen ist
    print("Wurde nicht gefuden")

# continue
for i in range(50):

    if i % 2 == 0:
        print("i:", i)
        continue

    print("i**2 => ", i**2) # simuliert zb. einen Renderprozess
        
