import random
import requests
from typing import Dict, List
from src.utils.logger import setup_logger

logger = setup_logger("proxy_manager")

class ProxyManager:
    def __init__(self, proxy_list: List[str] = None):
        self.proxies = proxy_list or []
        self.current_proxy = None
        
    def get_random_proxy(self) -> Dict[str, str]:
        """Returns a random proxy from the pool"""
        if not self.proxies:
            logger.warning("No proxies configured - using direct connection")
            return {}
            
        proxy = random.choice(self.proxies)
        self.current_proxy = proxy
        return {
            "http": proxy,
            "https": proxy
        }
        
    def test_proxy(self, proxy: Dict, test_url: str = "http://example.com") -> bool:
        """Tests if a proxy is working"""
        try:
            response = requests.get(test_url, proxies=proxy, timeout=10)
            return response.status_code == 200
        except Exception as e:
            logger.debug(f"Proxy test failed: {e}")
            return False

# Example proxy list (replace with your actual proxies)
DEFAULT_PROXIES = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080"
]