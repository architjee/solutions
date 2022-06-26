from sys import stdin;
import sys
n=0
nums = []
dp=[[-1 for x in range(1000)] for y in range(1000)]
def mixingOrder(nums, i, j):
    if(i>=j):
        return 0;
    if(dp[i][j]!=-1):
        return dp[i][j]
    dp[i][j] = sys.maxsize
    for k in range(i, j+1):
        dp[i][j] = min(dp[i][j], mixingOrder(nums, i, k)+ mixingOrder(nums, k+1, j) + csum(nums,i, k)*csum(nums, k+1, j))
    return dp[i][j]
def csum(nums, start, end):
    summation = 0;
    for x in range(start, end+1):
        summation += nums[x];
        summation %= 100;
    return summation
t=0
for line in stdin:
    line = line.strip();
    if t%2==0:
        n = int(line);
    else:
        nums = []
        dp=[[-1 for x in range(1000)] for y in range(1000)]
        nums = list(map(int, line.split()));
        # here we have both n and nums;
        # now we can proceed with operations that we need to perform
        print(mixingOrder(nums, 0, n-1))

    t+=1