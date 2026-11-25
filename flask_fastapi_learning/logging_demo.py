import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("Task created successfully")
logger.warning("Task status was not provided")
logger.error("Database operation failed")
logger.critical("Application encountered a critical failure")
