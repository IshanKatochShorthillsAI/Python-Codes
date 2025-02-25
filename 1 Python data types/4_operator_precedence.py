# Demonstrating Operator Precedence and Associativity in Python

# Precedence of '+' & '*'
# '*' has higher precedence than '+', so the multiplication is performed first.
expr = 10 + 20 * 30
print(expr)  # Output: 610

# ---------

# Precedence of 'or' & 'and'
# 'and' has higher precedence than 'or', so the 'and' condition is evaluated first.
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")  # Output: Hello! Welcome.
else:
    print("Good Bye!!")

# ---------

# Using parentheses to change precedence
# Parentheses alter the default precedence, so the 'or' condition is evaluated first.
name = "Alex"
age = 0

if (name == "Alex" or name == "John") and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")  # Output: Good Bye!!

# ---------

# Associativity of Python Operators

# Left-right associativity
# 100 / 10 * 10 is calculated as (100 / 10) * 10 and not as 100 / (10 * 10)
print(100 / 10 * 10)  # Output: 100.0

# Left-right associativity
# 5 - 2 + 3 is calculated as (5 - 2) + 3 and not as 5 - (2 + 3)
print(5 - 2 + 3)  # Output: 6

# Demonstrating the effect of parentheses
print(5 - (2 + 3))  # Output: 0

# Right-left associativity
# 2 ** 3 ** 2 is calculated as 2 ** (3 ** 2) and not as (2 ** 3) ** 2
print(2**3**2)  # Output: 512

# --------

# Operators Precedence and Associativity in Python
# Demonstrating a complex expression with multiple operators
expression = 100 + 200 / 10 - 3 * 10
print(expression)  # Output: 70.0

# --------

# Non-associative Operators
# Demonstrating an invalid operation with non-associative operators
a = 5
b = 10
c = 15

# This line will cause a syntax error because '<' and '+=' are non-associative
# a = b = (a < b) += (b < c)
