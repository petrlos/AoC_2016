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

#MAIN:
with open("data.txt") as file:
    text = file.readline()
regex = re.compile(r"\(\w+\)")


print(simpleTask1(text))
