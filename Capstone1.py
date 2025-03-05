import os

# Define the structure of the project
project_structure = {
    "demand_forecasting_project": {
        ".gitignore": "",
        "README.md": "",
        "requirements.txt": "",
        "main.py": "",
        "data": {
            "Competitor_Products_Dataset.csv": "",
            "nykaa_inventory.csv": "",
            "Nykaa_Products_Dataset.csv": "",
            "processed_demand_data.csv": "",
            "processed_competitor_data.csv": "",
            "product_mapping.csv": "",
            "inventory_optimization_data.csv": "",
        },
        "models": {
            "demand_forecast_model.pkl": "",
            "inventory_eoq_model.pkl": "",
            "inventory_rl_model.pkl": "",
        },
        "src": {
            "__init__.py": "",
            "agents": {
                "__init__.py": "",
                "decision_maker.py": "",
                "demand_predictor.py": "",
                "market_watcher.py": "",
                "inventory_manager.py": "",
                "inventory_eoq.py": "",
                "inventory_rl.py": "",
            },
            "api": {
                "__init__.py": "",
                "fastapi_app.py": "",
                "scrape_competitor.py": "",
            },
            "chatbot": {
                "__init__.py": "",
                "chatbot.py": "",
            },
            "data_processing": {
                "__init__.py": "",
                "preprocess.py": "",
                "match_products.py": "",
            },
            "pipeline": {
                "__init__.py": "",
                "data_pipeline.py": "",
                "model_training.py": "",
                "reinforcement_learning_pipeline.py": "",
            },
        },
        "tests": {
            "test_preprocess.py": "",
            "test_model.py": "",
            "test_api.py": "",
        },
    }
}

# Function to create directories and files
def create_project_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(value, dict):  # If it's a directory, create the folder and recursively call
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, value)
        else:  # If it's a file, create the file
            with open(path, "w") as file:
                file.write(value)

# Define the base path for the project directory
base_path = "demand_forecasting_project"  # Adjust this if you want to place it elsewhere

# Create the project structure
os.makedirs(base_path, exist_ok=True)
create_project_structure(base_path, project_structure)

print(f"Project structure created at {os.path.abspath(base_path)}")
