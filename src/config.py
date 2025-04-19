from pathlib import Path
from src.utils.logger import setup_logger

logger = setup_logger("config")

# Directory Structure
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOGS_DIR = BASE_DIR / "logs"

# Create directories if they don't exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, LOGS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
    logger.debug(f"Ensured directory exists: {directory}")

# Scraping Configuration
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Excel Export Settings
EXCEL_SETTINGS = {
    "raw_format": {
        "sheet_name": "Raw Data",
        "freeze_panes": "A2"
    },
    "processed_format": {
        "sheet_name": "Analyzed Data",
        "auto_filter": True
    }
}