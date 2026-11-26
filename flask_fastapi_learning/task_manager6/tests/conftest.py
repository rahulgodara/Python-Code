import pytest
from app import create_app
import sqlite3

@pytest.fixture
def client(tmp_path):
    test_db = tmp_path / "test_task.db"
    connection = sqlite3.connect(test_db)

    connection.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE task_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            old_status TEXT,
            new_status TEXT,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS task_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER NOT NULL,
            old_status TEXT NOT NULL,
            new_status TEXT NOT NULL,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        )
    """)

    connection.execute("""
        INSERT INTO tasks (title, status)
        VALUES (?, ?)
    """, ("Learn FastAPI properly", "completed"))

    connection.commit()
    connection.close()


    app = create_app()
    app.config["TESTING"] = True
    app.config["DATABASE"] = str(test_db)

    return app.test_client()