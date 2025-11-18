'''*args and **kwargs in Python
They let you pass a variable number of arguments to a function.

*args - Non-keyword arguments (positional)
Collects extra positional arguments into a tuple'''

def add_number(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    return total

print(add_number(1, 3))
print(add_number(1, 3, 5, 7, 9, 11))
print(add_number(3, 5, 7))
print(add_number(10))

# Example 2: Mixing normal params with *args
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")