class Student:
    def __init__(self, name, marks):
        self.name = name.strip()
        self.marks = int(marks)

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    @classmethod
    def from_line(cls, line):
        name, marks = line.strip().split("|")
        return cls(name, marks)

