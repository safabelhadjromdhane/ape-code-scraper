import logging
from pathlib import Path
from datetime import datetime
import sys

def setup_logger(name: str, log_level: str = "INFO", log_to_file: bool = True) -> logging.Logger:
    """
    Configures a logger with both console and file handlers.
    
    Args:
        name: Logger name (use __name__ typically)
        log_level: DEBUG/INFO/WARNING/ERROR/CRITICAL
        log_to_file: Whether to save logs to file
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Formatter
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    
    # Console Handler (always active)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File Handler (optional)
    if log_to_file:
        log_dir = Path("logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"{name}_{timestamp}.log"
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger