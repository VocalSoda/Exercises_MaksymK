from dotenv import load_dotenv
import os
load_dotenv()
import requests
import urllib.parse


api = os.getenv("API")

city = input("City name: ")


url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid":api,
    "lang":"fi"
}

url = url + "?" + urllib.parse.urlencode(params)

response = requests.get(url)
data = response.json()

degrees_k = data["main"]["temp"]

degrees = degrees_k - 273.15

print(f"{city}, {degrees:.1f} Celsius")