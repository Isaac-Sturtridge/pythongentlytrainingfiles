
def area(length, width):
    return length * width

def perimeter(length, width):
    return length * 2 + width * 2

def volume(length, width, height):
    return length * width * height

def surfaceArea(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)



assert area(10, 10) == 100

assert area(0, 9999) == 0

assert area(5, 8) == 40

assert perimeter(10, 10) == 40

assert perimeter(0, 9999) == 19998

assert perimeter(5, 8) == 26

assert volume(10, 10, 10) == 1000

assert volume(9999, 0, 9999) == 0

assert volume(5, 8, 10) == 400

assert surfaceArea(10, 10, 10) == 600

assert surfaceArea(9999, 0, 9999) == 199960002

assert surfaceArea(5, 8, 10) == 340

height = int(input("enter height, if 2D enter 0: "))
width = int(input("enter width: "))
length = int(input("enter length: "))
calc = str(input("enter calculation, supported are 'area', 'perimeter', 'volume', 'surface area': "))

if calc == "area":
           print(area(length, width))

if calc == "perimeter":
           print(perimeter(length, width))

if calc == "volume":
           print(volume(length, width, height))

if calc == "surface area":
           print(surfaceArea(length, width, height))

