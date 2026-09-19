from fastapi import FastAPI

app = FastAPI(title="Sample API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}


@app.get("/items")
def get_items():
    return [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Keyboard", "price": 49.99},
    ]
