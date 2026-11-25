import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "rotation.log",
    maxBytes=1024,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s-%(levelname)s-%(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(100):
    logger.info(f"This is log message number {i}")