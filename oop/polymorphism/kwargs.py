'''**kwargs - Keyword arguments
Collects extra keyword arguments into a dictionary.'''

def print_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name = "alice", city = "nyc", age = 34)

# Example 4: Mixing normal params with **kwargs
def create_profile(username, **details):
    print(f"Username: {username}")
    print("Other details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_profile("john123", age=30, email="john@email.com", country="USA")
