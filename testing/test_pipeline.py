import sys
import os

# This ensures that test_pipeline.py finds the correct file
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pipeline.pipeline import WeatherPipeline

def test_pipeline_initialization():

    # Test if the class stores the folder path correctly:
    pipeline = WeatherPipeline("test_folder")
    assert pipeline.input_folder == "test_folder"

def test_process_data_sorting():
    pipeline = WeatherPipeline("test_folder")

    data = [
        {
        "location":{"name":"Auckland", "country":"New Zealand"}, 
        "current":{"temp_c":9.4, "humidity":81, "condition":{"text":"Patchy rain nearby"}}
        },
        {
        "location":{"name":"Milan", "country":"Italy"}, 
        "current":{"temp_c":25.2, "humidity":27, "condition":{"text":"Sunny"}}
        }
    ]

    df = pipeline.process_data(data)

    assert df.iloc[0]["city"] == "Milan" # Hottest city in data

    assert "temperature_c" in df.columns