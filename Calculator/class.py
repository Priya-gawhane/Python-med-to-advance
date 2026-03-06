#building a calculator using class function
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero")
        return a / b
    
calc = Calculator()

num1 = float(input("Enter 1st no:"))
num2 = float(input("Enter 2nd no:"))

print("Addition:", calc.add(num1, num2))
print("Subtraction:", calc.subtract(num1, num2))