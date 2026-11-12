from student_app.student import Student
from student_app.student_manager import StudentManager

manager = StudentManager()
s = Student("Rahul", 90)
manager.add_student(s)

for student in manager.students:
    student.show()