class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# vehicle = Car, Bus("Child Class")

School_bus = Bus("School Volvo", 180, 12)
print("Color:", School_bus.color, ", Vehicle name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print("Color:", car.color, ", Vehicle name:", car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18