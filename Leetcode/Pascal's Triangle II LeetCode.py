from typing import *
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]]
        if(rowIndex==0):
            return result[-1]
        result.append([1,1]) 
        if(rowIndex==1):
            return result[-1]
        prev_row = result[-1]
        for _ in range(2, rowIndex+1):
            new_row = [1]
            for index in range(len(prev_row)-1):
                new_row.append(prev_row[index]+prev_row[index+1])
            new_row.append(1)
            prev_row = new_row
        return prev_row