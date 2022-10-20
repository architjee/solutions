
def mainFunc():
    answer = False
    n, m = map(int, input().split())
    adjList = [[] for i in range(n)]
    white, grey, black = range(3) 
    for edg in range(m):
        u, v = map(int, input().split())
        adjList[u].append(v)
    colors= [white for i in range(n)]
    def isCyclePresentViaDFS(adjList, root, colors):
        if colors[root]==grey:
            return True
        colors[root] = grey
        # We will start processing from 1 grey.
        for child in adjList[root]:
            if isCyclePresentViaDFS(adjList, child, colors):
                return True
        colors[root]=black
        return False
    if isCyclePresentViaDFS(adjList, 0, colors): 
            answer=True
    if answer:
        print("NO")
    else:
        print("YES")
mainFunc()