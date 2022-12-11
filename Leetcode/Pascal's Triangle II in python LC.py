from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        result.append([1])
        if(numRows==1):
            return result
        result.append([1,1]) 
        if(numRows==2):
            return result
        for _ in range(2, numRows):
            prev_row = result[-1]
            new_row = [1]
            for index in range(len(prev_row)-1):
                new_row.append(prev_row[index]+prev_row[index+1])
            new_row.append(1)
            result.append(new_row)
        return result