from googlesearch import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
from sentence_transformers import SentenceTransformer, util
import time

# Load BERT Model for Semantic Ranking
model = SentenceTransformer("all-MiniLM-L6-v2")

def fetch_search_results(query, num_results=10):
    """Fetch product search results from Google."""
    return list(search(query, num_results=num_results))

def extract_price(url):
    """Extract price using Selenium for dynamically loaded pages."""
    try:
        options = Options()
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        time.sleep(3)  # Wait for JavaScript to load
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        # Try to find price using common patterns
        price_patterns = [
            r'\₹\s?(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)',  # Indian Rupee
            r'\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)'   # USD Dollar
        ]
        for pattern in price_patterns:
            matches = re.findall(pattern, soup.text)
            if matches:
                return matches[0]  # Return the first found price
    except Exception:
        return None

def rank_results(query, results):
    """Rank search results based on semantic similarity using BERT."""
    if not results:
        return []

    docs = [desc for _, _, desc in results]

    query_embedding = model.encode(query, convert_to_tensor=True)
    doc_embeddings = model.encode(docs, convert_to_tensor=True)

    # Compute cosine similarity
    similarity_scores = util.pytorch_cos_sim(query_embedding, doc_embeddings).squeeze(0).tolist()

    # Rank results
    ranked_results = sorted(zip(similarity_scores, results), key=lambda x: x[0], reverse=True)

    return ranked_results[:10]  # Return top 10 results

class CompetitorScraper:
    def __init__(self):
        self.driver = None

    def fetch_competitor_price(self, product_name):
        """Fetch competitor price for a given product from Google."""
        query = f"{product_name} price online"
        results = fetch_search_results(query)
        
        filtered_results = []
        for url in results:
            title, description = extract_price(url), url
            if title:
                filtered_results.append((title, url, description))

        most_relevant = rank_results(query, filtered_results)
        
        if most_relevant:
            return most_relevant[0][1]  # Return the first ranked result (URL)
        else:
            return "No relevant price found."
