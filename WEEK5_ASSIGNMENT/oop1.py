class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Function to demonstrate polymorphism
def vehicle_action(vehicle):
    vehicle.move()

# Create instances
vehicles = [Car(), Plane(), Boat()]

# Use polymorphism
for v in vehicles:
    vehicle_action(v)
