import functools
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return functools.reduce(
            lambda result, element : (result*26) + ord(element)-ord('A')+1, 
            columnTitle,
            0
        )