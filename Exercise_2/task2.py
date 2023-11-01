# ---Internal state, do not touch---
counters = {
    'pass_instantly': 0,
    'pass_after_third_try': 0,
    'pass_after_fifth_try': 0,
    'never_pass': 0,
}

# Write your code here:
def retry(func):
    def inner(attempt, *args, **kwargs):
        return False if attempt == 3 else func(*args, **kwargs) or inner(attempt+1, *args, **kwargs)
    return lambda *args, **kwargs: inner(0, *args, **kwargs)

# Tests
@retry
def pass_instantly():
    counters['pass_instantly'] += 1
    return True

@retry
def pass_after_third_try():
    counters['pass_after_third_try'] += 1
    return counters['pass_after_third_try'] == 3

@retry
def pass_after_fifth_try():
    counters['pass_after_fifth_try'] += 1
    return counters['pass_after_fifth_try'] == 5

@retry
def never_pass():
    counters['never_pass'] += 1
    return False


assert pass_instantly() == True
assert counters['pass_instantly'] == 1
assert pass_after_third_try() == True
assert counters['pass_after_third_try'] == 3
assert pass_after_fifth_try() == False
assert counters['pass_after_fifth_try'] == 3
assert never_pass() == False
assert counters['never_pass'] == 3

"✅ All OK! +0.5 points"