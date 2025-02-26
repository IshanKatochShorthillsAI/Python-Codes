"""
This module demonstrates various operations on dictionaries:
1. Creating and printing a dictionary.
2. Accessing items.
3. Changing item values.
4. Adding new items.
5. Removing items.
6. Looping through a dictionary.
7. Copying dictionaries.
8. Creating nested dictionaries.
9. Using the dict() constructor.
"""


def demo_create_print_dict():
    # Creating a dictionary with key:value pairs.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print("Dictionary:", thisdict)
    # Expected output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
    print()


def demo_access_items():
    # Accessing items in a dictionary by key.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # Access the value associated with the key "brand"
    print("Brand:", thisdict["brand"])
    # Expected output: Ford
    print()


def demo_change_items():
    # Changing the value of an existing key in the dictionary.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # Update the 'year' value
    thisdict["year"] = 2020
    print("Updated Dictionary:", thisdict)
    # Expected output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
    print()


def demo_add_items():
    # Adding new key:value pairs to a dictionary.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # Adding a new key 'color'
    thisdict["color"] = "red"
    print("Dictionary after adding color:", thisdict)
    # Expected output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
    print()


def demo_remove_items():
    # Removing items from a dictionary.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # Remove an item using the del statement.
    del thisdict["model"]
    print("After deleting 'model' key:", thisdict)
    # Expected output: {'brand': 'Ford', 'year': 1964}

    # Remove an item using the pop() method.
    removed_year = thisdict.pop("year")
    print("Popped 'year':", removed_year)
    # Expected output: 1964
    print("Dictionary after pop():", thisdict)
    # Expected output: {'brand': 'Ford'}

    # Using popitem() to remove the last inserted item (Python 3.7+).
    thisdict["year"] = 2020
    removed_item = thisdict.popitem()
    print("Popped item using popitem():", removed_item)
    # Expected output: ('year', 2020)
    print("Dictionary after popitem():", thisdict)
    print()


def demo_loop_dictionary():
    # Looping through keys, values, and key:value pairs in a dictionary.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    print("Looping through keys:")
    for key in thisdict:
        print(key)
        # Expected output: brand, model, year (each in a new line)
    print()

    print("Looping through values:")
    for value in thisdict.values():
        print(value)
        # Expected output: Ford, Mustang, 1964 (each in a new line)
    print()

    print("Looping through key-value pairs:")
    for key, value in thisdict.items():
        print(key, ":", value)
        # Expected output: key and value pairs printed on separate lines.
    print()


def demo_copy_dictionary():
    # Copying a dictionary using the copy() method.
    thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    mydict = thisdict.copy()
    print("Original dictionary:", thisdict)
    print("Copied dictionary:", mydict)
    # Expected output: Both dictionaries should be the same.
    print()


def demo_nested_dictionary():
    # Creating a nested dictionary where dictionary items contain dictionaries.
    myfamily = {
        "child1": {"name": "Emil", "year": 2004},
        "child2": {"name": "Tobias", "year": 2007},
        "child3": {"name": "Linus", "year": 2011},
    }
    print("Nested Dictionary:", myfamily)
    # Expected output: A dictionary with keys child1, child2, child3 and each key has an inner dictionary.
    print()


def demo_dict_constructor():
    # Creating a dictionary using the dict() constructor.
    thisdict = dict(name="John", age=36, country="Norway")
    print("Dictionary using dict() constructor:", thisdict)
    # Expected output: {'name': 'John', 'age': 36, 'country': 'Norway'}
    print()


def main():
    print("Python Dictionary Learning Module\n")
    demo_create_print_dict()
    demo_access_items()
    demo_change_items()
    demo_add_items()
    demo_remove_items()
    demo_loop_dictionary()
    demo_copy_dictionary()
    demo_nested_dictionary()
    demo_dict_constructor()


if __name__ == "__main__":
    main()
