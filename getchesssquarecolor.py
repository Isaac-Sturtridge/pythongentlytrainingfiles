def getChessSquareColor(column, row):
    if column >= 8 or column < 0 or row >= 8 or row < 0:
        return ''

    total = column + row
    if total % 2 == 0:
        return 'white'
    else:
        return 'black'

assert getChessSquareColor(1, 1) == 'white'

assert getChessSquareColor(2, 1) == 'black'

assert getChessSquareColor(1, 2) == 'black'

assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''

column = int(input("enter column: "))
row = int(input("enter row: "))

print(getChessSquareColor(column, row))
