from typing import *


def depthFirstSearch(V: int, E: int, edges: List[List[int]]):
    # write your code here
    # We are having V vertices and E edges
    adjList = []
    for v in range(V):
        adjList.append([])
    for u,v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    visited = [False for v in range(V)]
    output = []

    def dfsTraversal(adjList, node, parent, dump):
        dump.append(node)
        visited[node] = True
        for child in adjList[node]:
            if child != parent and not visited[child]:
                visited[child]=True
                dfsTraversal(adjList, child, node, dump)
    def getIndexForFirstFalse(visited):
        for index, value in enumerate(visited):
            if not value:
                return True, index
        return False, 0
    while True:
        isFalsePresent, indexFirst = getIndexForFirstFalse(visited)
        if isFalsePresent:
            dump=[]
            dfsTraversal(adjList, indexFirst, None, dump)
            dump.sort()
            output.append(dump)    
        else:
            break
    return output
    
