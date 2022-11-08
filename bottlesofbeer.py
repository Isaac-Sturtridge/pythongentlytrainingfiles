def bottlesOfBeer(numberOfBottles):
    for numberOfBottles in range(numberOfBottles, 0, -1):
        if numberOfBottles == 1: 
            print('One bottle of beer on the wall')
            print('One bottle of beer')
            print('Take one down')
            print('Pass it around')
            print('No more bottles of beer on the wall!')
        else:
            print(f'{numberOfBottles} bottles of beer on the wall')
            print(f'{numberOfBottles} bottles of beer')
            print('Take one down')
            print('Pass it around')
            if numberOfBottles == 2:
                print('1 bottle of beer on the wall')
            else:
                print(f'{numberOfBottles - 1} bottles of beer on the wall')
        print(' ')
number = int(input("Enter number: "))
bottlesOfBeer(number)