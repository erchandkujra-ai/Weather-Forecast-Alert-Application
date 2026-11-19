def generate_alerts(weather):
    alerts = []

    current = weather["current"]
    hourly = weather["hourly"]
    daily = weather["daily"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_gusts_10m"]
    uv = current["uv_index"]

    # Rain alert: next 12 hours
    rain_probability = max(
        hourly["precipitation_probability"][:12],
        default=0
    )

    if rain_probability >= 60:
        alerts.append({
            "level": "WARNING",
            "type": "Rain Alert",
            "message": (
                f"Rain probability is {rain_probability}% "
                "within the next 12 hours."
            )
        })

    # Heat alert
    tomorrow_max = daily["temperature_2m_max"][1]

    if tomorrow_max >= 40:
        alerts.append({
            "level": "DANGER",
            "type": "Heat Alert",
            "message": (
                f"Tomorrow's maximum temperature may reach "
                f"{tomorrow_max}°C."
            )
        })

    # Humidity alert
    if humidity >= 85:
        alerts.append({
            "level": "WARNING",
            "type": "Humidity Alert",
            "message": f"Current humidity is high at {humidity}%."
        })

    # Wind alert
    if wind >= 54:
        alerts.append({
            "level": "DANGER",
            "type": "Wind Alert",
            "message": f"Strong wind gusts detected: {wind} km/h."
        })

    # UV alert
    if uv >= 8:
        alerts.append({
            "level": "WARNING",
            "type": "UV Alert",
            "message": f"High UV index detected: {uv}."
        })

    if not alerts:
        alerts.append({
            "level": "SAFE",
            "type": "Weather Status",
            "message": "No configured weather alerts detected."
        })

    return alerts