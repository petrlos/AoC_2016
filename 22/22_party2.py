#Advent of Code 2016: Day 22
from collections import defaultdict, deque
import re

def tuple_sum(a,b):
    return tuple([x + y for x, y in zip(a,b)])

def create_grid(lines):
    reg_line = re.compile(r"\d+")
    grid = defaultdict(lambda: "#")
    for line in lines[1:]:
        x,y,size, used, avail, use_perc = list(map(int,reg_line.findall(line)))
        if used == 0:
            start = (x,y)
        elif used < 100: #empirically found
            grid[(x,y)] = "."
    max_x = max([coord[0] for coord in grid.keys()]) #horizontal size of a grid
    max_y = max([coord[1] for coord in grid.keys()]) #vertical size of a grid
    return grid, max_x, max_y, start

#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

grid, max_x, max_y, start, = create_grid(lines)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # UDLR

queue = deque([start])
distances = defaultdict(lambda: "", {start: 0})

while queue: #bfs - find distance to all points
    current_location = queue.popleft()
    for direction in directions:
        possible_location = tuple_sum(direction, current_location)
        if possible_location in grid.keys() and possible_location not in distances.keys():
            distances[possible_location] = distances[current_location] +1
            queue.append(possible_location)

print("Distance from start (empty packet) to (x_max-1, 0):",distances[(max_x-1, 0)])
print("Width:", max_x)
print("To move G packet ONE slot left, 5 moves must be done")
print("Start here:    End here:")
print(". - 0 - G      0 - G - .")
print(". - . - .      . - . - .")
print("(width - 1) * 5 +  +1 move to swap at the end.", end="\n\n")

result = sum([distances[(max_x-1, 0)], (max_x-1)*5, 1])
print("Totally: {0} + ({1}-1)*5 +1 = {2}".format(distances[(max_x-1, 0)],max_x, result))