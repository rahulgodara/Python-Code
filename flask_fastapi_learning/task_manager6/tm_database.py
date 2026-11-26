import sqlite3
from pathlib import Path
from flask import has_app_context, current_app

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR.parent / "tasks.db"

def get_db_connection():
    if has_app_context():
        db_path = current_app.config.get("DATABASE", DB_PATH)
    else:
        db_path = DB_PATH

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection