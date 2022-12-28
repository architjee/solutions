n = int(input())
arr = list(map(int,input().split()))
total_sum = 0
arr.sort()
i= 0
import functools
while i<n and arr[i]<0:
    i+=1
## There are i+1 negative numbers.
if (i+1)%2:
    if arr[0]>=0:
        total_sum = sum(arr)
    else:
        total_sum = functools.reduce(lambda v,c : v+abs(c), arr[:i-1], 0) + arr[i-1] +  functools.reduce(lambda v,c : v+abs(c), arr[i:], 0)
else:
    total_sum = functools.reduce(lambda v,c: v+abs(c),arr,0)
    ## Take abs of every number.
print(total_sum)