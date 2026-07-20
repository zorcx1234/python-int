"""
Aufgabe 1:
Gib alle Servernamen aus der Liste einzeln aus.
"""

servers = ["srv-web01", "srv-db01", "srv-backup01"]


"""
Aufgabe 3:
Filtere alle Server, deren Name mit "srv-web" beginnt.
"""

servers = ["srv-web01", "srv-db01", "srv-web02", "test01"]


"""
Aufgabe 4:
Filtere alle Ports zwischen 1024 und 10000.
Gib die gefilterte Liste aus.
"""

ports = [22, 80, 443, 3306, 8080, 9999, 12000]


"""
Aufgabe 5:
Gib das letzte Logfile aus, falls die Liste nicht leer ist.
"""

logfiles = ["auth.log", "syslog", "kernel.log"]


"""
Aufgabe 6:
Übernimm nur erlaubte Statuscodes in eine neue Liste.
Erzeuge neue Liste mit erlaubten STatuscodes
"""

status_codes = [200, 404, 500, 200, 301, 403, 500]
allowed_codes = [200, 301]


"""
Aufgabe 7:
Entferne Unterstriche aus Benutzernamen.
Leere Namen sollen nicht übernommen werden.
Erzeuge neue Liste
"""

users = ["max_muster", "admin_user", "_", "backup_"]


"""
Aufgabe 8 (schwer)
Bereinige Hostnamen.
Entferne Leerzeichen, Steuerzeichen und den Buchstaben "x".
Leere Hostnamen sollen nicht übernommen werden. Recherchiere dazu die String-Methode "strip"
"""

hosts = [" xweb01 ", "\ndbx01", "\tproxy ", " x "]