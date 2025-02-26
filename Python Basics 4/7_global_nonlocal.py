# Global variable example
x = 10


def modify_global():
    """
    Modify the global variable 'x' using the global keyword.

    The global keyword allows the function to update the variable defined
    outside its scope. Without declaring 'x' as global, assignment inside the
    function would create a new local variable instead.

    Returns
    -------
    int
        The updated value of the global variable 'x'.

    Examples
    --------
    >>> x = 10
    >>> modify_global()
    20
    >>> x
    20
    """
    global x
    x = x + 10
    return x


def nonlocal_example():
    """
    Demonstrate the use of the nonlocal keyword in nested functions.

    In this example, the outer function defines a local variable 'x' which is
    then modified by the inner function using nonlocal. This allows the inner
    function to update the variable defined in the enclosing scope rather than
    creating a new local variable.

    Returns
    -------
    str
        The modified value of the nonlocal variable 'x'.

    Examples
    --------
    >>> nonlocal_example()
    'hello'
    """
    x = "John"

    def inner_change():
        nonlocal x
        x = "hello"

    inner_change()
    return x


if __name__ == "__main__":
    print("Global variable before modification:", x)
    print("Calling modify_global() ->", modify_global())
    print("Global variable after modification:", x)

    print("\nNonlocal variable example:")
    result = nonlocal_example()
    print("Result from nonlocal_example():", result)
