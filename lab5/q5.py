from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
        self._rental_price = rental_price  
        self.available = True

    def is_available(self):
        return self.available

    def calculate_rental_cost(self, days):
        return days * self._rental_price

    def rent(self):
        if self.is_available():
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True

    def display_details(self):
        return f"{self.make} {self.model} - ${self._rental_price}/day - {'Available' if self.available else 'Rented'}"


class Car(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)
        self.vehicle_type = "Car"


class SUV(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)
        self.vehicle_type = "SUV"


class Truck(Vehicle):
    def __init__(self, make, model, rental_price):
        super().__init__(make, model, rental_price)
        self.vehicle_type = "Truck"


class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def rental_duration(self):
        return (self.end_date - self.start_date).days

    def total_cost(self):
        return self.vehicle.calculate_rental_cost(self.rental_duration())

    def display_reservation_details(self):
        return (f"Reservation for {self.customer.name}:\n"
                f"Vehicle: {self.vehicle.display_details()}\n"
                f"Rental Duration: {self.rental_duration()} days\n"
                f"Total Cost: ${self.total_cost():.2f}")


class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self._contact_info = contact_info  
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle, start_date, end_date):
        if vehicle.rent():
            reservation = RentalReservation(self, vehicle, start_date, end_date)
            self.rented_vehicles.append(reservation)
            return reservation
        return None

    def return_vehicle(self, vehicle):
        vehicle.return_vehicle()
        self.rented_vehicles = [r for r in self.rented_vehicles if r.vehicle != vehicle]

    def display_rental_history(self):
        history = "Rental History:\n"
        for reservation in self.rented_vehicles:
            history += reservation.display_reservation_details() + "\n"
        return history


def display_vehicle_details(vehicle):
    print(vehicle.display_details())

def display_reservation_details(reservation):
    print(reservation.display_reservation_details())




car = Car("Toyota", "Corrola", 50)
suv = SUV("Ford", "Raptor", 75)
truck = Truck("Chevrolet", "Camaro", 90)
customer = Customer("Muhammad", "555-1234")
start_date = datetime.now()
end_date = start_date + timedelta(days=3)
reservation = customer.rent_vehicle(car, start_date, end_date)
display_vehicle_details(car)
print(customer.display_rental_history())
if reservation:
    display_reservation_details(reservation)


customer.return_vehicle(car)
display_vehicle_details(car)
