import pytest
from src.agents.demand_predictor import DemandPredictor
from src.agents.inventory_manager import InventoryManager
from src.agents.inventory_eoq import InventoryManagerEOQ

# Test Demand Prediction
def test_demand_prediction():
    predictor = DemandPredictor()
    predicted_demand = predictor.predict_demand("P1")  # Sample product ID
    assert isinstance(predicted_demand, (int, float)), "Demand prediction should return a number"

# Test Inventory Manager (Stock Level Check)
def test_inventory_manager():
    manager = InventoryManager()
    stock_status = manager.check_stock("P1")  # Sample product ID
    assert "Stock level" in stock_status, "Stock check failed or invalid response"

# Test Economic Order Quantity (EOQ) calculation
def test_inventory_eoq():
    eoq_calculator = InventoryManagerEOQ()
    eoq = eoq_calculator.calculate_eoq("P1")  # Sample product ID
    assert isinstance(eoq, (int, float)), "EOQ calculation should return a number"
