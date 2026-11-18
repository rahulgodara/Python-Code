from repositories.task_repository import create_task, get_task_by_id, patch_task_by_id, delete_task_by_id, get_task_history_repo, update_task_with_history
from exceptions import BusinessRuleError

def create_task_service(title):
    status = "pending"
    return create_task(title, status)

def update_task_service(task_id, title, status):
    task = get_task_by_id(task_id)
    
    existing_status = task["status"]

    requested_status = status if status is not None else existing_status

    if existing_status=='completed' and requested_status !="completed":
        raise BusinessRuleError("Completed task cannot move back backwards")
    if existing_status=='in_progress' and requested_status not in {"in_progress", "completed"}:
        raise BusinessRuleError("In_progress task cannot move back to pending")

    return patch_task_by_id(task_id, title, status)

def delete_task_service(task_id):
    return delete_task_by_id(task_id)

def get_task_history_service(task_id):
    return get_task_history_repo(task_id)