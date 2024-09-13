class Vehicle:
    def __init__(self,seating_capacity):
        self.seating_capacity = seating_capacity
        
    def fare(self):
        return self.seating_capacity*100
    
class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare() #calculating fare on base class implementation
        final_fare = total_fare + (total_fare*0.10)
        return final_fare
    
vehicle = Vehicle(50)
print(f"fare of the vehicle is {vehicle.fare()}")
bus = Bus(50)
print(f"the fare of the bus is {bus.fare()}")
