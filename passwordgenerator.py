import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = LOWER_LETTERS.upper()
NUMBERS = '0123456789'
SPECIAL = '~!@#$%^&*()_+'

ALLCHARACTERS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def generatePassword(length):
    if length < 12:
        length = 12
    password = []
    password += LOWER_LETTERS[random.randint(0, 25)]
    password += UPPER_LETTERS[random.randint(0, 25)]
    password += NUMBERS[random.randint(0, 9)]
    password += SPECIAL[random.randint(0, 12)]
    for i in range(length - 4):
        password += ALLCHARACTERS[random.randint(0,74)]
    random.shuffle(password)
    return ''.join(password)

length = int(input("Enter length: "))
print(generatePassword(length))

assert len(generatePassword(8)) == 12

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWER_LETTERS:

        hasLowercase = True

    if character in UPPER_LETTERS:

        hasUppercase = True

    if character in NUMBERS:

        hasNumber = True

    if character in SPECIAL:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial