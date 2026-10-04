import os, requests, json, time
from dotenv import load_dotenv

"""
Source: https://www.weatherapi.com/
This code goes through a .csv file with random cities, checks if 
there is data on weatherapi.com for each city, and then downloads
.json files with weather data, which is then used for pipeline.py.
"""

# load API key from hidden .env file
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("Error: API key not found")

# set output folder
output_folder = "cities_weather_json"
os.makedirs(output_folder, exist_ok=True)

# append cities from cities.csv
cities = []
with open("cities.csv", "r", encoding="utf-8") as file:
    for city in file:
        cities.append(f"{city.strip().capitalize()}")

print(f"Found {len(cities)} cities. Starting download...")

# download a .json file for each city in cities
for city in cities:
    query_city = city.replace("_", " ")
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={query_city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        file_path = os.path.join(output_folder, f"{city}.json") # name and location of the city
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Successfully saved {city}.json")

    except requests.exceptions.RequestException as e:
        print(f"Failed to get data for {city}: {e}")

    time.sleep(0.5)

print("Download complete!")
