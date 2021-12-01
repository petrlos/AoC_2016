# Advent of Code 2016 - Day 13
from Office import Office
import bfs

testOffice = Office(10,7,10) #sizeX, sizeY, ODF
print(testOffice)
print("Test data, should be 11, result:",bfs.breadthFirstSearch(testOffice.office, 7, 4))


realOffice = Office(100, 100, 1352)
print(realOffice)
print("Task1:",bfs.breadthFirstSearch(realOffice.office, 31,39))
