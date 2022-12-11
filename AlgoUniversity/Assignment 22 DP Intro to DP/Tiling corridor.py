n = int(input())
PRIME = 1000000007
dp = [x%PRIME for x in range(n+1)]
for i in range(3,n+1):
    dp[i] = dp[i-1]%PRIME+dp[i-2]%PRIME
    dp[i] = dp[i]%PRIME
print(dp[n])