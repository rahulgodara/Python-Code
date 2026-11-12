import sqlite3
connection = sqlite3.connect("tasks.db")

cursor = connection.cursor()
cursor.execute(
    """
    CREATE Table if not exists tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT NOT NULL
    )
"""
)

cursor.execute(
    """
    INSERT INTO tasks (title, status)
    VALUES (?, ?)
    """,
    ("Learn Flask", "pending")
)

cursor.execute(
    """
    INSERT INTO tasks (title, status)
    VALUES (?, ?)
    """,
    ("Learn FastAPI", "completed")
)

cursor.execute("SELECT * FROM tasks")
rows = cursor.fetchall()
print("All tasks - ")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM tasks where status=?",("pending",))
rows = cursor.fetchall()
print("Pending tasks - ")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
rows = cursor.fetchall()
print("Tasks in descending id order - ")
for row in rows:
    print(row)

connection.commit()
connection.close()