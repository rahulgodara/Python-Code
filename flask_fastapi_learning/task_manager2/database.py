import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR.parent / "tasks.db"

def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    return connection
