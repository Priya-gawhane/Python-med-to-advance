# 3. Static Methods
# Independent utility methods that don't need access to instance or class data. Use @staticmethod decorator.
# Characteristics:

# No self or cls parameter
# Cannot access instance or class attributes
# Behave like regular functions but belong to the class
# Used for utility/helper functions related to the class
# Can be called on class or instances

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def is_positive(num):
        return num > 0
    
    @staticmethod
    def validate_age(age):
        if age < 0 or age > 150:
            return False
        return True
    

print(Calculator.add(8, 9))
print(Calculator.is_positive(-5))     
print(Calculator.validate_age(25))    

calc = Calculator()
print(calc.add(10, 20))              
