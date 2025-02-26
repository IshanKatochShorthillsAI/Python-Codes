"""
String Indexing Demonstration
Christopher Bailey
Strings and Character Data in Python

Strings are ordered sequences of characters. Indexing allows you to access
individual characters in a string directly by using a numeric value.
String indexing is zero-based: the first character in the string has index 0,
the next is 1, and so on.

This script demonstrates:
    - Positive indexing
    - Negative indexing
    - Handling index errors with try/except blocks
"""

# Define the string
s = "mybacon"

# Positive Indexing Examples:
print("Positive Indexing:")
print("s =", s)
print("s[0]:", s[0])  # Expected output: 'm'
print("s[1]:", s[1])  # Expected output: 'y'
print("s[6]:", s[6])  # Expected output: 'n'
print("s[len(s)-1]:", s[len(s) - 1])  # Expected output: 'n'

# Attempt to access an out of range index:
try:
    print("s[7]:", s[7])
except IndexError as e:
    print("s[7]: IndexError:", e)

print("\nNegative Indexing:")
# Negative Indexing Examples:
print("s[-1]:", s[-1])  # Expected output: 'n'
print("s[-4]:", s[-4])  # Expected output: 'a'
print("s[-len(s)]:", s[-len(s)])  # Expected output: 'm'
print("s[-7]:", s[-7])  # Expected output: 'm'

# Attempt to access an out of range negative index:
try:
    print("s[-8]:", s[-8])
except IndexError as e:
    print("s[-8]: IndexError:", e)

print("\nEmpty String Example:")
# Working with an empty string:
t = ""
print("t =", repr(t))
print("type(t):", type(t))  # Expected output: <class 'str'>
try:
    print("t[0]:", t[0])
except IndexError as e:
    print("t[0]: IndexError:", e)  # Expected output: IndexError message
print("len(t):", len(t))  # Expected output: 0
