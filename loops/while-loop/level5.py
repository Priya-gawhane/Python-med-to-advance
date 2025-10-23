#Find factorial of a number

n = int(input("enter a no:"))

i = 1
j = 1

while i <= n:
    j *= i
    i += 1
    
print(j)