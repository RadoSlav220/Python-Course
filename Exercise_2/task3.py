list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3, 4, 5]
list_3 = []
list_4 = [1]
list_5 = [1, 2]


# Write your code here:
def pair_up(list):
    return [] if len(list) < 2 else [(list[0], list[1])] + pair_up(list[2:])

assert pair_up(list_1) == [(1, 2), (3, 4), (5, 6)]
assert pair_up(list_2) == [(1, 2), (3, 4)]  # We ignore the last element, if we cannot pair it up
assert pair_up(list_3) == []
assert pair_up(list_4) == []
assert pair_up(list_5) == [(1, 2)]

"✅ All OK! +0.5 points"