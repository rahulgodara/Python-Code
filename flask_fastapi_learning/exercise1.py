from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page for my application"

@app.route("/about")
def about():
    return "We are learning Flask here"

@app.route("/tasks", methods=["GET"])
def tasks():
    tasks = [
        {"id": 1, "Name": "Tasks1"},
        {"id": 2, "Name": "Tasks2"},
        {"id": 3, "Name": "Tasks3"}
    ]
    return {
        "tasks": tasks
    }

@app.route("/add_numbers", methods=["POST"])
def add_numbers():
    data = request.get_json()
    total = 0
    for value in data.values():
        total += value

    return {
        "result" : total
    }


if __name__ == "__main__":
    app.run(debug=True)