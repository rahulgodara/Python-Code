from flask import Blueprint, request, abort
from database import get_db_connection

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks",methods=["GET"])
def get_tasks():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        tasks = []

        for row in rows:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "status": row[2]
            })

        return {"tasks": tasks}

    finally:
        connection.close()



@task_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):

    connection = get_db_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE id=?",
            (task_id,)
        )

        row = cursor.fetchone()

        if row is None:
            abort(404)

        task = {
            "id": row[0],
            "title": row[1],
            "status": row[2]
        }

        return {"task": task}

    finally:
        connection.close()

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    connection = get_db_connection()
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
        cursor.execute(
            "insert into tasks (title, status) values(?,?)",
            (title, status)
        )
        connection.commit()
        new_task = {
            "id": cursor.lastrowid,
            "title":title,
            "status":status
        }
        return {
            "message": "Task created successfully",
            "task": new_task
        }, 201
    finally:
        connection.close()

@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    connection = get_db_connection()
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
        cursor.execute(
            "SELECT id FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            abort(404)
                
        cursor.execute(
            "update tasks set title=?, status=? where id=?",
            (title, status, task_id)
        )
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

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            abort(404)

        cursor.execute(
            "delete from tasks where id=?",
            (task_id,)
        )
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


@task_bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def patch_task(task_id):
    connection = get_db_connection()
    try:
        data = request.get_json(silent=True)
        if data is None:
            return {"error":"Invalid Json"},400

        if not data:
            return {"error": "At least one field is required"}, 400
        
        title = data.get("title")
        status = data.get("status")
        
        allowed_status = {"pending","completed","in_progress"}

        
        if title is not None: 
            if not isinstance(title, str) or not title.strip():
                return {"error":"Title is invalid"}, 400
            title = title.strip()
        
        if status is not None:
            if not isinstance(status, str) or status not in allowed_status:
                return {"error": "Status is not valid"}, 400

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            abort(404)

        if title is None:
            title = task[1]

        if status is None:
            status = task[2]

        title = title.strip()
        cursor.execute(
            "update tasks set title=?, status=? where id=?",
            (title, status, task_id)
        )

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