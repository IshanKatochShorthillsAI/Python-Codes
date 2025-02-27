"""
This module demonstrates polymorphism in Python.

It defines a base class Polygon with a render method, and two derived classes
Square and Circle that override the render method.
"""


class Polygon:
    def render(self):
        """
        Prints a default message for rendering a polygon.

        Expected output: Rendering Polygon
        """
        print("Rendering Polygon")  # Expected output: Rendering Polygon


class Square(Polygon):
    def render(self):
        """
        Prints a message for rendering a square.

        Expected output: Rendering Square
        """
        print("Rendering Square")  # Expected output: Rendering Square


class Circle(Polygon):
    def render(self):
        """
        Prints a message for rendering a circle.

        Expected output: Rendering Circle
        """
        print("Rendering Circle")  # Expected output: Rendering Circle


# Create objects of derived classes and call their render method
s1 = Square()
s1.render()  # Expected output: Rendering Square

c1 = Circle()
c1.render()  # Expected output: Rendering Circle
