#Advent of Code 2016 - Day1
def tuple_sum(a, b):
    return tuple([x + y for x, y in zip(a, b)])

def manh_distance(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

directions = [(0,1), (1,0), (0,-1), (-1,0)] #ULDR
turn = dict(zip("LR", [+1, -1]))

with open("data.txt") as file:
    data = file.read().split(", ")

location = (0,0)
direction = 0
visited = []
hq_found = 0

for instruction in data:
    direction = (direction + turn[instruction[0]]) % 4
    distance = int(instruction[1:])
    for i in range(distance):
        location = tuple_sum(location, directions[direction])
        if location in visited and not hq_found:
            hq_found = location
        visited.append(location)

print("Task 1:",manh_distance(visited[-1], (0,0)))
print("Task 2:",manh_distance(hq_found, (0,0)))
