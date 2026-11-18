from flask import Flask
from routes.task_routes import task_bp
from config import DevelopmentConfig, ProductionConfig
import os
from exceptions import (
    TaskNotFoundError,
    InvalidTaskDataError,
    BusinessRuleError
)


def create_app():
    app = Flask(__name__)
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
        logging.exception("Unexpected application error")
        return {
            "error": "Internal server error"
        }, 500

    environment = os.getenv("APP_ENV", "development")

    if environment=="production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    app.register_blueprint(task_bp)

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