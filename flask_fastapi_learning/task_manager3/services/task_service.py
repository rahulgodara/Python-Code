from repositories.task_repository import create_task

def create_task_service(title, status):
    return create_task(title, status)