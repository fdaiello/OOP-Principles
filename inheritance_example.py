# Inheritance Example
# A mechanism that allows a new class (subclass) to inherit properties and behaviors
# from an existing class (superclass), promoting code reusability.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} ({self.breed}) barks!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        return f"{self.name} ({self.color} cat) meows!"

# Usage
my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "black")

print(my_dog.speak())
print(my_dog.eat())

print(my_cat.speak())
print(my_cat.eat())

# Demonstrating inheritance hierarchy
print(f"Is my_dog an instance of Dog? {isinstance(my_dog, Dog)}")
print(f"Is my_dog an instance of Animal? {isinstance(my_dog, Animal)}")
print(f"Is my_cat an instance of Cat? {isinstance(my_cat, Cat)}")
print(f"Is my_cat an instance of Animal? {isinstance(my_cat, Animal)}")


