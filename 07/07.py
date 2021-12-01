#Advent of Code 2016: Day 7
import re

def findABBA(adressPart):
    for i in range(len(adressPart)-4):
        cutOf = adressPart[i: i+4]
        if (cutOf[1] == cutOf[2]) and (cutOf[0] == cutOf[3]) and (cutOf[0] != cutOf[1]):
            return True
    return False

def checkAdressABBA(outOf, inside):
    #pokud najde ABBA skupinu ve vnejsi casti a zaroven ji nenajde ve vnitrni, vrati True
    if findABBA(outOf) == True and findABBA(inside) == False:
            return True
    return False

def checkAdressSSL(outOf, inside):
    for i in range(len(outOf)-3):
        cutOf = outOf[i:i+3]
        #pokud je stejny prvni a posledni znak, prostredni neni zavorka a prostredni je jiny
        if cutOf[0] == cutOf[2] and cutOf[1] != "[" and cutOf[0] != cutOf[1]:
            turnOver = cutOf[1] + cutOf[0] + cutOf[1]
            if turnOver in inside:
                return True
    return False

#MAIN
with open("data.txt", "r") as file:
    adresses = file.read().splitlines()

#vnejsi cast je takova, ktera KONCI na [
#vnitrni cast konci vzdy na ]
rePartOutOfBracket = re.compile(r"[a-z]+\[")
rePartInBrackets = re.compile(r"[a-z]+]")

resultABBA, resultSLS = 0, 0

for line in adresses:
    #na konci line se pripise jedna [, aby regex vzal i poslendi vnitrni zavorku
    outOf = "".join(rePartOutOfBracket.findall(line.lower() + "["))
    inside = "".join(rePartInBrackets.findall(line.lower()))
    if checkAdressABBA(outOf, inside):
        resultABBA += 1
    if checkAdressSSL(outOf, inside):
        resultSLS += 1

print("Task 1:", resultABBA)
print("Task 2:", resultSLS)