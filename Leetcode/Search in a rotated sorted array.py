from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## First we will search for the mid point.
        ## Look at an example nums = 100,200,300,1,2,3,4
        ##                            0,  1,  2, 3,4,5,6
        def getMidPoint(nums):
            left ,right = 0, len(nums)-1
            while left<right:
                mid = (left+right)//2
                if nums[mid]>nums[right]:
                    left = mid+1
                else:
                    right = mid
            return left
        def custom_b_search(start_idx, end_idx, search_key):
            low, high = start_idx, end_idx
            ans = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==search_key:
                    return mid # This is our answer
                elif nums[mid]>search_key:
                    high = mid-1
                else :
                    low = mid+1
            return -1
        x = getMidPoint(nums)
        if not x:
            return custom_b_search(0, len(nums)-1, target)
        left_ans = custom_b_search(0, x-1, target)
        right_ans = custom_b_search(x, len(nums)-1, target)
        if left_ans == -1:
            return right_ans
        if right_ans == -1:
            return left_ans