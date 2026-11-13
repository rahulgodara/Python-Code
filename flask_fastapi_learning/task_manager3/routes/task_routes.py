from flask import Blueprint, request, abort
from database import get_db_connection
from repositories.task_repository import get_task_by_id, get_all_tasks, create_task as create_new_task, delete_task_by_id, update_task_by_id, patch_task_by_id

task_bp = Blueprint("tasks", __name__)

@task_bp.route("/tasks",methods=["GET"])
def get_tasks():
    tasks = get_all_tasks()
    return {
        "tasks": tasks
    }

@task_bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = get_task_by_id(task_id)

    if task is None:
        abort(404)

    return {"task": task}, 200

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)
    if data is None:
        return {"error":"Invalid JSON"},400
        
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return {"error":"Title is invalid"}, 400
    
    allowed_status = {"pending","completed","in_progress"}
    status = data.get("status")
    if not isinstance(status, str) or status not in allowed_status:
        return {"error": "Status is not valid"}, 400

    new_task = create_new_task(title, status)

    return {
        "message": "Task created successfully",
        "task": new_task
    }, 201
    
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

        task = update_task_by_id(task_id, title, status)
        if task is None:
            abort(404)
                
        return {
            "message": "Task updated successfully",
            "task": task
        }, 200
    finally:
        connection.close()

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted_task = delete_task_by_id(task_id)
    if deleted_task is None:
        abort(404)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }, 200

@task_bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def patch_task(task_id):
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

    task = patch_task_by_id(task_id, title, status)
    if task is None:
        abort(404)

    return {
        "message": "Task updated successfully",
        "task": task
    }, 200