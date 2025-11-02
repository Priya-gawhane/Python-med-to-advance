# 1. Instance Methods (Regular Methods)
# These are the most common methods. They work with instance data (specific object data).
# Characteristics:

# First parameter is always self
# Can access and modify instance attributes
# Can access class attributes
# Called on objects (instances)

class Student:
    school_name = "ABC School"  # Class attribute
    
    def __init__(self, name, age, grade):
        self.name = name      # Instance attributes
        self.age = age
        self.grade = grade
    
    # Instance method
    def display_info(self):
        return f"{self.name}, Age: {self.age}, Grade: {self.grade}"
    
    # Instance method that modifies data
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"Grade updated to {self.grade}"
    
    # Instance method accessing class attribute
    def get_school(self):
        return f"{self.name} studies at {self.school_name}"

# Usage
student1 = Student("Alice", 15, "A")
print(student1.display_info())      # Output: Alice, Age: 15, Grade: A
print(student1.update_grade("A+"))  # Output: Grade updated to A+
print(student1.get_school())        # Output: Alice studies at ABC School