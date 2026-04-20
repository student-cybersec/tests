# =============================================================
# Cwiczenie: Aktualna pogoda dla Warszawy
# =============================================================
# Napisz skrypt ktory wyswietli aktualna pogode dla Warszawy
# korzystajac z serwisu OpenWeatherMap.
#
# API: https://openweathermap.org/current
# Endpoint: https://api.openweathermap.org/data/2.5/weather
# Parametry: q=Warsaw&units=metric&lang=pl
#
# Klucz API jest dostepny w zmiennej srodowiskowej:
#   OPENWEATHERMAP_API_KEY
#
# Wyswietl:
#   - Nazwe miasta
#   - Temperature (main.temp)
#   - Opis pogody (weather[0].description)
#   - Wilgotnosc (main.humidity)
# =============================================================

import os
import urllib.request
import json

api_key = os.environ.get("OPENWEATHERMAP_API_KEY", "")
city = "Warsaw"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pl&appid={api_key}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

print(f"Miasto:      {data['name']}")
print(f"Temperatura: {data['main']['temp']} °C")
print(f"Pogoda:      {data['weather'][0]['description']}")
print(f"Wilgotnosc:  {data['main']['humidity']} %")
