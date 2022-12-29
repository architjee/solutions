class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s1)+len(s2)==len(s3):
            pass
        else:
            return False;
        dp = {}
        import collections
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        if c1+c2!=collections.Counter(s3):
            return False
        # Code here
        def aux_is_interleaved(a_idx, b_idx, c_idx):
            key = a_idx, b_idx, c_idx
            
            if c_idx<0:
                return False
            if c_idx==0:
                dp[key] = True
                return True
            if key not in dp:
                if (a_idx>=0 and c_idx>=0 and s1[a_idx]==s3[c_idx] and  aux_is_interleaved(a_idx-1, b_idx,c_idx-1)) or (b_idx>=0 and c_idx>=0 and s2[b_idx]==s3[c_idx] and aux_is_interleaved(a_idx, b_idx-1, c_idx-1)):
                    dp[key] = True
                else:
                    dp[key]= False
            return dp[key]
        return aux_is_interleaved(len(s1)-1, len(s2)-1, len(s3)-1)