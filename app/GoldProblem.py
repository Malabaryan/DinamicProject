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

        # Solve the problem iterating on each last number
        valoresFinales = []
        for rowNumber in range(maxFila):
            valores = []
            valoresFinales.append([self.dinamicSolveAux(rowNumber, 0, matrix, matrix[rowNumber][0], valores), valores])

        # Check the max value in the results
        checkMax = []
        for row in valoresFinales:
            checkMax.append(row[0])
        result = valoresFinales[checkMax.index(max(checkMax))]
        result[1].reverse()
        for index in range (0,len(result[1])):
            result[1][index][1] = index
        return result

    # Auxiliary function
    def dinamicSolveAux( self, fila, columna, matrix, valor, valores):
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
                return self.dinamicSolveAux(fila - 1, columna + 1, matrix,  valor1, valores)

            if (valor2 == maximo):
                return self.dinamicSolveAux(fila + 1, columna + 1, matrix,  valor2, valores)

            if (valor3 == maximo):
                return self.dinamicSolveAux(fila, columna + 1, matrix,  valor3, valores)

        return valor

    def bruteForce(self, matrix):
        maxFila = len(matrix)
        maxColumna = len(matrix[0])

        # Solve the problem iterating on each last number
        valoresFinales = []
        finalList = []
        for rowNumber in range(maxFila):
            valores = []
            self.bruteForceAux(rowNumber, 0, matrix, matrix[rowNumber][0], valores, finalList)

        # Check the max value in the results
        checkMax = []
        for row in finalList:
            checkMax.append(row[0])

        return finalList[checkMax.index(max(checkMax))]

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

    def start(self):
        for iteration in range(self.iterations):
            if(self.algorithm == 1):
                return self.bruteForce(self.matrix)
            if(self.algorithm == 2):
                return self.dinamicSolve(self.matrix)




pIterations = 1
pMatrix = [[1,20,3,4,5,  6,70,8,9,10],
           [10,9,8,70,68, 52,4,30,21,1],
           [5,45,30,2,10, 6,70,86,9,92],
           [5,4,30,21,10, 6,70,8,92,9],
           [56,4,30,2,10, 60,70,8,90,9]]

pAlgorithm = 1
gp = GoldProblem(pAlgorithm, pMatrix, pIterations)
result = gp.start()
print(result)

pAlgorithm = 2
gp = GoldProblem(pAlgorithm, pMatrix, pIterations)
result = gp.start()
print(result)