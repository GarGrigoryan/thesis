import requests
import csv
import os
from dotenv import load_dotenv

# load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

input_file = "armenia_cities.csv"
output_file = "armenia_wind.csv"

url = "https://api.openweathermap.org/data/2.5/weather"

rows = []

with open(input_file, encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        city = row["city"]
        lon = float(row["longitude"])
        lat = float(row["latitude"])

        print(f"Fetching wind data for {city}...")

        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if "wind" in data:
                wind_speed = int(data["wind"]["speed"])
                wind_dir = int(data["wind"]["deg"])
            else:
                wind_speed = -1
                wind_dir = -1

        except Exception as e:
            print("Error:", e)
            wind_speed = -1
            wind_dir = -1

        rows.append([city, lon, lat, wind_speed, wind_dir])

# write CSV with ; separator
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")

    writer.writerow([
        "city",
        "longitude",
        "latitude",
        "wind_speed",
        "wind_direction"
    ])

    writer.writerows(rows)

print("Finished. File saved as armenia_wind.csv")
