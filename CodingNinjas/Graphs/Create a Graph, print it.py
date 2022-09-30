from os import *
from sys import *
from collections import *
from math import *

def printAdjacency(n, m, edges):
    # Write your code here.
    adjList = []
    for i in range(n):
        adjList.append([i])
    for (u, v) in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList