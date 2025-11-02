# 2. Class Methods
# Work with class data (shared across all instances). Use @classmethod decorator.
# Characteristics:

# First parameter is cls (refers to the class)
# Can access and modify class attributes
# Cannot access instance attributes directly
# Can be called on class or instances
# Often used for alternative constructors (factory methods)

class Employee:
    company = 'priz'
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    #class method access class data
    @classmethod
    def get_company(cls):
        return cls.company
    
    #class emthod - modify class data

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    #class method - alternative constructor(factory method)

    @classmethod
    def fromstr(cls, str):
        name, salary = str.split('-')
        return cls(name, int(salary))
    
    #class method - get statistics
    @classmethod
    def get_total(cls):
        return f"total employees {cls.total_employees}"
    
print(Employee.get_company())

# Using alternative constructor
emp1 = Employee.fromstr("John-50000")
emp2 = Employee.fromstr("Sarah-60000")

print(Employee.get_total())

# Change company name for ALL employees
Employee.change_company("NewTech")
print(Employee.get_company())

