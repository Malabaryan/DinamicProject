import sys

def checkLAbyrint(maxColumna, maxFila, matrix):

    return checkNext(maxColumna, maxFila, 0, 0, matrix, 0)


def checkNext(maxColumna, maxFila, columna, fila, matrix, valor):
    valor1 = 0
    valor2 = 0
    valor3 = 0

    if (columna < maxColumna):

        # Revisar diagonal arriba
        if (fila > 0):
            print("valor seleccionado: " + str(matrix[fila][columna]))
            print("fila seleccionada: " + str(fila))
            print("columna seleccionada: " + str(columna))
            print("\n")
            valor1 = valor + matrix[fila][columna]
            return checkNext(maxColumna, maxFila, columna + 1, fila - 1, matrix,  valor + matrix[fila][columna]);

        # Revisar diagonal abajo
        if (fila < maxFila):
            print("valor seleccionado: " + str(matrix[fila][columna]))
            print("fila seleccionada: " + str(fila))
            print("columna seleccionada: " + str(columna))
            print("\n")
            valor2 = valor + matrix[fila][columna]
            return checkNext(maxColumna, maxFila, columna + 1, fila + 1, matrix, valor + matrix[fila][columna]);

        # Revisar derecho
        print("valor seleccionado: " + str(matrix[fila][columna]))
        print("fila seleccionada: " + str(fila))
        print("columna seleccionada: " + str(columna))
        print("\n")
        valor3 = valor + matrix[fila][columna]
        return checkNext(maxColumna, maxFila, columna + 1, fila, matrix, valor + matrix[fila][columna]);

        print(str(valor1) + " " + str(valor2) + " " +str(valor3) + " ")
        if(valor1 >= valor2 and valor1 >= valor3):
            print("El valor " + str(valor1) + " es el mayor.")
            return valor1
        if (valor2 >= valor1 and valor2 >= valor3):
            print("El valor " + str(valor2) + " es el mayor.")
            return valor2
        if (valor3 >= valor2 and valor3 >= valor1):
            print("El valor " + str(valor3) + " es el mayor.")
            return valor3
    return valor

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix)
valorF = checkLAbyrint(3,3,matrix)

print(valorF)