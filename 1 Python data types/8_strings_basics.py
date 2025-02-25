# ---------------------------------------------------------------------------
# Strings Basics in Python
# This file demonstrates various operations with strings including:
# - Basic printing of strings
# - Multiline strings
# - Accessing characters in a string (arrays)
# - Looping through strings
# - Getting the length of strings
# - Checking for substrings
# ---------------------------------------------------------------------------

# Basic String Printing
print("Hello")
print("Hello")

# ---------------------------------------------------------------------------
# Quotes Inside Quotes
# Demonstrates how to use single and double quotes appropriately when one needs to
# include quotes inside a string.
print("It's alright")  # Using double-quotes to enclose a string with a single quote.
print("He is called 'Johnny'")  # Single quotes inside a double-quoted string.
print('He is called "Johnny"')  # Double quotes inside a single-quoted string.

# ---------------------------------------------------------------------------
# Assigning a String to a Variable
a = "Hello"
print(a)

# ---------------------------------------------------------------------------
# Multiline Strings
# Multiline strings allow the string to span several lines.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# We can also assign another identical multiline string to demonstrate usage.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# ---------------------------------------------------------------------------
# Strings as Arrays
# Strings can be treated as sequences (arrays) of characters.
a = "Hello, World!"
print(a[1])  # Prints the second character ('e').

# ---------------------------------------------------------------------------
# Looping Through a String
# Each character in the string "banana" is printed on a new line.
for x in "banana":
    print(x)

# ---------------------------------------------------------------------------
# String Length
# The len() function returns the number of characters in the string.
a = "Hello, World!"
print(len(a))  # Output: 13

# ---------------------------------------------------------------------------
# Check if a String Contains a Substring
# The 'in' keyword checks for the presence of a substring.
txt = "The best things in life are free!"
print("free" in txt)  # Output: True

# ---------------------------------------------------------------------------
# Check if a String Does NOT Contain a Substring
# The 'not in' keyword returns True if the substring is not present.
txt = "The best things in life are free!"
print("expensive" not in txt)  # Output: True
