"""
This script demonstrates various escape sequences in Python.
An escape sequence is a series of characters that represents a special character.

Examples included:
    - Escaping single quotes in a string.
    - Using newline (\n) to break a line.
    - Printing a backslash (\\).
    - Using a tab (\t) to add spacing.
    - Using hex (\xhh) and octal (\ooo) representations.
    - Creating raw strings to ignore escape sequences.
"""

# Escaping a single quote:
print('Who\'s this?')  
# Expected output: Who's this?

# Using newline to print on separate lines:
print('Ishan\nKatoch')
# Expected output:
# Ishan
# Katoch

# Printing a backslash:
print("This is a backslash: \\")
# Expected output: This is a backslash: \

# Using a tab to add spacing:
print("Interview\tBit")
# Expected output: Interview    Bit

# Printing characters using hex values:
print("\x48\x45\x4C\x4C\x4F \x57\x4F\x52\x4C\x44")
# Expected output: HELLO WORLD

# Printing characters using octal values:
print("\110\105\114\114\117 \127\117\122\114\104")
# Expected output: HELLO WORLD

# Using a raw string to ignore escape sequence interpretation:
print(r"Hello\nWorld")
# Expected output: Hello\nWorld

# Demonstrating an invalid escape sequence (remains unchanged):
print("Ishan\cKatoch")
# Expected output: Ishan\cKatoch