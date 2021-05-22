class ContainerProblem:
    def __init__(self, maxWeight, elementsWeight, elementsProfit, loops):
        self.maxWeight = maxWeight
        self.weights = elementsWeight
        self.profits = elementsProfit
        self.loop = loops

    #return a list of the items which combination gets the max possible value of all
    def bruteForce(self):
        if(self.weights[-1] < self.maxWeight):
            maxValue = self.profits[-1]
            maxList = [len(self.weights)-1]
        else:
            maxValue = 0
            maxList = []
        fixedItem = 0
        while fixedItem < len(self.weights):
            currentItem = fixedItem + 1
            while currentItem < len(self.weights):
                actualList = self.bruteForceIteration(fixedItem, currentItem)
                actualValue = self.actualValue(actualList)
                if(actualValue > maxValue):
                    maxValue = actualValue
                    maxList = actualList
                currentItem = currentItem + 1
            fixedItem = fixedItem + 1
        return maxList

    def bottomUp(self):
        return

    def topDown(self):
        return

    def actualValue(self, actualList):
        value = 0
        for element in actualList:
            value += self.profits[element]
        return value

    #return a list of items of the max value that included two specific items
    def bruteForceIteration(self, fixedItem, currentItem):
        return []