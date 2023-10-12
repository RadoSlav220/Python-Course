from math import inf, pi
from sys import getsizeof

a = 42
print("a =",a)
a = "random string"
print("a =",a)
del a
a = 12
print("a =",a)

# Three numerical types: int, float, complex
# Numeric operations: +, -, *, /, ** , //, % 

print(6 ** 2)      # -> 36
imaginary = 3 + 2j # -> 3 + 2i
print(7 // 2)      # -> 3

print(1 / inf)     # -> 0
# But division by 0 does not give us inf

print("size of 1 is:", getsizeof(1), "bytes")                      # -> 28 bytes lol
print("size of 2 ** 30 is:", getsizeof(2 ** 30), "bytes")          # -> 32 bytes
print("size of 3.5 is:", getsizeof(3.5), "bytes")                  # -> 24 bytes
print("size of 3.5 ** 105 is:", getsizeof(3.5 ** 105), "bytes")    # -> 24 bytes
# Float always has the same size because of the precision that we get (default precision: 18 signs after dec point)

# Integer values can be expressed in binary (0b1010), octa (0o12) or hex (0xA) 

# Strings - random length, using "" or ''
s1 = "hello"
s2 = 'world'
print(s1 + " " + s2)

# Multiline string are written using """ """
multi_line_string = """first line
second line
third one
final"""
print(multi_line_string)

# Unicode symbols are supported
# Functions to convert from and to ASCII symbols:
print(ord('A')) 
print(chr(65))

# Formatting strings
archaic = "Hey, %s, how old are you? Are you %d?" % ("Radoslav", 20)
print(archaic)

classic = "{} only knows first 5 digits of π: {:.5f}.".format("Silvia", pi)
print(classic)

some_variable = 0xdeadbeef
fstr = f"fstring: {some_variable}"
print(fstr)
fstr_withVarName = f"fstring: {some_variable=}"
print(fstr_withVarName)

s = "hello"
print(len(s))
print(s[0])
for char in s:
    print("===" + char + "===")
# There are also many built-in string functionalities like replace, split, lower etc.
print("HElLo".lower()) # -> hello

# Boolean 
# Instead of !, ||, && we use not, or, and

t = True
f = not t

print(f"{f = }")
print(f"{t or f = }")
print(f"{t and f = }")
print(f"{t and not f = }")

# Every non zero number converts True, zero converts to False
# "And" and "Or" do not return boolean. They return first element that defines the outcome of the operation
a, b, c = 1, 2, 3
print(f"{a or b or c = }")
print(f"{a and b and c = }")
print(f"{a or 0 or c = }")
print(f"{a and 0 and c = }")
# a or b or c = 1
# a and b and c = 3
# a or 0 or c = 1
# a and 0 and c = 0

# None - like void, empty return type
# type - returns the type of an object
print(type(42)) # -> <class 'int'>

