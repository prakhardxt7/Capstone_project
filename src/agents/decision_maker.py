from src.agents.demand_predictor import DemandPredictor
from src.agents.market_watcher import MarketWatcher
from src.agents.inventory_manager import InventoryManager

class DecisionMaker:
    def __init__(self):
        self.demand_predictor = DemandPredictor()
        self.market_watcher = MarketWatcher()
        self.inventory_manager = InventoryManager()

    def make_decision(self, product_id):
        """Combines insights from all agents to make a decision."""
        predicted_demand = self.demand_predictor.predict_demand(product_id)
        competitor_price = self.market_watcher.get_competitor_price(product_id)
        stock_status = self.inventory_manager.check_stock(product_id)

        return {
            "predicted_demand": predicted_demand,
            "competitor_price": competitor_price,
            "stock_status": stock_status
        }

if __name__ == "__main__":
    decision_maker = DecisionMaker()
    print(decision_maker.make_decision("P1"))  # Make decision for a sample product
