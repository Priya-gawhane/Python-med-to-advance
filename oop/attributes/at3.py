#Accessing and modifying the attributes

class Person:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def introduce(self):
        # accessing attribute inside method using self
        return f"Ho!, I am {self.name} and I am {self.age} years old"
    
person = Person('alice', 30)

#Accessing attribute
print(person.name)

#Modifying age 
person.age = 35
print(person.age)

#calling method that uses attribute
print(person.introduce())