from fastapi import FastAPI
from src.agents.demand_predictor import DemandPredictor
from src.agents.market_watcher import MarketWatcher
from src.agents.inventory_manager import InventoryManager
from src.agents.inventory_eoq import InventoryManagerEOQ
from src.agents.inventory_rl import InventoryEnv
from src.api.scrape_competitor import CompetitorScraper  # Import CompetitorScraper

app = FastAPI()

# Initialize agents
demand_predictor = DemandPredictor()
market_watcher = MarketWatcher()
inventory_manager = InventoryManager()
inventory_eoq = InventoryManagerEOQ()
inventory_rl = InventoryEnv(demand=50)
competitor_scraper = CompetitorScraper()  # Initialize CompetitorScraper

@app.get("/predict_demand")
def predict_demand(product_id: str):
    """Predict demand for a product."""
    predicted_demand = demand_predictor.predict_demand(product_id)
    return {"product_id": product_id, "predicted_demand": predicted_demand}

@app.get("/get_competitor_price")
def get_competitor_price(product_name: str):
    """Get competitor price for a product."""
    competitor_price = competitor_scraper.fetch_competitor_price(product_name)
    return {"product_name": product_name, "competitor_price": competitor_price}

@app.get("/check_inventory")
def check_inventory(product_id: str):
    """Check stock level for a product."""
    stock_status = inventory_manager.check_stock(product_id)
    return {"product_id": product_id, "stock_status": stock_status}

@app.get("/calculate_eoq")
def calculate_eoq(product_id: str):
    """Calculate Economic Order Quantity (EOQ) for a product."""
    eoq = inventory_eoq.calculate_eoq(product_id)
    return {"product_id": product_id, "EOQ": eoq}

@app.get("/reinforcement_learning")
def reinforcement_learning(action: int):
    """Get RL model decision for a given action (reorder quantity)"""
    state, reward, done, info = inventory_rl.step(action)
    return {"stock": state[0], "reward": reward}
