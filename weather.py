# =============================================================
# Exercise: Current weather for Warsaw
# =============================================================
# Write a script that displays the current weather for Warsaw
# using the OpenWeatherMap service.
#
# API: https://openweathermap.org/current
# Endpoint: https://api.openweathermap.org/data/2.5/weather
# Parameters: q=Warsaw&units=metric
#
# The API key is available in the environment variable:
#   OPENWEATHERMAP_API_KEY
#
# Display:
#   - City name        (name)
#   - Temperature      (main.temp)
#   - Weather          (weather[0].description)
#   - Humidity         (main.humidity)
# =============================================================

import os
import urllib.request
import json

api_key = os.environ.get("OPENWEATHERMAP_API_KEY", "")
city = "Swidnik"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

print(f"City:        {data['name']}")
print(f"Temperature: {data['main']['temp']} °C")
print(f"Weather:     {data['weather'][0]['description']}")
print(f"Humidity:    {data['main']['humidity']} %")
