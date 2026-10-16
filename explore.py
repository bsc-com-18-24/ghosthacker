import urllib.request
import json

base_url = "http://10.48.178.100:8080"
paths = ["/status", "/activate", "/arm", "/dispense", "/api/activate", "/api/status", "/api/dispense", "/api/arm"]

for path in paths:
    url = base_url + path
    for method in ["GET", "POST"]:
        try:
            req = urllib.request.Request(url, method=method)
            with urllib.request.urlopen(req, timeout=2) as resp:
                print(f"[+] {method} {path} -> Status {resp.status}: {resp.read().decode()[:100]}")
        except urllib.error.HTTPError as e:
            print(f"[-] {method} {path} -> HTTPError {e.code}")
        except Exception:
            pass
