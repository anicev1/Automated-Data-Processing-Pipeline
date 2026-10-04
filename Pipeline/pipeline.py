import json

with open("../cities_weather_json/zurich_current_weather.json", "r") as file:
    data = json.load(file)

city = data.get("location", {}).get("name", "Unknown")
temp = data.get("current", {}).get("temp_c", "Unknown")
time = data.get("location", {}).get("localtime", "Unknown")

print(f"City: {city}, Date: {time[:-6]}, Time: {time[-5:]}, Temperature: {temp}°C")


#dict_keys([
# 'name', 
# 'region', 
# 'country', 
# 'lat', 
# 'lon', 
# 'tz_id', 
# 'localtime_epoch', 
# 'localtime'
# ])