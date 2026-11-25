from app import create_app

def test_get_tasks():
    app = create_app()
    client = app.test_client()
    response = client.get("/tasks")

    assert response.status_code == 200