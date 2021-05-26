class ContainerProblem:
    def __init__(self, maxWeight, elementsWeight, elementsProfit, loops):
        self.maxWeight = maxWeight
        self.weights = elementsWeight
        self.profits = elementsProfit
        self.loop = loops

        #to track the combination that gave the maximum profit
        self.maxProfit = 0
        self.itemList = []

    #return a list of the items which combination gets the max possible value of all
    def bruteForce(self):
        self.addNextItem(0, 0, 0, [], len(self.weights))

    def bottomUp(self):
        return

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