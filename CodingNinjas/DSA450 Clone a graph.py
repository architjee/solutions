from os import *
from sys import *
from collections import *
from math import *

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraph(root):
    # Write your code here.
    if not root:
        return None
    
    newRoot = graphNode(root.data)
    vertexMirror = {root: newRoot}
    q = deque([root])
    while q:
        v = q.popleft()
        for neigh in v.neighbours:
            if neigh not in vertexMirror :
                vertexMirror[neigh]=graphNode(neigh.data)
                q.append(neigh)
            # if neigh is in vertexMirror we shouldn't have to create it again.
            vertexMirror[v].neighbours.append(vertexMirror[neigh])
    return vertexMirror[root]