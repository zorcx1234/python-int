username = input("Bitte geben Sie den Benutzernamen ein: ")

if username.startswith("adm"):
    print("Administratorkonto erkannt.")
elif username.endswith("$"):
    print("Dienstkonto erkannt.")
else:
    print("Standardbenutzer erkannt.")
