def calculateSum(numbers):
    ssum = 0
    for no in numbers:
        ssum += no
    return ssum

def calculateProduct(numbers):
    product = 1
    for no in numbers:
        product *= no
    return product


if __name__ == '__main__':
    choice = input("+ or *:")

    if choice == "+":
        try:
            sum_list = []
            while True:
                sum_list.append(int(input()))
        except:
            print(calculateSum(sum_list))
    if choice == "*":
        try:
            product_list = []
            while True:
                product_list.append(int(input()))
        except:
            print(calculateProduct(product_list))

assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840

    
