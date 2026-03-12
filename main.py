import requests
import json
from dotenv import load_dotenv
import os

lat = 40.1792
lon = 44.4991

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)   # debug

if "wind" in data:
    wind_speed = data["wind"]["speed"]
    wind_direction = data["wind"]["deg"]

    print("Wind speed:", wind_speed)
    print("Wind direction:", wind_direction)
else:
    print("Wind data not available")
