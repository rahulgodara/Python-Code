from student_app_new.student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.show()

    def update_student(self, name, new_marks):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.marks = int(new_marks)
                print(f"Marks updated for {student.name}.")
                return True

        print("Student not found.")
        return False

    def delete_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"Student {student.name} removed successfully.")
                return True

        print("Student not found.")
        return False

    def search_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                student.show()
                return student

        print("Student not found.")
        return None

    def save_to_file(self, file_path):
        with open(file_path, "w") as file:
            for student in self.students:
                file.write(f"{student.name}|{student.marks}\n")
        print("Successfully written to file.")

    def load_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                self.students = []
                for line in file:
                    line = line.strip()
                    if not line or "|" not in line:
                        continue
                    self.students.append(Student.from_line(line))
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved student file found.")

