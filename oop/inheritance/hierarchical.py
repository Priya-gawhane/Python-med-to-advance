#Hierarchical Inheritance
#Multiple child classes inherit from the same parent class.

class Parent:
    def parent_method(self):
        print('parent method')

class Child1(Parent):
    def child1_method(self):
        print('child1 method')

class Child2(Parent):
    def child2_method(self):
        print('child2 method')

obj = Child1()
obj1 = Child2()
obj.parent_method()