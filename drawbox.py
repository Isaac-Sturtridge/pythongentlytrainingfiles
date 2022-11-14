def drawBox(size):
    print(' ' * (size + 1) + '+' + '-' * size * 2 + '+')
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * size * 2 + '/' + ' ' * i + '|')
    print('+' + '-' * size * 2 + '+' + ' ' * size + '+')
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * size * 2 + '|' + ' ' * i + '/')
    print('+' + '-' * size * 2 + '+' + ' ' * size)

drawBox(1)
drawBox(2)
drawBox(3)
drawBox(4)
drawBox(5)
drawBox(6)