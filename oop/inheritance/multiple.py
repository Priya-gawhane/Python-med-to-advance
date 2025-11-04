#Multiple Inheritance
#A child class inherits from multiple parent classes
class Father:
    def skills(self):
        print('programming, gardening')

class Mother:
    def skills(self):
        print('cooking, singing')

class Child(Father, Mother):
    def child_skills(self):
        print('gaming')

obj = Child()
obj.skills() #calls father method resolution order