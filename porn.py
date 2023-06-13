import requests

print('starting')
with open("porn.list") as f:
    link = f.readlines()
    for l in link:
        try:
            l = f"http://{l.rstrip()}"
            r = requests.get(l)
            with open('porn.out', "w") as outfile:
                outfile.write(f'{l.rstrip()} | Accessible | Status Code: {r.status_code}\n')
        except Exception as e:
            if "NameResolutionError" in str(e):
                continue
            elif "ConnectionResetError" in str(e):
                print(f'{l.rstrip()} was blocked by firewall')
                continue
            else:
                print(f'{l.rstrip()} resulted in unexpected error: {str(e)}')
                continue

print('complete')