import re

#definition of regEx
regNumber = re.compile(r"\d+")
regRoomChecksum = re.compile(r"\[\w+")  # add [1:] to replace "["
regRoomName = re.compile(r"[a-z]+-*")

class Room:

    def __init__(self, description):
        self.valid = True
        self.checkSum = regRoomChecksum.search(description).group()[1:] #[abcde]
        self.number = int(regNumber.search(description).group())
        self.name = regRoomName.search(description).group()

        self.__generateCheckSum()

    def __str__(self):
        return self.name + " " + str(self.number) + " " + self.checkSum

    def __checkValidity(self):
        """
        works for test, not for data, dont know why
        """
        for i in range(0,len(self.checkSum)-1):
            if self.checkSum[i] not in self.name:
                self.valid = False
            if self.name.count(self.checkSum[i]) < self.name.count(self.checkSum[i+1]):
                self.valid = False
            if self.name.count(self.checkSum[i]) == self.name.count(self.checkSum[i+1]):
                if self.checkSum[i] > self.checkSum[i+1]:
                    self.valid = False

    def __generateCheckSum(self):
        """
        vrati retezec setrizeny dle poctu, v pripade stejneho poctu podle abecedy
        """
        checkSum = "".join(list(sorted(set(self.name) - {'-'},
                                       key=lambda letter: (-self.name.count(letter), letter))))[:5]
        self.valid = (checkSum == self.checkSum)

    def encode(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        for char in self.name:
            startIndex = alphabet.find(char)
            endIndex = startIndex + self.number
            while endIndex > len(alphabet)-1:
                endIndex -= len(alphabet)
            result += alphabet[endIndex]
        if "north" in result:
            return self.number