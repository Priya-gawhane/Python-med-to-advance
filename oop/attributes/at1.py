#Instance attribute

#These belong to a specific instance (object) of a class. Each object has its own copy.

class Dog:
    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute

dog1 = Dog('bunny', 22)
dog2 = Dog('tom', 12)

print(dog1.name)
print(dog2.age)