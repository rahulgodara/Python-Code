from flask import Flask
from routes.task_routes import task_bp
from config import DevelopmentConfig

app = Flask(__name__)
app.config["DEBUG"]=True
app.config["APP_NAME"]="Task Manager API"
app.register_blueprint(task_bp)

if __name__=="__main__":
    print("Application name:",app.config["APP_NAME"])
    print("Debug mode:",app.config["DEBUG"])
    app.run()
    #or use just - app.run(debug=app.config["DEBUG"])
    