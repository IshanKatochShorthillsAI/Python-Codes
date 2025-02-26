"""
This script demonstrates string formatting in Python.
It performs various formatting operations:
    - Formats a float to two decimal places.
    - Formats strings using named placeholders.
    - Formats strings using positional placeholders.
    - Formats strings using implicit placeholders.

Predicted outputs:
    For only 49.00 dollars!
    My name is John, I'm 36
    My name is John, I'm 36
    My name is John, I'm 36
"""

# Format string using named argument, formatting `price` as a two-decimal float:
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))  # Expected output: For only 49.00 dollars!

# Format strings using different approaches:

# Using named placeholders:
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)

# Using positional placeholders with explicit numbering:
txt2 = "My name is {0}, I'm {1}".format("John", 36)

# Using implicit positional placeholders:
txt3 = "My name is {}, I'm {}".format("John", 36)

print(txt1)  # Expected output: My name is John, I'm 36
print(txt2)  # Expected output: My name is John, I'm 36
print(txt3)  # Expected output: My name is John, I'm 36
