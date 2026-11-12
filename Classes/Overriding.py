class Person:
    def intro(self):
        print("I am a person")

class Student(Person):
    def intro(self):
        print("I am a student")


s = Student()
s.intro()
Person().intro()
Student().intro()