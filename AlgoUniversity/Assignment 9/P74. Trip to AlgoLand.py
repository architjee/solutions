numCities, numRoads = map(int, input().split())
matrix = [[-1 for i in range(numCities)] for j in range(numCities)]
citiesDict= {}
from collections import deque
for _ in range(numRoads):
    u, v, roadName = input().split()
    if u not in citiesDict:
        citiesDict[u] = len(citiesDict)
    if v not in citiesDict:
        citiesDict[v] = len(citiesDict)
    matrix[citiesDict[u]][citiesDict[v]] = roadName
source, target = input().split()
def bfsAlgo(source, target, matrix):
    sourceNode = citiesDict[source]
    targetNode = citiesDict[target]
    visited = [False for x in range(numCities)]
    distances = [float('inf') for x in range(numCities)]
    q = deque()
    q.append(sourceNode)
    distances[sourceNode] = 0
    while q:
        front = q.popleft()
        for cityCode, roadName in enumerate(matrix[front]):
            if roadName!=-1:
                if cityCode not in q and not visited[cityCode]:
                    distances[cityCode] = distances[front] + 1
                    visited[cityCode] = True
                    q.append(cityCode)
    print(distances[targetNode])
bfsArray = bfsAlgo(source, target, matrix)

print("Debugging ", matrix)