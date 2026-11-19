import json
import pandas as pd
import matplotlib.pyplot as plt

from src.config import OUTPUT_DIR, REPORT_DIR


def generate_reports(weather, alerts):
    hourly = weather["hourly"]

    dataframe = pd.DataFrame({
        "time": hourly["time"],
        "temperature": hourly["temperature_2m"],
        "rain_probability": hourly["precipitation_probability"],
        "rainfall": hourly["precipitation"],
        "wind_speed": hourly["wind_speed_10m"],
        "humidity": hourly["relative_humidity_2m"]
    })

    csv_path = REPORT_DIR / "hourly_weather_report.csv"
    dataframe.to_csv(csv_path, index=False)

    alert_path = OUTPUT_DIR / "weather_alerts.json"

    with open(alert_path, "w", encoding="utf-8") as file:
        json.dump(alerts, file, indent=4)

    plt.figure(figsize=(12, 5))

    plt.plot(
        dataframe["time"][:24],
        dataframe["temperature"][:24],
        marker="o"
    )

    plt.title("Next 24 Hours Temperature Forecast")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    chart_path = OUTPUT_DIR / "temperature_forecast.png"
    plt.savefig(chart_path)
    plt.close()

    return {
        "csv": str(csv_path),
        "alerts": str(alert_path),
        "chart": str(chart_path)
    }