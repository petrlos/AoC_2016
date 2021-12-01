#Advent of Code 2106 - Day 5
import hashlib

def task1(input):
    print("Searching password for task1: ")
    result = ""
    index = 1
    while len(result) < 8:
        textToEncode = input + str(index)
        hashNumber = hashlib.md5(textToEncode.encode()).hexdigest()
        if hashNumber[0:5] == "0" * 5:
            result += hashNumber[5]
            print("Position {0}/8 found".format(len(result)))
        index += 1
    return result

def task2(input):
    result = {"0":None, "1":None, "2": None, "3": None, "4": None, "5":None, "6":None, "7":None}
    print("Searching password for task2: ")
    index = 1
    numbersFound = 0
    while numbersFound < 8:
        textToEncode = input + str(index)
        hashNumber = hashlib.md5(textToEncode.encode()).hexdigest()
        if hashNumber[0:5] == "0" * 5:
            if hashNumber[5] in result.keys():
                if result[hashNumber[5]] == None:
                    result[hashNumber[5]] = hashNumber[6]
                    numbersFound += 1
                    print("Position {0}/8 found".format(numbersFound))
        index += 1
    password = ""
    for i in range(0,8):
        password += result[str(i)]
    return password

#MAIN
input = "ffykfhsq"

print("Task1:",task1(input))
print("Task2:",task2(input))
