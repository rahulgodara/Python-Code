from flask import Flask, request

app = Flask(__name__)

tasks = [
    {"id":1, "title": "Learn Flask", "status": "pending"},
    {"id":2, "title": "Learn FastAPI", "status": "completed"}
]

@app.route("/")
def home():
    return {
        "message":"Task Manager API"
    }

@app.route("/welcome/<name>")
def welcome(name):
    return {
        "message":f"Welcome {name}!"
    }

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return {
        "user_id": user_id
    }

@app.route("/tasks", methods=["GET"])
def get_tasks():
    status = request.args.get("status")
    if status:
        filtered_tasks = [
            task for task in tasks
            if task["status"] == status
        ]
        return {
            "tasks": filtered_tasks
        }
    return{
        "tasks": tasks
    }


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)
    if not data:
        return{
            "error":"Invalid Json"
        },400
    title = data.get("title")
    if not title:
        return {
            "error": "Title is required"
        },400
    new_task = {
        "id": len(tasks)+1,
        "title": title,
        "status": "pending"
    }
    tasks.append(new_task)

    return {
        "message": "Task created",
        "task": new_task
    },201

if __name__ == "__main__":
    app.run(debug=True)