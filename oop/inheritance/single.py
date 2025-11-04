# A single level inheritance 
# A child class inherits from one parent class.

class Parent:
    def parent_method(self):
        print("This is a parent method")

class Child(Parent):
    def child_method(self):
        print("This is a child method")

obj = Child()
obj.parent_method()
obj.child_method()