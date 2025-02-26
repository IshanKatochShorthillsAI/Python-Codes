"""
Mutable vs Immutable Objects in Python
-----------------------------------------
In Python, every variable holds an instance of an object. Objects can be either mutable or immutable.
Immutable objects (like int, float, bool, string, tuple) cannot be changed after creation.
Mutable objects (like list, dict, set) can be modified after they are created.

This script demonstrates:
    - Immutable objects: tuple and string modification (which will raise errors).
    - Mutable objects: list, dictionary, and set modifications.
"""

# Immutable Objects Examples:
print("Immutable Objects:")

# Example 1: Tuple (immutable)
tuple1 = (0, 1, 2, 3)
try:
    tuple1[0] = 4
except TypeError as e:
    print("Error modifying tuple:", e)
# Expected error: 'tuple' object does not support item assignment

# Example 2: String (immutable)
message = "Welcome Here"
try:
    message[0] = "p"
except TypeError as e:
    print("Error modifying string:", e)
# Expected error: 'str' object does not support item assignment

# Mutable Objects Examples:
print("\nMutable Objects:")

# Example 1: List (mutable)
my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  # Expected output: [1, 2, 3, 4]
my_list.insert(1, 5)
print("After insert at index 1:", my_list)  # Expected output: [1, 5, 2, 3, 4]
my_list.remove(2)
print("After removing value 2:", my_list)  # Expected output: [1, 5, 3, 4]
popped_element = my_list.pop(0)
print("After pop index 0:", my_list, ", popped element:", popped_element)
# Expected output: [5, 3, 4] and popped element is 1

# Example 2: Dictionary (mutable)
my_dict = {"name": "Ram", "age": 25}
new_dict = my_dict  # Both variables reference the same dictionary
new_dict["age"] = 37
print("Dictionary after modification:", my_dict)
# Expected output: {'name': 'Ram', 'age': 37}

# Example 3: Set (mutable)
my_set = {1, 2, 3}
new_set = my_set  # Both variables reference the same set
new_set.add(4)
print("Set after adding 4:", my_set)
# Expected output: {1, 2, 3, 4}
