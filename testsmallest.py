import random, getsmallest

numbers = []
for i in range(10000):
    numbers.append(random.randint(1, 1000000))
print('Numbers:', numbers)
print('Smallest number is', getsmallest.getSmallest(numbers))
