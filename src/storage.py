import json
import sqlite3
from datetime import datetime

from src.config import DATABASE_PATH


def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS weather_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            recorded_at TEXT,
            weather_data TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_weather(city, weather):
    initialize_database()

    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute(
        """
        INSERT INTO weather_records
        (city, recorded_at, weather_data)
        VALUES (?, ?, ?)
        """,
        (
            city,
            datetime.now().isoformat(),
            json.dumps(weather)
        )
    )

    connection.commit()
    connection.close()


def get_weather_history(limit=20):
    initialize_database()

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.execute(
        """
        SELECT city, recorded_at, weather_data
        FROM weather_records
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    records = cursor.fetchall()
    connection.close()

    return [
        {
            "city": row[0],
            "recorded_at": row[1],
            "weather": json.loads(row[2])
        }
        for row in records
    ]