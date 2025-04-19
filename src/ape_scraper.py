from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils import logger, file_utils
import time
import pandas as pd

class APECodeScraper:
    def __init__(self, headless=True):
        self.driver = self._init_driver(headless)
        self.logger = logger.setup_logger("ape_scraper")
        self.base_url = "https://infonet.fr/recherche-entreprises"

    def _init_driver(self, headless):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"user-agent={get_random_user_agent()}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return webdriver.Chrome(options=options)

    def scrape_ape_code(self, ape_code: str, pages: int = 10) -> List[Dict]:
        """Scrape companies by APE code"""
        companies = []
        
        for page in range(1, pages + 1):
            url = f"{self.base_url}/{page}/P2FwZUNvZGVzPT{ape_code}...rest_of_url"
            self.driver.get(url)
            time.sleep(2)  # Use WebDriverWait in production
            
            # Extract company rows
            rows = self.driver.find_elements(By.CSS_SELECTOR, "tr.toggle-add-to-list-button")
            for row in rows:
                company = self._extract_company(row)
                if company:
                    companies.append(company)
        
        return companies

    def _extract_company(self, row) -> Dict:
        """Extract detailed company info from a row"""
        try:
            return {
                "name": self._safe_extract(row, By.CLASS_NAME, "cse-company-name"),
                "ape_code": self._safe_extract(row, By.ID, "company-code-ape"),
                "revenue": self._clean_revenue(
                    self._safe_extract(row, By.CLASS_NAME, "text-nowrap.font-weight-semibold")
                ),
                "employees": self._safe_extract(row, By.CSS_SELECTOR, "td:nth-child(10) span"),
                "address": self._safe_extract(row, By.CSS_SELECTOR, "#company-address #address-copy"),
                "website": self._safe_extract_link(row, By.ID, "header-company-website"),
                "linkedin": self._safe_extract_link(row, By.ID, "header-company-linkedin"),
                "facebook": self._safe_extract_link(row, By.CSS_SELECTOR, "[data-test='facebook-link']"),
            }
        except Exception as e:
            self.logger.error(f"Extraction failed: {e}")
            return None

    def _safe_extract(self, element, by, value):
        """Safe element text extraction"""
        try:
            return element.find_element(by, value).text.strip()
        except:
            return None

    def _safe_extract_link(self, element, by, value):
        """Safe link extraction"""
        try:
            return element.find_element(by, value).get_attribute("href")
        except:
            return None

    def _clean_revenue(self, revenue_str: str) -> float:
        """Convert revenue strings like '1.2M€' to numeric"""
        if not revenue_str:
            return 0.0
        return float(revenue_str.replace("M€", "").replace(",", ".")) * 1_000_000