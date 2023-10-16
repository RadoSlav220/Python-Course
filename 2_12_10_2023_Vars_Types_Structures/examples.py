# Collections
# tuple - Наредена n-торка, immutable
# list - mutable tuple
# set - HashSet
# dict - HashMap

tuple = (1, 2, 3)
tuple2 = 4, 5
list = [1, "string", False]
set = {1, 2, 3}
dict = {"a":1, "b":2, "c":3}

print(f"{set=}")
print(f"{tuple2=}")

# The keyword 'in' - check if element is part of a collection
print("miles" in "smiles") # True

# dict.values
# dict.keys

# Immutable types: int, float, complex, string, tuple, boolean 
head, *tail = [1, 2, 3, 4, 5]
first, *inbetween, last = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(f"{head=}, {tail=}")
print(f"{first=}, {inbetween=}, {last=}")