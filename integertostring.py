DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

def convertIntToStr(integerNum):
    if integerNum == 0:
        return '0'

    stringNum = ''
    
    if integerNum < 0:
        isNegative = True
        integerNum = -integerNum
    else:
        isNegative = False

    while integerNum > 0:
        onesPlaceDigit = integerNum % 10
        stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
        integerNum = integerNum // 10

    if isNegative:
        return '-' + stringNum
    else:
        return stringNum


print(convertIntToStr(-500))
print(convertIntToStr(500))


for i in range(-10000, 10000):

    assert convertIntToStr(i) == str(i)