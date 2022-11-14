LOWER_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}

def getUpperCase(text):
    upperCaseText = ''
    for letter in text:
        if letter in LOWER_TO_UPPER:
            upperCaseText += LOWER_TO_UPPER[letter]
        else:
            upperCaseText += letter
    return upperCaseText

print(getUpperCase('hello'))
print(getUpperCase('Winter is coming'))