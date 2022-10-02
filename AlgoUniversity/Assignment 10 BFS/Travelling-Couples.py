from collections import deque
INF = float('inf')
# Program to solve Graph Problem for Travelling Couples.
# In summary c1,c2,c3, n, m
c1,c2,c3,n,m = map(int,input().split())
adjList = [[]]
for x in range(1, n+1):
    adjList.append([])
for y in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

# Successful Graph creation
# Will now implement generic BFS Function.
def bfsFun(adjList, src):
    q = deque()
    distance = [INF for x in range(n+1)]
    visited = [False for x in range(n+1)]
    q.append(src)
    visited[src] = True
    distance[src] = 0
    while q:
        front = q.popleft()
        for node in adjList[front]:
            if not visited[node]:
                distance[node] = distance[front]+1
                q.append(node)
                visited[node] = True
    return distance

# Now we are supposed to use this BFS function 3 times, and create 3 lists. From 1 from 2 and from N
distM = bfsFun(adjList, 1)
distF = bfsFun(adjList, 2)
distH = bfsFun(adjList, n)

# We are trying to halt at all the possible intermediary nodes
minimumCost = INF
for intermediateNode in range(1, n+1):
    if (not distM[intermediateNode]==INF) and (not distF[intermediateNode]==INF) and (not distH[intermediateNode]==INF):
        currentCost = c1*distM[intermediateNode]+c2*distF[intermediateNode]+c3*distH[intermediateNode] 
        minimumCost = min(currentCost, minimumCost)
print(minimumCost)