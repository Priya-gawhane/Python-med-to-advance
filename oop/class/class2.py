#Method using self

class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")

dog1 = Dog("Tommy")
dog2 = Dog("blackie")
dog1.bark()
dog2.bark()