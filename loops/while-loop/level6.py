#count digits in a number

n = int(input("enter a no:"))
i = 0

while n > 0:
    n //= 10
    i += 1
print(i)