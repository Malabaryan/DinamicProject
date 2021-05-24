function checkLAbyrint():
    return checkNext()


function checkNext(maxColumna, maxFila, columna, fila, valor):

    if (columna < maxColumna):

        # Revisar diagonal arriba
        if (fila > 0):
            return checkNext(maxColumna, maxFila, columna + 1, fila - 1, valor + matrix[columna][fila]);

        # Revisar diagonal abajo
        elif (fila < maxFila):
            return checkNext(maxColumna, maxFila, columna + 1, fila + 1, valor + matrix[columna][fila]);

        # Revisar derecho
        else:
            return checkNext(maxColumna, maxFila, columna + 1, fila, valor + matrix[columna][fila]);

    return 0