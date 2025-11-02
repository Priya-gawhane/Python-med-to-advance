#Creating multiple objects

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("Toyota", "Red")

print(car.brand)  
print(car.color)  

print(getattr(car, 'brand'))  

if hasattr(car, 'brand'):
    print("Car has brand attribute")

setattr(car, 'year', 2024)
print(car.year)  