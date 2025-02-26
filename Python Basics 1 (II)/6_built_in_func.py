"""
Python Built-in Functions Demonstration
-----------------------------------------
This script demonstrates various Python built-in functions such as:
    - abs(), all(), any(), ascii(), bin(), bool(), bytearray(), bytes(), callable(), chr(), complex()
    - dict(), dir(), divmod(), enumerate(), eval(), filter(), float(), format(), frozenset(), getattr()
    - globals(), hasattr(), hash(), hex(), id(), int(), isinstance(), iter(), len(), list(), map()
    - max(), min(), next(), oct(), open(), ord(), pow(), print(), range(), repr(), reversed(), round()
    - set(), sorted(), str(), sum(), tuple(), type(), vars(), zip()
    
Each example includes inline comments with the expected outcome.
"""

# abs() - absolute value
print("abs(-42) =", abs(-42))  # Expected output: 42

# all() - True if all items in iterable are True
print("all([True, 1, 'non-empty']) =", all([True, 1, "non-empty"]))  # Expected: True
print("all([True, 0, 'yes']) =", all([True, 0, "yes"]))  # Expected: False

# any() - True if any item in iterable is True
print(
    "any([0, '', None, False, 'Hello']) =", any([0, "", None, False, "Hello"])
)  # Expected: True

# ascii() - Returns a readable version of an object
print("ascii('ñandú') =", ascii("ñandú"))  # Expected: "'\\xf1and\\xfa'"

# bin() - Binary representation of a number
print("bin(42) =", bin(42))  # Expected output: '0b101010'

# bool() - Boolean value of an object
print("bool(0) =", bool(0))  # Expected output: False
print("bool(123) =", bool(123))  # Expected output: True

# bytearray() - Array of bytes
ba = bytearray("Hello", "utf-8")
print("bytearray('Hello', 'utf-8') =", ba)  # Expected output: bytearray(b'Hello')

# bytes() - Immutable bytes object
b = bytes("Hello", "utf-8")
print("bytes('Hello', 'utf-8') =", b)  # Expected output: b'Hello'


# callable() - Check if an object is callable (like a function)
def example_func():
    return "Called!"


print("callable(example_func) =", callable(example_func))  # Expected: True
print("callable(123) =", callable(123))  # Expected: False

# chr() - Converts an integer to a character (Unicode)
print("chr(65) =", chr(65))  # Expected output: 'A'

# complex() - Create a complex number
print("complex(2, 3) =", complex(2, 3))  # Expected output: (2+3j)

# dict() - Create a dictionary
d = dict(a=1, b=2)
print("dict(a=1, b=2) =", d)  # Expected output: {'a': 1, 'b': 2}

# dir() - List properties and methods of an object
print("dir(d) =", dir(d))  # Expected: List of dictionary attributes

# divmod() - Returns the quotient and remainder
print("divmod(10, 3) =", divmod(10, 3))  # Expected output: (3, 1)

# enumerate() - Enumerate indices and items in an iterable
for index, value in enumerate(["apple", "banana", "cherry"]):
    print(f"Index {index} -> {value}")
# Expected output:
# Index 0 -> apple
# Index 1 -> banana
# Index 2 -> cherry

# eval() - Evaluate a string as code
result = eval("3 * 7")
print("eval('3 * 7') =", result)  # Expected output: 21

# filter() - Filter elements from an iterable
nums = [0, 1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: (x % 2 == 0), nums))
print("Even numbers:", even_nums)  # Expected: [0, 2, 4]

# float() - Convert to floating point
print("float('3.14') =", float("3.14"))  # Expected: 3.14

# format() - Format values (here, format float to 2 decimals)
print("format(3.14159, '.2f') =", format(3.14159, ".2f"))  # Expected: '3.14'

# frozenset() - Immutable set
fs = frozenset([1, 2, 3, 2])
print("frozenset([1, 2, 3, 2]) =", fs)  # Expected: frozenset({1, 2, 3})


# getattr() - Get attribute value of an object
class Person:
    name = "Alice"


print("getattr(Person, 'name') =", getattr(Person, "name"))  # Expected: Alice

# globals() - Current global symbol table (print a few keys)
print("globals() keys:", list(globals().keys())[:10])

# hasattr() - Check if object has a given attribute
print("hasattr(Person, 'name') =", hasattr(Person, "name"))  # Expected: True

# hash() - Returns hash value of an object
print("hash('hello') =", hash("hello"))

# hex() - Hexadecimal representation of an integer
print("hex(255) =", hex(255))  # Expected: '0xff'

# id() - Returns identifier of an object
print("id(42) =", id(42))

# int() - Convert to integer
print("int('123') =", int("123"))  # Expected: 123

# isinstance() - Check object type
print("isinstance(123, int) =", isinstance(123, int))  # Expected: True

# iter() - Create an iterator
iter_obj = iter([10, 20, 30])
print("next(iter_obj) =", next(iter_obj))  # Expected: 10

# len() - Length of an object
print("len('Hello') =", len("Hello"))  # Expected: 5

# list() - Convert to list
print("list('ABC') =", list("ABC"))  # Expected: ['A', 'B', 'C']

# map() - Apply function to each item in an iterable
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))
print("Squared numbers:", squared)  # Expected: [1, 4, 9, 16]

# max() and min() - Largest and smallest items
print("max([1, 5, 3]) =", max([1, 5, 3]))  # Expected: 5
print("min([1, 5, 3]) =", min([1, 5, 3]))  # Expected: 1

# next() - Already used with iter()

# oct() - Octal representation of a number
print("oct(64) =", oct(64))  # Expected: '0o100'

# ord() - Get unicode of a character
print("ord('A') =", ord("A"))  # Expected: 65

# pow() - Power function
print("pow(2, 3) =", pow(2, 3))  # Expected: 8

# print() - Already used extensively.

# range() - Create a sequence of numbers
print("list(range(0, 5)) =", list(range(0, 5)))  # Expected: [0, 1, 2, 3, 4]

# repr() - Get string representation of an object
print("repr('Hello World') =", repr("Hello World"))

# reversed() - Return reverse iterator
print("list(reversed([1, 2, 3])) =", list(reversed([1, 2, 3])))  # Expected: [3, 2, 1]

# round() - Rounds a number
print("round(3.14159, 2) =", round(3.14159, 2))  # Expected: 3.14

# set() - Create a set
print("set([1, 2, 2, 3]) =", set([1, 2, 2, 3]))  # Expected: {1, 2, 3}

# sorted() - Return a sorted list
print("sorted([3, 1, 2]) =", sorted([3, 1, 2]))  # Expected: [1, 2, 3]

# str() - Convert to string
print("str(123) =", str(123))  # Expected: '123'

# sum() - Sum of an iterable
print("sum([1, 2, 3, 4]) =", sum([1, 2, 3, 4]))  # Expected: 10

# tuple() - Convert to tuple
print("tuple([1, 2, 3]) =", tuple([1, 2, 3]))  # Expected: (1, 2, 3)

# type() - Returns the type of an object
print("type(123) =", type(123))  # Expected: <class 'int'>


# vars() - Returns __dict__ for objects that have one
class Example:
    x = 10


print("vars(Example) =", vars(Example))  # Expected: {'x': 10, '__module__': ..., ...}

# zip() - Iterate over several iterables in parallel
for a, b in zip([1, 2, 3], ["a", "b", "c"]):
    print(f"zip pair: {a}, {b}")
# Expected:
# zip pair: 1, a
# zip pair: 2, b
# zip pair: 3, c
