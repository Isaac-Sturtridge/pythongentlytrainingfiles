import leapyear

def isValidDate(year, month, day):
    if month > 12 or month < 1:
        return False
    if day > 31 or day < 1:
        return False
    if month in [4, 6, 9, 11] and day == 31:
        return False
    if month == 2 and day > 29:
        return False
    if leapyear.isLeapYear(year) == False and month == 2 and day == 29:
        return False
    else:
        return True

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Date: "))
print(isValidDate(year, month, day))

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False