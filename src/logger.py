# Importing the required modules
import logging
import os
from datetime import datetime

# Creating a log file with the current date and time as the name of the file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating a logs folder if it does not exist
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Setting the log file path and the log level
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
