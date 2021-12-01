#Advent of Code 2016, Day 6
from collections import Counter

def mostFrequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def leastFrequent(line):
    minimal = len(line)
    result = ""
    for char in line:
        if line.count(char) < minimal:
            minimal = line.count(char)
            result = char
    return result

def decode(lines):
    task1, task2 = "", ""
    for line in lines:
        task1 += mostFrequent(line)
        task2 += leastFrequent(line)
    return [task1, task2]

#MAIN
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

result = decode(list(zip(*lines[::-1])))
print("Task 1:", result[0])
print("Task 2:", result[1])
