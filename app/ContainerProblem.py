import timeit
import random

class ContainerProblem():
    def __init__(self, pAlgorithm, maxWeight, pMatrix, pIterations):
        self.algorithm = pAlgorithm
        self.maxWeight = maxWeight
        self.weights = pMatrix[0]
        self.profits = pMatrix[1]
        self.iterations = pIterations

        #to track the combination that gave the maximum profit
        self.maxProfit = 0
        self.itemList = []

    #make a list of the items which combination gets the max possible value of all
    def bruteForce(self):
        self.addNextItem(0, 0, 0, [], len(self.weights))
        #print(self.itemList)
        #print(self.maxProfit)

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
        #print(table)
        '''for row in table:
            print(row)
        self.itemList = self.getItems(table)
        print(self.itemList)'''


    def topDown(self):
        table = self.createTable(len(self.weights) + 1)
        self.maxProfit = self.topDownAux(table, len(self.weights), self.maxWeight-1) #columns goes from 0 to maxWeight-1
        
        self.itemList = self.getItems(table)

    def topDownAux(self, matrix, row, column): #row current item, column "current" weight
        # stop conditions
        if row == 0 or column == 0:
            return 0
        #avoid out of index
        if matrix[row][column] != 0:
            return matrix[row][column]

        # choice diagram code
        if self.weights[row - 1] <= column+1: #compensate the -1
            matrix[row][column] = max(self.profits[row - 1] + self.topDownAux(matrix, row-1, column-self.weights[row-1]), self.topDownAux(matrix, row-1, column))
            return matrix[row][column]
        elif self.weights[row - 1] > column:
            matrix[row][column] = self.topDownAux(matrix, row - 1, column)
            return matrix[row][column]

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

    #create a matrix of nxm row, n = number of items + 1, m = maximun soported weight
    def createTable(self, rows):
        table = [0]*rows
        for row in range(rows):
            table[row] = [0]*self.maxWeight
        return table

    def getItems(self, table):
        items = []
        row = len(self.profits)
        column = self.maxWeight - 1 #avoid out of range
        while row > 0:
            if table[row][column] != table[row-1][column]:
                items.append(row-1) #avoid out of range
                column = column - self.weights[row-1]
            row = row - 1
        return items

    def printResults(self, results, fulltime, averageTime):
        print("The maximum value is: " + str(self.maxProfit))
        print("The combination founded is: " + str(self.itemList))

        print("Time taken to execute all the iterations: " + str(fulltime))
        print("Average time taken in each execution: " + str(averageTime))

        return [str(self.maxProfit), str(self.itemList), str(fulltime), str(averageTime)]

    def start(self):
        result = []
        times = []
        startFulltime = timeit.default_timer()

        #Execute iterations
        for iteration in range(self.iterations):
            starttime = timeit.default_timer()
            if (self.algorithm == 1):
                self.bruteForce()
            elif (self.algorithm == 2):
                self.bottomUp()
            elif(self.algorithm == 3):
                self.topDown()
            exitTime = timeit.default_timer() - starttime

            #Add the time measured
            times.append(exitTime)

        #Full time of execution
        exitFullTime = timeit.default_timer() - startFulltime
        return self.printResults(result, exitFullTime, sum(times)/len(times))
