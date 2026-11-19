

# 🌦️ Weather Forecast & Alert Application

An interactive Python-based Weather Forecast and Alert Application that provides real-time weather information, 7-day weather forecasts, automated weather alerts, data visualization, and downloadable weather reports.

## 📌 Project Overview

The Weather Forecast & Alert Application is designed to help users monitor weather conditions and identify potentially dangerous weather situations.

It retrieves weather information using the Open-Meteo API and presents it through an interactive Streamlit dashboard and FastAPI backend.

The application generates alerts for:
- Heavy rainfall probability
- High temperature and heat conditions
- High humidity
- Strong wind speed

## 🎯 Project Objectives

- Retrieve real-time weather information.
- Generate 7-day weather forecasts.
- Identify potentially risky weather conditions.
- Generate automated weather alerts.
- Visualize temperature and weather trends.
- Export weather forecast reports in CSV format.
- Store weather information using SQLite.

## 🚀 Features

- Real-time weather data
- 7-day weather forecasting
- City-based weather search
- Rain probability monitoring
- Heat and humidity alerts
- Wind speed alerts
- Interactive Streamlit dashboard
- FastAPI REST API
- SQLite weather history
- CSV report generation
- Temperature forecast visualization
- Automated unit testing

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data processing |
| Requests | API integration |
| Open-Meteo API | Weather data |
| Streamlit | Interactive dashboard |
| FastAPI | REST API |
| SQLite | Data storage |
| Matplotlib | Data visualization |
| Pytest | Unit testing |
| Git & GitHub | Version control |

## 📁 Project Structure

```text
Weather-Forecast-Alert-Application/
│
├── api/
│   ├── __init__.py
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── geocoding.py
│   ├── weather_client.py
│   ├── forecast.py
│   ├── alert_engine.py
│   ├── simulation.py
│   ├── storage.py
│   └── report.py
│
├── data/
├── outputs/
├── reports/
├── images/
│
├── docs/
│   └── INTERVIEW_NOTES.md
│
├── tests/
│   └── test_alert_engine.py
│
├── main.py
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/erchandkujra-ai/Weather-Forecast-Alert-Application.git
```

### 2. Open project directory

```bash
cd Weather-Forecast-Alert-Application
```

### 3. Create virtual environment

```bash
python -m venv .venv
```

### 4. Activate virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

### Run weather forecast using API

```bash
python main.py --mode api --city Delhi
```

Other examples:

```bash
python main.py --mode api --city Mumbai
```

```bash
python main.py --mode api --city Patiala
```

### Run Streamlit Dashboard

```bash
python -m streamlit run dashboard/app.py
```

Open in your browser:

http://localhost:8501

### Run FastAPI Backend

```bash
uvicorn api.app:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

## 📊 Generated Outputs

The application generates:

- `reports/hourly_forecast.csv`
- `reports/daily_forecast.csv`
- `outputs/temperature_forecast.png`

## 🧪 Testing

Run unit tests:

```bash
python -m pytest -v
```

The test suite covers:

- Rain alert generation
- Heat alert generation
- Normal weather conditions without alerts

## 🌐 Weather Data Source

This project uses the Open-Meteo API for weather forecasts and geocoding.

Website: https://open-meteo.com/

No API key is required for the standard free Open-Meteo API.

## 🔮 Future Improvements

- Weather notifications through email
- Severe weather warning integration
- Machine learning-based weather prediction
- Interactive weather maps
- User authentication
- Cloud deployment
- Mobile-friendly interface

## 👨‍💻 Author

**ER.CHAND KUJRA**

GitHub: https://github.com/erchandkujra-ai

## 🙏 Acknowledgement

Special thanks to **Umesh Yadav Sir** and **IIP – Indian Institute of Technology Delhi** for their mentorship, guidance, and support throughout the project learning journey.

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you find this project useful, consider giving it a star on GitHub.

