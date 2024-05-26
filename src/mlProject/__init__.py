import os 
import sys
import logging
import sys
sys.path.append('/Users/gangminlee/Projects/Mlflow-Project/src')  # Add the parent directory

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok = True)


logging.basicConfig(
    level=  logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger")