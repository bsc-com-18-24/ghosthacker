import urllib.request
import json

# FNV-1a 64-bit hash implementation
def fnv1a_hash(data: bytes) -> int:
    FNV_OFFSET_BASIS = 0xcbf29ce484222325
    FNV_PRIME = 0x100000001b3
    
    h = FNV_OFFSET_BASIS
    for b in data:
        h ^= b
        h = (h * FNV_PRIME) & 0xFFFFFFFFFFFFFFFF
    return h

def get_activation_code(nonce_str: str) -> str:
    # Hash nonce + "ENBANK"
    combined = nonce_str.encode() + b"ENBANK"
    hash_val = fnv1a_hash(combined)
    
    # Modulo 10^8 for 8-digit output
    code = hash_val % 100000000
    return f"{code:08d}"

# Fetch live nonce from the ATM status endpoint
try:
    req = urllib.request.urlopen("http://10.48.178.100:8080/status")
    status = json.loads(req.read().decode())
    nonce = status.get("nonce")
    print(f"[*] Active Session Nonce: {nonce}")
    
    code = get_activation_code(nonce)
    print(f"[*] Calculated Activation Code: {code}")
except Exception as e:
    print(f"[-] Error fetching status: {e}")
