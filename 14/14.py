#Advent of Code 2016 - Day 14
from hashlib import md5

def checkTriplet(hash):
    triplets = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    for index in range(len(hash)):
        cutOff = hash[index:index+3]
        for letter in triplets:
            if cutOff == letter * 3:
                return letter
    return -1

def checkQuinquets(hashes, letter):
    for hash in hashes:
        if letter * 5 in hash:
            return True
    return False
#MAIN

salt = "zpqevtbw"

hashes = []
index = 0
counter = 1

for index in range(1001):
    textToEncode = salt + str(len(hashes))
    hash = md5(textToEncode.encode()).hexdigest()
    hashes.append(hash)

results = []
index = 0
while counter < 65:
    letter = checkTriplet(hashes[index])
    if letter != -1:
        if checkQuinquets(hashes[index+1:index + 1001], letter):
            results.append("{}: {}, {}".format(counter, index, hashes[index]))
            counter += 1
    index += 1
    textToEncode = salt + str(len(hashes))
    hash = md5(textToEncode.encode()).hexdigest()
    hashes.append(hash)

print("Task 1:", results[-1])

