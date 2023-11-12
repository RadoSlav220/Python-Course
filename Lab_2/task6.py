# Write your code here:

def findForParticularM(list1, list2, m, i):
    return 0 if i < 0 or m-i >= len(list1) else list1[i] * list2[m-i] + findForParticularM(list1, list2, m, i-1)

def conv(list1, list2):
    length = len(list1)
    return [findForParticularM(list1, list2, m, min(m, length-1)) for m in range(0, 2*length-1)]

assert conv([1, 2, 3], [4, 5, 6]) == [4, 13, 28, 27, 18]
assert conv([1, 2, 3], [3, 2, 1]) == [3, 8, 14, 8, 3]

assert conv([2, 4, 6, 7], [-1, -2, -3, -4]) == [-2, -8, -20, -39, -48, -45, -28]

assert conv([1], [2]) == [2]
assert conv([], []) == []

"✅ All OK! +1.5 points"