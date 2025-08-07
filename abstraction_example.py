# Abstraction Example
# Hiding complex implementation details and showing only the essential features.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_info(self):
        # This method is concrete, but relies on abstract methods
        print(f"This is a shape. Area: {self.area()}, Perimeter: {self.perimeter()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Usage
circle = Circle(5)
print("Circle details:")
circle.display_info()

rectangle = Rectangle(4, 6)
print("\nRectangle details:")
rectangle.display_info()

# This would raise a TypeError because Shape is an abstract class
# generic_shape = Shape()


