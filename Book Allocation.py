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
n,m = map(int, input().split())
listA =list( map(int, input().split()));
high = (sum(listA));
# print(listA)
mid=0;
low = max(listA);
while low<=high:
    mid =( low+ high)//2;
    if isValid(listA, n, m, mid):
        # We can go for lower
        high = mid-1;
    else:
        # We can go for higher
        low = mid+1;
# Now max allowed sum is mid.
summation  = 0;
maxSoFar = 0;
students = 0;
i=0;
print("here ", mid)
summation = 0;
while(i<n):
    summation += listA[i];
    if(summation>mid):
        students += 1;
        summation = listA[i];
    maxSoFar = max(summation, maxSoFar)
    i+=1
print(maxSoFar);