def ordinalSuffix(number):

    digits = str(number)
    if digits[-2:] in ('11', '12', '13'):
        return ''.join(digits) + 'th'
    else:
        if digits[-1] == '1':
            return ''.join(digits) + 'st'
        elif digits[-1] == '2':
            return ''.join(digits) + 'nd'
        elif digits[-1] == '3':
            return ''.join(digits) + 'rd'
        else:
            return ''.join(digits) + 'th'



assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'

number = int(input('Enter number: '))
print(ordinalSuffix(number))
