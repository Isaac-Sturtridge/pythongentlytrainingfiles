def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    mini = numbers[0]
    for number in numbers:
        if number < mini:
            mini = number
    return mini

def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    maxi = numbers[0]
    for number in numbers:
        if number > maxi:
            maxi = number
    return maxi

if __name__ == '__main__':
    choice = input("Big or Small:")

    if choice == "Big":
        try:
            numbers_list = []
            while True:
                numbers_list.append(int(input()))
        except:
            print(getBiggest(numbers_list))

    else:
        try:
            numbers_list = []
            while True:
                numbers_list.append(int(input()))
        except:
            print(getSmallest(numbers_list))





assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None
