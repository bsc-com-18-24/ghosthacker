import socket

target = "10.48.178.100"
ports = [80, 8080, 9000, 9100, 9999, 5000, 3000, 21, 22]

print(f"[*] Scanning {target}...")
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()
