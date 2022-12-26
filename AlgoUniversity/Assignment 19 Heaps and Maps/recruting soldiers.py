n = int(input())
arr = list(map(int, input().split()))
import collections
c_map = collections.Counter(arr)
count = 0
print(c_map)
for c in c_map.values():
    count += (c//2)%2
print(count)