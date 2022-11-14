def commaFormat(number):
    number = str(number)
    if '.' in number:
        fraction = number[number.index('.'):]
        number = number[:number.index('.')]
    else:
        fraction = ''

    commaNumber = ''

    triplet = ''

    for i in range(len(number) -1, -1, -1):
        triplet = number[i] + triplet
        if len(triplet) == 3:
            commaNumber = triplet + ',' + commaNumber
            triplet = ''

    if triplet != '':
        commaNumber = triplet + ',' + commaNumber
    return commaNumber[:-1] + fraction

print(commaFormat(10000.3431))
        