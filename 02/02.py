#Advent of Code 2016 - Day 2

def getNewNumber(start, sequence):
    directions = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    for char in sequence:
        newCoord = tuple(map(lambda x, y: x + y, start, directions[char]))
        if decodeCoords(newCoord) != "#":
            start = newCoord
    return start

def decodeCoords(coord):
    return matrix[coord[1]][coord[0]]

#MAIN
with open("data.txt", "r") as file:
    inputData = file.read().splitlines()

#Task1: Simple Mask 3x3, numbers 1-9
start = (2,2) #Coords Nr 5
resultTask1 = ""
matrix = ["#####", "#789#", "#456#", "#123#" , "#####"]
for line in inputData:
    start = getNewNumber(start, line)
    resultTask1 += decodeCoords(start)

#Task2: Mask in maskTask2.txt saved
start = (1,3) #Coords from Nr5
resultTask2 = ""
with open("maskTask2.txt", "r") as file:
    matrix = file.read().splitlines()
for line in inputData:
    start = getNewNumber(start, line)
    resultTask2 += decodeCoords(start)

print("Task1:", resultTask1)
print("Task2:", resultTask2)