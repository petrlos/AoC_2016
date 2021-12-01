#Advent of Code 2016 - Day 08
from Screen import Screen

#MAIN

with open("data.txt", "r") as file:
    instructions = file.read().splitlines()

testScreen = Screen(50,6)

for index, instruction in enumerate(instructions):
    testScreen.performAction(instruction)

print(testScreen)

