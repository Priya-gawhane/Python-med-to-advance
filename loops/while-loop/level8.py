#Sum the digit 1234 = 10

n = int(input("Enter a no:"))

i = 0

while n > 0:
    digit = n % 10
    i += digit
    n //= 10

print(i)