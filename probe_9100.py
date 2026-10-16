import socket
import subprocess

# Get current activation code
res = subprocess.run(["python3", "pyhelper.py"], capture_output=True, text=True)
code = res.stdout.strip()
print(f"[*] Using activation code: {code}")

target = "10.48.178.100"
port = 9100

try:
    s = socket.create_connection((target, port), timeout=3)
    print("[+] Connected to port 9100!")
    # Try receiving banner/initial data
    s.settimeout(2)
    try:
        data = s.recv(1024)
        print(f"[<] Received: {data}")
    except Exception:
        print("[-] No immediate banner received.")

    # Try sending the activation code
    s.sendall(code.encode() + b"\n")
    try:
        resp = s.recv(1024)
        print(f"[<] Response to code: {resp}")
    except Exception:
        print("[-] No response after sending code.")
    
    s.close()
except Exception as e:
    print(f"[-] Connection failed: {e}")
