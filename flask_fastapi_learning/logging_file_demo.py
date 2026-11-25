import logging

logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

logger = logging.getLogger(__name__)

logger.info("This is an info message")
logger.error("This is an error message")
logger.warning("This is a warning message")