import os
import sys

if __package__ is None or __package__ == "":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from student_app_new.student import Student
    from student_app_new.student_manager import StudentManager
else:
    from .student import Student
    from .student_manager import StudentManager


def main():
    manager = StudentManager()
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.txt")

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Save to file")
        print("4. Update student marks")
        print("5. Delete student")
        print("6. Search student")
        print("7. Load from file")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name of student: ").strip()
            marks = int(input(f"Enter marks for {name}: "))
            manager.add_student(Student(name, marks))

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            manager.save_to_file(file_path)

        elif choice == "4":
            name = input("Enter student name to update: ").strip()
            new_marks = int(input("Enter new marks: "))
            manager.update_student(name, new_marks)

        elif choice == "5":
            name = input("Enter student name to delete: ").strip()
            manager.delete_student(name)

        elif choice == "6":
            name = input("Enter student name to search: ").strip()
            manager.search_student(name)

        elif choice == "7":
            manager.load_from_file(file_path)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

