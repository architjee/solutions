class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ## Consider this as a variant of longest common substring/ subsequence.
        dp = [[0]*(len(nums1)+1) for x in range(len(nums2) + 1)]
        
        for j in range(len(nums1)+1):
            for i in range(len(nums2)+1):
                if i==0 or j==0:
                    continue
                if nums1[j-1]==nums2[i-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=0
        mymax = dp[0][0]
        for row in dp:
            mymax = max(mymax, max(row))
        return mymax