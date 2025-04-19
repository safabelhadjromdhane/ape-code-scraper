from fake_useragent import UserAgent
from typing import List
import random

# Initialize UserAgent only once
ua = UserAgent()

def get_random_user_agent() -> str:
    """Returns a random user agent string"""
    return ua.random

def get_user_agents_by_device(device_type: str = "desktop") -> List[str]:
    """
    Get user agents filtered by device type
    
    Args:
        device_type: 'desktop', 'mobile', or 'all'
    """
    if device_type == "desktop":
        return [ua.chrome, ua.firefox, ua.safari]
    elif device_type == "mobile":
        return [ua.android, ua.iphone]
    else:
        return [ua.random for _ in range(10)]  # 10 random agents