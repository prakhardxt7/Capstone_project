from src.api.scrape_competitor import CompetitorScraper

class MarketWatcher:
    def __init__(self):
        self.scraper = CompetitorScraper()

    def get_competitor_price(self, product_name):
        """Get competitor price for a product."""
        competitor_price = self.scraper.fetch_competitor_price(product_name)
        return competitor_price
