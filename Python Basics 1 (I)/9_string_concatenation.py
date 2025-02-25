"""
9_string_concatenation.py

This script demonstrates how to perform string concatenation in Python.
It provides examples of joining two strings without and with a space between them.
"""

# Define two string variables
a = "Hello"
b = "World"

# Concatenate strings without adding a space in between
# Result: "HelloWorld"
c = a + b
print("Without space:", c)

# Concatenate strings with a space between them by explicitly adding " "
# Result: "Hello World"
c = a + " " + b
print("With space:", c)
