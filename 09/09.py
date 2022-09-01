# Advent of Code 2016 - Day 9

import re
def simpleTask1(text):
    position = 0
    counter = 0
    while position < len(text):
        if text[position] == "(":
            marker = re.search(regex, text[position:]).group()
            length, repeats = list(map(int, marker[1:-1].split("x")))
            position += length + len(marker)
            counter += length * repeats
        else:
            counter += 1
            position += 1
    return counter

def harderTask2(text):
    totalWeight = 0
    position = 0
    charWeights = [1] * len(text)
    while position < len(text):
        if text[position] != "(":
            totalWeight += charWeights[position]
            position += 1
        else:
            marker = re.search(regex, text[position:]).group()
            length, repeats = list(map(int, marker[1:-1].split("x")))
            start = position + len(marker)
            for i in range(start, start + length):
                charWeights[i] *= repeats
            position += len(marker)
    return totalWeight

#MAIN:
with open("data.txt") as file:
    text = file.readline()
regex = re.compile(r"\(\w+\)")

print("Task 1:", simpleTask1(text))
print("Task 2:", harderTask2(text))
