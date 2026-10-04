import sys
import os

# This ensures that test_pipeline.py finds the correct file
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Pipeline.pipeline import WeatherPipeline

def test_pipeline_initialization():

    # Test if the class stores the folder path correctly:
    pipeline = WeatherPipeline("test_folder")
    assert pipeline.input_folder == "test_folder"