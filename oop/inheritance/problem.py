#  Vehicle Management System
# Create a base class Vehicle with attributes like brand, model, and year. 
# Create child classes Car and Motorcycle that inherit from Vehicle and add their specific attributes
# (e.g., num_doors for Car, engine_type for Motorcycle).
#  Implement methods to display vehicle information.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"brand {self.brand}")
        print(f"model{self.model}")
        print(f"year{self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_type):
        super().__init__(brand, model, year)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")

car1 = Car("Toyota", "Camry", 2022, 4)
bike1 = Motorcycle("Yamaha", "R15", 2021, "Petrol")

print("Car Details:")
car1.display_info()

print("\nMotorcycle Details:")
bike1.display_info()