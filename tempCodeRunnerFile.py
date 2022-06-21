 maxSubArraySum(listA):
    maxSoFar = 0;
    summation = 0;
    for x in listA:
        summation += x;
        maxSoFar = max(maxSoFar, summation)
        if(summation<0):
            summation = 0;
    return maxSoFar