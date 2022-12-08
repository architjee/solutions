
class Solution:
    def minMoves2(self, nums) -> int:
        # The question is trying to mess with me,
        # After looking at a solution, Now I know that I have to find a median,
        nums.sort()
        minMoves = 0
        median = nums[len(nums)//2]
        for num in nums:
            minMoves += abs( num - median)
        return minMoves