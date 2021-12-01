#Advent of Code 2016 - Day3
import re

def checkTriangle(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]

#MAIN
regExNumber = re.compile(r"\d+")

#Task1
with open("data.txt") as file:
    triangles = file.read().splitlines()

counter = 0
lines = []
for triangle in triangles:
    sides = [int(size) for size in regExNumber.findall(triangle)]
    lines.append(sides)
    if checkTriangle(sides):
        counter += 1
print("Task 1:",counter)

#Task2
#rotate array by 90dg
rotated = list(zip(*lines[::-1]))

counter = 0
for row in rotated:
    for i in range(0,len(row)-2, 3):
        if checkTriangle([row[i], row[i+1], row[i+2]]):
            counter += 1
print("Task 2:",counter)
