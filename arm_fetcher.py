import requests
import csv
import os

API_KEY = os.getenv("API_KEY")

cities = [
    ("Yerevan", 44.4991, 40.1792),
    ("Gyumri", 43.8475, 40.7894),
    ("Vanadzor", 44.4939, 40.8128),
    ("Hrazdan", 44.7667, 40.5000),
    ("Abovyan", 44.6333, 40.2667),
    ("Kapan", 46.4167, 39.2000),
    ("Armavir", 44.0500, 40.1500),
    ("Artashat", 44.5500, 39.9667),
    ("Gavar", 45.1333, 40.3500)
]

url = "https://api.openweathermap.org/data/2.5/weather"

rows = []

for city, lon, lat in cities:
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "wind" in data:
        wind_speed = int(data["wind"]["speed"])
        wind_dir = int(data["wind"]["deg"])
    else:
        wind_speed = -1
        wind_dir = -1

    rows.append([city, lon, lat, wind_speed, wind_dir])

with open("armenia_wind.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["city", "longitude", "latitude", "wind_speed", "wind_direction"])
    writer.writerows(rows)

print("CSV file created: armenia_wind.csv")
