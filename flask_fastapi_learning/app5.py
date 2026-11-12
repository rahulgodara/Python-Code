from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    connection = sqlite3.connect("tasks.db")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        
        tasks = []
        for row in rows:
            tasks.append({
                "id": row[0],
                "title": row[1],
                "status": row[2]
            })
        return {
            "tasks": tasks
        }
    finally:
        connection.close()
    

if __name__== "__main__":
    app.run(debug=True)