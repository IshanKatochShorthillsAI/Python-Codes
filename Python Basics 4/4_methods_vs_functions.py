"""
Key Points:
- A function is defined at the module level and can be invoked independently.
- A method is defined inside a class; it is bound to the class or its instances.
- Methods require the first parameter (commonly named 'self') to access instance data.
"""


# ---------------------------
# Standalone Function Example
# ---------------------------
def subtract(a, b):
    """
    Subtracts b from a. This is a standalone function.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of a minus b.
    """
    return a - b


# Calling the standalone function:
print("Function 'subtract' outputs:")
print(subtract(10, 4))  # Expected output: 6
print(subtract(5, 7))  # Expected output: -2


# ---------------------------
# Class with Methods Example
# ---------------------------
class MyClass:
    def __init__(self, value):
        """
        Initializes the object with a value.

        Args:
            value (int or float): The initial value.
        """
        self.value = value

    def display_value(self):
        """
        An instance method that prints the stored value.

        The 'self' parameter refers to the instance on which this method is called.
        """
        print("The value is:", self.value)

    def update_value(self, new_value):
        """
        An instance method that updates the stored value.

        Args:
            new_value (int or float): The new value to set.
        """
        self.value = new_value
        print("Updated value to:", self.value)


# Instantiating an object of MyClass:
obj = MyClass(100)

# Invoking methods (note that they are called on the object):
print("\nMethod calls from MyClass instance:")
obj.display_value()  # Expected output: The value is: 100
obj.update_value(250)  # Expected output: Updated value to: 250

# ---------------------------
# Inbuilt Function and Method Comparison
# ---------------------------
import math

# 'math.ceil' is a function provided by Python's math module.
ceil_val = math.ceil(15.25)
print("\nInbuilt function example:")
print(
    "Ceiling value of 15.25 is:", ceil_val
)  # Expected output: Ceiling value of 15.25 is: 16

# Note:
# - Functions are called by their name (e.g., subtract, math.ceil).
# - Methods must be called on an object (e.g., obj.display_value()).
# - In methods, the object is automatically passed as the first argument (self).
