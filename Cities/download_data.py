import os, requests, json, time
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("Error: API key not found")

output_folder = "cities_weather_json"
os.makedirs(output_folder, exist_ok=True)

cities = []
with open("cities.csv", "r", encoding="utf-8") as file:
    for city in file:
        cities.append(f"{city.strip().capitalize()}")

print(f"Found {len(cities)} cities. Starting download...")

for city in cities:
    query_city = city.replace("_", " ")
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={query_city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        file_path = os.path.join(output_folder, f"{city}.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Successfully saved {city}.json")

    except requests.exceptions.RequestException as e:
        print(f"Failed to get data for {city}: {e}")

    time.sleep(0.5)

print("Download complete!")
