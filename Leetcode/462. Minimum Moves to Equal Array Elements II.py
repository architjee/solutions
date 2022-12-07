from typing import *
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        ## We just have to choose a number as target and find the difference between all elements to that target.
        ## The number will always be between min and max that is certain.
        ## The following is a brute force and unoptimized solution but just testing the waters
        def getDifference(nums, target):
            diff = 0
            for ele in nums:
                diff += abs(target-ele)
            return diff
        min_ele = min(nums)
        max_ele = max(nums)
        if min_ele == max_ele:
            return 0
        minPossible = 1000000007
        for targetC in range(min_ele, max_ele):
            minPossible = min(minPossible, getDifference(nums, targetC))
        return minPossible
