n = int(input())
nums = list(map(int, input().split()))
maxValPossible = float('-inf')
for i in range(n):
    for j in range(i+1, n):
        maxValPossible = max(maxValPossible, nums[i]&nums[j])
print(maxValPossible)