def onlyFromFirstRow(s):
    return all(c in "qwertyuiop" for c in s)

def onlyFromSecondRow(s):
    return all(c in "asdfghjkl" for c in s)

def onlyFromThirdRow(s):
    return all(c in "zxcvbnm" for c in s)

def onlyFromASingleRow(s:str):
    return onlyFromFirstRow(s.lower()) or \
            onlyFromSecondRow(s.lower()) or \
            onlyFromThirdRow(s.lower())

def findWords(words):
    return [x for x in words if onlyFromASingleRow(x)]

words = ["Hello","Alaska","Dad","Peace"]
print(findWords(words))
