#Class attributes

#These are shared by all instances of a class. Defined directly inside the class but outside any methods.

class Dog:
    species = 'goldern retriever' #class attribute

    def __init__(self, name):
        self.name = name #instance attribute

dog1 = Dog('tommy')
print(dog1.species)

