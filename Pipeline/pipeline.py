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
df_clean = df_filtered.rename(columns={
    "location.name": "city",
    "location.country": "country",
    "current.temp_c": "temperature_c",
    "current.humidity": "humidity_percent",
    "current.condition.text": "condition"
})

print(df_clean)

