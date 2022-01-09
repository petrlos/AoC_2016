#Advent of Code 2016 Day 22
import re
from itertools import combinations

class Node:
    def __init__(self, path, size, used, avail, use):
        self.path = path
        self.size = size
        self.used = used
        self.avail = avail
        self.use = use

def parseData(lines):
    nodes = []
    for line in lines:
        data = regEx.findall(line)
        path, size, used, avail, use = data
        newNode = Node(path, int(size[:-1]), int(used[:-1]), int(avail[:-1]), int(use[:-1]))
        nodes.append(newNode)
    return nodes

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()
regEx = re.compile(r"\S+")

nodes = parseData(lines[2:])

viablePairs = 0
for first, node1 in enumerate(nodes):
    for second, node2 in enumerate(nodes):
        if (first != second) and (node1.used != 0) and (node1.used < node2.avail):
            viablePairs += 1

print("Task 1:",viablePairs)
