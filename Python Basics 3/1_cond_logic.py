"""
This module demonstrates various aspects of conditional logic in Python:
1. Basic if statement.
2. if, elif, and else.
3. Single-line (shorthand) if and if-else statements.
4. Ternary operators (conditional expressions).
5. Logical operators: and, or, not.
6. Nested if statements.
7. The pass statement within conditionals.
"""


def demo_basic_if():
    a = 33
    b = 200
    # Basic if statement: checks whether b is greater than a.
    if b > a:
        print("b is greater than a")
        # Expected output: "b is greater than a"


def demo_if_elif_else():
    a = 33
    b = 33
    # Using if, elif, and else to check conditions.
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
        # Expected output: "a and b are equal"
    else:
        print("a is greater than b")


def demo_else_only():
    a = 200
    b = 33
    # Using else without elif.
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")
        # Expected output: "b is not greater than a"


def demo_short_hand_if():
    a = 50
    b = 25
    # Single-line if statement.
    if a > b:
        print("a is greater than b")
    # Expected output: "a is greater than b"


def demo_short_hand_if_else():
    a = 2
    b = 330
    # Single-line if-else statement (ternary operator).
    print("A") if a > b else print("B")
    # Expected output: "B" because a is not greater than b.


def demo_multi_condition_ternary():
    a = 330
    b = 330
    # Nested ternary operator to handle three conditions.
    print("A") if a > b else print("=") if a == b else print("B")
    # Expected output: "=" since a equals b.


def demo_logical_operators():
    a = 200
    b = 33
    c = 500
    # and: True if both conditions are True.
    if a > b and c > a:
        print("Both conditions are True")
        # Expected output: "Both conditions are True"

    # or: True if at least one condition is True.
    if a > b or a > c:
        print("At least one condition is True")
        # Expected output: "At least one condition is True"

    # not: reverses the result of a condition.
    if not a > b:
        print("a is NOT greater than b")
        # Not executed because a > b is True.


def demo_nested_if():
    x = 41
    # Nested if statements to test multiple conditions.
    if x > 10:
        print("Above ten,")
        # Expected output: "Above ten,"
        if x > 20:
            print("and also above 20!")
            # Expected output: "and also above 20!" (since 41 > 20)
        else:
            print("but not above 20.")
            # This branch would execute if x were between 11 and 20.


def demo_pass_statement():
    a = 33
    b = 200
    # The pass statement is used as a placeholder.
    if b > a:
        pass  # No operation is performed.
    # No output is expected here.


def main():
    print("Python Conditional Logic Learning Module\n")
    demo_basic_if()
    demo_if_elif_else()
    demo_else_only()
    demo_short_hand_if()
    demo_short_hand_if_else()
    demo_multi_condition_ternary()
    demo_logical_operators()
    demo_nested_if()
    demo_pass_statement()


if __name__ == "__main__":
    main()
