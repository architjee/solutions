class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_array = {}
        def lcs_aux(idx1, idx2):
            key = (idx1,idx2)
            if idx1<0 or idx2<0:
                return 0
            if key not in dp_array:
                if text1[idx1]==text2[idx2]:
                    dp_array[key] = 1 + lcs_aux(idx1-1, idx2-1)
                else:
                    dp_array[key]= max(lcs_aux(idx1-1,idx2),lcs_aux(idx1,idx2-1))
            return dp_array[key]
        result = lcs_aux(len(text1)-1, len(text2)-1)
        return result