# Polymorphism Example
# The ability of different objects to respond to the same method call in their own unique ways.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        return "Vehicle moves."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def move(self):
        return f"The {self.brand} {self.model} drives on the road."

class Boat(Vehicle):
    def __init__(self, brand, name):
        super().__init__(brand)
        self.name = name

    def move(self):
        return f"The {self.brand} {self.name} sails on the water."

class Plane(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def move(self):
        return f"The {self.brand} {self.type} flies in the air."

# Function demonstrating polymorphism
def make_it_move(vehicle):
    print(vehicle.move())

# Usage
car = Car("Toyota", "Camry")
boat = Boat("Sea Ray", "Sundancer")
plane = Plane("Boeing", "747")

make_it_move(car)
make_it_move(boat)
make_it_move(plane)

# Another example of polymorphism: operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(f"Point addition: {p3}")


