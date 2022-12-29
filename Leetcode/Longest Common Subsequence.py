class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def LCSLength(X, Y, i, j, dp):

            if i == 0 or j == 0:
                return 0
            key = (i, j)
            if key not in dp:

                if X[i - 1] == Y[j - 1]:
                    dp[key] = LCSLength(X, Y, i - 1, j - 1, dp) + 1

                else:
                    dp[key] = max(LCSLength(X, Y, i, j - 1, dp), LCSLength(X, Y, i - 1, j, dp))

            return dp[key]
        return LCSLength(text1,text2,len(text1), len(text2),dp)
                    