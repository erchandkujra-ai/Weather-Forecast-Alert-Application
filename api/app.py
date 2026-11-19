from fastapi import FastAPI, HTTPException

from src.weather_client import get_weather
from src.rules import generate_alerts
from src.storage import save_weather


app = FastAPI(
    title="Weather Forecast and Alert API",
    description="Weather forecasting and risk alert application",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Weather Forecast and Alert API is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/weather")
def weather_endpoint(city: str = "Patiala"):
    try:
        weather = get_weather(city)
        alerts = generate_alerts(weather)

        save_weather(city, weather)

        return {
            "city": city,
            "weather": weather,
            "alerts": alerts
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )