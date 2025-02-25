x = "Hello World"
print(x, type(x))  # Output: Hello World <class 'str'>

x = 20
print(x, type(x))  # Output: 20 <class 'int'>

x = 20.5
print(x, type(x))  # Output: 20.5 <class 'float'>

x = 1j
print(x, type(x))  # Output: 1j <class 'complex'>

x = ["apple", "banana", "cherry"]
print(x, type(x))  # Output: ['apple', 'banana', 'cherry'] <class 'list'>

x = ("apple", "banana", "cherry")
print(x, type(x))  # Output: ('apple', 'banana', 'cherry') <class 'tuple'>

x = range(6)
print(x, type(x))  # Output: range(0, 6) <class 'range'>

x = {"name": "John", "age": 36}
print(x, type(x))  # Output: {'name': 'John', 'age': 36} <class 'dict'>

x = {"apple", "banana", "cherry"}
print(x, type(x))  # Output: {'apple', 'banana', 'cherry'} <class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(
    x, type(x)
)  # Output: frozenset({'apple', 'banana', 'cherry'}) <class 'frozenset'>

x = True
print(x, type(x))  # Output: True <class 'bool'>

x = b"Hello"
print(x, type(x))  # Output: b'Hello' <class 'bytes'>

x = bytearray(5)
print(x, type(x))  # Output: bytearray(b'\x00\x00\x00\x00\x00') <class 'bytearray'>

x = memoryview(bytes(5))
print(x, type(x))  # Output: <memory at 0x...> <class 'memoryview'>

x = None
print(x, type(x))  # Output: None <class 'NoneType'>
