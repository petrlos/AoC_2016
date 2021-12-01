#Advent of Code 2016 Day 13
from datetime import datetime
timeStart = datetime.now()
def createOffice(sizeX, sizeY, odf):
    office = []
    for y in range(sizeY):
        for x in range(sizeX):
            possilbleFurniture = bin((x * x + 3 * x + 2 * x * y + y + y * y) + odf)
            if possilbleFurniture.count("1") % 2 == 0:
                office.append((x,y))
    return office

def findNeighbours(midpoint):
    neighbours = []
    neighboursCoords = [(-1, 0), (1, 0), (0, 1), (0, -1)] #left right down up
    for deltaCoords in neigh                boursCoords:
        possibleNeighbour = tuple(map(lambda x, y: x + y, midpoint, deltaCoords))
        if possibleNeighbour in office:
            neighbours.append(possibleNeighbour)
    return neighbours

def breathFirstSearch(start, end):
    queue = [start]
    visited = {start: 0}
    while end not in queue:
        newNeigbours = findNeighbours(queue[0])
        for newNeighbour in newNeigbours:
            if newNeighbour not in visited.keys():
                visited.setdefault(newNeighbour, visited[queue[0]]+1)
                queue.append(newNeighbour)
        queue.pop(0)
        if len(queue) == 0 and end not in office:
            return -1
    return visited

#MAIN

#TEST OFFICE
office = createOffice(10, 10, 10)
start = (1,1); end = (7,4)
test = breathFirstSearch(start, end)
print("Test office:", test[end])

#REAL OFFICE
office = createOffice(100, 100, 1352)
start = (1,1); end = (31,39)
task1 = breathFirstSearch(start, end)
print("Task 1:", task1[end])

#TASK 2 - spocitej vsechny klice v seznamu visited, ktere maji vzdalenost <= 50
counter = 0
for coord in task1.keys():
    if task1[coord] <= 50:
        counter += 1

print("Task 2:",counter)

print("Runtime: ", datetime.now() - timeStart)