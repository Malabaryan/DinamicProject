import sys
import csv
sys.path.append('../GoldProblem.py')
sys.path.append('../ContainerProblem.py')
from GoldProblem import GoldProblem
from ContainerProblem import ContainerProblem
import argparse
import numpy as np
from numpy import random


#<editor-fold desc="Functions">

# Returns a matrix specified in the path
def ReadFile(problem, algorithm, path, iterations):
    print(algorithm + path + iterations)
    if(problem == "1"):
        print("")
    return algorithm


def RandomMatrix(problem, algorithm, rows, columns, minValue, maxValue, iterations):
    if(problem == "container"):
        print("Aleatorio Container")
        W = rows
        N = columns
        rangoPesos = minValue.split("-")
        rangoBeneficios = maxValue.split("-")

        matrixC  = [
            np.random.randint(int(rangoPesos[0]), high=int(rangoPesos[1]), size=(1, int(N))).tolist()[0] ,
            np.random.randint(int(rangoBeneficios[0]), high=int(rangoBeneficios[1]), size=(1, int(N))).tolist()[0]
        ]

        return ExecuteProblem(problem, algorithm, matrixC, iterations,  W)

    elif (problem == "goldmine"):
        matrixR = np.random.randint(int(minValue), high=int(maxValue), size=(int(rows), int(columns))).tolist()
        return ExecuteProblem(problem, algorithm, matrixR, iterations, 0)

def ExecuteProblem(problem, algorithm, matrix, iterations, pMaxWeight):
    if(problem == "container"):
        container = ContainerProblem(int(algorithm), int(pMaxWeight), matrix, int(iterations))
        return container.start()
    elif(problem == "goldmine"):
        goldMine = GoldProblem(int(algorithm), matrix, int(iterations))
        return goldMine.start()

#</editor-fold>

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('problem',
                       metavar='problem',
                       type=str,
                       help='the problem to solve. Use 1 for Container and  2 for Goldmine.')

my_parser.add_argument('algorithm',
                       metavar='algorithm',
                       type=str,
                       help='the algorithm to use. Use 1 for Brute-Force and  2 for Dinamic.')

my_parser.add_argument('-a',
                       '--archive',
                       action="store",
                       default = "",
                       nargs = 2,
                       help='Read a file and load the matrix from there.')

my_parser.add_argument('-p',
                       '--pro',
                       action="store",
                       default = "",
                       nargs = 5,
                       help='Create a matrix with random values.')

# Execute parse_args()
args = my_parser.parse_args()
algorithmReceived = args.algorithm
problem = args.problem

if(args.archive != ""):
    ReadFile(problem, algorithmReceived, args.archive[0], args.archive[1])

elif (args.pro != ""):
    print (RandomMatrix(problem, algorithmReceived, (args.pro)[0], (args.pro)[1], (args.pro)[2], (args.pro)[3],(args.pro)[4]))

else:
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for sizeMatrix in range (2, 30):
            W = 5 # Generar random
            mSize = sizeMatrix
            random1 = 4  # generar random
            random2 = 8  # generar random
            random3 = 4  # generar random
            random4 = 8  # generar random

            rango1 = str(random1) + "-" + str(random2)
            rango2 = str(random3) + "-" + str(random4)
            for iterations in range(1,5):
                amountIterations = 10 ** iterations
                writer.writerow(RandomMatrix(problem, 1, W, mSize, rango1, rango2, amountIterations))
                writer.writerow(RandomMatrix(problem, 2, W, mSize, rango1, rango2, amountIterations))
                writer.writerow(RandomMatrix(problem, 3, W, mSize, rango1, rango2, amountIterations))
