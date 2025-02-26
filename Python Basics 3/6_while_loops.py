"""
This module demonstrates various aspects of while loops:
1. Basic while loop.
2. Using break in a while loop.
3. Using continue in a while loop.
4. Using an else clause with a while loop.
"""


def demo_basic_while():
    print("Basic while loop:")
    i = 1
    while i < 6:
        print(i)
        i += 1
    # Expected output: numbers 1 to 5.


def demo_break_while():
    print("\nWhile loop with break (exit when i==3):")
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1
    # Expected output: 1, 2, 3; then loop breaks.


def demo_continue_while():
    print("\nWhile loop with continue (skip when i==3):")
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)
    # Expected output: numbers 1, 2, 4, 5, 6 (3 is skipped).


def demo_while_else():
    print("\nWhile-else loop:")
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")
    # Expected output: 1 to 5 then message from else block.


def main():
    demo_basic_while()
    demo_break_while()
    demo_continue_while()
    demo_while_else()


if __name__ == "__main__":
    main()
