import requests
from langchain.chat_models import ChatGoogleGenerativeAI

# FastAPI endpoint URL
FASTAPI_URL = "http://localhost:8000/get_competitor_price"

def chat_with_ai(query, product_name=None):
    """Generates a response using Gemini AI and fetches competitor price if necessary."""
    
    if product_name:
        response = requests.get(FASTAPI_URL, params={"product_name": product_name})
        competitor_data = response.json()
        competitor_price = competitor_data["competitor_price"]
        return f"The competitor price for {product_name} is {competitor_price}."
    else:
        chat_model = ChatGoogleGenerativeAI(model="gemini-pro")
        response = chat_model.predict(query)
    
    return response

def main():
    user_input = input("Ask about product, pricing, inventory or demand forecasting: ")
    if "competitor price" in user_input.lower():
        product_name = input("Enter the product name to fetch competitor price: ")
        print(chat_with_ai(user_input, product_name))
    else:
        print(chat_with_ai(user_input))

if __name__ == "__main__":
    main()
