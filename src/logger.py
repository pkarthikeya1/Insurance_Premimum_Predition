import sys
import os
import logging


log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging_format = "[%(asctime)s, %(levelname)s, %(module)s, %(message)s ]"

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
    ]
)
logger=logging.getLogger("Insurance_Premium_Prediction_Logger")