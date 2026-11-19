import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

from src.weather_client import get_weather
from src.sample_data import generate_sample_weather
from src.rules import generate_alerts
from src.storage import save_weather


st.set_page_config(
    page_title="Weather Forecast & Alerts",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background-color: #1e202b;
    color: white;
}

header[data-testid="stHeader"] {
    background-color: #1e202b;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

div[data-testid="stMetric"] {
    background: #303342;
    padding: 15px;
    border-radius: 12px;
}

div[data-testid="stMetricLabel"] {
    color: #c4c7d4;
}

div[data-testid="stMetricValue"] {
    color: white;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #303342;
    border-radius: 14px;
}

div.stButton > button {
    background-color: #079bd0;
    color: white;
    border-radius: 10px;
    border: none;
    min-height: 42px;
}

div.stButton > button:hover {
    background-color: #087eae;
    color: white;
}

.forecast-icon {
    font-size: 38px;
    text-align: center;
}

.forecast-day {
    font-weight: bold;
    text-align: center;
    color: white;
}

.forecast-temp {
    text-align: center;
    color: white;
    font-size: 14px;
}

.section-heading {
    font-size: 22px;
    font-weight: bold;
    color: white;
    margin-top: 25px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- WEATHER HELPERS ----------------

def weather_description(code):
    descriptions = {
        0: ("Clear sky", "☀️"),
        1: ("Mainly clear", "🌤️"),
        2: ("Partly cloudy", "⛅"),
        3: ("Overcast", "☁️"),
        45: ("Fog", "🌫️"),
        48: ("Fog", "🌫️"),
        51: ("Drizzle", "🌦️"),
        53: ("Drizzle", "🌦️"),
        55: ("Heavy drizzle", "🌧️"),
        61: ("Light rain", "🌧️"),
        63: ("Moderate rain", "🌧️"),
        65: ("Heavy rain", "🌧️"),
        71: ("Light snow", "🌨️"),
        73: ("Snow", "❄️"),
        75: ("Heavy snow", "❄️"),
        80: ("Rain showers", "🌦️"),
        81: ("Rain showers", "🌧️"),
        82: ("Heavy showers", "⛈️"),
        95: ("Thunderstorm", "⛈️"),
        96: ("Thunderstorm", "⛈️"),
        99: ("Thunderstorm", "⛈️")
    }

    return descriptions.get(code, ("Weather", "🌤️"))


def wind_direction(degrees):
    directions = [
        "North", "North-East", "East", "South-East",
        "South", "South-West", "West", "North-West"
    ]
    return directions[int((degrees + 22.5) / 45) % 8]


# ---------------- SEARCH ----------------

st.title("🌤️ Weather Forecast & Alerts")

search_col, button_col = st.columns([4, 1])

with search_col:
    city = st.text_input(
        "Search city",
        value="Patiala",
        placeholder="Enter city name"
    )

with button_col:
    st.write("")
    search_button = st.button("Search", use_container_width=True)


if search_button:
    try:
        with st.spinner("Loading weather data..."):
            weather = get_weather(city)
            alerts = generate_alerts(weather)
            save_weather(city, weather)

            st.session_state["weather"] = weather
            st.session_state["alerts"] = alerts

    except Exception as error:
        st.error(f"Weather loading failed: {error}")


# ---------------- DEFAULT DATA ----------------

if "weather" not in st.session_state:
    st.session_state["weather"] = generate_sample_weather("Patiala")
    st.session_state["alerts"] = generate_alerts(
        st.session_state["weather"]
    )


weather = st.session_state["weather"]
alerts = st.session_state["alerts"]

current = weather["current"]
location = weather["location"]
daily = weather["daily"]
hourly = weather["hourly"]

temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]
uv = current["uv_index"]

weather_code = current.get("weather_code", 1)
description, icon = weather_description(weather_code)

wind_degrees = current.get("wind_direction_10m", 90)


# ---------------- CURRENT WEATHER + MAP ----------------

st.markdown(
    '<div class="section-heading">Current Weather</div>',
    unsafe_allow_html=True
)

weather_col, map_col = st.columns([1, 1])

with weather_col:
    with st.container(border=True):

        st.subheader(f"📍 {location['name']}")

        temp_col, icon_col = st.columns([2, 1])

        with temp_col:
            st.markdown(
                f"<h1 style='font-size:55px'>{temperature} °C</h1>",
                unsafe_allow_html=True
            )
            st.write(description)

        with icon_col:
            st.markdown(
                f"<h1 style='font-size:65px;text-align:center'>{icon}</h1>",
                unsafe_allow_html=True
            )

        st.divider()

        metric1, metric2 = st.columns(2)

        metric1.metric("Humidity", f"{humidity}%")
        metric2.metric("Wind Speed", f"{wind} km/h")

        metric3, metric4 = st.columns(2)

        metric3.metric("Wind Direction", wind_direction(wind_degrees))
        metric4.metric("UV Index", uv)

        feels_like = current.get("apparent_temperature", temperature)
        st.caption(f"Feels like: {feels_like} °C")


with map_col:
    st.subheader("📍 Location Map")

    latitude = location["latitude"]
    longitude = location["longitude"]

    map_url = (
        "https://www.openstreetmap.org/export/embed.html"
        f"?bbox={longitude-0.5},{latitude-0.3},"
        f"{longitude+0.5},{latitude+0.3}"
        f"&layer=mapnik&marker={latitude}%2C{longitude}"
    )

    components.html(
        f'<iframe src="{map_url}" width="100%" height="390" '
        'style="border:0;border-radius:12px;" '
        'loading="lazy"></iframe>',
        height=400
    )


# ---------------- 8 DAY FORECAST ----------------

st.markdown(
    '<div class="section-heading">📅 8-Day Weather Forecast</div>',
    unsafe_allow_html=True
)

forecast_count = min(8, len(daily["time"]))
forecast_columns = st.columns(forecast_count)

for index in range(forecast_count):

    date = daily["time"][index]

    from datetime import datetime

    day_name = datetime.fromisoformat(date).strftime("%A")

    maximum = daily["temperature_2m_max"][index]
    minimum = daily["temperature_2m_min"][index]

    codes = daily.get("weather_code", [])
    code = codes[index] if index < len(codes) else 1

    forecast_description, forecast_icon = weather_description(code)

    with forecast_columns[index]:
        with st.container(border=True):

            st.markdown(
                f"<div class='forecast-day'>{day_name}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='forecast-icon'>{forecast_icon}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='forecast-temp'><b>{maximum} °C</b></div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='forecast-temp' style='color:#aeb2c0'>{minimum} °C</div>",
                unsafe_allow_html=True
            )


# ---------------- WEATHER ALERTS ----------------

st.markdown(
    '<div class="section-heading">🚨 Weather Alerts</div>',
    unsafe_allow_html=True
)

for alert in alerts:

    if alert["level"] == "DANGER":
        st.error(f"{alert['type']}: {alert['message']}")

    elif alert["level"] == "WARNING":
        st.warning(f"{alert['type']}: {alert['message']}")

    else:
        st.success(alert["message"])


# ---------------- HOURLY FORECAST ----------------

st.markdown(
    '<div class="section-heading">📈 Next 24 Hours Forecast</div>',
    unsafe_allow_html=True
)

hourly_dataframe = pd.DataFrame({
    "Time": hourly["time"][:24],
    "Temperature": hourly["temperature_2m"][:24],
    "Rain Probability": hourly["precipitation_probability"][:24]
})

st.line_chart(
    hourly_dataframe.set_index("Time")[["Temperature"]]
)

st.area_chart(
    hourly_dataframe.set_index("Time")[["Rain Probability"]]
)

st.caption(
    "Educational weather forecasting project. "
    "Always follow official weather warnings for safety."
)
