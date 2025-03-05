import os
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../../data')

class InventoryManagerEOQ:
    def __init__(self, ordering_cost=50, holding_cost=5):
        self.data = pd.read_csv(os.path.join(DATA_DIR, "inventory_optimization_data.csv"))
        self.ordering_cost = ordering_cost
        self.holding_cost = holding_cost

    def calculate_eoq(self, product_id):
        """Calculate Economic Order Quantity (EOQ) for a product."""
        product_data = self.data[self.data["product_id"] == product_id]
        if product_data.empty:
            return "Product not found"

        demand = product_data["sales_units"].mean() * 365  # Approximate annual demand
        eoq = np.sqrt((2 * demand * self.ordering_cost) / self.holding_cost)

        return f"📦 EOQ for {product_id}: {int(eoq)} units"

if __name__ == "__main__":
    manager = InventoryManagerEOQ()
    print(manager.calculate_eoq("P1"))  # Calculate EOQ for a sample product
