class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for x in range(len(s)//2):
            s[x], s[~x]= s[~x], s[x]