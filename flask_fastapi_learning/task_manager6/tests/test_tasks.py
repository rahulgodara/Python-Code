from unittest.mock import patch
import sqlite3

def test_get_tasks(client):
    response = client.get("/tasks")

    assert response.status_code == 200

def test_get_task_success(client):
    response = client.get("/tasks/1")
    print(response.json)
    assert response.status_code == 200
    assert response.json["task"]["id"] == 1
    assert response.json["task"]["status"] == 'completed'
    assert response.json["task"]["title"] == 'Learn FastAPI properly'

def test_get_task_failure(client):
    response = client.get("/tasks/99999")
    assert response.status_code == 404

def test_create_task_success(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn pytest"}
    )

    print(response.json)

    assert response.status_code == 201
    assert response.json["message"] == "Task created successfully"
    assert response.json["task"]["title"] == "Learn pytest"

def test_create_task_missing_title(client):
    response = client.post(
        "/tasks",
        json={}
    )

    print(response.json)

    assert response.status_code == 400
    assert response.json["error"] == "Title is invalid"

def test_create_task_empty_title(client):
    response = client.post(
        "/tasks",
        json={"title": ""}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Title is invalid"

def test_create_task_whitespace_title(client):
    response = client.post(
        "/tasks",
        json={"title": "     "}
    )

    assert response.status_code == 400
    assert response.json["error"] == "Title is invalid"


def test_create_task_invalid_json(client):
    response = client.post(
        "/tasks",
        data = "This is not json",
        content_type = "application/json"
    )

    assert response.status_code==400
    assert response.json['error']== 'Invalid JSON'

def test_create_task_json_array(client):
    response = client.post(
        "/tasks",
        json=["Learn pytest", "Learn Flask"]
    )

    assert response.status_code==400
    assert response.json['error']== 'Invalid JSON'

def test_create_task_unsupported_field(client):
    response = client.post(
        "/tasks",
        json={"title": "a new task", "priority":"high"}
    )
    print(response.json)
    assert response.status_code==400
    assert response.json['error']== 'Unsupported fields'

def test_create_task_title_number(client):
    response = client.post(
        "/tasks",
        json={"title": 123}
    )
    print(response.json)
    assert response.status_code==400
    assert response.json['error']== 'Title is invalid'

def test_create_task_title_boolean(client):
    response = client.post(
        "/tasks",
        json={"title": True}
    )
    print(response.json)
    assert response.status_code==400
    assert response.json['error']== 'Title is invalid'

def test_create_task_title_null(client):
    response = client.post(
        "/tasks",
        json={"title": None}
    )
    print(response.json)
    assert response.status_code==400
    assert response.json['error']== 'Title is invalid'

def test_create_task_database_error(client):
    with patch(
        "routes.task_routes.create_task_service",
        side_effect=sqlite3.Error("Database error")
    ):
        response = client.post(
            "/tasks",
            json = {"title":"New task"}
        )
    print(response.json)
    assert response.status_code==500
    assert response.json['error']== "Unable to create task due to a database error"

def test_update_task_with_title(client):
    response = client.post(
        "/tasks",
        json={"title": "Learn pytest"}
    )

    print(response.json)

    assert response.status_code == 201
    assert response.json["message"] == "Task created successfully"
    assert response.json["task"]["title"] == "Learn pytest"
