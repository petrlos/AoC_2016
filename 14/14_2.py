#Advent of Code 2016: Day 14 Task 2
#TODO: Day 14 Task2: first key working, last key not

import hashlib
import datetime
start = datetime.datetime.now()

def generateHashWithIndex(starter, index):
    hash = starter + str(index)
    for _ in range(2017):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def checkKey(hash, endIndex):
    triplets = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    for letter in triplets:
        if letter*3 in hash:
            for ind in range(endIndex-1000, endIndex):
                if letter*5 in hashes[ind]:
                    return True
    return False

salt = "abc"

hashes = []
#start sequence - first 1000 hashes
for index in range(1000):
    hashes.append(generateHashWithIndex(salt, index))



index = 1000
keys = []
while len(keys) < 65:
    newHash = generateHashWithIndex(salt, index)
    hashes.append(newHash)
    if checkKey(hashes[index-1000], index-1000):
        keys.append(index)
        print(index-1000, hashes[index-1000])

    index +=1

print(keys[-1])


print("Runtime:", datetime.datetime.now() - start)