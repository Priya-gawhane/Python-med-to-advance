#Sum only even numbers:

i = 1
j = 0

while i < 21:
    if i % 2 == 0:
        j += i
    i += 1
print(j)