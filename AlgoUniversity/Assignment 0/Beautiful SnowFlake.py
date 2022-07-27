# 11 8
# 1 2
# 2 3
# 4 5
# 6 5
# 7 5
# 8 5
# 9 5
# 10 5
#
n, m = map(int, input().split())
bigAdjacencyList = {}
for x in range(1,n+1):
    fromNode = x
    toNode = []
    bigAdjacencyList[fromNode] = toNode
for x in range(m):
    fromNode, toNode = map(int, input().split())
    bigAdjacencyList[fromNode].append(toNode)
    bigAdjacencyList[toNode].append(fromNode)
# print(bigAdjacencyList)
hashMap = {}
for node, adjacencyList in bigAdjacencyList.items():
    if(len(adjacencyList)!= 1):
        # Goto, neighbours of node that is elements in adjacencyList
        condition = True
        for x in adjacencyList:
            if(len(bigAdjacencyList[x])!=1):
                condition = False
        if condition:
            # This means that degree of node is != 1 and deg of all neighbours of node is = 1;
            if len(adjacencyList) in hashMap:
                hashMap[len(adjacencyList)]+=1
            else:
                hashMap[len(adjacencyList)]=1
cnt= 0
for x , y in hashMap.items():
    if y==1:
        cnt+=1
print(cnt)