from fastapi import FastAPI
from src.api.fastapi_app import app

# This will serve the FastAPI app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
