# [f(item) for item in collection if p(item)]

numbers = [7, 12, 5, 6, 9, 15, 1, 11]

results = ["Yes" if number % 3 == 0 or number % 5 == 0 else "No" for number in numbers]

print(f'Results are: {results}')

# Speed comparison:
# for loop < list comprehension < map

def foo(x):
    return x + 1

list = [1, 2, 3, 4, 5]
l2 = [fx for x in list if (fx := foo(x)) % 2 == 0]
print(l2)

""" PATERN MATCHING REQUIRES PYTHON 10

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

operation = input('Enter an operation (+, -, * or /)')

match operation:
    case '+':
        result = first_number + second_number
    case '-':
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case '/':
        result = first_number / second_number
    case _:
        print('Operation not supported')

print(f'{first_number} {operation} {second_number} = {result}')
"""

l = ['a', 'b', 'c']
for item in enumerate(l):
    print(item)
