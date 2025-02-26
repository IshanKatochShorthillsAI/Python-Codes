"""
Key Concepts:
- Sets are unordered collections that do not allow duplicate elements.
- Items in a set cannot be accessed via indexing.
- You can add or remove items from a set.
- When printed, the order of set items is arbitrary.
"""


def demo_create_set():
    # Creating a set using curly braces.
    fruits = {"apple", "banana", "cherry"}
    print("Set of fruits:", fruits)
    # Expected output: e.g., {'banana', 'apple', 'cherry'} (order may vary)


def demo_duplicates_not_allowed():
    # Demonstrates that duplicate values are automatically removed.
    fruits = {"apple", "banana", "cherry", "apple"}
    print("Set with duplicates:", fruits)
    # Expected output: {'apple', 'banana', 'cherry'}


def demo_add_items():
    # Adding new items to a set using add().
    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
    print("After adding 'orange':", fruits)
    # Expected output: set containing apple, banana, cherry, orange (order may vary)


def demo_remove_items():
    # Removing items from a set.
    fruits = {"apple", "banana", "cherry"}
    fruits.remove("banana")  # Removes 'banana'; raises KeyError if not found.
    print("After removing 'banana':", fruits)
    # Expected output: {'apple', 'cherry'}

    # Using discard() to remove an item safely (no error if item not present).
    fruits.discard("pineapple")
    print("After discarding 'pineapple':", fruits)
    # Expected output: {'apple', 'cherry'}


def demo_loop_set():
    # Looping through a set. Order is not guaranteed.
    fruits = {"apple", "banana", "cherry"}
    print("Looping through set items:")
    for fruit in fruits:
        print(fruit)
    # Expected output: Each fruit printed on a new line in arbitrary order


def demo_set_operations():
    # Demonstrates common set operations.
    set1 = {"apple", "banana", "cherry"}
    set2 = {"banana", "kiwi", "mango"}

    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)

    print("Union of set1 and set2:", union_set)
    # Expected output: Set containing all unique elements from set1 and set2.
    print("Intersection of set1 and set2:", intersection_set)
    # Expected output: {'banana'}
    print("Difference of set1 and set2:", difference_set)
    # Expected output: {'apple', 'cherry'}


def demo_set_constructor():
    # Creating a set using the set() constructor.
    fruits = set(("apple", "banana", "cherry"))  # Note the double round-brackets.
    print("Set using constructor:", fruits)
    # Expected output: {'apple', 'banana', 'cherry'}


def main():
    print("Python Sets Learning Module\n")
    demo_create_set()
    demo_duplicates_not_allowed()
    demo_add_items()
    demo_remove_items()
    demo_loop_set()
    demo_set_operations()
    demo_set_constructor()
    print("\nEnd of Sets Demonstration.")


if __name__ == "__main__":
    main()
