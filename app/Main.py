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
    if (problem == "container"):
        matrixC = np.loadtxt(path).tolist()
        return ExecuteProblem(problem, algorithm, matrixC, iterations, 70)
    elif (problem == "goldmine"):
        matrixR = np.loadtxt(path).tolist()
        return ExecuteProblem(problem, algorithm, matrixR, iterations, 0)



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
                       help='The problem to solve. Use "container" for Container and "goldmine" for Goldmine.')

my_parser.add_argument('algorithm',
                       metavar='algorithm',
                       type=str,
                       help='The algorithm to use. Use 1 for Brute-Force and  2 for Dinamic.')

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
                       help='Create a matrix with random values. If you are going to solve the container problem you can'
                            'use the following example:\n'
                            'Base: -p maxWeight NSize weightsRange benefitsRange iterations \n'
                            'Example: -p 70 10 10-15 20-50 1000 \n'
                            '\n'
                            'If you are going to solve the gold problem:\n'
                            'Base: -p N M Min Max iteraciones\n'
                            'Example: -p 5 6 0 100 1000'
                                )

# Execute parse_args()
args = my_parser.parse_args()
algorithmReceived = args.algorithm
problem = args.problem

if(args.archive != ""):
    ReadFile(problem, algorithmReceived, args.archive[0], args.archive[1])

elif (args.pro != ""):
    print (RandomMatrix(problem, algorithmReceived, (args.pro)[0], (args.pro)[1], (args.pro)[2], (args.pro)[3],(args.pro)[4]))

else:
    print("Use -h to get help.")
