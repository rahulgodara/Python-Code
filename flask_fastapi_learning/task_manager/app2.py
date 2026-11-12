from flask import Flask
from routes.task_routes import task_bp
from config import DevelopmentConfig, ProductionConfig
import os

app = Flask(__name__)
environment = os.getenv("APP_ENV", "development")

if environment=="production":
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

app.register_blueprint(task_bp)


if __name__=="__main__":
    print("Application name:",app.config["APP_NAME"])
    print("Debug mode:",app.config["DEBUG"])
    app.run()