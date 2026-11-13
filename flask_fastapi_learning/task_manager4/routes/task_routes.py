from flask import Blueprint, request, abort
from repositories.task_repository import get_task_by_id, get_all_tasks, delete_task_by_id, update_task_by_id, patch_task_by_id
from services.task_service import create_task_service, patch_task_service

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
    
    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    allowed_fields = {"title", "status"}
    if not set(data.keys()).issubset(allowed_fields):
        return {"error": "Unsupported fields"}, 400
    
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return {"error":"Title is invalid"}, 400
    title = title.strip()

    new_task = create_task_service(title)

    return {
        "message": "Task created successfully",
        "task": new_task
    }, 201
    
@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json(silent=True)
    
    if data is None:
        return {"error":"Invalid JSON"},400
    
    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    allowed_fields = {"title", "status"}
    if not set(data.keys()).issubset(allowed_fields):
        return {"error": "Unsupported fields"}, 400
    
    title = data.get("title")
    if not isinstance(title, str) or not title.strip():
        return {"error":"Title is invalid"}, 400
    title = title.strip()

    allowed_status = {"pending","completed","in_progress"}
    status = data.get("status")
    if not isinstance(status, str) or status not in allowed_status:
        return {"error": "Status is not valid"}, 400
    
    task = update_task_by_id(task_id, title, status)
    if task is None:
        abort(404)
            
    return {
        "message": "Task updated successfully",
        "task": task
    }, 200

@task_bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def patch_task(task_id):
    data = request.get_json(silent=True)
    
    if data is None:
        return {"error":"Invalid Json"},400

    if not isinstance(data, dict):
        return {"error": "Invalid JSON"}, 400

    if not data:
        return {"error": "At least one field is required"}, 400

    allowed_fields = {"title", "status"}
    if not set(data.keys()).issubset(allowed_fields):
        return {"error": "Unsupported fields"}, 400
    
    title = data.get("title")
    if "title" in data:
        if not isinstance(title, str) or not title.strip():
            return {"error":"Title is invalid"}, 400
        title = title.strip()
    else:    
        title = None

    status = data.get("status")
    allowed_status = {"pending","completed","in_progress"}

    if "status" in data:
        if not isinstance(status, str) or status not in allowed_status:
            return {"error": "Status is not valid"}, 400
    else:
        status = None

    try:
        task = patch_task_service(task_id, title, status)
        if task is None:
            abort(404)
    except ValueError as e:
        return {
            "message": str(e)
        }, 400

    return {
        "message": "Task updated successfully",
        "task": task
    }, 200

@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted_task = delete_task_by_id(task_id)
    if deleted_task is None:
        abort(404)

    return {
        "message": "Task deleted successfully",
        "task": deleted_task
    }, 200
