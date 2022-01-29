#Advent of Code 2016: Day 11
from itertools import combinations
from collections import deque
from copy import deepcopy
from datetime import datetime
import re
timeStart = datetime.now()

class Roomsetting():
    def __init__(self, rooms, elementCount):
        self.elevator = 0
        self.counter = 0
        self.rooms = rooms
        self.elementCount = elementCount
        self.visited = []
    def __str__(self):
        result = "Elevator at: {0}, steps: {1}".format(self.elevator + 1, self.counter) + "\n"
        for index in range(3,-1,-1):
            result += "{0}: {1}".format(str(index+1), str(self.rooms[index])) + "\n"
        for visited in self.visited:
            result += visited + "\n"
        return result

    def roomFried(self):
        #if microchip is not protected with own generator, room is fried
        for room in self.rooms:
            for item in room:
                if "MC" in item:
                    protectingGen = item.split(" ")[0] + " G" #corresponding generator
                    if protectingGen not in room and "G" in " ".join(room):
                        return True
        return False

    def statusVisited(self):
        #generates string to check state inkl. elevator position
        status = "el{0} ".format(self.elevator+1)
        for floor, room in enumerate(self.rooms):
            status += "Fl:{1} {0} ".format(" ".join(sorted(room)), str(floor+1))
        return status

    def possibleLoad(self):
        #returns all possible loads depending on elevator position
        load = [[item] for item in self.rooms[self.elevator]]
        pairs = list(combinations(self.rooms[self.elevator], 2))
        for pair in pairs:
            load.append(list(pair))
        return load

    def finalState(self):
        #room 3 = top floor has all elements
        if len(self.rooms[3]) == self.elementCount:
            return True
        else:
            return False

def parseData(lines):
    reMicrochip = re.compile(r"\w+ MC")
    reGenerator = re.compile(r"\w+ G")
    rooms = []
    for line in lines:
        currentLine = line.replace("-compatible","").replace("microchip", "MC").replace("generator","G")
        rooms.append(reMicrochip.findall(currentLine) + reGenerator.findall(currentLine))
    elements = set()
    for room in rooms:
        for item in room:
            elements.add(item)
    start = Roomsetting(rooms, len(elements))
    return start

def findWinner(start):
    queue = deque()
    queue.append(start)
    visited = []
    while queue:  # brute force BFS
        directions = [[1], [1, -1], [1, -1], [-1]]  # which direction possible from which floor
        currentState = queue[0]
        possibleLoad = currentState.possibleLoad()
        for direction in directions[currentState.elevator]:  # up or down
            for load in possibleLoad:  # which load is possible
                newState = deepcopy(currentState)  # get new state as copy of current one
                for item in load:  # move elements along up/down
                    newState.rooms[newState.elevator].remove(item)
                    newState.rooms[newState.elevator + 1 * direction].append(item)
                newState.elevator += direction  # move elevetor
                statusVisited = newState.statusVisited()
                if not newState.roomFried():  # room fried?
                    if statusVisited not in visited:  # not yet visited?
                        newState.visited.append(statusVisited)
                        visited.append(statusVisited)
                        newState.counter += 1
                        if newState.finalState():  # got you! :)
                            return newState
                        else:  # not winner? add to queue
                            queue.append(newState)
            queue.popleft()  # delete last state
        if len(visited) % 5000 == 0:
            print("Nodes in queue: {0}, States checked: {1}, "
                  "total runtime {2}".format(len(queue), len(visited), datetime.now()- timeStart))

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

start = parseData(lines)

print(start)

winner = findWinner(start)
print(winner)