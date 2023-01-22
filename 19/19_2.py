#Advent of Code 2016: Day 19 - Part 2
def steal_present_opposite(count):
    elves = list(range(1, count+1))
    current_elf = 1 #elf number
    while len(elves) > 1:
        location_current_elf = elves.index(current_elf)
        opposite = len(elves) // 2 #index
        elves.pop((location_current_elf + opposite)%len(elves))
        location_current_elf = elves.index(current_elf)
        current_elf = elves[(location_current_elf + 1) % len(elves)]
        if len(elves) % 1000 == 0:
            print(len(elves))
    return elves[0]

#naive solution, used for testing and to create xlsx table, works reasonably quick up to +-10000 elves