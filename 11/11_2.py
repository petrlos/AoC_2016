#Advent of Code 2016 Day 11 - 2nd try :)
from collections import deque
import re

def sortRoomContent(roomStatus):
    #sorts room content alphabetically
    roomsSorted = []
    for room in roomStatus[1:].split("#"):
        roomsSorted.append("".join(sorted([room[i:i + 3] for i in range(0, len(room), 3)])))
    return roomStatus[0] + "#".join(roomsSorted)

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
    result = sortRoomContent("0" + "#".join(rooms))
    return result

def roomFried():
    #pokud obsahuje chip, ktery nema odpovidajici generator
    #napr. HG + HM + LG je ok
    return True

def printState(state):
    #prints table of room content
    print("Elevator: ", state[0])
    for floor, room in enumerate(reversed(state[1:].split("#"))):
        print(4-floor, room)

#MAIN
with open("test.txt") as file:
    lines = file.read().splitlines()

start = parseData(lines)
printState(start)