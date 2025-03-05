import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../../data')

def load_and_preprocess(nykaa_data_file, inventory_data_file, competitor_data_file):
    """Load raw data and preprocess for model training."""
    
    # Load data
    nykaa_data = pd.read_csv(os.path.join(DATA_DIR, nykaa_data_file))
    inventory_data = pd.read_csv(os.path.join(DATA_DIR, inventory_data_file))
    competitor_data = pd.read_csv(os.path.join(DATA_DIR, competitor_data_file))

    # Clean Nykaa data (remove missing values)
    nykaa_data.dropna(inplace=True)  # Remove rows with NaN values

    # Create features for day of the week and month from the 'date' column
    nykaa_data['day_of_week'] = pd.to_datetime(nykaa_data['date']).dt.dayofweek  # Day of the week feature
    nykaa_data['month'] = pd.to_datetime(nykaa_data['date']).dt.month  # Month feature

    # Clean inventory data (remove rows where 'initial_stock' is negative)
    inventory_data = inventory_data[inventory_data['initial_stock'] >= 0]

    # Clean competitor data (remove missing values)
    competitor_data.dropna(inplace=True)  # Remove rows with NaN values

    # Merge Nykaa data with inventory data using 'product_id'
    merged_data = pd.merge(nykaa_data, inventory_data[['product_id', 'initial_stock', 'daily_restock', 'warehouse_id']], on="product_id", how="left")

    # Merge with competitor data (assuming 'product_id' is common)
    merged_data = pd.merge(merged_data, competitor_data[['product_id', 'sales_units', 'price', 'discount', 'stock_level', 
                                                        'rating', 'is_sale_period', 'holiday', 'weather', 'ad_spend', 
                                                        'initial_stock', 'daily_restock', 'warehouse_id']], 
                            on="product_id", how="left")

    # Feature engineering: Create price gap feature
    merged_data['price_gap'] = merged_data['price'] - merged_data['competitor_price']

    # Save processed data for further use (model training)
    merged_data.to_csv(os.path.join(DATA_DIR, 'processed_demand_data.csv'), index=False)
    print("✅ Data preprocessing completed and saved!")

if __name__ == "__main__":
    # Example: preprocess the raw data files
    load_and_preprocess("Nykaa_Products_Dataset.csv", "nykaa_inventory.csv", "Competitor_Products_Dataset.csv")
