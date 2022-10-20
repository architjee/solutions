
global isCyclePresent
isCyclePresent = False
def mainFunc():
    n, m = map(int, input().split())
    adjList = [[] for i in range(n+1)]
    white, grey, black = range(3) 
    for edg in range(m):
        if u==v:
            global isCyclePresent
            isCyclePresent = True
            return
        u, v = map(int, input().split())
        adjList[u].append(v)
    colors= [white for i in range(n+1)]
    lastBlack=False
    def isCyclePresentViaDFS(adjList, root, colors):
        if colors[root]==grey:
            return True
        colors[root] = grey
        # We will start processing from 1 grey.
        for child in adjList[root]:
            if isCyclePresentViaDFS(adjList, child, colors):
                return True
        colors[root]=black
        if root == n:
            global lastBlack
            lastBlack=True
        return False

    def getFirstIndexOfWhite(colors):
        for index, c in enumerate(colors):
            if index==0:
                continue
            if c==white:
                return True, index
        return False, -1
    isWhitePresent, indexOfWhite = getFirstIndexOfWhite(colors)
    while not lastBlack and isWhitePresent:
        if isCyclePresentViaDFS(adjList, indexOfWhite, colors): 
            print(isCyclePresent)
            global isCyclePresent
            isCyclePresent= True
            break
        isWhitePresent, indexOfWhite = getFirstIndexOfWhite(colors)
    else:
        return
mainFunc()
if isCyclePresent:
    print("NO")
else:
    print("YES")