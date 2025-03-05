import pytest
from fastapi.testclient import TestClient
from src.api.fastapi_app import app

client = TestClient(app)

# Test /predict_demand endpoint
def test_predict_demand():
    response = client.get("/predict_demand?product_id=P1")  # Sample product ID
    assert response.status_code == 200
    assert "predicted_demand" in response.json(), "Response does not contain predicted_demand"

# Test /get_competitor_price endpoint
def test_get_competitor_price():
    response = client.get("/get_competitor_price?product_name=Maybelline%20Fit%20Me%20Foundation")
    assert response.status_code == 200
    assert "competitor_price" in response.json(), "Response does not contain competitor_price"

# Test /check_inventory endpoint
def test_check_inventory():
    response = client.get("/check_inventory?product_id=P1")  # Sample product ID
    assert response.status_code == 200
    assert "stock_status" in response.json(), "Response does not contain stock_status"

# Test /calculate_eoq endpoint
def test_calculate_eoq():
    response = client.get("/calculate_eoq?product_id=P1")  # Sample product ID
    assert response.status_code == 200
    assert "EOQ" in response.json(), "Response does not contain EOQ"

# Test /reinforcement_learning endpoint
def test_reinforcement_learning():
    response = client.get("/reinforcement_learning?action=10")  # Sample action (e.g., reorder quantity)
    assert response.status_code == 200
    assert "reward" in response.json(), "Response does not contain reward"
