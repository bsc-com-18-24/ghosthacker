import urllib.request
import json

url = "http://10.49.187.73/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        print(f"Status: {resp.status}")
        html = resp.read().decode('utf-8')
        print(html[:1500]) # Print first 1500 chars of HTML
except Exception as e:
    print(f"Error: {e}")
