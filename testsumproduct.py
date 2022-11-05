import numbers
import random, calculateSumProduct

numbers = []
for i in range(10000):
    numbers.append(random.randint(1, 10000000))
print('Numbers: ', numbers)
print('Sum is: ', calculateSumProduct.calculateSum(numbers))
print('Product is: ', calculateSumProduct.calculateProduct(numbers))