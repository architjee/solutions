def cycleDetection(edges, n, m):

    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".
    white, grey ,black = range(3)
    adjList = []
    for x in range(n+1):
        adjList.append([])
    for u, v in edges:
        adjList[u].append(v)
        adjList[v].append(u)
    
    answer = "No"
    visited = [False for x in range(n+1)]
    color = [white for x in range(n+1)]
    def getFirstIndexWithFalse(visited):
        for index, value in enumerate(visited):
            if index==0:
                continue
            if not value:
                return True, index
        return False, -1
    def cycleDetectDFS(adjList, node, parent):
        if color[node]==grey:
            return True
        color[node]=grey
        visited[node] = True
        for child in adjList[node]:
            if child!=parent:
                visited[child] = True
                if cycleDetectDFS(adjList, child, node):
                    return True
        color[node] = black
        return False
    while True:
        isSomewhereFalse, indexOfFalse = getFirstIndexWithFalse(visited)
        if isSomewhereFalse:
            if cycleDetectDFS(adjList, indexOfFalse, None):
                answer = "Yes"
                break
        else:
            break
    return answer