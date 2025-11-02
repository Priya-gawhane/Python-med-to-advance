""""Write a program that finds the largest individual digit in a number.

input : 268937
op: 9 """
n = int(input("Enter a number: "))
i = 0
j = n 

while n > 0:
    digit = n % 10
    if digit > i:
        i = digit
    n //= 10

print(f"The largest individual digit in {j} is: {i}")

