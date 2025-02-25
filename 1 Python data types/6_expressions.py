# Constant Expressions
# A constant expression is an expression that always evaluates to the same result.
x = 15 + 1.3
print(x)  # Output: 16.3

# ---------

# Arithmetic Expressions
# Arithmetic expressions use arithmetic operators to perform calculations.
x = 40
y = 12

add = x + y  # Addition
sub = x - y  # Subtraction
mul = x * y  # Multiplication
div = x / y  # Division
mod = x % y  # Modulus

print(add)  # Output: 52
print(sub)  # Output: 28
print(mul)  # Output: 480
print(div)  # Output: 3.3333333333333335
print(mod)  # Output: 4

# ---------

# Integral Expressions
# Integral expressions involve only integers.
a = 13
b = 12.0
c = a + int(b)  # Convert float to int before addition
print(c)  # Output: 25

# ---------

# Floating Expressions
# Floating expressions involve floating-point numbers.
a = 13
b = 5
print(a / b)  # Output: 2.6

# ---------

# Relational Expressions
# Relational expressions compare two values and return a boolean result.
a = 21
b = 13
c = 40
d = 12

p = (a + b) >= (
    c - d
)  # True if the sum of a and b is greater than or equal to the difference of c and d
print(p)  # Output: True

# ---------

# Logical Expressions
# Logical expressions combine boolean values using logical operators.
P = 10 == 9  # False
Q = 7 > 5  # True

R = P and Q  # Logical AND
print(R)  # Output: False

S = P or Q  # Logical OR
print(S)  # Output: True

T = not P  # Logical NOT
print(T)  # Output: True

# ---------

# Bitwise Expressions
# Bitwise expressions perform bit-level operations on integers.
a = 12
x = a >> 2  # Right shift
y = a << 1  # Left shift

print(x, y)  # Output: 3 24

# ---------

# Combinational Expressions
# Combinational expressions use a combination of different types of operators.
a = 16
b = 12
c = a + (b >> 1)  # Right shift b by 1 and then add to a
print(c)  # Output: 22

# ---------

# Operator Precedence
# Operator precedence determines the order in which operators are evaluated.
# Multi-operator expression
a = 10 + 3 * 4  # Multiplication has higher precedence than addition
print(a)  # Output: 22

b = (10 + 3) * 4  # Parentheses change the order of evaluation
print(b)  # Output: 52

c = 10 + (3 * 4)  # Multiplication inside parentheses
print(c)  # Output: 22
