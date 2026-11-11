import requests

r = requests.get("https://api.chucknorris.io/jokes/random")

data = r.json()

print(data.get("value", {}))
