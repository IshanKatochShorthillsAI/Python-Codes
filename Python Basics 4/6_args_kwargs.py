def sum_args(*args):
    """
    Return the sum of all the positional arguments.

    *args collects any number of non-keyword arguments into a tuple, allowing
    you to pass a variable number of arguments.

    Parameters
    ----------
    *args : tuple of int or float
        A variable-length tuple of numbers to be summed.

    Returns
    -------
    int or float
        The sum of all provided arguments.

    Examples
    --------
    >>> sum_args(1, 2, 3)
    6
    >>> sum_args(5, 10, 15)
    30
    """
    return sum(args)


def print_kwargs(**kwargs):
    """
    Print all key-value pairs passed as keyword arguments.

    **kwargs collects any number of keyword arguments into a dictionary,
    allowing you to access them with their respective keys.

    Parameters
    ----------
    **kwargs : dict
        A dictionary of keyword arguments.

    Returns
    -------
    None

    Examples
    --------
    >>> print_kwargs(a=1, b=2, c=3)
    a: 1
    b: 2
    c: 3
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def combined_example(*args, **kwargs):
    """
    Demonstrate using both positional (*args) and keyword (**kwargs) arguments.

    Parameters
    ----------
    *args : tuple
        Positional arguments.
    **kwargs : dict
        Keyword arguments.

    Returns
    -------
    tuple
        A tuple containing:
        - A tuple of all positional arguments.
        - A dictionary of all keyword arguments.

    Examples
    --------
    >>> combined_example(1, 2, 3, a=4, b=5)
    ((1, 2, 3), {'a': 4, 'b': 5})
    """
    return args, kwargs


# Demonstration of the functions
if __name__ == "__main__":
    print("Sum of positional arguments:")
    print(sum_args(1, 2, 3, 4))  # Expected output: 10

    print("\nPrinting keyword arguments:")
    print_kwargs(x=100, y=200, z=300)
    # Expected output:
    # x: 100
    # y: 200
    # z: 300

    print("\nCombined usage of *args and **kwargs:")
    result = combined_example(10, 20, flag=True, mode="test")
    print(result)
    # Expected output: ((10, 20), {'flag': True, 'mode': 'test'})
