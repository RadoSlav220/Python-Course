from functools import reduce

matrix_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_2 = [
    [2, 3, 4, 5],
    [5, 6, 7, 8],
    [9, 1, 6, 3],
    [-2, 3, 7, 7]
]

matrix_3 = []

# Write your code here

# Using list comprehension and sum.
def sum_main_diagonal(matrix):
    return sum([matrix[i][i] for i in range(0, len(matrix))])

def sum_second_diagonal(matrix):
    return sum([matrix[i][len(matrix)-i-1] for i in range(0, len(matrix))])

def power_of_matrix(matrix):
    return sum_main_diagonal(matrix) - sum_second_diagonal(matrix)

# Using map and reduce
def plus(a, b):
    return a + b

def power_of_matrix(matrix):
    def indexValue(i):
        return matrix[i][i] - matrix[i][len(matrix)-i-1]
    return reduce(plus, map(indexValue, range(0, len(matrix))), 0)

assert power_of_matrix(matrix_1) == 0
assert power_of_matrix(matrix_2) == 10
assert power_of_matrix(matrix_3) == 0

"✅ All OK! +0.5 points"