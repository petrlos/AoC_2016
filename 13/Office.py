class Office:

    def __init__(self, x, y, odf):
        self.x = x
        self.y = y
        #Officer's designer favourite
        self.odf = odf
        self.office = []

        #create office grid
        for i in range(0,y):
            row = []
            for j in range(0,x):
                row.append(1)
            self.office.append(row)

        #put furniture in place
        self.__furniture()

    def __str__(self):
        result = ""
        for row in self.office:
            result += "".join([str(cell) for cell in row]) + "\n"
        return result.replace("1","#").replace("0", ".")

    def __furniture(self):
        for x in range(self.x):
            for y in range(self.y):
                codeForPositin = bin((x*x + 3*x + 2*x*y + y + y*y)+ self.odf)
                if codeForPositin.count("1") % 2 != 0:
                    self.office[y][x] = 0