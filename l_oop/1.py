class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(150, 10)
# print(modelX)
print(modelX.max_speed, modelX.mileage)
