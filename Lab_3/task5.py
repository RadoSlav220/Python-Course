import bisect

def arrayRankTransform(arr):
    sortNoDuplicates = sorted(set(arr))
    return [bisect.bisect_left(sortNoDuplicates, x) + 1 for x in arr]

print(arrayRankTransform([40,10,20,30]))