import json, os, argparse, logging
import pandas as pd

""" Create processed_weather.csv and weather_summary.json through the terminal:
python3 pipeline.py --input ../Cities/cities_json/ """

# using logging to track what the script is doing
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

if __name__ == "__main__":

    # using argparse to enable using the folder dynamically
    parser = argparse.ArgumentParser(description="Process weather JSON files.")
    parser.add_argument("--input", type=str, required=True, help="Path to the JSON folder")
    args = parser.parse_args()
    folder = args.input

    logging.info(f"Starting pipeline for folder: {folder}")

    data = [] # Current weather data of all cities in the folder

    # Open each file in the folder and append the data to the list
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        with open(file_path, "r") as file:
            file_data = json.load(file)
            data.append(file_data)

    # flattens JSON data into a tabular pandas DataFrame
    df = pd.json_normalize(data) 

    columns = [
        "location.name",
        "location.country",
        "current.temp_c",
        "current.humidity",
        "current.condition.text",
    ]

    df_filtered = df[columns] # filter JSON data with categories from columns
    df_clean = df_filtered.rename(columns={ # rename column names from columns
        "location.name": "city",
        "location.country": "country",
        "current.temp_c": "temperature_c",
        "current.humidity": "humidity_percent",
        "current.condition.text": "condition"
    })

    df_sorted = df_clean.sort_values(by="temperature_c", ascending=False) # sort values by temperature_c
    df_sorted.to_csv("processed_weather.csv", index=False) # create a CSV file with the sorted data

    # using index location from pandas (iloc)
    stats = { 
        "hottest_city": df_sorted.iloc[0]["city"],
        "coldest_cidy": df_sorted.iloc[-1]["city"],
        "average_temp_c": round(df_sorted["temperature_c"].mean(), 2)
    }

    # create a JSON summary file with the criteria from stats
    with open("weather_summary.json", "w") as f:
        json.dump(stats, f, indent=4)


