import re
regNumber = re.compile(r"\d+")

class Screen:

    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY

        #vytvori novy screen o velikosti X * Y
        screen = [ [" "]*self.sizeX ] * self.sizeY
        self.screen = []
        #vytvori deepcopy
        for line in screen:
            self.screen.append(line * 1)

    def __str__(self):
        result = ""
        for line in self.screen:
            result += " "*7 + " ".join(line)  + "\n"
        result = "Total: {0}, on {1}".format(self.sizeX*self.sizeY, result.count("■")) + "\n" + result
        return result

    def performAction(self, instruction):
        #kazda instrukce ma prave dve cisla, rozpoznani pomoci regex muzu pouzit v teto fci
        instrNumbers = [int(x) for x in regNumber.findall(instruction)]
        if "row" in instruction:
            self.__rotateRow(instrNumbers)
        elif "rect" in instruction:
            self.__rect(instrNumbers)
        elif "column" in instruction:
            self.__rotateColumn(instrNumbers)
        #pokud by ve vstupnich datech nerozpoznal instrukci
        else:
            print("INVALID")

    def __rotateRow(self, instrNumb):
        #zdvoji radek a usekne z vysledneho seznamu novy tak, aby se "posunul"
        row = (self.screen[instrNumb[0]]) * 2
        self.screen[instrNumb[0]] = row[self.sizeX-instrNumb[1]: - 1*instrNumb[1]]

    def __rotateScreen(self, count):
        #otoci screen o "count" otocek - pri otaceni sloupcu se jednoduseji hleda ten spravny
        for i in range(0,count):
            self.screen = list(reversed(list(zip(*self.screen)))) *1
        #predchozi radek vraci self.screen ve formatu tuple, nasledujici cyklus ho prevede zpet na list
        newScreen = []
        for row in self.screen:
            newRow = []
            for item in row:
                newRow.append(item)
            newScreen.append(newRow)
        self.screen = newScreen * 1

    def __rotateColumn(self, instrNumb):
        #3x otoci screen, posune radek (tzn. odpovidaji sloupec), 1x otoci screen do puvodni polohy
        self.__rotateScreen(3)
        row = list(reversed(self.screen[instrNumb[0]])) * 2
        self.screen[instrNumb[0]] = list(reversed(row[self.sizeY-instrNumb[1]: -1 * instrNumb[1]]))
        self.__rotateScreen(1)

    def __rect(self, coords):
        #vypise novy obdelnik
        for x in range(0, coords[1]):
            for y in range(0, coords[0]):
                self.screen[x][y] = "■"