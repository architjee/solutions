# We are given n
n = int(input())

bossArray = list(map(int, input().split()))
adjList = [[] for j in range(n+1)]
i= 2
for x in bossArray:
    adjList[x].append(i)
    i+=1
noOfPeepsUnderThisGuy = [0 for x in range(n+2)]
# Note we are call this as peopleUnderGuy is inclusive of the guy itself always.

def peopleUnderGuy(adjList,node):
    peopleUnder = 0
    if len(adjList)>node:
        for child in adjList[node]:
            peopleUnder += peopleUnderGuy(adjList, child)
        # Finally set the people under this guy to the array equivalent.
    noOfPeepsUnderThisGuy[node] = peopleUnder
    return peopleUnder+1
# what if there are only 1 people
noOfPeepsUnderThisGuy[1]=peopleUnderGuy(adjList, 1) -1 
for i in range(1, n):
    print(noOfPeepsUnderThisGuy[i], end=' ')
print(0)