n = int(input())
arr = list(map(int,input().split()))
min_prefix = [arr[0] for x in range(n)]
max_prefix = [arr[0] for x in range(n)]
for i in range(1, n):
    min_prefix[i] = min(min_prefix[i-1],arr[i])
    max_prefix[i] = max(max_prefix[i-1],arr[i])
total_sum = 0
for i in range(n):
    for j in range(i+1, n):
        ## Maximum integer at j is max_prefix[j]
        ## Maximum integer at i is max_prefix[i]
        val = max_prefix[j]-max_prefix[i]+min_prefix[j]-min_prefix[j]
        total_sum += val
print(total_sum)