DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def convertStrToInt(stringNum):
    integerNum = 0
    if stringNum[0] == '-':
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False
    for i in range(len(stringNum)):
        digit = DIGITS_STR_TO_INT[stringNum[i]]
        integerNum = (integerNum * 10) + digit
    
    if isNegative:
        return -integerNum
    else:
        return integerNum

print(convertStrToInt('150'))
print(convertStrToInt('-150'))



for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i