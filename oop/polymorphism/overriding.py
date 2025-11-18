# What is Method Overriding?

# Method overriding happens when a child class defines a method with the same name 
# and same parameters as its parent class — but changes its behavior.

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):   # overriding the parent's sound()
        print("Bark")

d = Dog() #calling child clas obj
d.sound()
