"""
Key Concepts:
- Logical operators (and, or) in Python employ short-circuit evaluation.
- For "and": if the first operand is falsy, the second operand is not evaluated.
- For "or": if the first operand is truthy, the second operand is not evaluated.
- This behavior can improve efficiency and avoid unnecessary computations.
"""


def demo_and_short_circuit():
    # In an AND expression, if the left operand is False, the right operand is not evaluated.
    def func():
        print("Function executed")
        return True

    # Since the first operand False is falsy, func() is never called.
    result = False and func()
    print("Result of False and func():", result)
    # Expected output:
    #   Result of False and func(): False
    # (No "Function executed" printed)


def demo_or_short_circuit():
    # In an OR expression, if the left operand is True, the right operand is not evaluated.
    def func():
        print("Function executed")
        return True

    # Since the first operand True is truthy, func() is not called.
    result = True or func()
    print("Result of True or func():", result)
    # Expected output:
    #   Result of True or func(): True
    # (No "Function executed" printed)


def demo_mixed_short_circuit():
    # Demonstrates evaluation when neither operand short-circuits immediately.
    def func(x):
        print(f"Evaluating {x}")
        return x

    # For an AND operation, if the first operand is True, the second is evaluated.
    result = func(True) and func(False)
    print("Result of func(True) and func(False):", result)
    # Expected output:
    #   Evaluating True
    #   Evaluating False
    #   Result of func(True) and func(False): False


def main():
    print("Python Short-Circuiting Learning Module\n")
    demo_and_short_circuit()
    print()  # Blank line for separation.
    demo_or_short_circuit()
    print()  # Blank line for separation.
    demo_mixed_short_circuit()


if __name__ == "__main__":
    main()
