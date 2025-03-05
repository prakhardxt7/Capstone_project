import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../../data')

class InventoryManager:
    def __init__(self, stock_threshold=20):
        self.data = pd.read_csv(os.path.join(DATA_DIR, "inventory_optimization_data.csv"))
        self.stock_threshold = stock_threshold

    def check_stock(self, product_id):
        """Check if stock level is sufficient for a product."""
        product_data = self.data[self.data["product_id"] == product_id]
        if product_data.empty:
            return "Product not found"

        stock_level = product_data["stock_level"].values[0]
        if stock_level < self.stock_threshold:
            return f"⚠️ Reorder needed! Stock Level: {stock_level}"
        return f"✅ Stock level is sufficient: {stock_level}"

if __name__ == "__main__":
    manager = InventoryManager()
    print(manager.check_stock("P1"))  # Check stock for a sample product
