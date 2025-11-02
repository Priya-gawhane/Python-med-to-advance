#Print all prime numbers between 1 and 50 using loops.
for n in range(1, 51):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)