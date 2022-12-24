class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find e
        size = len(nums)
        for index in reversed(range(size)):
            if index == 0:
                nums.sort()
                return 
            if nums[index-1]<nums[index]:
                break
        e = index-1
        # print('index e is ',e)
        for j in range(len(nums)-1, e-1, -1):
            if nums[j]>nums[e]:
                break
        nums[e], nums[j] = nums[j], nums[e]
        def reverse(start_idx, end_idx):
            while start_idx < end_idx:
                nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                start_idx+=1
                end_idx-=1
        reverse(e+1, len(nums)-1)