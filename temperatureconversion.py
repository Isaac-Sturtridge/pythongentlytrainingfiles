


def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9/5) + 32
    


def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5/9)


choice = input("Enter desired output C or F: ")
degrees = int(input("Enter the amount in degrees in the other scale: "))

if choice == "C":
    print(convertToCelsius(degrees))

if choice == "F":
    print(convertToFahrenheit(degrees))

assert convertToCelsius(0) == -17.77777777777778

assert convertToCelsius(180) == 82.22222222222223

assert convertToFahrenheit(0) == 32

assert convertToFahrenheit(100) == 212

assert convertToCelsius(convertToFahrenheit(15)) == 15


# Rounding errors cause a slight discrepancy:

assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
