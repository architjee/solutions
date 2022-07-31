x = int(input())
bigList = list(map(int, input().split()))
bigList.sort()

# Instead of deleting two consecutive we will traverse using two pointers.
maxDiffGreaterIndex = 1
maxDiffLesserIndex =0
for j in range(0, len(bigList)):
    for i in range(j+1, len(bigList)):
        if(bigList[i]-bigList[j])>(bigList[maxDiffGreaterIndex]-bigList[maxDiffLesserIndex]):
            maxDiffGreaterIndex, maxDiffLesserIndex = i , j
print(bigList)
print(maxDiffGreaterIndex)
print(maxDiffLesserIndex)
del bigList[maxDiffGreaterIndex]
del bigList[maxDiffLesserIndex]
print(bigList)
summation = 0
for j in range(0, len(bigList)-1,2):
    summation += bigList[j+1]-bigList[j]
print(summation)