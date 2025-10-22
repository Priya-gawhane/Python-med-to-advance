#Print the same fruits but start the index from 1 instead of 0.

fruits = ["apple", "banana", "strawberry", "jackfruit", "lime"]

for i, fruit in enumerate(fruits, start = 1):
    print(i, fruit)
    