import logging
import sys
# Configure the logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
    logging.FileHandler("queue.log"),
    logging.StreamHandler(sys.stdout)
    
    ])

# Create a logger
logger = logging.getLogger(__name__)
