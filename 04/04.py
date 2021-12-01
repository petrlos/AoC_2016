#Advent of Code 2016: Day 04
from Room import Room

#MAIN

with open("data.txt", "r") as file:
    rooms = file.read().replace("-","").splitlines()

validRooms = []
for room in rooms:
    newRoom = Room(room)
    if newRoom.valid:
        validRooms.append(newRoom)

task1result = sum([room.number for room in validRooms])
print("Task 1:", task1result)

for room in validRooms:
    if room.encode() != None:
        print("Task 2:", room.encode())


