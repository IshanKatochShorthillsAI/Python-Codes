"""
This module demonstrates:
1. Iterating over an iterable and using its iterator.
2. Using the range() function with default, start, and step parameters.
"""


def demo_iterable_iterator():
    # Demonstrate the use of iter() on a tuple.
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)
    print("Iterator from tuple:")
    print(next(myit))  # Expected output: apple
    print(next(myit))  # Expected output: banana
    print(next(myit))  # Expected output: cherry


def demo_range_default():
    print("\nUsing range(6):")
    for x in range(6):
        print(x)
    # Expected output: 0, 1, 2, 3, 4, 5


def demo_range_start():
    print("\nUsing range(2,6):")
    for x in range(2, 6):
        print(x)
    # Expected output: 2, 3, 4, 5


def demo_range_step():
    print("\nUsing range(2,30,3):")
    for x in range(2, 30, 3):
        print(x)
    # Expected output: numbers starting at 2, incrementing by 3 up to <30


def main():
    demo_iterable_iterator()
    demo_range_default()
    demo_range_start()
    demo_range_step()


if __name__ == "__main__":
    main()
