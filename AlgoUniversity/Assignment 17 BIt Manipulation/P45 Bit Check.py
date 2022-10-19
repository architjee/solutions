# We are given two integers, n and k.
n, k = map(int, input().split())
if((n>>k)&1):
    print(1)
else:
    print(0)