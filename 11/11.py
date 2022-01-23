#Advent of Code 2016: Day 11
from itertools import combinations
from collections import deque
from copy import deepcopy
import re

class Roomsetting():
    def __init__(self, rooms, elementCount):
        self.elevator = 0
        self.counter = 0
        self.rooms = rooms
        self.elementCount = elementCount
    def __str__(self):
        result = "Elevator at: {0}".format(self.elevator) + "\n"
        for index in range(3,-1,-1):
            result += "{0}: {1}".format(str(index), str(self.rooms[index])) + "\n"
        return result

    def roomFried(self):
        for room in self.rooms:
            roomComplete = " ".join(room)
            for item in room:
                element, type = item.split(" ")
                if type == "generator":
                    possibleMicrochip = "{0} microchip".format(element)
                    if possibleMicrochip in roomComplete:
                        roomComplete = roomComplete.replace(possibleMicrochip, "").replace(item, "")
            if "generator" in roomComplete:
                if "microchip" in roomComplete:
                    return True
        return False

    def statusVisited(self):
        status = "el{0} ".format(self.elevator)
        for floor, room in enumerate(self.rooms):
            status += str(floor) + str(" ".join(sorted(room)))
        return status

    def possibleLoad(self):
        load = [[item] for item in self.rooms[self.elevator]]
        pairs = list(combinations(self.rooms[self.elevator], 2))
        for pair in pairs:
            load.append(list(pair))
        return load

    def finalState(self):
        if len(self.rooms[3]) == self.elementCount:
            return True
        else:
            return False

def parseData(lines):
    reMicrochip = re.compile(r"\w+ microchip")
    reGenerator = re.compile(r"\w+ generator")
    rooms = []
    for line in lines:
        currentLine = line.replace("-compatible","")
        rooms.append(reMicrochip.findall(currentLine) + reGenerator.findall(currentLine))
    elements = set()
    for room in rooms:
        for item in room:
            elements.add(item)
    start = Roomsetting(rooms, len(elements))
    return start

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

start = parseData(lines)
print(start)
print("Let's roll:")
queue = deque()
queue.append(start)

visited = []
winners = []
while queue:
    directions = [[1], [1,-1], [1,-1], [-1]] #which direction possible from which floor
    for _ in range(len(queue)):
        currentState = queue[0]
        possibleLoad = currentState.possibleLoad()
        for direction in directions[currentState.elevator]:
            for load in possibleLoad:
                newState = deepcopy(currentState)
                for item in load:
                    newState.rooms[newState.elevator].remove(item)
                    newState.rooms[newState.elevator + 1*direction].append(item)
                newState.elevator += direction
                statusVisited = newState.statusVisited()
                if not newState.roomFried():
                    if statusVisited not in visited:
                        visited.append(statusVisited)
                        newState.counter += 1
                        if newState.finalState():
                            winners.append(newState.counter)
                            print("!!!!WINNER!!!!", newState.counter)
                        else:
                            queue.append(newState)
    print(len(queue), len(visited))
    queue.popleft()

print("Winners", winners)