import argparse

from src.weather_client import get_weather
from src.sample_data import generate_sample_weather
from src.rules import generate_alerts
from src.storage import save_weather
from src.reports import generate_reports


def main():
    parser = argparse.ArgumentParser(
        description="Weather Forecast and Alert Application"
    )

    parser.add_argument(
        "--city",
        default="Patiala",
        help="City name"
    )

    parser.add_argument(
        "--mode",
        choices=["live", "simulation"],
        default="simulation"
    )

    args = parser.parse_args()

    print("\nWEATHER FORECAST AND ALERT APPLICATION")
    print("-------------------------------------")

    try:
        if args.mode == "live":
            weather = get_weather(args.city)
        else:
            weather = generate_sample_weather(args.city)

        city = weather["location"]["name"]

        alerts = generate_alerts(weather)

        save_weather(city, weather)

        report_files = generate_reports(weather, alerts)

        print(f"\nCity: {city}")
        print(
            "Temperature:",
            weather["current"]["temperature_2m"],
            "°C"
        )
        print(
            "Humidity:",
            weather["current"]["relative_humidity_2m"],
            "%"
        )

        print("\nWEATHER ALERTS")

        for alert in alerts:
            print(
                f"[{alert['level']}] "
                f"{alert['type']}: {alert['message']}"
            )

        print("\nREPORTS GENERATED")

        for name, path in report_files.items():
            print(f"{name}: {path}")

        print("\nProject executed successfully.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()