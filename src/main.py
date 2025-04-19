from ape_scraper import APECodeScraper
from utils.file_utils import save_to_excel
# Add this at the top of main.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

if __name__ == "__main__":
    scraper = APECodeScraper()
    data = scraper.scrape(ape_code="6201Z", pages=3)
    save_to_excel(data, "data/raw/output.xlsx")