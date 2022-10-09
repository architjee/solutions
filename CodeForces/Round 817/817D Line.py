def getDifference(people):
    n = len(people)
    result = []
    for index, person in enumerate(people):
        if person=="L":
            # will be changed to R
            # means the lower index.
            result.append(n-index-1 - index)
        else:
            result.append(index - (n - index-1))
    result.sort(reverse=True)
    return result
def getCurrentSum(people):
    n = len(people)
    totalSum = 0
    for index, person in enumerate(people):
        if person=="L":
            totalSum += index
        else:
            totalSum += n - index - 1
    return totalSum
t = int(input())
# t is no. of test cases.
for _ in range(t):
    n = int(input())
    # Length of the line is given.
    people = list(input())
    oldSum = getCurrentSum(people=people)
    diffList = getDifference(people=people)
    for k in range(n):
        if diffList[k]>0:
            currSum = oldSum+diffList[k]
        else:
            currSum = oldSum
        print(currSum, end=" ")
        oldSum = currSum
    print("")