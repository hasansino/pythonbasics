# Configuration

import logging

# Constants
LOGGER_INSTANCE_NAME = "default"

# Init code
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt = '%H:%M:%S')
LOGGER = logging.getLogger(LOGGER_INSTANCE_NAME)