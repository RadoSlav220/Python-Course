# Task 1
def seconds_to_time(seconds):
    secs = seconds % 60
    mins = seconds // 60 % 60
    hours = seconds // 3600
    return (hours, mins, secs)

print(seconds_to_time(0) == (0, 0, 0))
print(seconds_to_time(1) == (0, 0, 1))
print(seconds_to_time(69) == (0, 1, 9))
print(seconds_to_time(420) == (0, 7, 0))
print(seconds_to_time(3661) == (1, 1, 1))
print(seconds_to_time(86399) == (23, 59, 59))


# Task 2
def number_of_vowels(text):
    vowelCount = 0
    for i in text:
        if (isVowel(i)):
            vowelCount += 1
    return vowelCount

def isVowel(letter):
    return letter in ['a', 'o', 'i', 'e', 'u', 'A', 'O', 'I', 'E', 'U']

print(number_of_vowels("grrrrgh!") == 0)
print(number_of_vowels("The quick brown fox jumps over the lazy dog.") == 11)
print(number_of_vowels("MONTHY PYTHON") == 2)

# Task 3
DIGIT_MULTIPLIERS = [2, 4, 8, 5, 10, 9, 7, 3, 6]

def is_valid_UCN(ucn, should_bypass_checksum=False):
    ucn = str(ucn)
    if len(ucn) != 10:
        return False
    year = int(ucn[:2])
    month = int(ucn[2:4])
    day = int(ucn[4:6])
   
    return is_month_valid(month) and\
            is_day_valid(day, month, year) and\
            (should_bypass_checksum or is_last_digit_correct(ucn)) 

def is_month_valid(month):
    return month in range(1, 13) or month in range(41, 53) 

def is_day_valid(day, month, year):
    if month in range(41, 53):
        month -= 40
        year += 2000
    else:
        year += 1900

    return (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31) or\
            (month in [4, 6, 9, 11] and 1 <= day <= 30) or\
            (month == 2 and 1 <= day <= 28) or\
            (month == 2 and is_year_lear(year) and 1 <= day <= 29)

def is_year_lear(year):
    return (year % 4 == 0 and year % 100 != 0) or\
            (year % 400 == 0)

def is_last_digit_correct(ucn):
    weightedSum = calculateWeightedSum(ucn)
    return getCorrectLastDigit(weightedSum) == (int)(ucn[9])

def calculateWeightedSum(ucn):
    sum = 0
    for i in range(0, 9):
        sum += int(ucn[i]) * DIGIT_MULTIPLIERS[i]
    return sum

def getCorrectLastDigit(weightedSum):
    remainder = weightedSum % 11
    return 0 if remainder == 10 else remainder

print(is_valid_UCN("6101057509") == True)
print(is_valid_UCN("6101057500", should_bypass_checksum=True) == True)
print(is_valid_UCN("6101057500") == False)
print(is_valid_UCN("6913136669") == False)