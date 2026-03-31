import requests
import json
chuck_joke = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(chuck_joke)
    if response.status_code == 200:
        data = response.json()
        print(data["value"])
except requests.exceptions.ConnectionError:
    print("Connection Error")