class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Vehicle):
    pass

School_Bus = Bus("School volvo", 180, 12)
print("Vehicle name:", School_Bus.name, "speed:", School_Bus.max_speed, "mileage:", School_Bus.mileage)
    
    
# Vehicle Name: School Volvo Speed: 180 Mileage: 12