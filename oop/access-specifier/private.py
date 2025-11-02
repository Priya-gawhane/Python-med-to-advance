'''Private Members (name mangling: double underscore __)

 Python internally renames it to _ClassName__attribute,
so it’s harder (but still possible) to access from outside.'''

class Employee:
    def __init__(self, name, salary):
        self.__salary = salary   # private attribute

emp = Employee("Priya", 50000)
# print(emp.__salary)   .. AttributeError

# You can still access it with name mangling:
print(emp._Employee__salary)  
