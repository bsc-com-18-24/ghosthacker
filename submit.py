import urllib.request
import urllib.parse
import json

base_url = "http://10.48.178.100:8080"
endpoints = ["/", "/activate", "/api/activate", "/submit", "/admin"]
code = "14946076"

print(f"[*] Submitting activation code: {code}\n")

for ep in endpoints:
    url = base_url + ep
    # 1. Try JSON POST
    try:
        data = json.dumps({"code": code}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"[+] POST JSON {url} -> Status {resp.status}")
            print(resp.read().decode())
            break
    except Exception:
        pass

    # 2. Try Form-encoded POST
    try:
        data = urllib.parse.urlencode({"code": code}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"}, method="POST")
        with urllib.request.urlopen(req, timeout=3) as resp:
            print(f"[+] POST Form {url} -> Status {resp.status}")
            print(resp.read().decode())
            break
    except Exception:
        pass
