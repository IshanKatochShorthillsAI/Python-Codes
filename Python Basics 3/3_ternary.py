"""
This module demonstrates various approaches to using conditional logic in a single line (ternary operator) in Python:
1. Basic ternary operator to assign a value based on a condition.
2. Nested ternary operator to handle multiple conditions.
3. Ternary operator using a tuple for alternative selection.
4. Ternary operator using a dictionary for mapping conditions.
5. Ternary operator using a lambda function.
6. Direct usage of the ternary operator within a print statement.
"""


def demo_basic_ternary():
    # Basic Example:
    # Determine if a number is even or odd.
    n = 5
    result = "Even" if n % 2 == 0 else "Odd"
    print(result)
    # Expected output: Odd


def demo_nested_ternary():
    # Nested Ternary Operator:
    # Evaluate a number to determine if it is positive, negative, or zero.
    n = -5
    result = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
    print(result)
    # Expected output: Negative


def demo_ternary_using_tuple():
    # Ternary operator using a tuple:
    # Tuple indexing provides an alternative way to choose between two values.
    n = 7
    result = ("Odd", "Even")[n % 2 == 0]
    print(result)
    # Expected output: Odd
    # Explanation: n % 2 == 0 evaluates to False (i.e., index 0), selecting "Odd"


def demo_ternary_using_dict():
    # Ternary operator using a dictionary:
    # Map a condition to its corresponding value using a dictionary.
    a = 10
    b = 20
    maximum = {True: a, False: b}[a > b]
    print(maximum)
    # Expected output: 20
    # Explanation: Since a > b is False, the dictionary returns the value for key False, which is b.


def demo_ternary_using_lambda():
    # Ternary operator using a lambda function:
    # Define an anonymous function that returns the greater of two values.
    a = 10
    b = 20
    maximum = (lambda x, y: x if x > y else y)(a, b)
    print(maximum)
    # Expected output: 20


def demo_ternary_with_print():
    # Ternary operator directly within a print statement.
    a = 10
    b = 20
    print("a is greater" if a > b else "b is greater")
    # Expected output: b is greater


def main():
    print("Python Ternary Operator Learning Module\n")
    demo_basic_ternary()
    demo_nested_ternary()
    demo_ternary_using_tuple()
    demo_ternary_using_dict()
    demo_ternary_using_lambda()
    demo_ternary_with_print()


if __name__ == "__main__":
    main()
