# Base Class: Vehicle
class Vehicle:
    def move(self):
        """
        Abstract move method to be overridden by subclasses.
        """
        raise NotImplementedError("This method should be overridden in subclasses.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗."

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️."

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water ⛵."

# Demonstration of Polymorphism
def demonstrate_movement(vehicle):
    """
    Show how different vehicles move.
    :param vehicle: An instance of a Vehicle subclass.
    """
    print(vehicle.move())

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphic behavior
demonstrate_movement(car)
demonstrate_movement(plane)
demonstrate_movement(boat)
