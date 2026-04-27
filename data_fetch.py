import urllib.request
import json

url = "https://api.github.com/zen"
try:
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        print("GitHub Zen:", data)
except Exception as e:
    print(f"Error: {e}")
