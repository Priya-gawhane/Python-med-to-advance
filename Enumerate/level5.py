#Print elements that are at even index positions only

fruits = ["apple", "banana", "strawberry", "jackfruit", "lime"]

for i, fruit in enumerate(fruits):
    if i % 2 == 0:
        print(i, fruit)