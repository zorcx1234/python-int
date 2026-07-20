# Aufgabe 1

servers = ["srv-web01", "srv-db01", "srv-backup01"]

for server in servers:
    print(server)

# Aufgabe 3
servers = ["srv-web01", "srv-db01", "srv-web02", "test01"]
filtered_servers = []

for server in servers:
    if server.startswith("srv-web"):
        filtered_servers.append(server)

print(filtered_servers)


# Aufgabe 4

ports = [22, 80, 443, 3306, 8080, 9999, 12000]
filtered_ports = []

for port in ports:
    if 1024 < port < 10000:
        filtered_ports.append(port)

print(sorted(filtered_ports))



# Aufgabe 5

logfiles = ["auth.log", "syslog", "kernel.log"]

if logfiles:
    print("Letztes Logfile:", logfiles[-1])


# Aufgabe 6

status_codes = [200, 404, 500, 200, 301, 403, 500]
allowed_codes = [200, 301]
filtered_codes = []

for code in status_codes:
    if code in allowed_codes:
        filtered_codes.append(code)

print(filtered_codes)


# Aufgabe 7

users = ["max_muster", "admin_user", "_", "backup_"]
clean_users = []

for user in users:
    user = user.replace("_", "")
    if user:
        clean_users.append(user)

print(clean_users)


# Aufgabe 8
hosts = [" xweb01 ", "\ndbx01", "\tproxy ", " x "]
clean_hosts = []

for host in hosts:
    host = host.strip().replace("x", "")
    if host:
        clean_hosts.append(host)

print(clean_hosts)