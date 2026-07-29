import logging
import os

# Create logs folder automatically
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/jarvis.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)


def log(message):
    logging.info(message)