def drawRectangle(width, height):
    if width < 0 or height < 0:
        return
    for row in range(height):
        print('#' * width, end='')
        print()

drawRectangle(10, 4)