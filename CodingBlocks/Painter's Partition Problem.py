# 2
# 2
# 1 10
def isValidOperation(bigList, k,  maxAllowedSum):
    cntPainters = 1;
    maxSumTillNow = 0;
    for x in bigList:
        if( x> maxAllowedSum):
            return False;
        if((x+maxSumTillNow)> maxAllowedSum):
            cntPainters +=1;
            if(cntPainters>k):
                return False;
            maxSumTillNow = x;
        else:
            maxSumTillNow += x;
    if(cntPainters>k):
        return False;
    return True;
k = int(input());
n = int(input());
bigList = list(map(int, input().split()))

low = max(bigList);
high = sum(bigList);
result = -1
while low<=high:
    mid = (low+high)//2;
    if isValidOperation(bigList, k, mid):
        result = mid;
        high = mid-1;
    else:
        low = mid+1;
print(result);