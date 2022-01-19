#Advent of Code 2016: Day 25
def runProgram(registerA):
    def decodeInput(input):
        if input.isalpha():
            return registers[input]
        else:
            return int(input)

    output = []
    registers = {"a": registerA, "b": 0, "c": 0, "d": 0}
    position = 0
    while position < len(lines):
        currentLine = lines[position].split(" ")
        if len(currentLine) == 3:
            instruction, what, where = currentLine
        else:
            instruction, where = currentLine

        if "dec" in instruction:
            registers[where] -= 1
        if "cpy" in instruction:
            registers[where] = decodeInput(what)
        if "jnz" in instruction:
            if decodeInput(what) != 0:
                position += decodeInput(where)
            else:
                position += 1
        else:
            position += 1
        if "inc" in instruction:
            registers[where] += 1
        if "out" in instruction:
            output.append(decodeInput(where))
            if len(output) > 9: #minimal count found out empirically
                return registerA
            for index, number in enumerate(output):
                if index % 2 != number:
                    return -1
#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

carryOn = True
registerA = 0
while carryOn:
    if runProgram(registerA) == registerA:
        carryOn = False
    else:
        registerA += 1

print("Task 1:",registerA)