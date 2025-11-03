'''A property decorator in Python is a built-in decorator that allows
 you to define methods that can be accessed like attributes, while
   providing control over getting, setting, and deleting values.'''

# Method 2: Using @property Decorator (Pythonic Way)
# Makes methods look like attributes but with validation!

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #getter for name
    @property
    def name(self):
        return self.__name
    
    #getter for age
    @property
    def age(self):
        return self.__age
    
    #setter for 
    @age.setter
    def age(self, value):
        if 0 < value or value > 150:
            self.__age = value
        else:
            raise ValueError("invalid age")
        
person = Person('Alice', 25)
print(person.name)
print(person.age)

person.age = 30
print(person.age)