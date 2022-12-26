n, k = map(int,input().split())
arr = list(map(int,input().split()))
import collections
count = collections.Counter(arr)
d = collections.defaultdict(list)
for number, frequency in count.items():
    d[frequency].append(number)
frequencies = list(d.keys())
frequencies.sort(reverse=True)
result = []
for f in frequencies:
    numbers_with_give_f = d[f]
    numbers_with_give_f.sort()
    need = k-len(result)
    final = min(need, len(numbers_with_give_f))
    if need<=0:
        break 
    result += numbers_with_give_f[:final]
print(*result, sep=' ')