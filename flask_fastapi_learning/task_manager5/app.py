from flask import Flask
import logging
from routes.task_routes import task_bp
from config import DevelopmentConfig, ProductionConfig
import os
from exceptions import (
    TaskNotFoundError,
    InvalidTaskDataError,
    BusinessRuleError
)
from logging.handlers import RotatingFileHandler

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
file_handler = RotatingFileHandler(
    os.path.join(log_dir, "app.log"),
    maxBytes=1024*1024,
    backupCount=5
)

console_handler = logging.StreamHandler()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        console_handler,
        file_handler
    ],
    force=True
)

def create_app():
    """Basic logging config for initial learning"""
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    # )

    # file_handler.setFormatter(
    #     logging.Formatter(
    #         "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    #     )
    # )

    app = Flask(__name__)
        
    # app.logger.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)
    
    @app.errorhandler(TaskNotFoundError)
    def handle_task_not_found(error):
        return {
            "error": str(error)
        }, 404
    
    @app.errorhandler(InvalidTaskDataError)
    def handle_invalid_task_data(error):
        return {
            "error": str(error)
        }, 400
    
    @app.errorhandler(BusinessRuleError)
    def handle_business_rule_error(error):
        return {
            "error": str(error)
        }, 400

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception("Unexpected application error")
        return {
            "error": "Internal server error"
        }, 500

    environment = os.getenv("APP_ENV", "development").lower().strip()
    print("####################---------",environment)
    
    if environment=="production":
        if not ProductionConfig.SECRET_KEY:
            raise ValueError("SECRET_KEY is required in production")
        app.config.from_object(ProductionConfig)
    elif environment=="development":
        app.config.from_object(DevelopmentConfig)
    else:
        raise ValueError(f"Invalid APP_ENV value: {environment}")

    app.register_blueprint(task_bp)
    app.logger.info("Task Manager API started successfully")

    @app.errorhandler(404)
    def not_found(error):
        return {
            "success": False,
            "error": "Resource not found",
            "status_code": 404
        }, 404
    
    return app

app1 = create_app()
app2 = create_app()

app1.config["APP_NAME"] = "Application One"
app2.config["APP_NAME"] = "Application Two"



if __name__=="__main__":
    # print("Application name:",app1.config["APP_NAME"])
    # print("Debug mode:",app1.config["DEBUG"])
    print("App1 ---------",app1.config["APP_NAME"])
    print("App2 ---------",app2.config["APP_NAME"])
    app1.run(port=8000)
    # app2.run(port=9000)