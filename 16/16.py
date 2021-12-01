#Advent of Code 2016: Day 16
def dragonCurve(input):
    #adds one zero to end of input
    input += "0"
    #adds opposite char, except extra zero
    for char in reversed(list(input[:-1])):
        if char == "0":
            input += "1"
        else:
            input += "0"
    return input

def checkSum(input):
    output = ""
    for i in range(0, len(input), 2):
        if input[i] == input[i+1]:
            output += "1"
        else:
            output += "0"
    return output

def generateCheckSum(input, length):
    while len(input) < length:
        input = dragonCurve(input)

    #cut string for desired length
    input = input[:length]

    while True:
        input = checkSum(input)
        if len(input) % 2 == 1:
            break

    return(input)


#MAIN
print("Check task1, should be 01100: ", end="")
print(generateCheckSum("10000",20))

print("Task1:",generateCheckSum("01111010110010011", 272))
print("Task2:",generateCheckSum("01111010110010011",35651584))