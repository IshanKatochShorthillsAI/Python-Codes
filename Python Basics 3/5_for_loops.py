"""
This module demonstrates various aspects of for loops:
1. Looping through a list.
2. Looping through a string.
3. Using break to exit a loop.
4. Using continue to skip an iteration.
5. Using an else clause with for loops.
6. Nested loops.
7. Using pass in a for loop.
"""


def demo_iterate_list():
    fruits = ["apple", "banana", "cherry"]
    print("Iterating over list:")
    for fruit in fruits:
        print(fruit)
    # Expected output: each fruit on a new line.


def demo_loop_string():
    print("\nIterating over string 'banana':")
    for char in "banana":
        print(char)
    # Expected output: each character of 'banana' on a new line.


def demo_break_loop():
    fruits = ["apple", "banana", "cherry"]
    print("\nUsing break (exit when 'banana' found):")
    for fruit in fruits:
        print(fruit)
        if fruit == "banana":
            break
    # Expected output: "apple" then "banana" then loop breaks.


def demo_continue_loop():
    fruits = ["apple", "banana", "cherry"]
    print("\nUsing continue (skip 'banana'):")
    for fruit in fruits:
        if fruit == "banana":
            continue
        print(fruit)
    # Expected output: "apple" then "cherry" (skipping "banana").


def demo_for_else():
    print("\nFor-else demonstration:")
    for x in range(3):
        print(x)
    else:
        print("Loop finished!")
    # Expected output: 0, 1, 2 then "Loop finished!"


def demo_nested_loops():
    adjectives = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    print("\nNested loops:")
    for adj in adjectives:
        for fruit in fruits:
            print(adj, fruit)
    # Expected output: each adjective paired with each fruit.


def demo_pass_loop():
    print("\nFor loop with pass (no output):")
    for _ in [0, 1, 2]:
        pass
    # Expected: loop runs without error and no output.


def main():
    demo_iterate_list()
    demo_loop_string()
    demo_break_loop()
    demo_continue_loop()
    demo_for_else()
    demo_nested_loops()
    demo_pass_loop()


if __name__ == "__main__":
    main()
