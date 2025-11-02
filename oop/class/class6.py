#  Student Grade Calculator (Easy)
# Create a Student class with:

# Attributes: name, marks (list of marks)
# Methods:

# add_mark(mark) - adds a mark to the list
# calculate_average() - returns average of all marks
# get_grade() - returns grade based on average (A: >90, B: >80, C: >70, D: >60, F: ≤60)

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)
        print(f"Added marks{mark} current marks{self.marks}")

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        total = sum(self.marks)
        average = total / len(self.marks)
        return average

    def get_grade(self):
        avg = self.calculate_average()
        
        if avg > 90:
            return 'A'
        elif avg > 80:
            return 'B'
        elif avg > 70:
            return 'C'
        elif avg > 60:
            return 'D'
        else:
            return 'fail'
        
student1 = Student("Alice")

student1.add_mark(88)
student1.add_mark(76)
student1.add_mark(56)
student1.add_mark(30)

average = student1.calculate_average()
print(f"student name {student1.name} the aveg is {average}")

grade = student1.get_grade()
print(f"student{student1.name} the grade is {grade}")
