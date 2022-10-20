n, c = map(int, input().split())
RED = 1
colors =[0]
colors.extend(map(int,input().split()))
adjList = [[] for i in range(n+1)]
for _ in range(n-1):
    u, v= map(int,input().split())
    adjList[u].append(v)
def dfs(adjList, root, limit):
    print("This is a stackTrace", root, limit)
    if limit<0 :
        return 0
    leafCount = 0
    if colors[root]==RED:
        limit-=1
    if adjList[root]==[] and limit>=0:
        return 1
    for u in adjList[root]:
        leafCount +=dfs(adjList, u, limit)
    return leafCount

print(dfs(adjList, 1, c))