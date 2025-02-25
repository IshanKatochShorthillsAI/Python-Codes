# This file demonstrates various augmented assignment operators in Python.
# Augmented assignment operators perform an operation and assignment in a single step.

# ---------
# Addition and Assignment (+=)
# Adds the right operand to the left operand and assigns the result to the left operand.
a = 15
b = 20
a += b
print(a)  # Output: 35

# ---------
# Subtraction and Assignment (-=)
# Subtracts the right operand from the left operand and assigns the result to the left operand.
a = 107
b = 99
a -= b
print(a)  # Output: 8

# ---------
# Multiplication and Assignment (*=)
# Multiplies the left operand by the right operand and assigns the result to the left operand.
a = 12
b = 13
a *= b
print(a)  # Output: 156

# ---------
# Division and Assignment (/=)
# Divides the left operand by the right operand and assigns the result to the left operand.
a = 56
b = 5
a /= b
print(a)  # Output: 11.2

# ---------
# Floor Division and Assignment (//=)
# Divides the left operand by the right operand, performs floor division, and assigns the result to the left operand.
a = 56
b = 8
a //= b
print(a)  # Output: 7

# ---------
# Modulus and Assignment (%=)
# Finds the remainder when the left operand is divided by the right operand, then assigns that remainder to the left operand.
a = 34
b = 5
a %= b
print(a)  # Output: 4

# ---------
# Exponentiation and Assignment (**=)
# Raises the left operand to the power of the right operand and assigns the result to the left operand.
a = 5
b = 3
a **= b
print(a)  # Output: 125

# ---------
# Bitwise AND and Assignment (&=)
# Performs a bitwise AND on the left and right operands and assigns the result to the left operand.
a = 12
b = 10
a &= b
print(a)  # Output: 8

# ---------
# Bitwise OR and Assignment (|=)
# Performs a bitwise OR on the left and right operands and assigns the result to the left operand.
a = 12
b = 10
a |= b
print(a)  # Output: 14

# ---------
# Bitwise XOR and Assignment (^=)
# Performs a bitwise XOR on the left and right operands and assigns the result to the left operand.
a = 12
b = 10
a ^= b
print(a)  # Output: 6

# ---------
# Bitwise Right Shift and Assignment (>>=)
# Shifts the bits of the left operand to the right by the number specified in the right operand.
a = 17
b = 2
a >>= b
print(a)  # Output: 4

# ---------
# Bitwise Left Shift and Assignment (<<=)
# Shifts the bits of the left operand to the left by the number specified in the right operand.
a = 17
b = 2
a <<= b
print(a)  # Output: 68
