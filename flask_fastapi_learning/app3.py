from flask import Flask, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "status": "pending"},
    {"id": 2, "title": "Learn FastAPI", "status": "completed"}
]


@app.route("/tasks",methods=["GET"])
def get_tasks():
    return {"tasks": tasks}

@app.route("/tasks", methods=["POST"])
def create_tasks():
    data = request.get_json(silent=True)
    if not data:
        return {"error":"Invalid JSON"},400
    
    title = data.get("title")
    if not title:
        return {"error":"Missing title"},400

    status = data.get("status")
    if not status:
        return {"error":"status is missing"},400

    new_task = {
        "id": len(tasks)+1,
        "title":title,
        "status":status
    }
    tasks.append(new_task)
    return {
        "message": "Task created",
        "task":new_task
    },201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next(
        (task for task in tasks if task["id"]==task_id),
        None
    )
    if not task:
        return {"Error": "Invalid task id"},404
    
    data = request.get_json(silent=True)
    if not data:
        return {"error":"Invalid JSON"},400
    task["title"] = data.get("title", task["title"])
    task["status"] = data.get("status", task["status"])
    return {
        "message": "task updated",
        "task": task
    },200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = next(
        (task for task in tasks if task["id"]==task_id),
        None
    )
    if not task:
        return {"Error": "Invalid task id"},404

    tasks.remove(task)

    return {
        "message": "task deleted successfully"
    },200

if __name__ == "__main__":
    app.run(debug=True)