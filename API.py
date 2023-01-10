import requests
import json

response = requests.get("https://api.tomitokko.repl.co/")

res = json.loads(response.text)

for data in res:
    print(data)

print(response.status_code)
print(response.text)
