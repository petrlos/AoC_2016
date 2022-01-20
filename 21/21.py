#Advent of Code - 2016 Day 21
import re
from itertools import permutations

def swap(line, string):
    if "position" in line:
        first, second = map(int, regNum.findall(line))
    else: #swap letters
        first, second = regLetter.findall(line)
        first = string.index(first[-1])
        second = string.index(second[-1])
    string[first], string[second] = string[second], string[first]
    return string

def rotate(line, string):
    if "left" in line:
        counter = list(map(int, regNum.findall(line)))[-1]
        for i in range(counter):
            string = string[1:] + [string[0]]
    elif "right" in line:
        counter = list(map(int, regNum.findall(line)))[-1]
        for i in range(counter):
            string = [string[-1]] + string[:-1]
    else: #based on letter
        counter = string.index(regLetter.findall(line)[-1][-1])
        if counter >= 4:
            counter += 1
        for i in range(counter+1):
            string = [string[-1]] + string[:-1]
    return string

def reverse(line, string):
    begin, end = map(int, regNum.findall(line))
    reversedString = list(reversed(string[begin:end+1]))
    string = string[:begin] + reversedString + string[end+1:]
    return string

def move(line, string):
    first, second = map(int, regNum.findall(line))
    removed = string.pop(first)
    string.insert(second, removed)
    return string

def scrambleString(string):
    for line in lines:
        if "swap" in line:
            string = swap(line, string)
        elif "rotate" in line:
            string = rotate(line, string)
        elif "reverse" in line:
            string = reverse(line, string)
        elif "move" in line:
            string = move(line, string)
    return "".join(string)

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
regNum = re.compile(r"\d+")
regLetter = re.compile(r"letter \w")

#Task1
string = list("abcdefgh")
print("Task 1:", scrambleString(string))

#Task2
passwords = list(permutations(string))
unscrambled = "fbgdceah"
passwordFound = False
index = 0
while not passwordFound: #check all permutations of "abcdefgh" to find unscrambled password
    result = scrambleString(list(passwords[index]))
    if result == unscrambled:
        passwordFound = True
    index += 1
print("Task 2:", "".join(passwords[index-1]))