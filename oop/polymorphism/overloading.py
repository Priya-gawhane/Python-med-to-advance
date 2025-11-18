# # Overloading = Same method name, different parameters

# # Python supports overloading behavior, but not true overloading like Java.
# Overloading using Default Arguments

class Calculator:
    def sub(self, a, b=0, c=0):
        return a - b - c
    
calc = Calculator()

print(calc.sub(7))
print(calc.sub(10, 5))
print(calc.sub(12, 7, 4))