x = int(input())
bigList = list(map(int, input().split()))
bigList.sort()
# print(bigList, 2*(x-1))
# To find the minimum height difference.
# After sorting let's traverse this two at a time a check the difference if it greater than max difference.
maxDiffIndex = 0
for j in range(0, len(bigList)-1):
    # To check bigList[j] and bigList[j+1]
    if((bigList[j+1]-bigList[j])>(bigList[maxDiffIndex+1]-bigList[maxDiffIndex])):
        # If this is the case then update maxDiffIndex
        maxDiffIndex = j
# To ignore maxDiffIndex+1 and maxDiffIndex
# Trying to delete maxDiffIndex and maxDiffIndex+1
# print(bigList)
bigList = bigList[:maxDiffIndex]+bigList[maxDiffIndex+2:]
# print(bigList)
# print(maxDiffIndex)
summation = 0
for j in range(0, len(bigList)-1,2):
    summation += bigList[j+1]-bigList[j]
print(summation)