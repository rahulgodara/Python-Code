"""
Create a program that:
asks for student name and marks
stores them in a list/dictionary
saves to a file
reads them back later
"""
students = []

while True:
    name = input("Enter name of student or enter exit to stop : ")
    if(name.lower() == 'exit'):
        break
    
    try:
        marks = int(input("Enter marks:"))
    except ValueError:
        print("Please enter valid number.")
        continue
    
    student = {
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    
print(students)

with open("E:\\Python\\Students.txt", "w") as file:
    for stu in students:
        file.write(f"Name: {stu['name']}, Marks: {stu['marks']}\n")
        file.write(f"{stu['name']}|{stu['marks']}\n")


try:
    with open("E:\\Python\\Students.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Mentioned file not found")


try:
    with open("E:\\Python\\Students.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, marks = line.split("|")
            print(f"Name: {name}, Marks: {marks}")
except FileNotFoundError:
    print("Mentioned file not found")
