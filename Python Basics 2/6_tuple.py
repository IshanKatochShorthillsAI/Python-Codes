"""
Key Concepts:
- Tuples are used to store multiple items in a single variable.
- They are ordered, unchangeable, and allow duplicate values.
- Tuples use round brackets; a single-item tuple requires a trailing comma.
"""


def demo_create_tuple():
    # Creating a tuple with multiple items.
    thistuple = ("apple", "banana", "cherry")
    print("Tuple:", thistuple)
    # Expected output: ("apple", "banana", "cherry")


def demo_access_items():
    # Accessing items in a tuple by index.
    thistuple = ("apple", "banana", "cherry")
    # Accessing the first and second items.
    print("First item:", thistuple[0])  # Expected output: apple
    print("Second item:", thistuple[1])  # Expected output: banana


def demo_duplicate_values():
    # Tuples allow duplicate values.
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print("Tuple with duplicates:", thistuple)
    # Expected output: ("apple", "banana", "cherry", "apple", "cherry")


def demo_tuple_length():
    # Determining the length (number of items) of a tuple.
    thistuple = ("apple", "banana", "cherry")
    print("Length of tuple:", len(thistuple))
    # Expected output: 3


def demo_single_item_tuple():
    # Creating a tuple with only one item requires a trailing comma.
    tuple_one = ("apple",)
    print("Single-item tuple:", tuple_one)
    print("Type of single-item tuple:", type(tuple_one))
    # Expected output for type: <class 'tuple'>

    # Without a trailing comma, Python does not recognize it as a tuple.
    not_a_tuple = "apple"
    print("Without trailing comma - type:", type(not_a_tuple))
    # Expected output for type: <class 'str'>


def demo_tuple_constructor():
    # Creating a tuple using the tuple() constructor.
    thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
    print("Tuple using constructor:", thistuple)
    # Expected output: ("apple", "banana", "cherry")


def main():
    print("Python Tuples Learning Module\n")
    demo_create_tuple()
    demo_access_items()
    demo_duplicate_values()
    demo_tuple_length()
    demo_single_item_tuple()
    demo_tuple_constructor()


if __name__ == "__main__":
    main()
