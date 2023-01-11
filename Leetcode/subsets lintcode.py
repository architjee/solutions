from typing import (
    List,
)

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
             we will sort your return value in output
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        result = []
        def aux(idx, partial_answer):
            if idx==len(nums):
                partial_answer.sort()
                result.append(partial_answer[:])
                return
            aux(idx+1, partial_answer)
            aux(idx+1, partial_answer+[nums[idx]])
        aux(0, [])
        
        return result