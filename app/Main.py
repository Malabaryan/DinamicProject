import sys
sys.path.append('../GoldProblem.py')
from GoldProblem import GoldProblem
import argparse
import numpy as np


#<editor-fold desc="Functions">

# Returns a matrix specified in the path
def ReadFile(problem, algorithm, path, iterations):
    print(algorithm + path + iterations)
    if(problem == "1"):
        print("")
    return algorithm


def RandomMatrix(problem, algorithm, rows, columns, minValue, maxValue, iterations):
    matrixR = np.random.randint(int(minValue),high = int(maxValue), size=(int(rows), int(columns))).tolist()
    ExecuteProblem(problem, algorithm, matrixR, iterations)
    return algorithm

def ExecuteProblem(problem, algorithm, matrix, iterations):
    if(problem == "container"):
        print("Aqui metemos el codigo de Isaac")
    elif(problem == "goldmine"):
        goldMine = GoldProblem(int(algorithm), matrix, int(iterations))
        goldMine.start()

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
    RandomMatrix(problem, algorithmReceived, (args.pro)[0], (args.pro)[1], (args.pro)[2], (args.pro)[3],(args.pro)[4])

else:
    print("Use -h to get help.")
