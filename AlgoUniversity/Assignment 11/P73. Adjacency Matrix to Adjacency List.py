# We are given N nodes, representing a Adjacency matrix.
n = int(input())
adjList = [[]]
for i in range(1, 1+n):
    line = list(map(int, input().split()))
    for index, j in enumerate(line):
        if (j==0):
            continue
        if len(adjList) > i:
            # Then we can add this directly. BY saying
            adjList[i].append(index+1)
        else:
            adjList.append([index+1])

for vertice in range(1, len(adjList)):
    print(str(vertice)+":", end=' ')
    for edges in adjList[vertice]:
        print(edges, end=' ')
    print()