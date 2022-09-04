#Advent of Code 2016 Day 11 - 2nd try :)
from collections import deque
from itertools import combinations
import re

def sortFloorContent(roomStatus):
    #sorts room content alphabetically
    roomsSorted = []
    for room in roomStatus[5:].split("#"):
        roomsSorted.append("".join(sorted(triplets(room))))
    return roomStatus[:5] + "#".join(roomsSorted)

def triplets(s): #cuts string to a list of triplets
    return [s[i:i + 3] for i in range(0, len(s), 3)]

def parseData(lines):
    rooms = []
    regMicrochip = re.compile(r"\w+-com")
    regGenerator = re.compile(r"\w+ gen")
    for line in lines:
        roomContent = regMicrochip.findall(line) +  regGenerator.findall(line)
        singleRoom = ""
        for item in roomContent:
            if " gen" in item:
                singleRoom += (item[:2]+"G").upper()
            elif "-com" in item:
                singleRoom += (item[:2]+"M").upper()
        rooms.append(singleRoom)
    result = sortFloorContent("000#0" + "#".join(rooms))
    return result

def roomFried(roomState): #True = room is fried - not valid to be used in queue
    #HYG HYM LIG is ok - HYM is protected by HYG, LIG has no power here
    #vs. HYM LIG LIM is fried - HYM is not protected
    for floor in roomState[5:].split("#"):
        for item in triplets(floor):
            if "M" in item: #item is a microchip
                if "G" in floor and item[:2]+ "G" not in floor:
                    #generator in room AND microchip not protected -> room fried
                    return True
    return False

def getPossibleLoad(currentRoom):
    result = []
    for item in currentRoom:
        result.append([item])
    possibleLoads = combinations(currentRoom, 2)
    for load in possibleLoads:
        result.append(list(load))
    return result

def printState(state):
    #prints table of room content
    print("Elevator: {0}, steps: {1}".format(state[4],state[0:3]))
    for floor, room in enumerate(reversed(state[5:].split("#"))):
        print(4-floor, room)

def getNewRoomState(currentState, load, direction):
    #TODO: not working yet
    newState = ""
    return currentState

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

start = parseData(lines)
queue = deque([start])
visited = [start[4:]]

#which directions can elevator move - floor 0 only +1, floor 1 up and down etc
possibleDirections = [[+1], [-1, +1], [-1, +1], [+1]]

while queue:
    currentState = queue[0]
    elevatorLocation = int(currentState[4])
    currentFloor = triplets(currentState[5:].split("#")[elevatorLocation]) #from current state where elevator is
    possibleLoad = getPossibleLoad(currentFloor)
    for direction in possibleDirections[elevatorLocation]:
        for load in possibleLoad:
            newState = getNewRoomState(currentState, load, direction)
            if not roomFried(newState) and newState[4:] not in visited:
                visited.append(newState[4:0])
                queue.append(newState)


    #TODO: check win - everything on top - print counter, queue = []

    queue.popleft()
