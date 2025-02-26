# ----------------------------------------------------------------------------
# Function: return_42
# Demonstrates an explicit return statement.
# The function returns the number 42, which can then be used in expressions.
# ----------------------------------------------------------------------------
def return_42():
    """
    Returns:
        int: The value 42.
    """
    return 42


# Calling return_42() and using its return value in various expressions.
print(return_42())  # Expected output: 42
print(return_42() * 2)  # Expected output: 84
print(return_42() + 5)  # Expected output: 47


# ----------------------------------------------------------------------------
# Function: add_one
# Demonstrates an implicit return.
# The function performs a calculation but does not return any value,
# so it implicitly returns None.
# ----------------------------------------------------------------------------
def add_one(x):
    """
    Adds 1 to the input but forgets to return the result.
    Implicit return: Python returns None.

    Args:
        x (int): A number.
    """
    result = x + 1  # Calculation is made, but not returned


value = add_one(5)
print(value)  # Expected output: None


# ----------------------------------------------------------------------------
# Function: get_even
# Returns a list containing only the even numbers from the provided list.
# Uses a list comprehension in the return statement.
# ----------------------------------------------------------------------------
def get_even(numbers):
    """
    Filters even numbers from a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: Even numbers extracted from the input.
    """
    return [num for num in numbers if not num % 2]


print(get_even([1, 2, 3, 4, 5, 6]))  # Expected output: [2, 4, 6]


# ----------------------------------------------------------------------------
# Function: mean
# Returns the arithmetic mean of a numeric sample.
# Demonstrates using an expression directly in the return statement.
# ----------------------------------------------------------------------------
def mean(sample):
    """
    Calculates the mean of a list of numbers.

    Args:
        sample (list): A list of numeric values.

    Returns:
        float: The mean value.
    """
    return sum(sample) / len(sample)


print(mean([1, 2, 3, 4]))  # Expected output: 2.5


# ----------------------------------------------------------------------------
# Function: my_abs
# Returns the absolute value of a number, using conditional statements.
# Also shows the importance of handling every case to avoid an implicit None.
# ----------------------------------------------------------------------------
def my_abs(number):
    """
    Returns the absolute value of the given number.

    Args:
        number (int or float): The number to convert.

    Returns:
        int or float: The absolute value.
    """
    if number > 0:
        return number
    elif number < 0:
        return -number
    else:
        return 0


print(my_abs(-15))  # Expected output: 15
print(my_abs(0))  # Expected output: 0
print(my_abs(15))  # Expected output: 15


# ----------------------------------------------------------------------------
# Function: is_divisible
# Returns True if 'a' is divisible by 'b' (i.e. remainder is 0), else False.
# Demonstrates a concise return with a Boolean expression.
# ----------------------------------------------------------------------------
def is_divisible(a, b):
    """
    Checks if 'a' is divisible by 'b'.

    Args:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        bool: True if a is divisible by b, False otherwise.
    """
    return not a % b


print(is_divisible(4, 2))  # Expected output: True
print(is_divisible(7, 4))  # Expected output: False


# ----------------------------------------------------------------------------
# Function: my_any
# Emulates the built-in any() function.
# Iterates through an iterable and short-circuits (returns immediately)
# when a truthy value is encountered.
# ----------------------------------------------------------------------------
def my_any(iterable):
    """
    Returns True if any element in the iterable is truthy.

    Args:
        iterable (iterable): An iterable of values.

    Returns:
        bool: True if at least one item is truthy; otherwise False.
    """
    for item in iterable:
        if item:
            # Short-circuit once a truthy item is found.
            return True
    return False


print(my_any([0, 0, 1, 0, 0]))  # Expected output: True
print(my_any([0, 0, 0, 0, 0]))  # Expected output: False

# ----------------------------------------------------------------------------
# Function: describe
# Returns multiple values (mean, median, and mode) from a sample.
# Demonstrates that multiple return values are automatically
# packed into a tuple.
# ----------------------------------------------------------------------------
import statistics as st


def describe(sample):
    """
    Computes statistical measures from a list of numbers.

    Args:
        sample (list): A list of numeric values.

    Returns:
        tuple: (mean, median, mode) of the sample.
    """
    return st.mean(sample), st.median(sample), st.mode(sample)


sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
mean_val, median_val, mode_val = describe(sample)
print(mean_val)  # Expected output: Mean value (e.g., 6.5)
print(median_val)  # Expected output: Median value (e.g., 7.0)
print(mode_val)  # Expected output: Mode (e.g., 7)
print(describe(sample))  # Expected output: Tuple with three statistical measures

# ----------------------------------------------------------------------------
# Additional Notes:
# - Remember that when using a function in a script,
#   the return value is not automatically printed. Use print()
#   if you want to see the output.
#
# - If you omit an explicit return statement,
#   Python will return None by default.
#
# - Multiple values returned are packed into a tuple,
#   which can be unpacked into individual variables.
# ----------------------------------------------------------------------------
