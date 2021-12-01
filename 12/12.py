#Advent of Code 2016 - Day 12

def runProgramm(registers):
    index = 0
    while index < len(instructions):
        instr = instructions[index].split(" ")
        if instr[0] == "cpy":
            if instr[1].isdigit():
                registers[instr[2]] = int(instr[1])
            else:
                registers[instr[2]] = registers[instr[1]]
        if instr[0] == "inc":
            registers[instr[1]] += 1
        if instr[0] == "dec":
            registers[instr[1]] -= 1
        if instr[0] == "jnz":
            #je potreba od jump odecist 1, protoze na konci cyklu se vzdy pricte 1
            if instr[1].isalpha():
                if registers[instr[1]] != 0:
                    index += int(instr[2]) - 1
            elif instr[1] != 0:
                index += int(instr[2]) - 1
        index += 1
    return registers["a"]

with open("data.txt", "r") as file:
    instructions = file.read().splitlines()

registers = {"a":0, "b": 0, "c": 0, "d":0}
task1 = runProgramm(registers)
print("Task 1:", task1)

registers = {"a":0, "b": 0, "c": 1, "d":0}
task2 = runProgramm(registers)

print("Task 2:", task2)