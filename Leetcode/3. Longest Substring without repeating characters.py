class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We will try to use a sliding window obtained via two-pointer approach::
       
        if not s:
            return 0
        
        maxSizePossible =0
        previousEnd = 0
        # TODO condition here
        while previousEnd < len(s)-1 :
            start = previousEnd
            curr = start
            validator = set(s[start])
            while curr<len(s)-1 and s[curr+1] not in validator:
                curr+=1
                validator.add(s[curr])
            maxSizePossible = max(maxSizePossible, len(validator))
            previousEnd = start+1
        if not maxSizePossible:
            return 1
        return maxSizePossible 