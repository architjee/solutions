n= int(input())
arr = list(map(int, input().split()))
min_sum , max_sum = 0, max(arr)
import itertools
for running_sum in itertools.accumulate(arr):
    min_sum = min(min_sum, running_sum)
    max_sum = max(max_sum, running_sum - min_sum)
if not max_sum:
    print(max(arr))
else:
    print(max_sum)