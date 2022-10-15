n = int(input())

# Now everyone has a boss
adjList = [[] for x in range(n+1)]
bossDict = {}
inpList = list(map(int,input().split()))
i=0
for x in range(2, n):
    bossDict[x]=inpList[i]
    adjList[inpList[i]].append(x)
    i+=1

def peopleUnderThisMan(adjList, man):
    print("Function is being called for adjList", adjList, " and man as ", man)
    if not adjList[man]:
        return 1
    sumation = 0
    for x in adjList[man]:
        sumation += peopleUnderThisMan(adjList, x)
    return sumation+1
result = peopleUnderThisMan(adjList, 1)
print(result)