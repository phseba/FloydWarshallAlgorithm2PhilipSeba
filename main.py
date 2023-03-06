import sys

import itertools

NO_PATH = sys.maxsize

graph = [[0, 5, NO_PATH, 10],
[NO_PATH, 0, 3, NO_PATH],
[NO_PATH, NO_PATH, 0, 1],
[NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(graph[0])

# Number of vertices in the graph
V = 4

# NO_PATH represents maximal value in the graph
NO_PATH = 99999

# Floyd Warshall Algorithm
def floyd(distance):
    """This function provides a solution matrix to the Floyd Warshall Algorithm, distance [][] will be the output into the matrix"""

    """Use of the initial distance matrix with distances between respective nodes listed up in form of a graph"""
    def MAX_LENGTH():
        if MAX_LENGTH == 0:
            return 0
        else:
            return itertools.product(range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH))

    """Iterative calculation of the vertex (k) with the shortest distance to its proximate vertices"""
    """Imperative re-use of distance[i][j]"""
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distance[i][j] = min(distance[i][j], distance [i][k] + distance [k][j])

    """Output"""
    printSolution(distance)

# Function to print out the solution matrix
def printSolution(distance):
    """Output function"""

    print("The following matrix is the solution matrix to the Floyd Warshall Algorithm containing\
    the shortest path between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (distance[i][j] == NO_PATH):
                print("%7s" % ("NO_PATH"), end=" ")
            else:
                print("%7d\t" % (distance[i][j]), end=' ')
            if j == V - 1:
                print()

# Function call
floyd(graph)

# Print docstring
print(floyd.__doc__)

# Performance Test
import timeit

import random

def test():
    floyd(graph)
    return random.randint(10, 50)

starting_time = timeit.default_timer()

print("Start time :",starting_time)

test()

print("Time difference :", timeit.default_timer() - starting_time)
