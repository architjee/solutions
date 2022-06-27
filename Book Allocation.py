def isValid(listA, n, m, mxp):
    students = 0;
    i=0;
    summation = 0;
    while(i<n):
        summation += listA[i];
        if(summation>mxp):
            students += 1;
            summation = listA[i];
        i+=1
    if students < m:
        return True
    return False;
t = int(input())
for _ in range(t):
        
    n,m = map(int, input().split())
    listA =list( map(int, input().split()));
    high = (sum(listA));
    # print(listA)
    mid=0;
    result = -1;
    low = max(listA);
    while low<=high:
        mid =( low+ high)//2;
        if isValid(listA, n, m, mid):
            # We can go for lower
            result =mid
            high = mid-1;
        else:
            # We can go for higher
            low = mid+1;
    # Now max allowed sum is mid.
    print(result)
