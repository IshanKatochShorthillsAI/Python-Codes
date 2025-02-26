"""
Python Booleans Demonstration
--------------------------------
Booleans represent one of two values: True or False.

This script demonstrates:
    - Evaluating expressions to Boolean values.
    - Using conditional statements.
    - Evaluating various types with the bool() function.
    - Custom objects and functions returning Boolean values.
"""

# Evaluating simple expressions:
print("10 > 9 =", 10 > 9)  # Expected output: True
print("10 == 9 =", 10 == 9)  # Expected output: False
print("10 < 9 =", 10 < 9)  # Expected output: False

# Conditional statement based on Boolean evaluation:
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Expected output: b is not greater than a

# Using bool() to evaluate values:
print("bool('Hello') =", bool("Hello"))  # Expected: True (non-empty string)
print("bool(15) =", bool(15))  # Expected: True (non-zero number)

x = "Hello"
y = 15
print("bool(x) =", bool(x))  # Expected: True
print("bool(y) =", bool(y))  # Expected: True

# Most empty values evaluate to False:
print("bool(False) =", bool(False))  # Expected: False
print("bool(None) =", bool(None))  # Expected: False
print("bool(0) =", bool(0))  # Expected: False
print("bool('') =", bool(""))  # Expected: False
print("bool(()) =", bool(()))  # Expected: False
print("bool([]) =", bool([]))  # Expected: False
print("bool({}) =", bool({}))  # Expected: False


# Custom object with __len__ returning 0 evaluates to False:
class MyClass:
    def __len__(self):
        return 0


myobj = MyClass()
print("bool(myobj) =", bool(myobj))  # Expected: False


# Function returning a boolean:
def myFunction():
    return True


print("myFunction() =", myFunction())  # Expected: True

# Execute code based on the boolean result of a function:
if myFunction():
    print("YES!")
else:
    print("NO!")
# Expected output: YES!

# Using isinstance() to check an object's type:
x = 200
print("isinstance(x, int) =", isinstance(x, int))  # Expected: True

# Simple boolean expression:
print("Result of 5 > 3 is", 5 > 3)  # Expected: True
