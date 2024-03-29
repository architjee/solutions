class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        dp = {}
        # Code here
        def aux_is_interleaved(a_idx, b_idx, c_idx):
            key = a_idx, b_idx, c_idx
            if key in dp:
                return dp[key]
            if c_idx<=0 and (a_idx>0 or b_idx>0) :
                dp[key] = False
                return False
            if c_idx<=0:
                dp[key] = True
                return True
            if key not in dp:
                if (A[a_idx]==C[c_idx] and  aux_is_interleaved(a_idx-1, b_idx,c_idx-1)) or (B[b_idx]==C[c_idx] and aux_is_interleaved(a_idx, b_idx-1, c_idx-1)):
                    dp[key] = True
                else:
                    dp[key]= False
            return dp[key]
        return aux_is_interleaved(len(A)-1, len(B)-1, len(C)-1)
