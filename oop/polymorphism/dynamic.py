#what is dynamic typing

#
#Dynamic typing is when a programming language determines variable types at runtime (when the code executes) rather than at compile time.

"""No type declarations needed - you don't specify what type a variable is
Variables can change types - the same variable can hold different types
Type checking happens during execution - errors show up when the code runs"""

# Example 2: Same variable, different operations
x = 10
result = x + 5  # Works: 15

x = "Python"
result = x + " rocks"  # Works: "Python rocks"

x = [1, 2]
result = x + [3, 4]  # Works: [1, 2, 3, 4]

# Python figures out what '+' means based on the OBJECT's type at runtime
print(x)
print(result)