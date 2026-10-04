import json
import os

folder = "../cities_weather_json"
data = [] # Current weather data of all cities in the folder

# Open each file in the folder and append the data to the list
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    with open(file_path, "r") as file:
        file_data = json.load(file)
        data.append(file_data)

# print City, Date, Local Time and Temperature of the first 5 cities
for item in data[:5]:
    city = item.get("location", {}).get("name", "Unknown")
    date = item.get("location", {}).get("localtime", "Unknown")
    temp_celsius = item.get("current", {}).get("temp_c", "Unknown")
    print(f"City: {city}, Date: {date[:-6]}, Local Time: {date[-5:]}, Temperature: {temp_celsius}°C")
