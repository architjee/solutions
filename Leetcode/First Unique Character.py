class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x] = 1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1;