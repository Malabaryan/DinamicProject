import sys
import numpy as np


class GoldProblem():
    def __init__(self, pAlgorithm, pMatrix, pIterations):
        self.algorithm = pAlgorithm
        self.matrix = pMatrix
        self.iterations = pIterations

    # Main function that solves dinamically the problem
    def dinamicSolve(self, matrix):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])

        # To start from the lasts numbers
        for row in matrix:
            row.reverse()

        # Aux matrix
        auxMatrix = [[0 for x in range(maxColumna)] for y in range(maxFila)]

        # Solve the problem iterating on each last number
        valoresFinales = []
        for rowNumber in range(maxFila):
            valores = []
            self.dinamicSolveAux(rowNumber, 0, matrix, matrix[rowNumber][0], auxMatrix[:])

        for index in range (0,len(auxMatrix)):
            auxMatrix[index].reverse()

        # Check the max value in the rows
        checkMax = []
        for row in auxMatrix:
            checkMax.append(row[0])

        rowIndexMaxValue = checkMax.index(max(checkMax))
        maxValue = auxMatrix[rowIndexMaxValue][0]

        listaReturn = []
        indices = [i for i, d in enumerate(checkMax) if d == maxValue]
        for index in indices:
            valores = []
            self.dinamicSolveAuxFinal(index, 0, auxMatrix, auxMatrix[index][0], valores, listaReturn)

        # Check the new path with maximum values
        return [maxValue, listaReturn]

    # Auxiliary function
    def dinamicSolveAux(self, fila, columna, matrix, valor, auxMatrix):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])
        valor1 = 0
        valor2 = 0
        valor3 = 0

        if (auxMatrix[fila][columna] < valor):
            auxMatrix[fila][columna] = valor

        if (columna < maxColumna-1):

            # Check right - diagonal - up
            if (fila > 0):
                valor1 = valor + matrix[fila-1][columna+1]
                self.dinamicSolveAux(fila - 1, columna + 1, matrix, valor1, auxMatrix)

            # Check right - diagonal - down
            if (fila < maxFila-1):
                valor2 = valor + matrix[fila+1][columna+1]
                self.dinamicSolveAux(fila + 1, columna + 1, matrix, valor2, auxMatrix)

            # Check right
            valor3 = valor + matrix[fila][columna+1]
            self.dinamicSolveAux(fila, columna + 1, matrix, valor3, auxMatrix)

            if(fila == maxFila-1):
                return auxMatrix

    # Auxiliary function
    def dinamicSolveAuxFinal( self, fila, columna, matrix, valor, valores, finalList):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])
        valor1 = 0
        valor2 = 0
        valor3 = 0
        valores.append([fila, columna])

        if (columna < maxColumna-1):

            # Check right - diagonal - up
            if (fila > 0):
                valor1 = valor + matrix[fila-1][columna+1]

            # Check right - diagonal - down
            if (fila < maxFila-1):
                valor2 = valor + matrix[fila+1][columna+1]

            # Check right
            valor3 = valor + matrix[fila][columna+1]

            # Check the max value in this stage
            listValores = [valor1, valor2, valor3]
            maximo = max(listValores)

            # Use the maximum value and that path to continue
            if(valor1 == maximo):
                self.dinamicSolveAuxFinal(fila - 1, columna + 1, matrix,  valor1, valores[:], finalList)

            if (valor2 == maximo):
                self.dinamicSolveAuxFinal(fila + 1, columna + 1, matrix,  valor2, valores[:], finalList)

            if (valor3 == maximo):
                self.dinamicSolveAuxFinal(fila, columna + 1, matrix,  valor3, valores[:], finalList)
        if(len(valores) == maxColumna):
            finalList.append(valores)

    # Main brute force algorithm
    def bruteForce(self, matrix):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])

        # Solve the problem iterating on each last number
        finalList = []
        for rowNumber in range(maxFila):
            valores = []
            self.bruteForceAux(rowNumber, 0, matrix, matrix[rowNumber][0], valores, finalList)

        # Check the max value in the results
        checkMax = []
        for row in finalList:
            checkMax.append(row[0])
        maxValue = max(checkMax)

        listaReturn = []
        indices = [i for i, d in enumerate(checkMax) if d == maxValue]
        for index in indices:
            listaReturn.append(finalList[index][1])

        return [maxValue,listaReturn]

    # Auxiliary function
    def bruteForceAux(self, fila, columna, matrix, valor, valores, finalList):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])
        valor1 = 0
        valor2 = 0
        valor3 = 0
        valores.append([fila, columna])

        if (columna < maxColumna - 1):

            # Check right - diagonal - up
            if (fila > 0):
                valor1 = valor + matrix[fila - 1][columna + 1]

            # Check right - diagonal - down
            if (fila < maxFila - 1):
                valor2 = valor + matrix[fila + 1][columna + 1]

            # Check right
            valor3 = valor + matrix[fila][columna + 1]

            # Use the maximum value and that path to continue
            if (valor1 != 0):
                 self.bruteForceAux(fila - 1, columna + 1, matrix, valor1, valores[:], finalList)

            if (valor2 != 0):
                 self.bruteForceAux(fila + 1, columna + 1, matrix, valor2, valores[:], finalList)

            if (valor3 != 0):
                self.bruteForceAux(fila, columna + 1, matrix, valor3, valores[:], finalList)
        else:
            # Ultimo chunche
            finalList.append([valor,valores[:]])
            #print([valores,valor])

            if(fila == maxFila-1):
                # Check if the penultimate position was from the last row
                if (valores[len(valores) - 2][0] == maxFila-1):
                    return finalList

    # Print the results from the program
    def printResults(self):

        print("Resultados")

    # Start the algorithm selected
    def start(self):
        for iteration in range(self.iterations):
            if(self.algorithm == 1):
                return self.bruteForce(self.matrix)
            if(self.algorithm == 2):
                return self.dinamicSolve(self.matrix)


pIterations = 1
pMatrix = [[1 ,20,3 ,4 ,5,  6,70,8,9,10],
           [10,9 ,8 ,70,68, 52,4,30,21,1],
           [5 ,45,30,2 ,10, 6,70,86,9,92],
           [5 ,4 ,30,21,10, 6,70,8,92,9],
           [56,4 ,30,2 ,10, 60,70,8,90,9]]



pMatrix2 = [[3,3,5],
            [5,5,3],
            [5,5,5]]


pAlgorithm = 1
gp = GoldProblem(pAlgorithm, pMatrix2, pIterations)
result = gp.start()
print(result)


pAlgorithm = 2
gp = GoldProblem(pAlgorithm, pMatrix2, pIterations)
result = gp.start()
print(result)