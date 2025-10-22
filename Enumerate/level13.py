#Enumerate Dictionary Keys

info = {"name": "Alice", "age": 25, "city": "Paris"}

for i, (key, value) in enumerate(info.items()):
    print(i, key, value)


# info.items() → gives key-value pairs: ("name", "Alice"), ("age", 25), ("city", "Paris")

# enumerate(info.items()) → gives (index, (key, value))

# i, (key, value) → unpacks the index and the key-value tuple

# print(i, key) → prints index and key only