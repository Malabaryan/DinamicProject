# myls.py
# Import the argparse library
import sys
import argparse
import os

sys.path.append('../app/GoldProblem.py')
from app.GoldProblem import GoldProblem

#<editor-fold desc="Functions">

# Returns a matrix specified in the path
def ReadFile(problem, algorithm, path, iterations):
    print(algorithm + path + iterations)
    if(problem == "1"):
        print("")
    return algorithm

def RandomMatrix(problem, algorithm, rows, columns, minValue, maxValue, iterations):
    print(algorithm + rows + + columns + minValue + maxValue +  iterations)
    return algorithm

def ExecuteProblem(problem, algorithm, matrix, iterations):
    if(problem == "container"):
        print("Aqui metemos el codigo de Isaac")
    elif(problem == "goldmine"):
        goldMine = GoldProblem(algorithm, matrix, iterations)

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
                       help='enable the long listing format')

my_parser.add_argument('-p',
                       '--pro',
                       action="store",
                       default = "",
                       nargs = 5,
                       help='enable the long listing format')

# Execute parse_args()
args = my_parser.parse_args()
algorithmReceived = args.algorithm
problem = args.problem

if(args.archive != ""):
    ReadFile(problem, algorithmReceived, args.archive[0], args.archive[1])

elif (args.pro != ""):
    RandomMatrix(problem, algorithmReceived. args.pro[0], args.pro[1], args.pro[2], args.pro[3], args.pro[4])

else:
    print("Use -h to get help.")

    matrix = [[1,1,1,9,1,9,9],
              [1,1,9,1,9,1,1],
              [9,9,1,1,1,1,1],
              [1,1,9,10,10,10,10]]

    #print(checkLAbyrint(matrix))