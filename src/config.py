from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DB_DIR = BASE_DIR / "db"
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = BASE_DIR / "reports"
IMAGE_DIR = BASE_DIR / "images"

for folder in [DATA_DIR, DB_DIR, OUTPUT_DIR, REPORT_DIR, IMAGE_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = DB_DIR / "weather.db"

DEFAULT_CITY = "Patiala"
DEFAULT_COUNTRY = "India"