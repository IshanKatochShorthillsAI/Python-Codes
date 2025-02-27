class Computer:
    """
    A Computer class demonstrating encapsulation by hiding the maximum price
    attribute.

    Attributes
    ----------
    __maxprice : int
        The maximum selling price of the computer (private attribute).
    """

    def __init__(self):
        self.__maxprice = 999

    def sell(self):
        """
        Prints the selling price of the computer.

        Expected output: Selling price: <current max price>
        """
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        """
        Sets a new value for the maximum selling price.

        Parameters
        ----------
        price : int
            The new maximum selling price.
        """
        self.__maxprice = price


# Create an object of the Computer class
c = Computer()
c.sell()  # Expected output: Selling price: 999

# Attempt to change __maxprice directly.
# This does not change the internal __maxprice due to name mangling;
# instead, it creates a new attribute in the instance.
c.__maxprice = 1000
c.sell()  # Expected output: Selling price: 999

# Using the setter function to change the private attribute __maxprice
c.setMaxPrice(1000)
c.sell()  # Expected output: Selling price: 1000
