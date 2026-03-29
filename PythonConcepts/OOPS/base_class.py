"""
This module illustrates the concept of a base class in Python.

A base class (also known as a parent class or superclass) defines
general attributes and methods that can be inherited by one or more
subclasses. Using base classes promotes code reuse and enables
polymorphism.

Example:
    class Animal:
        def __init__(self, name):
            self.name = name

        def speak(self):
            raise NotImplementedError("Subclasses must implement speak()")

    class Dog(Animal):
        def speak(self):
            return f"{self.name} says woof!"

    class Cat(Animal):
        def speak(self):
            return f"{self.name} says meow!"

Usage:
    dog = Dog("Rex")
    print(dog.speak())  # "Rex says woof!"

    cat = Cat("Whiskers")
    print(cat.speak())  # "Whiskers says meow!"

The `Animal` class provides a template that ensures all subclasses implement
`speak()`, demonstrating the base class concept and inheritance.
"""

# define the base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Subclasses should override this method."""
        raise NotImplementedError("Subclasses must implement speak()")

# subclasses demonstrate inheritance from the base class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# demonstration code when run as a script
if __name__ == "__main__":
    animals = [Dog("Rex"), Cat("Whiskers")]
    for a in animals:
        print(a.speak())
