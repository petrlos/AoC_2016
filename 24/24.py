#Advent of Code 2016 Day 24:
from itertools import combinations, permutations
from datetime import datetime
begin = datetime.now()

#zajisti, ze poradi bodu pri vypoctu vzdalenosti bude vzdy ve formatu [mensi][vetsi]
def sortIndexes(first, second):
    if first > second:
        first, second = second, first
    return first, second

def getCoords(value):
    for key in map.keys():
        if map[key] == value:
            return key

def findNeighbours(midpoint):
    neighbours = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        neighbour = tuple([sum(x) for x in zip(direction,midpoint)])
        if neighbour in map.keys():
            neighbours.append(neighbour)
    return neighbours

def bfs(start, end):
    queue = [start]
    visited = {start:0}
    while end not in queue:
        newNeighbours = findNeighbours(queue[0])
        for newNeighbour in newNeighbours:
            if newNeighbour not in visited.keys():
                visited.setdefault(newNeighbour, visited[queue[0]]+1)
                queue.append(newNeighbour)
        queue.pop(0)
        if len(queue) == 0 and end not in map:
            return -1
    return visited[end]

def countDistanceOnRoute(route):
    distance = 0
    for index in range(len(route)-1):
        cutOf = route[index: index+2]
        step1, step2 = sortIndexes(cutOf[0], cutOf[1])
        distance += distances[step1+step2]
    return distance

#MAIN:
with open("data.txt", "r") as file:
    fileMap = file.read().split("\n")

#ulozi mapu do formatu volne policko:souradnice, zdi ignoruje
map = {}
for x,line in enumerate(fileMap):
    for y,char in enumerate(list(line)):
        if char != "#":
            map.setdefault((x,y), char)

#vygeneruje seznam kombinaci bodu, ktere je potreba projit
points = list(filter(lambda x: x != ".", map.values()))
combinations = list(combinations(points, 2))

#provede BFS u vsech kombinaci bodu a ulozi je dict distance
distances = {}
for combination in combinations:
    start, end = sortIndexes(combination[0], combination[1])
    startCoord = getCoords(start); endCoord = getCoords(end)
    distances.setdefault(map[startCoord] + map[endCoord], bfs(startCoord, endCoord))

#permutace vsech moznych cest z indexu 1-7, provede jejich soucet slicovanim retezce z dictionary distances
#variant je pouze 7!, tzn. zhruba 5000, bruteforce v tomto pripade nevadi :)
resultTask1 = {}; resultTask2 = {}
possibleRoutes = permutations(list(range(1,len(points))))
for possibleRoute in possibleRoutes:
    route = "0" + "".join(str(x) for x in possibleRoute)
    distance = countDistanceOnRoute(route) #spocita vzdalenost 0 + permutace
    resultTask1.setdefault(route, distance)
    route = route + "0"
    distance = countDistanceOnRoute(route) #spocita vzdalenost 0 + permutace + 0
    resultTask2.setdefault(route, distance)

print("Task 1:", min(resultTask1.values()))
print("Task 2:",min(resultTask2.values()))
print("Total runtime: ", datetime.now() - begin)