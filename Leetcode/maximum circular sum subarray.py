class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_so_far = 0
        min_sum_possible = 0
        for x in itertools.accumulate(nums):
            max_so_far = max(max_so_far, x)
            min_sum_possible = min(min_sum_possible, x-max_so_far)
        print(min_sum_possible)

        min_so_far = 0
        max_sum_possible = 0
        for x in itertools.accumulate(nums):
            min_so_far = min(min_so_far, x)
            max_sum_possible = max(max_sum_possible, x-min_so_far)
        print(max_sum_possible-min_sum_possible)
        if sum(nums)==min_sum_possible:
            if max_sum_possible == 0:
                return max(nums)
            return max_sum_possible
        return max(max_sum_possible, sum(nums)-min_sum_possible) 