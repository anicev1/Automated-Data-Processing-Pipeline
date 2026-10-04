from Pipeline.pipeline import WeatherPipeline

def test_pipeline_initialization():

    # Test if the class stores the folder path correctly:
    pipeline = WeatherPipeline("test_folder")
    assert pipeline.input_folder == "test_folder"