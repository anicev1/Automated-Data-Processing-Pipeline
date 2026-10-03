import json

with open("zurich_current_weather.json", "r") as file:
    data = json.load(file)

print(f"{data["location"].keys()}")

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