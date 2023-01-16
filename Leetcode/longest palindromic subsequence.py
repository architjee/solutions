class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        s1 = s
        dp =[[0]*(len(s1)+1) for j in range(len(s2)+1)]
        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 or j==0:
                    continue
                if s1[i-1]==s2[j-1]:
                    dp[i][j]= 1+dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]