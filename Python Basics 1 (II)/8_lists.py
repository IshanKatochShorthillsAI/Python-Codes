"""
Python Lists Demonstration
---------------------------
Lists are used to store multiple items in a single variable.
Lists are ordered, changeable, and allow duplicate values.

This script demonstrates:
    - Creating a list.
    - Accessing list items by index.
    - Changing list items.
    - Adding list items.
    - Removing list items.
    - Checking the length of a list.
    - Storing different data types in a list.
    - Using the list() constructor.
"""

# Create a list using square brackets:
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)  # Expected: ['apple', 'banana', 'cherry']

# Accessing list items (indexing starts at 0):
print("First item:", fruits[0])  # Expected: 'apple'
print("Second item:", fruits[1])  # Expected: 'banana'
print("Third item:", fruits[2])  # Expected: 'cherry'
print("Last item with negative index:", fruits[-1])  # Expected: 'cherry'

# Changing list items:
fruits[1] = "blueberry"
print(
    "After changing second item:", fruits
)  # Expected: ['apple', 'blueberry', 'cherry']

# Adding list items:
# Append an item to the end of the list:
fruits.append("date")
print(
    "After appending 'date':", fruits
)  # Expected: ['apple', 'blueberry', 'cherry', 'date']

# Insert an item at a specific index:
fruits.insert(1, "banana")
print("After inserting 'banana' at index 1:", fruits)
# Expected: ['apple', 'banana', 'blueberry', 'cherry', 'date']

# Removing list items:
# Remove an item by value:
fruits.remove("blueberry")
print("After removing 'blueberry':", fruits)
# Expected: ['apple', 'banana', 'cherry', 'date']

# Remove an item by index using pop():
popped_item = fruits.pop(2)
print("After popping index 2:", fruits, ", Popped item:", popped_item)
# Expected: ['apple', 'banana', 'date'] with popped item 'cherry'

# Getting the length of the list:
print("List length:", len(fruits))  # Expected output depends on the current list length

# Lists can store different data types:
mixed_list = ["abc", 34, True, 40, "male"]
print("Mixed list:", mixed_list)
print("Type of mixed_list:", type(mixed_list))  # Expected: <class 'list'>

# Lists allow duplicate values:
dup_list = ["apple", "banana", "cherry", "apple", "cherry"]
print("List with duplicates:", dup_list)
# Expected: ['apple', 'banana', 'cherry', 'apple', 'cherry']

# Creating a list using the list() constructor:
constructed_list = list(("apple", "banana", "cherry"))  # Note the double round-brackets
print("Constructed list using list():", constructed_list)
# Expected: ['apple', 'banana', 'cherry']

# Looping through list items:
print("Looping through the fruits list:")
for fruit in fruits:
    print(fruit)
# Expected output:
# apple
# banana
# date
