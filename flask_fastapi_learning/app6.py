from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    connection = sqlite3.connect("tasks.db")

    try:
        cursor = connection.cursor()
        cursor.execute("select * from tasks")
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append({
                "id":row[0],
                "title":row[1],
                "status":row[2]
            })
        return {
            "tasks":tasks
        }
    finally:
        connection.close()

@app.route("/tasks/<int:task_id>",methods=["GET"])
def get_task(task_id):
    connection = sqlite3.connect("tasks.db")
    try:
        cursor = connection.cursor()
        cursor.execute("select * from tasks where id=?",(task_id,))
        row = cursor.fetchone()
        if row is None:
            return {
                "error":"Task not found"
            }, 404
        
        task = {
            "id":row[0],
            "title":row[1],
            "status":row[2]
        }
        return {
            "task":task
        }
    finally:
        connection.close()

@app.route("/tasks", methods=["POST"])
def create_task():
    connection = sqlite3.connect("tasks.db")
    try:
        data = request.get_json(silent=True)
        if data is None:
                return {"error":"Invalid JSON"},400
        
        title = data.get("title")
        if not isinstance(title, str) or not title.strip():
            return {"error":"Title is invalid"}, 400
        title = title.strip()

        allowed_status = {"pending","completed","in_progress"}
        status = data.get("status")
        if not isinstance(status, str) or status not in allowed_status:
            return {"error": "Status is not valid"}, 400
        
        cursor = connection.cursor()
        cursor.execute("insert into tasks (title, status) values(?,?)",(title, status))
        connection.commit()
        new_task = {
            "id": cursor.lastrowid,
            "title":title,
            "status":status
        }
        return {
            "Message": "Task created successfully",
            "task": new_task
        }, 201
    finally:
        connection.close()

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    connection = sqlite3.connect("tasks.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM tasks where id=?",(task_id,))
        task = cursor.fetchone()
        if task is None:
            return {"Error": "Invalid task id"}, 404
        
        data = request.get_json(silent=True)
        if data is None:
            return {"error":"Invalid JSON"},400
        
        title = data.get("title")
        if not isinstance(title, str) or not title.strip():
            return {"error":"Title is invalid"}, 400
        title = title.strip()

        allowed_status = {"pending","completed","in_progress"}
        status = data.get("status")
        if not isinstance(status, str) or status not in allowed_status:
            return {"error": "Status is not valid"}, 400
        
        cursor.execute("update tasks set title=?, status=? where id=?",(title, status, task_id))
        connection.commit()
        task = {
            "id": task_id,
            "title":title,
            "status":status
        }
        return {
            "message": "Task updated successfully",
            "task": task
        }, 200
    finally:
        connection.close()

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks where id=?",(task_id,))
        task = cursor.fetchone()
        if task is None:
            return {"Error": "Invalid task id"}, 404

        cursor.execute("delete from tasks where id=?",(task_id,))
        connection.commit()
        
        deleted_task = {
            "id": task[0],
            "title": task[1],
            "status": task[2]
        }

        return {
            "message": "Task deleted successfully",
            "task": deleted_task
        }, 200
    finally:
        connection.close()

if __name__ == "__main__":
    app.run(debug=True)