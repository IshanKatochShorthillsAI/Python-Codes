# Example 1: Function with positional arguments
def add_numbers(a, b):
    """
    This function takes two parameters a and b.
    It computes their sum and prints the result.

    Example:
    add_numbers(2, 3)
    Output: Sum: 5
    """
    sum_val = a + b
    print("Sum:", sum_val)


add_numbers(2, 3)  # Output: Sum: 5


# Example 2: Function with default parameter values
def add_default_numbers(a=7, b=8):
    """
    This function takes two parameters with default values.
    If arguments are provided, they override the defaults.
    Otherwise, default values are used.

    Examples:
    add_default_numbers(2, 3) -> Output: Sum: 5  (both arguments provided)
    add_default_numbers(a=2)    -> Output: Sum: 10 (b uses default value 8)
    add_default_numbers()       -> Output: Sum: 15 (both use default values)
    """
    sum_val = a + b
    print("Sum:", sum_val)


add_default_numbers(2, 3)  # Output: Sum: 5
add_default_numbers(a=2)  # Output: Sum: 10
add_default_numbers()  # Output: Sum: 15


# Example 3: Function with keyword arguments
def display_info(first_name, last_name):
    """
    This function prints the first and last name using keyword arguments.

    When calling the function with named parameters, the order does not matter.

    Example:
    display_info(last_name='Cartman', first_name='Eric')
    Output:
    First Name: Eric
    Last Name: Cartman
    """
    print("First Name:", first_name)
    print("Last Name:", last_name)


display_info(last_name="Cartman", first_name="Eric")
# Output:
# First Name: Eric
# Last Name: Cartman


# Example 4: Function with arbitrary arguments (*args)
def find_sum(*numbers):
    """
    This function accepts an arbitrary number of arguments and computes their sum.

    The * before the parameter name allows passing a variable number of arguments,
    which are accessible as a tuple.

    Examples:
    find_sum(1, 2, 3) -> Output: Sum = 6
    find_sum(4, 9)    -> Output: Sum = 13
    """
    result = 0
    for num in numbers:
        result += num
    print("Sum =", result)


find_sum(1, 2, 3)  # Output: Sum = 6
find_sum(4, 9)  # Output: Sum = 13
