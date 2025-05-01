
# 🕵️ APE Code Scraper - Data Management Guide

## 🗃️ Directory Structure

data/
├── raw/                    # Original scraped data (auto-created)
│   └── companies_raw_20230815.xlsx
└── processed/              # Analysis-ready data (auto-created)
    └── companies_analyzed.xlsx

### 📂 Data Storage Management

💾 Saving Raw Data

from src.config import RAW_DATA_DIR
from src.utils.file_utils import save_to_excel
from datetime import datetime

# Example: Save scraped data with timestamp
raw_data = [{"name": "Company A", "revenue": "1.2M€", "ape_code": "6201Z"}]
file_path = RAW_DATA_DIR / f"companies_raw_{datetime.now().strftime('%Y%m%d')}.xlsx"
save_to_excel(raw_data, file_path)

-------------------------------------------------------------------------------

Key Features:

✅ Automatic directory creation

📅 Daily timestamped files (prevents overwrites)

📏 Standardized Excel formatting

## 🔧 Saving Processed Data
python
from src.config import PROCESSED_DATA_DIR
import pandas as pd

# Example: Save cleaned data
processed_df = pd.DataFrame([
    {"name": "Company A", "revenue_clean": 1200000, "employees": 42}
])

processed_path = PROCESSED_DATA_DIR / "companies_analyzed.xlsx"
processed_df.to_excel(
    processed_path,
    sheet_name="Analyzed",  # Custom sheet name
    index=False            # Exclude index column
)
