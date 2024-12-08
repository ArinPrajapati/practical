# Write a Python program to implement inheritance by defining a base class Vehicle and a derived class Car.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"

# Example usage
vehicle = Vehicle("Toyota", "Corolla", 2020)
print(vehicle.display_info())

car = Car("Honda", "Civic", 2021, 4)
print(car.display_info())