# Function definition
def my_function():
    """
    This function prints a greeting message.
    """
    print("Hello from a function")


# Calling the function
my_function()
# Output: Hello from a function


# Function with one argument
def greet(name):
    """
    This function takes one argument 'name' and prints a greeting message.
    """
    print(f"Hello, {name}!")


# Calling the function with different arguments
greet("Alice")
# Output: Hello, Alice!
greet("Bob")
# Output: Hello, Bob!


# Function with multiple arguments
def full_name(first_name, last_name):
    """
    This function takes two arguments 'first_name' and 'last_name' and prints the full name.
    """
    print(f"{first_name} {last_name}")


# Calling the function with arguments
full_name("John", "Doe")
# Output: John Doe


# Function with default parameter value
def greet_country(country="Norway"):
    """
    This function takes an optional argument 'country' with a default value of 'Norway'.
    """
    print(f"I am from {country}")


# Calling the function with and without argument
greet_country("Sweden")
# Output: I am from Sweden
greet_country()
# Output: I am from Norway


# Function with arbitrary arguments (*args)
def kids_names(*kids):
    """
    This function takes an arbitrary number of arguments and prints the third one.
    """
    print(f"The youngest child is {kids[2]}")


# Calling the function with multiple arguments
kids_names("Emil", "Tobias", "Linus")
# Output: The youngest child is Linus


# Function with keyword arguments
def youngest_child(child1, child2, child3):
    """
    This function takes keyword arguments and prints the youngest child.
    """
    print(f"The youngest child is {child3}")


# Calling the function with keyword arguments
youngest_child(child1="Emil", child2="Tobias", child3="Linus")
# Output: The youngest child is Linus


# Function with arbitrary keyword arguments (**kwargs)
def child_info(**kid):
    """
    This function takes arbitrary keyword arguments and prints the last name.
    """
    print(f"His last name is {kid['lname']}")


# Calling the function with keyword arguments
child_info(fname="Tobias", lname="Refsnes")
# Output: His last name is Refsnes


# Function returning a value
def multiply(x):
    """
    This function takes one argument 'x' and returns its product with 5.
    """
    return 5 * x


# Calling the function and printing the result
print(multiply(3))
# Output: 15
print(multiply(5))
# Output: 25


# Recursive function
def tri_recursion(k):
    """
    This function demonstrates recursion by summing numbers from k to 0.
    """
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


# Calling the recursive function
print("Recursion Example Results:")
tri_recursion(6)
# Output:
# 1
# 3
# 6
# 10
# 15
# 21
