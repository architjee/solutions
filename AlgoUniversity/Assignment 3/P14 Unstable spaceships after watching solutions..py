x = int(input())
heightsArray = list(map(int, input().split()))
heightsArray.sort()
ans = float('inf')


def getPairWiseSum(tempList):
    bigSum = 0
    for i in range(0, len(tempList), 2):
        bigSum += (tempList[i + 1] - tempList[i])
    return bigSum

for i in range(0, 2*x):
    for j in range(i + 1, 2*x):
        tempList = []
        for alpha in range(0, 2*x):
            if alpha != i and alpha != j:
                tempList.append(heightsArray[alpha])
        ans = min(ans, getPairWiseSum(tempList))
print(ans)