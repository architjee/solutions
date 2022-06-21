def maxSubArraySum(listA):
    maxSoFar = 0;
    summation = 0;
    for x in listA:
        summation += x;
        maxSoFar = max(maxSoFar, summation)
        if(summation<0):
            summation = 0;
    return maxSoFar
t = int(input())
for _ in range(t):
    n = int(input())
    listA = list(map(int, input().split()))
    # print(max( kadane's, total + kadanes' on -ve))
    a = maxSubArraySum(listA);
    for i in range(len(listA)):
        listA[i] *=-1
    # print(sum(listA))
    b = maxSubArraySum(listA)
    print(max(a,b-sum(listA)))