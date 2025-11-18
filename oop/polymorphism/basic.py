# What is Polymorphism?

# Polymorphism means: same function name, 
# but different behavior depending on the object.

class Dog:
    def sound(self):
        return "Bark"
    
class Cat:
    def sound(self):
        return "cat"
    
for animal in [Dog(), Cat()]:
    print(animal.sound())