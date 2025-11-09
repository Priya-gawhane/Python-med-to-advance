# 3. Shape Calculator
# Create a base class Shape with a method area().
# Create child classes Rectangle, Circle, and Triangle that inherit
# from Shape and implement their own area() calculation methods.

import math

class Shape:
    def area(self):
        pass  # abstract placeholder (to be overridden)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

rect = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(6, 8)

print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())
print("Triangle Area:", triangle.area())
