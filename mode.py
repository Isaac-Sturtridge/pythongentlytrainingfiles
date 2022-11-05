def mode(numbers):
    if numbers == []:
        return None
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return max(counts, key=counts.get)

if __name__ == '__main__':
    try:
        numbers = []
        while True:
            numbers.append(int(input()))
    except:
        print(mode(numbers))

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4