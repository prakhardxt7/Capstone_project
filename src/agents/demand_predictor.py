import os
import pandas as pd
import joblib
from xgboost import XGBRegressor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../../data')

class DemandPredictor:
    def __init__(self, model_path="../../models/demand_forecast_model.pkl"):
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            self.model = XGBRegressor(objective="reg:squarederror")
        
        self.data = pd.read_csv(os.path.join(DATA_DIR, "processed_demand_data.csv"))

    def train_model(self):
        X = self.data[["nykaa_price", "competitor_price", "price_gap", "stock_level", "day_of_week", "month"]]
        y = self.data["sales_units"]

        # Train-test split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Save the model
        joblib.dump(self.model, "../../models/demand_forecast_model.pkl")
        print("✅ XGBoost Model Trained and Saved!")

    def predict_demand(self, product_id):
        """Predict demand based on the input features."""
        product_data = self.data[self.data["product_id"] == product_id]
        if product_data.empty:
            return "Product not found"

        features = product_data[["nykaa_price", "competitor_price", "price_gap", "stock_level", "day_of_week", "month"]]
        predicted_demand = self.model.predict(features)
        return predicted_demand[0]

if __name__ == "__main__":
    predictor = DemandPredictor()
    # Uncomment the next line to train the model
    # predictor.train_model()
    print(predictor.predict_demand("P1"))  # Predict demand for a Nykaa product
