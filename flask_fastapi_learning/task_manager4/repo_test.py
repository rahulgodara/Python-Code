from database import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()

"""checking the dab file location and foreign key"""
# cursor.execute("PRAGMA database_list")
# print(cursor.fetchall())
# cursor.execute("PRAGMA foreign_keys")
# print(cursor.fetchone())

"""Creating task_history table"""
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS task_history (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         task_id INTEGER NOT NULL,
#         old_status TEXT NOT NULL,
#         new_status TEXT NOT NULL,
#         FOREIGN KEY (task_id) REFERENCES tasks(id)
#     )
# """)
# connection.commit()

"""Checking if table exist"""
# cursor.execute("PRAGMA table_info(task_history)")
# print(cursor.fetchall())
# cursor.execute("PRAGMA foreign_key_list(task_history)")
# print(cursor.fetchall())

"""adding records in task_history table and checking result"""
# cursor.executemany(
#     """
#     INSERT INTO task_history (task_id, old_status, new_status)
#     VALUES (?, ?, ?)
#     """,
#     [
#         (1, "pending", "in_progress"),
#         (1, "in_progress", "completed")
#     ]
# )

# connection.commit()

# cursor.execute("select * from task_history")
# rows = cursor.fetchall()
# for row in rows:
#     print(row[0],row[1],row[2],row[3])

"""Checking inner join and left join"""
cursor.execute("SELECT t.id, t.title, t.status, h.old_status, h.new_status FROM tasks t " \
"INNER JOIN task_history h ON t.id = h.task_id")
result1 = cursor.fetchall()
print(result1)
cursor.execute("SELECT t.id, t.title, t.status, h.old_status, h.new_status FROM tasks t " \
"Left JOIN task_history h ON t.id = h.task_id")
result2 = cursor.fetchall()
print(result2)

connection.close()