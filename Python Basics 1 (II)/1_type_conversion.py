"""
This script demonstrates type conversion in Python.
It performs the following conversions:
    - Converts an integer to a float.
    - Converts a float to an integer (truncating the fractional part).
    - Converts an integer to a complex number.

Predicted outputs:
    1.0           # Result of converting int 1 to float and printing 'a'
    2             # Result of converting float 2.8 to int (truncation) and printing 'b'
    (1+0j)        # Result of converting int 1 to complex and printing 'c'
    <class 'float'>
    <class 'int'>
    <class 'complex'>
"""

x = 1  # int
y = 2.8  # float
z = 1j  # complex (not used in further conversions)

# Convert from int to float:
a = float(x)  # a becomes 1.0

# Convert from float to int:
b = int(y)  # b becomes 2 (fractional part is discarded)

# Convert from int to complex:
c = complex(x)  # c becomes (1+0j)

# Print the results of the conversions:
print(a)  # Expected output: 1.0
print(b)  # Expected output: 2
print(c)  # Expected output: (1+0j)

# Print the types of the converted values:
print(type(a))  # Expected output: <class 'float'>
print(type(b))  # Expected output: <class 'int'>
print(type(c))  # Expected output: <class 'complex'>
