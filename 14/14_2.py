#Advent of Code 2016: Day 14 Task 2
import hashlib
import re
from datetime import datetime
startTimer = datetime.now()

def generateHashWithIndex(starter, index):
    hash = starter + str(index)
    for _ in range(2017):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def checkKey(hash, start):
    triplet = re.search(regTriplet, hash)
    if triplet != None:
        triplet = 5* triplet.group()[0]
        for i in range(start+1, start+1001):
            if triplet in hashes[i]:
                return True
    return False

#MAIN:
salt = "zpqevtbw"
regTriplet = re.compile(r"(.)\1{2}")

print("Generating first 1000 hashes:")
hashes = []
#start sequence - first 1000 hashes
for index in range(1001):
    hashes.append(generateHashWithIndex(salt, index))

index = 1001
keys = []
while len(keys) < 64:
    hashes.append(generateHashWithIndex(salt, index))
    if checkKey(hashes[index-1000], index-1000):
        keys.append(index-1000)
        if len(keys) % 6 == 0:
            print(len(keys) // 6 * 10, "% done")
    index += 1

print("Result:", keys[-1])
print("Runtime:", datetime.now() - startTimer)