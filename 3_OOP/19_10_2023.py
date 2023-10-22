# we can hash only immutable objects!
# frozenset - immutable set
# p1 is p2 -> check if the 2 object are the same

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"{items[9] = }")
print(f"{items[-1] = }")
print()
print(f"{items[1:5] = }")
print(f"{items[1:] = }")
print(f"{items[:5] = }")
print(f"{items[:-1] = }")
print(f"{items[-6:-1] = }")
print()
print(f"{items[1:5:2] = }")
print(f"{items[1:5:-1] = }")
print(f"{items[5:1:-1] = }")
print()
print(f"{items[5::-1] = }")
print(f"{items[::-1] = }")
print(f"{items[:] = }")

# property is getter