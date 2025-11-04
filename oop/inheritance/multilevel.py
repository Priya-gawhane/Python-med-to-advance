#Multilevel Inheritance
#A chain of inheritance where a class inherits from a child class.

class Grandparent:
    def grandparent(self):
        print('grandparent method')

class Parent(Grandparent):
    def parent(self):
        print('parent method')

class Child(Parent):
    def child(self):
        print('child method')

obj = Child()
obj.grandparent() 