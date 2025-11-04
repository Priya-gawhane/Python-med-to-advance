#Hybrid Inheritance
#Multiple child classes inherit from the same parent class.

class A:
    def a(self):
        print('method a')

class B(A):
    def b(self):
        print('method b')

class C(A):
    def c(self):
        print('method c')
class D(B, C):
    def d(self):
        print('method d')

obj = D()
obj.a()