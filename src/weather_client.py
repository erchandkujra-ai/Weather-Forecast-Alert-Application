import httpx


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = httpx.get(
        GEOCODING_URL,
        params=params,
        timeout=20
    )
    response.raise_for_status()

    results = response.json().get("results", [])

    if not results:
        raise ValueError(f"City not found: {city}")

    location = results[0]

    return {
        "name": location["name"],
        "country": location.get("country", ""),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(city):
    location = get_coordinates(city)

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "wind_gusts_10m",
            "uv_index"
        ],
        "hourly": [
            "temperature_2m",
            "precipitation_probability",
            "precipitation",
            "wind_speed_10m",
            "relative_humidity_2m",
            "uv_index"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
            "sunrise",
            "sunset",
            "uv_index_max"
        ],
        "timezone": "auto",
        "forecast_days": 7
    }

    response = httpx.get(
        FORECAST_URL,
        params=params,
        timeout=30
    )
    response.raise_for_status()

    weather = response.json()
    weather["location"] = location

    return weather