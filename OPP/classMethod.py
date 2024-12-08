# Implement a class Student with attributes for name, marks, and grade. Include methods to display student details.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.calculateGrade()

    def calculateGrade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    def displayDetails(self):
        print(f"Name: {self.name}\nMarks: {self.marks}\nGrade: {self.grade}")
