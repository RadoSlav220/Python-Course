import os
import re

class InvalidLineError(Exception):
    def __init__(self, line: str) -> None:
        super().__init__(line)

class InvalidItemError(Exception):
    def __init__(self, item: str) -> None:
        super().__init__(item)

class InvalidQuantityError(Exception):
    def __init__(self, item: str, count: str) -> None:
        super().__init__(item + count)

class InvalidPriceError(Exception):
    def __init__(self, item: str, price: str) -> None:
        super().__init__(item + price)

class ListFileError (Exception):
    def __init__(self, path: str) -> None:
        super().__init__(path)

def validate_list(path: str) -> float:
    try:
        fd = open(path)
    except OSError:
        raise ListFileError(path)

    line = None
    totalPrice = 0
    try:
        while line != '':
            line = fd.readline()
            if line != '':
                totalPrice += validate_line(line)
    finally:
        fd.close()
    return totalPrice


def validate_line(line: str) -> float:
    data = validate_line_structure(line)
    itemName = validate_item_name(data[0][1::])

    try:
        quantity = int(data[1])
    except ValueError:
        raise InvalidQuantityError(itemName, data[1])
    
    if quantity < 0:
        raise InvalidQuantityError(itemName, data[1])
    
    try:
        singlePrice = float(data[2])
    except ValueError:
        raise InvalidPriceError(itemName, data[2])
    
    if singlePrice < 0:
        raise InvalidPriceError(itemName, data[2])

    return quantity * singlePrice

def validate_line_structure(line: str) -> list[str]:
    data = line.split(':')
    if not re.match(r'-.*:.*:.*', line) or len(data) != 3:
        raise InvalidLineError(line)
    return data

def validate_item_name(name: str) -> None:
    itemName = name.strip()
    if len(itemName) == 0 or itemName.isnumeric():
        raise InvalidItemError(name)
    return name
    
assert abs(validate_list(os.path.join("lab04_files", "task_1", "list1.txt")) - 11.25) < 0.001

assert int(validate_list(os.path.join("lab04_files", "task_1", "list2.txt"))) == 0, "Empty files should return 0"

try:
    validate_list(os.path.join("lab04_files", "task_1", "list3.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list4.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list5.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidItemError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list6.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list7.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list8.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidQuantityError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list9.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list10.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidPriceError:
    pass

try:
    validate_list(os.path.join("lab04_files", "task_1", "list11.txt"))
    assert False, "Should raise InvalidLineError"
except InvalidLineError:
    pass

"✅ All OK! +2 points"