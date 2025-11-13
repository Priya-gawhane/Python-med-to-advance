from abc import ABC, abstractmethod

class Shape(ABC):

    """Users need to know: Every shape has an area
       They Dont need to know how we calculate it"""
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):

        result = 3.14 * self.radius ** 2
        return result
    
class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):

        result = self.length * self.breadth
        return result
    
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):

        result = 1/2 * self.base * self.height
        return result
    
def print_area(shape : Shape):

    result = shape.area()
    print(result)
