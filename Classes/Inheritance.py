class Person:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s = Student("Rahul", 90)
s.intro()
s.show()