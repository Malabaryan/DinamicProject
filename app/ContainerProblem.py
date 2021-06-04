class ContainerProblem:
    def __init__(self, maxWeight, elementsWeight, elementsProfit, loops):
        self.maxWeight = maxWeight
        self.weights = elementsWeight
        self.profits = elementsProfit
        self.loop = loops

        #to track the combination that gave the maximum profit
        self.maxProfit = 0
        self.itemList = []

    #make a list of the items which combination gets the max possible value of all
    def bruteForce(self):
        self.addNextItem(0, 0, 0, [], len(self.weights))
        print(self.itemList)
        print(self.maxProfit)

    #get the max combination through iteration by "asking" if the current element fits in the "current" bag
    def bottomUp(self):
        rows = len(self.weights) + 1
        table = self.createTable(rows)
        for row in range(1, rows):
            item = row - 1      # -1 because it need to compensate the extra row
            for column in range(1, self.maxWeight): #column is the "current" weight
                if self.weights[item] > column:
                    table[row][column] = table[row-1][column]
                else:
                    if self.profits[item] + table[row-1][self.maxWeight-self.weights[item]] > table[row-1][column]:
                        table[row][column] = self.profits[item] + table[row-1][column-self.weights[item]]
                    else:
                        table[row][column] = table[row-1][column]
        self.maxProfit = table[-1][-1]
        print(table)
        self.itemList = self.getItems(table)
        print(self.itemList)
        #return

    def topDown(self):
        return

    #if it is possible add the next item position to the list
    def addNextItem(self, actualWeight, actualItem, actualValue, actualList, maxLengtList):
        if actualWeight == self.maxWeight:
            return
        while actualItem < maxLengtList:
            if actualWeight + self.weights[actualItem] <= self.maxWeight:
                if(actualValue + self.profits[actualItem] > self.maxProfit):
                    self.maxProfit = actualValue + self.profits[actualItem]
                    self.itemList = actualList + [actualItem]
                self.addNextItem(actualWeight + self.weights[actualItem], actualItem + 1, actualValue + self.profits[actualItem], actualList + [actualItem], maxLengtList)
            actualItem = actualItem + 1

    def createTable(self, rows):
        table = [0]*rows
        for row in range(rows):
            table[row] = [0]*self.maxWeight
        return table

    def getItems(self, table):
        items = []
        row = len(self.profits) - 1 #arrays start from 0
        column = self.maxWeight - 1
        while row > 0:
            if table[row][column] != table[row-1][column]:
                items.append(row)
                column = column - self.weights[row]
            row = row - 1
        return items