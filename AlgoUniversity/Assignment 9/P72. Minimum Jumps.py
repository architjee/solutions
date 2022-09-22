# Given N buildings numbered 1 to N.
# M edges are given.
adjList = [[]]
n, m = map(int, input().split())
for i in range(n):
    adjList.append([])
for _ in range(m):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)


def bfsAlgo(adjList, src):
    distances = [-1 for x in adjList]
    q = [src]
    distances[src] = 0
    while q:
        top = q.pop(0)
        for y in adjList[top]:
            if distances[y] == -1 and y not in q:
                q.append(y)
                distances[y] = distances[top] + 1
    return distances


src, target = map(int, input().split())
spArray = bfsAlgo(adjList, src)
if spArray[target] != -1:
    print(spArray[target])
else:
    print(0)
