"""
Key Concepts:
- None represents the absence of a value and is the sole value of type NoneType.
- In Boolean contexts, None is treated as False.
- It's recommended to use 'is' when comparing with None.
"""

x = None

print(x)  # Output: None
# Explanation: x is assigned the value None, so printing x displays "None".

# -----------------------------------

# Conditional check to explain how None behaves in if-elif-else statements:
if x:
    # This block is not executed because None is evaluated as False in Boolean contexts.
    print("Do you think None is True?")
elif x is False:
    # This condition checks if x is exactly False.
    # Note: Even though None is treated as False, it is not the same as the Boolean False.
    print("Do you think None is False?")
else:
    # This block executes because x is neither True nor exactly False.
    # It emphasizes that None is a special value that is not equal to either True or False.
    print("None is not True, or False, None is just None...")
    # Expected Output: None is not True, or False, None is just None...
