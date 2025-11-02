#Multiple methods

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof")

    def eat(self, food):
        print(f"{self.name} eats {food}")

dog1 = Dog("Tommy")

dog1.bark()
dog1.eat("chicken")