#Convert every element at an odd index to uppercase

fruits = ["apple", "banana", "strawberry", "jackfruit", "lime"]

for i, fruit in enumerate(fruits):
    if i % 2 == 1:
        fruits[i] = fruit.upper()
print(fruits)