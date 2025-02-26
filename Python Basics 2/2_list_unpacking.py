"""
Key Concepts Covered:
1. Basic list unpacking.
2. Unpacking with the asterisk (*) operator to pack leftover elements.
3. What happens when the number of variables does not match the number of list elements.
"""


def demo_basic_unpacking():
    # Basic list unpacking:
    colors = ["red", "blue", "green"]

    # Unpack each element of the list to its own variable.
    red, blue, green = colors
    # Expected values:
    # red   -> 'red'
    # blue  -> 'blue'
    # green -> 'green'

    print("Basic Unpacking:")
    print("red =", red)  # Output: 'red'
    print("blue =", blue)  # Output: 'blue'
    print("green =", green)  # Output: 'green'
    print()


def demo_unpacking_error():
    # colors = ['red', 'blue', 'green']
    # red, blue = colors
    #
    # Expected error message:
    # ValueError: too many values to unpack (expected 2)
    pass


def demo_unpacking_with_pack():
    # Unpacking with the asterisk (*) operator:
    # This allows capturing the remaining elements into a new list.

    # Example 1:
    colors = ["red", "blue", "green"]
    red, blue, *other = colors
    # Expected values:
    # red   -> 'red'
    # blue  -> 'blue'
    # other -> ['green']

    print("Unpacking with Asterisk (*) Operator (Example 1):")
    print("red =", red)  # Output: 'red'
    print("blue =", blue)  # Output: 'blue'
    print("other =", other)  # Output: ['green']
    print()

    # Example 2:
    colors = ["cyan", "magenta", "yellow", "black"]
    cyan, magenta, *other = colors
    # Expected values:
    # cyan    -> 'cyan'
    # magenta -> 'magenta'
    # other   -> ['yellow', 'black']

    print("Unpacking with Asterisk (*) Operator (Example 2):")
    print("cyan =", cyan)  # Output: 'cyan'
    print("magenta =", magenta)  # Output: 'magenta'
    print("other =", other)  # Output: ['yellow', 'black']
    print()


def main():
    print("Python List Unpacking Learning Module\n")
    demo_basic_unpacking()
    demo_unpacking_with_pack()
    # demo_unpacking_error()


if __name__ == "__main__":
    main()
