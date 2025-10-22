#Print the index and word only if the word’s length > 5.

fruits = ["apple", "banana", "strawberry", "jackfruit", "lime"]

for i, fruit in enumerate(fruits):
    if len(fruit) > 5:
        print(i, fruit)