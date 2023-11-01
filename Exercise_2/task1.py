def square(x):
    return x * x

def double(x):
    return 2 * x

def sum_(x, y):
    return x + y

# Write your code here:
def compose(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

assert compose(square, double)(5) == 100
assert compose(double, square)(5) == 50

h = compose(square, double)
assert h(5) == 100

assert compose(double, sum_)(2, 3) == 10
assert compose(square, sum_)(x=2, y=4) == 36

"✅ All OK! +0.25 points"