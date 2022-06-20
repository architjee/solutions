class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if(len(s)==len(t) and s==t): 
            return True
        return False
        