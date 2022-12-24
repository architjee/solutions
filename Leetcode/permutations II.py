class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [nums[:]]

        def next_perm(nums):
            size = len(nums)
            index = size - 2
            while index >= 0 and nums[index] > nums[index + 1]:
                index -= 1
            if index == -1:
                nums.sort()
                return nums
            j = size - 1
            for j in reversed(range(index + 1, size)):
                if nums[j] > nums[index]:
                    break
            nums[j], nums[index] = nums[index], nums[j]

            def reverse(start_idx, end_idx):
                while start_idx < end_idx:
                    nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                    start_idx += 1
                    end_idx -= 1

            reverse(index + 1, size - 1)
            return nums
        next_perm(nums)
        while True:
            if nums==ans[0]:
                break
            while nums==ans[-1]:
                next_perm(nums)
            if nums==ans[0]:
                break
            ans.append(nums[:])
            

        return ans
