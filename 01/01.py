#Advent of Code 2016 - Day1
import re

regEx = re.compile(r"\d+")

directions = [(0,1), (1,0), (0,-1), (-1,0)]

with open("data.txt") as file:
    data = file.read().split(", ")

location = (0,0)
direction = 0
visited = []
hqFoudn = False

for instruction in data:
    distance = int(regEx.search(instruction).group())
    if instruction[0] == "R":
        direction += 1
    elif instruction[0] == "L":
        direction -= 1
    if direction == 4:
        direction = 0
    elif direction == -1:
        direction  = 3
    for i in range(0,distance):
        location = tuple(map(lambda x, y: x + y, location, directions[direction]))
        if location not in visited:
            visited.append(location)
        else:
            if not hqFoudn:
                hqLocation = location
                hqFoudn = True

print("Task1:",abs(location[0]) + abs(location[1]))
print("Task2:",abs(hqLocation[0]) + abs(hqLocation[1]))