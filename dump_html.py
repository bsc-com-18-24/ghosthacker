import urllib.request
import re

url = "http://10.49.187.73/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8')
        print(f"[*] Total HTML length: {len(html)} bytes\n")
        
        # Find all inline script tags
        scripts = re.findall(r'<script.*?>(.*?)</script>', html, re.DOTALL)
        print(f"[*] Found {len(scripts)} inline script(s).")
        
        for i, script in enumerate(scripts):
            print(f"\n--- Inline Script #{i+1} ---")
            print(script[:1500]) # Print first 1500 chars of each script
            
        # Also check for any mention of api routes or endpoints
        endpoints = re.findall(r'[''"](/api/.*?)[''"]', html)
        if endpoints:
            print(f"\n[*] Potential API endpoints found: {set(endpoints)}")
            
except Exception as e:
    print(f"Error: {e}")
