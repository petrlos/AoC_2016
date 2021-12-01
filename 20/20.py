#Advent of Code 2016: Day 20

from datetime import datetime
start = datetime.now()

#zkontroluje, jestli cislo je nebo neni v intervalu
#tzn. jestli je >= nez dolni mez a zaroven <= nez horni mez
def findNumberInInterval(number):
    for line in intervals:
        if number >= line[0] and number <= line[1]:
            return True
    return False

#nacte cisla a prevede je na int
with open("data.txt", "r") as file:
    intervals = [x.split("-") for x in file.read().splitlines()]
for index, line in enumerate(intervals):
    intervals[index] = [int(x) for x in line]

intervals = sorted(intervals)

#nejmensi cislo, ktere neni v intervalu, je min z mnoziny cisel na horni hranici intervalu +1
result = []
for line in intervals:
    checkedNumber = line[1] + 1
    if not findNumberInInterval(checkedNumber):
        result.append(checkedNumber)
print("Task 1:",min(result))

lastNumnber = 4294967295

#Task 2:

number = 0
numbers = []
while number <= lastNumnber:
    found = False
    for interval in intervals:
        if number >= interval[0] and number <= interval[1]:
            found = True
            number = interval[1] + 1
            break
    if not found:
        numbers.append(number)
        number += 1

print("Task 2:", len(numbers))
print("Runtime:",datetime.now() - start)