# Abstract Classes - Classes that cannot be instantiated and are meant to be inherited
# Abstract Methods - Methods declared in abstract classes but have no implementation 
# (subclasses must implement them)

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

    def breathe(self):
        print("breathing")

class Dog(Animal):

    def make_sound(self):
        print("woof woof")

    def move(self):
        print("4 dogs run away")

class Bird(Animal):

    def make_sound(self):
        print("chirp chirp")

    def move(self):
        print("Bird flew away in sky")

dog = Dog()
dog.make_sound()
dog.move()
dog.breathe()