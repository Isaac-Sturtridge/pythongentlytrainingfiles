def median(numbers):
    if numbers == []:
        return None
    numbers.sort()
    middleIndex = int(len(numbers) / 2)
    # odd retrieves middle number (index is len / 2 - 1)
    if len(numbers) % 2 == 1:
        return numbers[middleIndex]
    # even retrieves average of middle numbers (indexes are len/2 and len/2-1)
    else:
        return (numbers[middleIndex] + numbers[middleIndex - 1]) / 2

if __name__ == '__main__':
    try:
        numbers = []
        while True:
            numbers.append(int(input()))
    except:
        print(median(numbers))

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6