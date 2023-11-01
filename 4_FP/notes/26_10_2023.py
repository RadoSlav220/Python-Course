def print_decorator(g):
    def inner():
        print("Hello")
        g()
    return inner

@print_decorator
def print_bye():
    print("bye")

# print_bye goes as first arg in print_decorator LOL

print_bye()

def log(f):
    def inner(*args, **kwargs):
        print(f'Calling {f} with {args} and {kwargs}')
        return f(*args, **kwargs)
    return inner

@log
def add(a, b):
    return a + b

print(add(2, 3))

import time

def time_it(f):
    def inner(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'{f} took {end - start:.2f} second')
    return inner

@time_it
def slow_function(a):
    return (a ** a) ** a

slow_function(1000)

(lambda x: print(x))(5)

l = [5, 2, 7, 3]
l.sort()
print(l)
l.sort(key=lambda x: -x)
print(l)



def generate_nth_perfect_square(n):
    return (n-1) ** 2

print(generate_nth_perfect_square(3))

def perfect_squares(n):
    for i in range(1, n+1):
        yield generate_nth_perfect_square(i)

print(perfect_squares(5))

perfect_square_generator = perfect_squares(5)
print(next(perfect_square_generator))
print(next(perfect_square_generator))
print(next(perfect_square_generator))
print(next(perfect_square_generator))

a = "str"
print(a ** 2)