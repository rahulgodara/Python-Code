from flask import Flask, request

app = Flask(__name__)

employees = [
    {"name":"Rahul", "department":"IT", "Salary": 10000},
    {"name":"Name", "department":"IT", "Salary": 20000},
    {"name":"Name2", "department":"HR", "Salary": 30000}
]

@app.route("/products/<int:product_id>")
def get_product(product_id):
    return {
        "product_id":product_id,
        "message":"Product details"
    }

@app.route("/employees", methods=["GET"])
def get_employees():
    department = request.args.get("department")
    name = request.args.get("name")
    if department:
        filtered_employees = [
            employee for employee in employees
            if employee["department"].strip().lower() == department.strip().lower()
        ]
        
    if name:
        filtered_employees = [
            employee for employee in employees
            if employee["name"].strip().lower() == name.strip().lower()
        ]

    return  {
        "employee": filtered_employees
    }

@app.route("/employees", methods=["POST"])
def create_employees():
    data = request.get_json(silent=True)
    if not data:
        return {
            "error": "Invalid JSON"
        },400
    name = data.get("name")
    if not name:
        return {"error": "Name is required"},400
    department = data.get("department")
    if not department:
        return {"error": "department is required"},400
    salary = data.get("salary")
    new_employee = {
        "name":name,
        "department":department,
        "salary": salary
    }

    employees.append(new_employee)

    return {
        "message":"New employee added",
        "name":name
    },201


if __name__ =="__main__":
    app.run(debug=True)