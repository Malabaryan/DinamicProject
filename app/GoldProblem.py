import sys
import numpy as np

def checkLAbyrint(matrix):
    maxFila = len(matrix)
    maxColumna = len(matrix[0])

    for row in matrix:
        row.reverse()

    valoresFinales = []
    for rowNumber in range(maxFila):
        valores = []
        valoresFinales.append( [checkNext(rowNumber, 0, matrix, matrix[rowNumber][0], valores), valores])

    checkMax = []
    for row in valoresFinales:
        checkMax.append(row[0])

    return valoresFinales[checkMax.index(max(checkMax))]


def checkNext( fila, columna, matrix, valor, valores):
    maxFila = len(matrix)
    maxColumna = len(matrix[0])
    valor1 = 0
    valor2 = 0
    valor3 = 0
    valores.append([fila, columna])
    print("Valor actual: " + str(valor))

    if (columna < maxColumna-1):

        # Revisar diagonal arriba
        if (fila > 0):
            valor1 = valor + matrix[fila-1][columna+1]

        # Revisar diagonal abajo
        if (fila < maxFila-1):
            valor2 = valor + matrix[fila+1][columna+1]

        # Revisar derecho
        valor3 = valor + matrix[fila][columna+1]

        listValores = [valor1, valor2, valor3]
        maximo = max(listValores)
        print(listValores)
        print("El valor maximo es: " + str(maximo) + "\n")

        if(valor1 == maximo):
            #valores.append([fila - 1, columna + 1])
            return checkNext( fila - 1  , columna + 1, matrix,  valor1, valores)
        if (valor2 == maximo):
            #valores.append([fila + 1, columna + 1])
            return checkNext( fila + 1  , columna + 1, matrix,  valor2, valores)
        if (valor3 == maximo):
            #valores.append([fila , columna + 1])
            return checkNext( fila      , columna + 1, matrix,  valor3, valores)

    return valor

matrix = [[1,1,1,9,1,9,9],
          [1,1,9,1,9,1,1],
          [9,9,1,1,1,1,1],
          [1,1,9,10,10,10,10]]

print(checkLAbyrint(matrix))

