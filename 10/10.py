#Advent of Code 2016: Day 10
def allDone(lines):
    for line in lines:
        if line != "":
            return False
    return True

def getTargets(line):
    targets = reTarget.findall(line)
    cleanedTargets = []
    for target in targets:
        cleanedTargets.append(target[0])
    return cleanedTargets

import re
from collections import Counter
from functools import reduce

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

reNum = re.compile(r"\d+")
reBot = re.compile(r"bot \d+")
reTarget = re.compile(r"((bot|output) \d+)")

bots = {}
#Inicializace:
for index, line in enumerate(lines):
    if "value" in line:
        bot = reBot.search(line).group()
        bots.setdefault(bot, [])
        bots[bot].append(int(reNum.search(line).group()))
        lines[index] = ""

task1 = []

while not allDone(lines):
    for index, line in enumerate(lines):
        targets = getTargets(line)
        if len(targets) > 0:
            if targets[0] in bots.keys():
                if len(bots[targets[0]]) == 2:
                    lowHigh = [min(bots[targets[0]]), max(bots[targets[0]])]
                    if 17 in lowHigh or 61 in lowHigh:
                        task1.append(targets[1])
                        task1.append(targets[2])
                    for i in range(1,3,1):
                        if targets[i] in bots.keys():
                            bots[targets[i]].append(lowHigh[i-1])
                        else:
                            bots.setdefault(targets[i], [])
                            bots[targets[i]].append(lowHigh[i-1])
                    bots[targets[0]] = []
                    lines[index] = ""


task1 = (Counter(task1))
print(task1)
#bot 147 ma dve navstevy, byla to spravna odpoved.. proc nebyla 195 resp. 30, ktera ma taky dve navstevy, nevim :)

task2 = []
reNum = re.compile(r"\d+")
for key in bots.keys():
    if "output" in key:
        number = int(reNum.search(key).group())
        if number in [0,1,2]:
            task2.append(bots[key][0])

print("Task2:", reduce(lambda x, y: x * y, task2))