"""
Python List Slicing Demonstration
-----------------------------------
List slicing is a fundamental concept that lets you easily access specific portions of a list.
The slicing syntax is:
    list_name[start : end : step]

Parameters:
    start (optional): Index to begin the slice (inclusive). Defaults to 0.
    end (optional): Index to end the slice (exclusive). Defaults to the length of the list.
    step (optional): Interval between elements. Defaults to 1.

This script demonstrates various list slicing examples including:
    - Slicing with positive indexes.
    - Omitting start or end to get all items.
    - Using the step parameter.
    - Out-of-bound slicing.
    - Using negative indexes.
    - Reversing a list using slicing.
"""

# Define a sample list:
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 1: Get elements from index 1 to 4 (exclusive)
slice1 = a[1:4]
print("a[1:4] =", slice1)
# Expected output: [2, 3, 4]

# Example 2: Get all items using [:] and [::]
print("a[:] =", a[:])  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("a[::] =", a[::])  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 3: Get all items from index 2 to end and before index 3
b = a[2:]
print("a[2:] =", b)  # Expected output: [3, 4, 5, 6, 7, 8, 9]
c = a[:3]
print("a[:3] =", c)  # Expected output: [1, 2, 3]

# Example 4: Get items at specified intervals (step)
d = a[::2]
print("a[::2] =", d)  # Expected output: [1, 3, 5, 7, 9]
e = a[1:8:3]
print("a[1:8:3] =", e)  # Expected output: [2, 5, 8]

# Example 5: Out-of-bound slicing (no error, returns available items)
f = a[7:15]
print("a[7:15] =", f)  # Expected output: [8, 9]

# Example 6: Negative Indexing Examples
g = a[-2:]
print("a[-2:] =", g)  # Expected output: [8, 9]
h = a[:-3]
print("a[:-3] =", h)  # Expected output: [1, 2, 3, 4, 5, 6]
i = a[-4:-1]
print("a[-4:-1] =", i)  # Expected output: [6, 7, 8]
j = a[-8:-1:2]
print("a[-8:-1:2] =", j)  # Expected output: [2, 4, 6, 8]

# Example 7: Reverse a list using slicing
k = a[::-1]
print("a[::-1] =", k)  # Expected output: [9, 8, 7, 6, 5, 4, 3, 2, 1]
