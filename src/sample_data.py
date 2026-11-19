
import random
import math
from datetime import datetime, timedelta


def generate_sample_weather(city="Patiala"):
    random.seed(42)

    # Current date and time
    now = datetime.now().replace(
        minute=0,
        second=0,
        microsecond=0
    )

    # Generate 48 hours of simulated weather
    hourly_times = []
    temperatures = []
    rain_probabilities = []
    rainfall = []
    wind_speeds = []
    humidity = []
    uv_values = []

    for hour in range(48):
        timestamp = now + timedelta(hours=hour)

        hourly_times.append(
            timestamp.strftime("%Y-%m-%dT%H:%M")
        )

        temperature = 25 + 8 * (
            0.5 + 0.5 * math.sin(hour / 24 * 6.28)
        )

        temperatures.append(round(temperature, 1))
        rain_probabilities.append(random.randint(0, 95))
        rainfall.append(round(random.uniform(0, 5), 1))
        wind_speeds.append(round(random.uniform(5, 45), 1))
        humidity.append(random.randint(40, 95))
        uv_values.append(random.randint(0, 10))

    # Current weather
    current = {
        "temperature_2m": temperatures[0],
        "relative_humidity_2m": humidity[0],
        "apparent_temperature": temperatures[0] + 1,
        "precipitation": rainfall[0],
        "weather_code": 1,
        "wind_speed_10m": wind_speeds[0],
        "wind_direction_10m": 90,
        "wind_gusts_10m": wind_speeds[0] + 5,
        "uv_index": uv_values[0]
    }

    # Generate 8-day forecast
    daily = {
        "time": [
            (now + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(8)
        ],

        "weather_code": [
            random.choice([0, 1, 2, 3, 61, 71])
            for _ in range(8)
        ],

        "temperature_2m_max": [
            round(random.uniform(28, 43), 1)
            for _ in range(8)
        ],

        "temperature_2m_min": [
            round(random.uniform(15, 25), 1)
            for _ in range(8)
        ],

        "precipitation_probability_max": [
            random.randint(0, 100)
            for _ in range(8)
        ],

        "uv_index_max": [
            random.randint(2, 11)
            for _ in range(8)
        ]
    }

    return {
        "location": {
            "name": city,
            "country": "India",
            "latitude": 30.34,
            "longitude": 76.39
        },

        "current": current,

        "hourly": {
            "time": hourly_times,
            "temperature_2m": temperatures,
            "precipitation_probability": rain_probabilities,
            "precipitation": rainfall,
            "wind_speed_10m": wind_speeds,
            "relative_humidity_2m": humidity,
            "uv_index": uv_values
        },

        "daily": daily,
        "simulation": True
    }
