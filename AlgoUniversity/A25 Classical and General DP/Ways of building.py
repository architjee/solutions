prime = 1000000007
from types import GeneratorType
t = int(input())
for ti in range(t):
    n, s = map(int,input().split())
    arr = list(map(int,input().split()))
    mat = [0]*(s+1)
    mat[0]=1
    for i in range(n):
        for j in range(arr[i],s+1):
            mat[j] += mat[j-arr[i]]
    print(mat[s]%prime)

    