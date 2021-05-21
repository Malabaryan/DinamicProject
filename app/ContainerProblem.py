class ContainerProblem:
    def __init__(self, maxWeight, elementsWeight, elementsProfit, loops):
        self.maxWeight = maxWeight
        self.weights = elementsWeight
        self.profits = elementsProfit
        self.loop = loops

    def bruteForce(self):
        return

    def bottomUp(self):
        return

    def topDown(self):
        maxValue = 0
        maxList = []
        actualList = []
        return

    def actualValue(self, actualList):
        value = 0
        for element in actualList:
            value += self.profits[element]
        return value