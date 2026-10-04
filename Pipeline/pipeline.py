import json
import os
import pandas as pd

folder = "../cities_weather_json"
data = [] # Current weather data of all cities in the folder

# Open each file in the folder and append the data to the list
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    with open(file_path, "r") as file:
        file_data = json.load(file)
        data.append(file_data)


df = pd.json_normalize(data) # flattens json data into a tabular pandas DataFrame

columns = [
    "location.name",
    "location.country",
    "current.temp_c",
    "current.humidity",
    "current.condition.text",
]

df_filtered = df[columns]
print(df_filtered)

#print(df.head()) # return first 5 rows of DataFrame

# # print City, Date, Local Time and Temperature of the first 5 cities
# for item in data[:5]:
#     city = item["location"]["name"]
#     date = item["location"]["localtime"]
#     temp_celsius = item["current"]["temp_c"]
#     print(f"City: {city}, Date: {date[:-6]}, Local Time: {date[-5:]}, Temperature: {temp_celsius}°C")
