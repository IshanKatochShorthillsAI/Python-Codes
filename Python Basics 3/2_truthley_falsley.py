"""
Key Concepts:
- Every object in Python has an inherent Boolean value.
- Falsy values include: False, None, 0, "" (empty string), empty sequences (e.g., (), []), and empty collections (e.g., {}).
- All other values are considered truthy.
- Using these values in conditional statements allows you to control program flow.
"""


def demo_truthy_values():
    # Examples of truthy values.
    examples = [True, 1, -1, "Hello", [0], (0,), {"key": "value"}]

    print("Truthy value tests:")
    for item in examples:
        if item:
            print(f"{repr(item)} is truthy")
        else:
            print(f"{repr(item)} is falsy")
    # Expected output: All items in the list are truthy.


def demo_falsy_values():
    # Examples of falsy values.
    examples = [False, None, 0, 0.0, "", (), [], {}, set()]

    print("\nFalsy value tests:")
    for item in examples:
        if item:
            print(f"{repr(item)} is truthy")
        else:
            print(f"{repr(item)} is falsy")
    # Expected output: All items in the list should be evaluated as falsy.


def demo_bool_conversion():
    # Using the bool() function to explicitly see the Boolean value.
    values = [None, 0, "", [], {}, "Non-empty string", [1, 2, 3]]

    print("\nBoolean conversion using bool():")
    for value in values:
        print(f"bool({repr(value)}) -> {bool(value)}")
    # Expected output:
    # bool(None) -> False
    # bool(0) -> False
    # bool("") -> False
    # bool([]) -> False
    # bool({}) -> False
    # bool("Non-empty string") -> True
    # bool([1, 2, 3]) -> True


def demo_conditional_usage():
    # Demonstrating how truthy and falsy values are used in conditions.
    test_values = [[], [1, 2, 3], "", "Python", 0, 10]

    print("\nConditional usage demonstration:")
    for value in test_values:
        if value:
            print(f"{repr(value)} is considered True in conditionals.")
        else:
            print(f"{repr(value)} is considered False in conditionals.")
    # Expected output:
    # [] is considered False in conditionals.
    # [1, 2, 3] is considered True in conditionals.
    # "" is considered False in conditionals.
    # "Python" is considered True in conditionals.
    # 0 is considered False in conditionals.
    # 10 is considered True in conditionals.


def main():
    print("Python Truthy/Falsy Values Learning Module\n")
    demo_truthy_values()
    demo_falsy_values()
    demo_bool_conversion()
    demo_conditional_usage()


if __name__ == "__main__":
    main()
