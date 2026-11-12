def add_student():
    name = input("Enter name of student: ")
    marks = int(input("Enter marks: "))
    student = {
        "name": name,
        "marks": marks
    }
    students.append(student)
    print(f"Student {name} added successfully.")


def view_students():
    if not students:
        print("No students found.")
    else:
        for stu in students:
            print(f"Name: {stu['name']}, Marks: {stu['marks']}")


def save_to_file():
    with open("E://python//Students1.txt", "w") as file:
        for stu in students:
            file.write(f"{stu['name']}|{stu['marks']}\n")
        print("Successfully written to file.")

def update_student():
    name = input("Enter student name to update: ").strip()
    for stu in students:
        if stu['name'].lower() == name.lower():
            new_marks = int(input("Enter new marks: "))
            stu['marks']= new_marks
            print(f"Marks updated for {name}")
            return
    print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    for stu in students:
        if stu['name'].lower() == name.lower():
            students.remove(stu)
            print(f"Student {name} removed successfully.")
            return
    print("Invalid student name")
  
def search_student():
    name = input("Enter student name to search: ").strip()

    for stu in students:
        if stu['name'].lower() == name.lower():
            print(f"Name: {stu['name']}, Marks: {stu['marks']}")
            return
    
    print("Student not found.")

def load_from_file():
    global students
    try:
        with open("E://python//Students1.txt", "r") as file:
            students = []
            for line in file:
                student = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) != 2:
                    continue

                name, marks = parts
                students.append({
                    "name": name,
                    "marks": int(marks)
                })
            print("Data load successful.")
    except FileNotFoundError:
        print("No saved student found.")


students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Save to file")
    print("4. Update student marks")
    print("5. delete student by name")
    print("6. Search student")
    print("7. Load from file")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        save_to_file()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        search_student()
    elif choice == '7':
        load_from_file()
    elif choice == '8':
        break
    else:
        print("Invalid choice")