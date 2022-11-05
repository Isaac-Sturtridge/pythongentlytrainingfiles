def writeToFile(filename, text):
    with open(filename, 'w') as FileObj:
        FileObj.write(text)
        

def appendToFile(filename, text):
    with open(filename, 'a') as FileObj:
        FileObj.write(text)

def readFromFile(filename):
    with open(filename, 'r') as FileObj:
        return FileObj.read()

method = str(input("Enter W, A or R: "))
filename = str(input("Enter filename: "))
if method == "W" or method == "A":
    text = str(input("Enter text: "))

if method == "W":
    writeToFile(filename, text)

if method == "A":
    appendToFile(filename, text)

if method == "R":
    print(readFromFile(filename))
