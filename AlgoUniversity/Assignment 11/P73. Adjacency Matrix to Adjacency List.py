# We are given n integers
n = int(input())
adjList = []
for i in range(n):
    line = list(map(int, input().split()))
    adjList.append([])
    for index, x in enumerate(line):
        if x:
            adjList[i].append(index)
for i in range(len(adjList)):
    print(str(i+1)+":", end=' ')
    for j in adjList[i]:
        print(j+1, end=' ')
    print()