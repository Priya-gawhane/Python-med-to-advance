# Parent/Base/Super Class: The class being inherited from
# Child/Derived/Sub Class: The class that inherits from the parent

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return 'some sound'
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"
    
dog = Dog('Buddy')
cat = Cat('meowdy')

print(dog.speak())
print(cat.speak())
