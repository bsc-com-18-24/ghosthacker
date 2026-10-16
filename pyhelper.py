import subprocess

def get_code(nonce):
    res = subprocess.run(["./jackpot", str(nonce)], capture_output=True, text=True)
    for line in res.stdout.splitlines():
        if "activation code:" in line:
            return line.split(":")[-1].strip()
    return None

print(get_code(271208))
