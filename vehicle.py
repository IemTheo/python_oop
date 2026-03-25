class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print("Vehicle is starting")
    
    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def __init__(self, make, model, year, number_doors, number_wheels):
        super().__init__(make, model, year)
        self.number_doors = number_doors
        self.number_wheels = number_wheels

class Bike(Vehicle):
    def __init__(self, make, model, year,number_wheels):
        super().__init__(make, model, year)
        self.number_wheels = number_wheels

car = Car("Ford", "Focus", 2020, 5, 4)

bike = Bike("Honda", "Scoopy", 2024, 2)

print(car.__dict__)
print(bike.__dict__)