class Parrot:
    """
    A simple Parrot class to illustrate basic object-oriented concepts.

    Attributes
    ----------
    name : str
        The name of the parrot.
    age : int
        The age of the parrot.
    """

    # Class attributes (default values)
    name = ""
    age = 0


# Create parrot1 object and set its attributes
parrot1 = Parrot()
parrot1.name = "Blu"
parrot1.age = 10

# Create parrot2 object and set its attributes
parrot2 = Parrot()
parrot2.name = "Woody"
parrot2.age = 15

# Access and print attributes of the parrot objects
print(f"{parrot1.name} is {parrot1.age} years old")
print(f"{parrot2.name} is {parrot2.age} years old")
