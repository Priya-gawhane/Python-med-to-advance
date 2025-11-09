#if you used super(), the child class will automatically adapt

class A:
    def __init__(self):
        print("A init called")

    def show(self):
        print("A show called")

class B(A):
    def __init__(self):
        super().__init__() #call A's constructor
        print("B init called")

    def show(self):
        super().show()     #call A's constructor 
        print("B show called")

obj = B()
obj.show()
    