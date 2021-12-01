#Advent of Code 2016: Day 19
from datetime import datetime
start = datetime.now()

elvesCount = 6
currentElf = 0

print("Pracuje v rozumnem case pro zhruba 10000 elfu, reseni viz 19_2.txt")

elves = {}
for i in range(elvesCount):
    elves.setdefault(i, 1)

while max(elves.values()) < elvesCount:
    if currentElf in elves.keys():
        steelFrom = currentElf
        while True:
            steelFrom = (steelFrom + 1) % elvesCount
            if steelFrom in elves.keys():
                break
        elves[currentElf] += elves[steelFrom]
        elves.pop(steelFrom)
    currentElf = (currentElf + 1) % elvesCount

for key in elves.keys():
    if elves[key] > 0:
        print(key+1)

print("Runtime:", datetime.now() - start)