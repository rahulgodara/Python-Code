import os

class DevelopmentConfig:
    DEBUG = True
    APP_NAME = "Task Manager API"
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret")
    
class ProductionConfig:
    DEBUG = False
    APP_NAME = "Task Manager API"
    SECRET_KEY = os.getenv("SECRET_KEY")