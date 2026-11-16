from ..database import get_db_connection

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

def delete_task_by_id(task_id):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id=? RETURNING *",
            (task_id,)
        )
        task = cursor.fetchone()
        if task is None:
            return None

        connection.commit()
        
        return {
            "id": task[0],
            "title": task[1],
            "status": task[2]
        }

    finally:
        connection.close()

def update_task_with_history(task_id, new_status):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        cursor.execute(
            "select status from tasks where id=?",
            (task_id,)
        )
        task = cursor.fetchone()

        # Check whether task exists
        if task is None:
            return None

        old_status = task[0]

        cursor.execute(
            "UPDATE tasks SET status=? WHERE id=?",
            (new_status, task_id)
        )

        cursor.execute(
            "INSERT INTO task_history (task_id, old_status, new_status) VALUES (?, ?, ?)",
            (task_id, old_status, new_status)
        )
        
        connection.commit()

        return True
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()

def get_task_history_repo(task_id):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT t.id, t.title, t.status, h.id AS history_id, h.old_status, h.new_status " \
            "FROM tasks t LEFT JOIN task_history h ON t.id = h.task_id WHERE t.id = ? ORDER BY h.id ",
            (task_id,)
        )
        rows = cursor.fetchall()

        if not rows:
            return None
        
        history = []
        for row in rows:
            if row[3] is not None:
                history.append({
                    "history_id": row[3],
                    "old_status": row[4],
                    "new_status": row[5]
                })
        
        row = rows[0]
        
        return{
            "id": row[0],
            "title": row[1],
            "status": row[2],
            "history": history
        }
    finally:
        connection.close()
