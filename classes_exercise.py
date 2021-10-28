# classes_exercise.py
# Instructions
"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:

Attributes/properties:
 name: str
 max_speed: int
 capacity: int

Methods:
   vroom() -> None
       Prints "Vroom" max_speed times

2. Create variables for a child/subclass of Vehicle called Bus with the following methods:

Methods:
   fare(age: float) -> None
       Prints "The fare of the bus ride is {}."
           Price depends on age:
               0-17 years - Free
               18-60 years - $5
               61+ years - Free
"""



import math

class Vehicle:
    """Represents vehicle

    Attributes/properties:
        name: str
        max_speed: int
        capacity: int
    """
    def __init__(self):
        """Creates a new shape with default values."""
        self.max_speed = 100
        self.capacity = 4

    def vroom(self) -> None:
        """Return nothing."""
        for vroom in range(self.max_speed):
            print("Vroom")


class Vehicle:
    """Represents a vehicle
    Attributes:
        name: name of the vehicle
        max_speed: maximum speed in km/h
        capacity: how many people it can hold
    """
    def __init__(self):
        self.name = ""
        self.max_speed = 0
        self.capacity = 0

    def vroom(self) -> None:
        """Vehicle goes vroom multipled by the
        amount of speed times"""

        print("Vroom" * self.max_speed)


class Bus(Vehicle):
    """Bus is a Vehicle that can drive
    humans around in it"""
    def fare(self, age: int) -> None:
        """Tells how much fare is for a particular age"""
        if 18 <= age <= 60:
            print("The fare of this bus ride is $5.00. 🚌")
        else:
            print("You ride free!~ 🚌")


a_vehicle = Vehicle()
a_vehicle.name = "La Ferrari"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_vehicle.vroom()

a_bus = Bus()
a_bus.name = "Tranlink Bus - 407"
a_bus.capacity = 35
a_bus.max_speed = 140
a_bus.vroom()
a_bus.fare(10)
print()
a_bus.fare(-1)
a_bus.fare(0)
a_bus.fare(17)
a_bus.fare(18)
a_bus.fare(60)
a_bus.fare(61)













