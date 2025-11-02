'''. Protected Members (convention: single underscore _)

🔸 Not enforced — it’s a warning to developers that it’s for internal use.
🔸 You can still access it from outside, but you shouldn’t.'''

class Employee:
    def __init__(self, name, salary):
        self._salary = salary   # protected attribute

emp = Employee("Priya", 50000)
print(emp._salary) 
