"""
Aufgabe: Routertabelle erstellen

Ein Netzwerkadministrator hat folgende Informationen
über Server und deren Dienste erhalten:

IP-Adresse       Port    Dienst
--------------------------------
192.168.1.10      80     HTTP
192.168.1.10      22     SSH
192.168.1.20      21     FTP
192.168.1.30     443     HTTPS

Erstelle daraus ein Dictionary namens 'routertabelle'.

Verwende als Key ein Tupel:

    (IP-Adresse, Port)

und als Value den Dienst.

Beispiel:

("192.168.1.10", 80) -> "HTTP"

Anschließend:

1. Gib die komplette Routertabelle aus.

2. Gib den Dienst auf
   192.168.1.10 Port 22 aus.

3. Gib den Dienst auf
   192.168.1.30 Port 443 aus.

4. Füge folgenden Eintrag hinzu:

   192.168.1.50 Port 53 -> DNS

5. Ändere den Dienst auf

   192.168.1.20 Port 21

   von FTP zu SFTP.

6. Gib die Anzahl der Einträge aus.

7. Prüfe, ob ein Eintrag für

   192.168.1.10 Port 443

   existiert.

Erwartete erste Lösung:

routertabelle = {
    ("192.168.1.10", 80): "HTTP",
    ("192.168.1.10", 22): "SSH",
    ("192.168.1.20", 21): "FTP",
    ("192.168.1.30", 443): "HTTPS"
}
"""
