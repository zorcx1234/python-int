dateiname = "systemlog"

if len(dateiname) < 3:
    print(dateiname)
elif dateiname.endswith("log"):
    print(dateiname + "1")
else:
    print(dateiname + "log")



# Aufgabe 4

# schluessel = input("Bitte geben Sie einen Lizenzschlüssel ein: ")
schluessel = "AbCDefgh"

anzahl = 0

for zeichen in schluessel[:4]:
    if zeichen.isupper():
        anzahl += 1

if anzahl >= 2:
    schluessel = schluessel.upper()

print(schluessel)

