#Advent of Code 2016 Day 18
from datetime import datetime
start = datetime.now()

def getNewLine(previousLine):
    willBecomeTrap = {"^^.": None, ".^^": None, "..^": None, "^..": None}
    newLine = ""
    previousLine = "." + previousLine + "."
    for index in range(0,len(previousLine)-2):
        slice = previousLine[index:index+3]
        if slice in willBecomeTrap.keys():
            newLine += "^"
        else:
            newLine += "."
    return newLine

def generateField(line, length):
    lines = [line]
    for _ in range(0, length - 1):
        newLine = getNewLine(lines[-1])
        lines.append(newLine)
    return "".join(lines).count(".")

#MAIN

firstLine = "^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^."

print("Task1:",generateField(firstLine, 40))
print("Runtime: ", datetime.now()-start)
print("Task2:",generateField(firstLine, 400000))
print("Runtime: ", datetime.now()-start)
