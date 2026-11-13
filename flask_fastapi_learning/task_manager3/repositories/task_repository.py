from database import get_db_connection

def get_task_by_id(task_id):
    connection = get_db_connection()
    
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE id=?",
            (task_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return row_to_task(row)

    finally:
        connection.close()

def get_all_tasks():
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()

        tasks = []

        for row in rows:
            tasks.append(row_to_task(row))

        return tasks

    finally:
        connection.close()

def row_to_task(row):
    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "status": row[2]
    }

def create_task(title, status):
    connection = get_db_connection()
    try:
        title = title.strip()

        cursor = connection.cursor()
        cursor.execute(
            "insert into tasks (title, status) values(?,?)",
            (title, status)
        )
        connection.commit()
        return {
            "id": cursor.lastrowid,
            "title":title,
            "status":status
        }

    finally:
        connection.close()

def delete_task_by_id(task_id):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            return None

        cursor.execute(
            "delete from tasks where id=?",
            (task_id,)
        )
        connection.commit()
        
        return {
            "id": task[0],
            "title": task[1],
            "status": task[2]
        }

    finally:
        connection.close()

def update_task_by_id(task_id, title, status):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            return None
                
        cursor.execute(
            "update tasks set title=?, status=? where id=?",
            (title, status, task_id)
        )
        connection.commit()
        return {
            "id": task_id,
            "title":title,
            "status":status
        }
    finally:
        connection.close()

def patch_task_by_id(task_id, title, status):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            return None

        if title is None:
            title = task[1]

        if status is None:
            status = task[2]

        title = title.strip()
        cursor.execute(
            "update tasks set title=?, status=? where id=?",
            (title, status, task_id)
        )

        connection.commit()
        return {
            "id": task_id,
            "title":title,
            "status":status
        }
    finally:
        connection.close()