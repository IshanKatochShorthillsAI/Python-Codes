def add(num1, num2):
    """
    Add up two integer numbers.

    This function wraps the ``+`` operator and returns the sum of the two
    provided numbers. It is a simple example to illustrate how to write a
    comprehensive docstring.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
