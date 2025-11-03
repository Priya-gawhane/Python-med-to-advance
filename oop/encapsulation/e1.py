'''Encapsulation is the concept of bundling data (attributes) and methods together in a class, and restricting direct access to some of the object's components. It's about hiding internal details and exposing only what's necessary.
Two Main Ideas:

Data Hiding - Hide internal data from outside access
Data Bundling - Group related data and methods together


Why Encapsulation?
✅ Protects data from accidental modification
✅ Hides complexity - users don't need to know internal details
✅ Easier to maintain - can change internal implementation without affecting external code
✅ Controlled access - validate data before modification

Access Modifiers in Python
Python doesn't have true "private" attributes like other languages, but uses naming conventions:
TypeSyntaxMeaningAccessPublicnameAccessible everywhereDirect accessProtected_nameInternal use (by convention)Can access but shouldn'tPrivate__nameStrongly hiddenName mangling applied'''

#Regular Method

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    # Setter methods with validation
    def set_name(self, name):
        if name and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name!")
    
    def set_age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            print("Invalid age!")

# Usage
person = Person("Alice", 25)

# Access through getters
print(person.get_name())  
print(person.get_age())   
# Modify through setters (with validation)
person.set_age(30)        #Valid
person.set_age(-5)        #invalid