from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask learning"

@app.route("/about")
def about():
    return "This is my first Flask application"

@app.route("/tasks",methods=["GET"])
def get_tasks():
    tasks = [
        {"id": 1, "title": "Learn Flask"},
        {"id": 2, "title": "Learn Fast API"}
    ]
    return {"tasks": tasks}

@app.route("/add_task", methods=["POST"])
def create_task():
    data = request.get_json()
    task_name = data.get("title")
    return {
        "message": "Task created successfully",
        "task": task_name
    }

@app.route("/welcome/<name>")
def welcome(name):
    return f"Welcome {name}!"

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return {
        "user_id": user_id,
        "message": "user found"
    }

if __name__ == "__main__":
    app.run(debug=True)
