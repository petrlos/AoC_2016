#Advent of Code 2016 Day 11 - 2nd try :)
from collections import deque
from itertools import combinations
from datetime import datetime
import re

starttime = datetime.now()

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
    for item in currentRoom: #add all single items
        result.append([item])
    possibleLoads = combinations(currentRoom, 2) #find all possible pairs
    for load in possibleLoads: #and add them
        result.append(list(load))
    return result

def printState(state):
    #prints table of room content
    print("Elevator: {0}, steps: {1}".format(state[4],state[0:3]))
    for floor, room in enumerate(reversed(state[5:].split("#"))):
        print(4-floor, room)

def getNewRoomState(currentState, load, targetLocation): #location = new position of elevator
    for item in load:
        currentState = currentState.replace(item, "") #delete moved item from floor
    floors = currentState[5:].split("#")
    floors[targetLocation] += "".join(load) #replace load to new floor
    counter = str(int(currentState[:3]) + 1).zfill(3) #increase counter by one
    newState = counter + "#" + str(targetLocation) + "#".join(floors) #generate status properly
    return sortFloorContent(newState) #return alphabetically sorted

def checkAllOnTopFloor(roomState):
    floors = roomState[5:].split("#")
    for floor in floors[:-1]: #every floor except the last one must have the string length == 0
        if len(floor) > 0:
            return False
    return True

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

start = parseData(lines)
queue = deque([start])
visited = set(start[4:])

#which directions can elevator move - floor 0 only +1, floor 1 up and down etc
possibleDirections = [[+1], [-1, +1], [-1, +1], [-1]]

loopcounter = 1
while queue: #bfs
    if loopcounter % 10000 == 0:
        print("{2} Loops: states visited: {0}; states in queue: {1}".format(len(visited), len(queue), loopcounter))
    currentState = queue[0]
    elevatorLocation = int(currentState[4])
    currentFloor = triplets(currentState[5:].split("#")[elevatorLocation]) #from current state where elevator is
    possibleLoad = getPossibleLoad(currentFloor) #list of items, which could be moved
    for direction in possibleDirections[elevatorLocation]:
        for load in possibleLoad:
            newState = getNewRoomState(currentState, load, elevatorLocation + direction) #new location
            if checkAllOnTopFloor(newState):
                result = int(newState[:3])
                break
            else:
                if not roomFried(newState) and newState[4:] not in visited:
                    visited.add(newState[4:])
                    queue.append(newState)
    loopcounter += 1
    queue.popleft()

print(" ")
print("Steps needed to replace all items to top floor:",result)
print("Runtime:", datetime.now() - starttime)