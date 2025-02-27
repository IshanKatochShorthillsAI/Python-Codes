"""
This module demonstrates basic inheritance in Python.

It defines a base class Animal with common behaviors and a derived class Dog
that inherits from Animal and adds its own behavior.
"""


# Base class definition
class Animal:
    def eat(self):
        """Prints a message indicating that the animal can eat."""
        print("I can eat!")  # Expected output: I can eat!

    def sleep(self):
        """Prints a message indicating that the animal can sleep."""
        print("I can sleep!")  # Expected output: I can sleep!


# Derived class that inherits from Animal
class Dog(Animal):
    def bark(self):
        """Prints a message indicating that the dog can bark."""
        print("I can bark!")  # Expected output: I can bark!


# Create an object of the derived class Dog
dog1 = Dog()

# Calling methods inherited from the Animal base class
dog1.eat()  # Expected output: I can eat!
dog1.sleep()  # Expected output: I can sleep!

# Calling the method defined in the Dog class
dog1.bark()  # Expected output: I can bark!
