#Reverse a number 1234 -> 4321

n = int(input("enter a no:"))

i = 0

while n > 0:
    digit = n % 10
    i = i * 10 + digit
    n //= 10

print(i)