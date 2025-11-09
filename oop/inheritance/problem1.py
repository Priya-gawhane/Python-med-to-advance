# # 2. Employee Hierarchy
# Design a class Employee with basic attributes like 
# name, employee_id, and salary. 
# Create subclasses Manager and Developer that
#  inherit from Employee and add specific attributes/methods 
# (e.g., team_size for Manager, programming_language for Developer).

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        print(f"name {self.name}")
        print(f"employee {self.employee_id}")
        print(f"salary {self.salary}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"team size{self.team_size}")


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"programming language {self.programming_language}")

employe1 = Employee('alice', 1234, 20000)
manager = Manager('sosy', 12332, 23132, 'large')

employe1.display()

manager.display()