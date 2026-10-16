import urllib.request
import re

url = "http://10.49.187.73/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        html = resp.read().decode('utf-8')
        # Find all script src or link href attributes
        scripts = re.findall(r'src=["\'](.*?)["\']', html)
        css = re.findall(r'href=["\'](.*?)["\']', html)
        print("[*] Scripts found:", scripts)
        print("[*] Styles/Links found:", css)
        
        # Download and print content of local scripts if any
        for s in scripts:
            if not s.startswith("http"):
                script_url = "http://10.49.187.73" + (s if s.startswith("/") else "/" + s)
                print(f"\n--- Content of {script_url} ---")
                with urllib.request.urlopen(script_url) as s_resp:
                    print(s_resp.read().decode('utf-8')[:2000])
except Exception as e:
    print(f"Error: {e}")
