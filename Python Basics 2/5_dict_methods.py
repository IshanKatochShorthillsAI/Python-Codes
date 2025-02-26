"""
1. clear()       - Removes all elements from the dictionary.
2. copy()        - Returns a shallow copy of the dictionary.
3. fromkeys()    - Creates a new dictionary from a sequence of keys with a specified value.
4. get()         - Returns the value associated with a key; if the key doesn't exist, returns a default value.
5. items()       - Returns a view object of the dictionary's key-value pairs.
6. keys()        - Returns a view object of the dictionary's keys.
7. pop()         - Removes a specified key and returns its value.
8. popitem()     - Removes and returns the last inserted key-value pair.
9. setdefault()  - Returns the value of a key if it exists; otherwise inserts the key with a default value.
10. update()     - Updates the dictionary with key/value pairs from another dictionary or iterable.
11. values()     - Returns a view object of the dictionary's values.
"""


def demo_clear():
    # Demonstrates clear(): Removes all elements from the dictionary.
    mydict = {"a": 1, "b": 2, "c": 3}
    mydict.clear()
    print("After clear():", mydict)
    # Expected output: {}


def demo_copy():
    # Demonstrates copy(): Returns a shallow copy of the dictionary.
    original = {"a": 1, "b": 2}
    copied = original.copy()
    print("Original:", original)
    print("Copied:", copied)
    # Expected output:
    # Original: {'a': 1, 'b': 2}
    # Copied: {'a': 1, 'b': 2}


def demo_fromkeys():
    # Demonstrates fromkeys(): Creates a new dictionary from a sequence of keys with the same value.
    keys = ["a", "b", "c"]
    new_dict = dict.fromkeys(keys, 0)
    print("New dictionary from keys:", new_dict)
    # Expected output: {'a': 0, 'b': 0, 'c': 0}


def demo_get():
    # Demonstrates get(): Returns the value for a key, or a default value if the key is missing.
    mydict = {"a": 1, "b": 2}
    value = mydict.get("a")
    missing = mydict.get("c", "Not Found")
    print("Value for 'a':", value)  # Expected output: 1
    print("Value for 'c':", missing)  # Expected output: Not Found


def demo_items():
    # Demonstrates items(): Returns a view of the dictionary's key-value pairs.
    mydict = {"a": 1, "b": 2}
    items = mydict.items()
    print("Dictionary items:", items)
    # Expected output: dict_items([('a', 1), ('b', 2)])


def demo_keys():
    # Demonstrates keys(): Returns a view of the dictionary's keys.
    mydict = {"a": 1, "b": 2}
    keys = mydict.keys()
    print("Dictionary keys:", keys)
    # Expected output: dict_keys(['a', 'b'])


def demo_pop():
    # Demonstrates pop(): Removes a key and returns its value.
    mydict = {"a": 1, "b": 2, "c": 3}
    value = mydict.pop("b")
    print("Popped value for 'b':", value)
    print("After pop:", mydict)
    # Expected output:
    # Popped value: 2
    # Dictionary: {'a': 1, 'c': 3}


def demo_popitem():
    # Demonstrates popitem(): Removes and returns the last inserted key-value pair.
    mydict = {"a": 1, "b": 2, "c": 3}
    pair = mydict.popitem()
    print("Popped item:", pair)
    print("After popitem:", mydict)
    # Expected output (if last inserted is 'c'):
    # Popped item: ('c', 3)
    # Dictionary: {'a': 1, 'b': 2}


def demo_setdefault():
    # Demonstrates setdefault(): Returns the value for a key if it exists; otherwise inserts the key with a default value.
    mydict = {"a": 1, "b": 2}
    result_existing = mydict.setdefault("a", 100)
    result_new = mydict.setdefault("c", 3)
    print("Result for existing key 'a':", result_existing)
    print("Result for new key 'c':", result_new)
    print("Dictionary after setdefault:", mydict)
    # Expected output:
    # For key 'a': 1 (existing value)
    # For key 'c': 3 (newly set)
    # Dictionary: {'a': 1, 'b': 2, 'c': 3}


def demo_update():
    # Demonstrates update(): Updates the dictionary with key/value pairs from another dictionary.
    mydict = {"a": 1, "b": 2}
    update_data = {"b": 3, "c": 4}
    mydict.update(update_data)
    print("Dictionary after update:", mydict)
    # Expected output: {'a': 1, 'b': 3, 'c': 4}


def demo_values():
    # Demonstrates values(): Returns a view of the dictionary's values.
    mydict = {"a": 1, "b": 2}
    values = mydict.values()
    print("Dictionary values:", values)
    # Expected output: dict_values([1, 2])


def main():
    print("Python Dictionary Methods Learning Module\n")
    demo_clear()
    demo_copy()
    demo_fromkeys()
    demo_get()
    demo_items()
    demo_keys()
    demo_pop()
    demo_popitem()
    demo_setdefault()
    demo_update()
    demo_values()


if __name__ == "__main__":
    main()
