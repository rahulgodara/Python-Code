from flask import Flask, request

app = Flask(__name__)

@app.route("/tasks")
def get_tasks():
    status = request.args.get("status")
    return {
        "requested_status": status
    }

@app.route("/tasks2")
def get_tasks2():
    status = request.args.get("status","all")
    return {
        "requested_status": status
    }

@app.route("/tasks3")
def get_tasks3():
    status = request.args.get("status", "all")
    priority = request.args.get("priority", "all")

    return {
        "requested_status": status,
        "requested_priority": priority
    }

@app.route("/tasks4", methods=["POST"])
def create_tasks():
    data = request.get_json(silent=True)
    if not data:
        return {"error":"Invalid JSON"},400
    
    title = data.get("title")
    if not title:
        return {"error":"Missing title"},400

    priority = data.get("priority")
    if not priority:
        return {"error":"Priority is missing"}
    completed = data.get("completed")

    return {
        "message": "Task created",
        "title":title,
        "priority":priority,
        "completed":completed
    },201


if __name__ == "__main__":
    app.run(debug=True)