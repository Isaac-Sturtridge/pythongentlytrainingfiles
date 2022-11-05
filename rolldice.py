import random

def rollDice(numberOfDice):
    total = 0
    for i in range(1, numberOfDice + 1):
        total += random.randint(1,6)
    return total

dice = int(input("Enter number of dice: "))
print(rollDice(dice))

assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600
