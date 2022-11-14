def drawPyramid(height):
    for i in range(1, height + 1):
        print(" " * (height - i), end='')
        print("#" * ((i * 2) - 1), end='')
        print(" " * (height - i))

drawPyramid(8)
