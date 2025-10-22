#Replace an Element Using Index

fruits = ["apple", "banana", "strawberry", "jackfruit", "lime"]

for i, fruit in enumerate(fruits):
    if fruit == "banana":
        fruits[i] = "mango"
    print(fruits)