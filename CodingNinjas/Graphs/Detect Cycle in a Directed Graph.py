def isCyclic(edges, v, e):
    # Given the graph is directed
    # Vertices are in the range(v) and there are e edges.
    adjList = []
    for vertices in range(v):
        adjList.append([])
    for fromVertice,toVertice in edges:
        adjList[fromVertice].append(toVertice)
    WHITE = 0
    GREY = 1
    BLACK = 2
    visited = [False for x in range(v)]
    color = [WHITE for x in range(v)]
    def dfs(adjList, node, parent, visited):
        if color[node]==GREY:
            return True
        color[node] = GREY
        visited[node] = True
        for child in adjList[node]:
       
            visited[child]=True
            if dfs(adjList, child, node, visited):
                return True
        color[node]=BLACK
        return False
    def getFirstFalse(visited):
        for index,value in enumerate(visited):
            if not value:
                return True, index
        return False, -1
    while True:
        isFalsePresent, indexOfFalsse = getFirstFalse(visited)
        if isFalsePresent:
            if dfs(adjList, indexOfFalsse, None, visited):
                return True
        else:
            break
    return False
t = int(input())
for ti in range(t):
    v, e = map(int,input().split())
    edges = []
    for _ in range(e):
        f, t = map(int,input().split())
        edges.append([f,t])
    print(isCyclic(edges, v ,e))