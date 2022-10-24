# With reference to code by Koutetsu666
from collections import defaultdict

n = int(input())
A = [0] + list(map(int, input().split()))
d = defaultdict(int)
for i in range(1, n+1):
    a=A[i]
    d[2*i]=d[a]+1
    d[2*i+1]=d[a]+1

for i in range(1,2*n+2):
    print(d[i])