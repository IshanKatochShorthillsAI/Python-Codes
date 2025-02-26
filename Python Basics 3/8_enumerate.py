"""
This module demonstrates the use of the enumerate() function:
1. Basic usage of enumerate().
2. Using a custom start index.
3. Using next() with an enumerate object.
"""


def demo_enumerate_basic():
    fruits = ["Geeks", "for", "Geeks"]
    print("Using enumerate() in a loop:")
    for i, name in enumerate(fruits):
        print(f"Index {i}: {name}")
    # Expected output: each index and fruit printed.


def demo_enumerate_custom_start():
    fruits = ["geeks", "for", "geeks"]
    print("\nUsing enumerate() with start=1:")
    for index, x in enumerate(fruits, start=1):
        print(index, x)
    # Expected output: indices starting from 1.


def demo_enumerate_with_next():
    fruits = ["Geeks", "for", "Geeks"]
    enum_obj = enumerate(fruits)
    print("\nAccessing next() on enumerate object:")
    print(next(enum_obj))  # Expected output: (0, 'Geeks')
    print(next(enum_obj))  # Expected output: (1, 'for')


def main():
    demo_enumerate_basic()
    demo_enumerate_custom_start()
    demo_enumerate_with_next()


if __name__ == "__main__":
    main()
