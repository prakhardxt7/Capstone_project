import pytest
import pandas as pd
from src.data_processing.preprocess import load_and_preprocess

# Test to check if the data is preprocessed correctly
def test_preprocess_data():
    # Run the preprocessing function
    load_and_preprocess("Nykaa_Products_Dataset.csv", "nykaa_inventory.csv", "Competitor_Products_Dataset.csv")
    
    # Load the processed data
    processed_data = pd.read_csv("../../data/processed_demand_data.csv")
    
    # Check if the data is not empty after preprocessing
    assert not processed_data.empty, "Processed data should not be empty"
    
    # Test if the new features like 'day_of_week' and 'month' exist
    assert 'day_of_week' in processed_data.columns, "'day_of_week' feature not found"
    assert 'month' in processed_data.columns, "'month' feature not found"

    # Test if missing values are handled (no NaN values in processed data)
    assert processed_data.isnull().sum().sum() == 0, "There are missing values in the processed data"
