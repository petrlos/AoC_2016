#Advent of Code 2016: Day 17
from hashlib import md5
from collections import deque
from datetime import datetime
timeStart = datetime.now()

class Room:
    def __init__(self, location, path):
        self.location = location
        self.path = path

def tupleSum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def checkDoorOpen(path):
    # returns list [True/False, True/False, True/False, True/False] which door in direction UDLR are open/closed
    hash = md5(path.encode()).hexdigest()[:4]
    doorOpen = []
    for char in hash:
        if char in "bcdef":
            doorOpen.append(True)
        else:
            doorOpen.append(False)
    return doorOpen

#MAIN
passcode = "mmsxrhfx"
queue = deque()
queue.append(Room((0,0), passcode))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR
directionLetters = "UDLR"

paths = []
while queue: #classic BFS
    currentRoom = queue[0]
    doorOpen = checkDoorOpen(currentRoom.path)
    for index, door in enumerate(doorOpen):
        if door: #if door open
            newLocation = tupleSum(currentRoom.location, directions[index])
            x,y = newLocation
            if (x in range(4)) and (y in range(4)): #if room exists
                if newLocation == (3,3): #end reached - add path to paths list
                    path = (currentRoom.path + directionLetters[index])[len(passcode):]
                    paths.append(path)
                else: #end not reached - add to queue
                    newRoom = Room(newLocation, currentRoom.path + directionLetters[index])
                    queue.append(newRoom)
    queue.popleft()

print("Task 1:",min(paths, key=len)) #returns the string with minimal length in list
print("Task 1:",len(max(paths, key=len)))
print("Runtime:", datetime.now() - timeStart)