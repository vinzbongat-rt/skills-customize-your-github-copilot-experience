from fastapi import FastAPI

app = FastAPI(title="Mini Weather API")

weather_data = {
    "seattle": {"city": "Seattle", "temperature": 62, "condition": "cloudy"},
    "miami": {"city": "Miami", "temperature": 82, "condition": "sunny"},
    "denver": {"city": "Denver", "temperature": 68, "condition": "windy"},
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Mini Weather API"}


@app.get("/weather/{city}")
def get_weather(city: str):
    city_name = city.lower()
    if city_name in weather_data:
        return weather_data[city_name]
    return {"message": f"Weather data for {city} was not found."}
