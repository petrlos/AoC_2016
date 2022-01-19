#Advent of Code 2016: Day 23

def decodeInput(input):
    if input.isalpha():
        return registers[input]
    else:
        return int(input)
#MAIN
with open("data.txt") as file:
    lines = file.read().splitlines()

registers = {"a": 7, "b": 0, "c": 0, "d":0}
print("Starting `a` at: ", registers["a"])
position = 0
while position < len(lines):
    currentLine =  lines[position].split(" ")
    if len(currentLine) == 3:
        instruction, what, where = currentLine
    else:
        instruction, where = currentLine

    if "dec" in instruction:
        registers[where] -= 1
    if "tgl" in instruction:
        if position + decodeInput(where) in range(len(lines)):
            toggledLine = lines[position + decodeInput(where)]
            instructionCount = len(toggledLine.split(" "))
            if instructionCount == 3: #two argument line
                if "jnz" in toggledLine:
                    newInstruction = "cpy"
                else:
                    newInstruction = "jnz"
            else: #one argument line
                if "inc" in toggledLine:
                    newInstruction = "dec"
                else:
                    newInstruction = "inc"
            lines[position + decodeInput(where)] = newInstruction + toggledLine[3:]
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

print("Result Task1:", registers["a"])