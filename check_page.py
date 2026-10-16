import urllib.request

url = "http://10.48.178.100:8080/"
try:
    with urllib.request.urlopen(url, timeout=3) as resp:
        print(f"Status: {resp.status}")
        print(resp.read().decode())
except Exception as e:
    print(f"Error: {e}")
