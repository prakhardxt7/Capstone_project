import pandas as pd
from fuzzywuzzy import fuzz, process

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../../data')

def match_products_with_competitors(nykaa_file, competitor_file):
    """Match Nykaa products with competitor products."""
    
    # Load the Nykaa and competitor datasets
    nykaa_data = pd.read_csv(os.path.join(DATA_DIR, nykaa_file))
    competitor_data = pd.read_csv(os.path.join(DATA_DIR, competitor_file))

    matched_products = []

    # Iterate through each Nykaa product and find the best match in competitor data
    for index, nykaa_product in nykaa_data.iterrows():
        nykaa_product_name = nykaa_product['product_name']
        
        # Use fuzzy matching to find the best match in competitor products
        match = process.extractOne(nykaa_product_name, competitor_data['product_name'], scorer=fuzz.token_sort_ratio)
        
        if match:
            competitor_name = match[0]  # The best matched competitor product name
            similarity_score = match[1]  # Similarity score (0-100)
            matched_products.append((nykaa_product['product_id'], competitor_name, similarity_score))
    
    # Create a dataframe for matched products
    matched_df = pd.DataFrame(matched_products, columns=['nykaa_product_id', 'competitor_product_name', 'similarity_score'])
    
    # Save matched products to a CSV file
    matched_df.to_csv(os.path.join(DATA_DIR, 'product_mapping.csv'), index=False)
    print("✅ Product matching completed and saved!")

if __name__ == "__main__":
    # Example: Match Nykaa products with competitor products
    match_products_with_competitors("Nykaa_Products_Dataset.csv", "Competitor_Products_Dataset.csv")
