x = 1.10
y = -35.0

print(x, type(x))  # Output: 1.1 <class 'float'>
print(y, type(y))  # Output: -35.0 <class 'float'>

# ----

x = 35e3
y = -87.7e100

print(x, type(x))  # Output: 35000.0 <class 'float'>
print(y, type(y))  # Output: -8.77e+101 <class 'float'>

# -----

x = 3 + 5j
y = -5j

print(x, type(x))  # Output: (3+5j) <class 'complex'>
print(y, type(y))  # Output: -5j <class 'complex'>

# -----

x = 1
y = 2.8
z = 2j

a = float(x)
b = int(y)
c = complex(x)

print(a, type(a))  # Output: 1.0 <class 'float'>
print(b, type(b))  # Output: 2 <class 'int'>
print(c, type(c))  # Output: (1+0j) <class 'complex'>

# -----
