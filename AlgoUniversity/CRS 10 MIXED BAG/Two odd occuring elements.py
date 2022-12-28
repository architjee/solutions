n = int(input())
arr = list(map(int,input().split()))
import collections
counter = collections.Counter(arr)
result = []
for key, value in counter.items():
    if value%2:
        result.append(key)
result.sort()
print(*result, sep=' ')

