student = {"first_name": "John","last_name": "Doe", "age": 25}
print(student["first_name"])

student["age"] = 27

print(student)

car = {"make":"Maruti", "model": "Alto", "year": 2015}
print(car["year"])

for key,value in student.items():
    print(key, value)