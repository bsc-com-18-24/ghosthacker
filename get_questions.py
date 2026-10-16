import urllib.request
import json

url = "http://10.49.187.73/api/questions"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Error: {e}")
