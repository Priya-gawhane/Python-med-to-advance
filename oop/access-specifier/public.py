# Python does not have traditional access specifiers like public, private, and protected as in Java or C++.

# But — Python uses naming conventions to indicate the level of access
''''public members 

Accessible everywhere (inside or outside the class)'''

class Employee:
    def __init__(self, name, salary):
        self.name = name           # public attribute
        self.salary = salary       # public attribute

emp = Employee("Priya", 50000)
print(emp.name)    
print(emp.salary) 