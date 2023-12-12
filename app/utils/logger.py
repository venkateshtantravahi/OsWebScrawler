"""
This script sets up logging for the application. It configures a logger with two handlers: one for writing logs to a file and another for outputting logs to the console.

- File logs: All log messages (including DEBUG level) are written to 'app.log'.
- Console logs: Only ERROR (and more severe) log messages are printed to the console.

This setup helps in monitoring and debugging the application by providing detailed logs and separating less critical logs (DEBUG) from more critical ones (ERROR).
"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler
fh = logging.FileHandler('app.log')
fh.setLevel(logging.DEBUG)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
