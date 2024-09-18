class Vehicle:
    def __init__(self, seating_cap):
        self.seating_cap = seating_cap

    def fare(self):
        return self.seating_cap * 100

class Bus(Vehicle):
    def __init__(self, seating_cap):
        super().__init__(seating_cap)

    def fare(self):
        x = super().fare()
        return x + (x * 0.10)

car = Vehicle(4)
print(f"The fare for the car is {car.fare()}")

bus = Bus(4)
print(f"The fare for the bus is {bus.fare()}")
