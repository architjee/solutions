class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def directed_subset_creator(idx, partial_subset):
            if idx==len(nums):
                result.append(partial_subset[:])
                return
            directed_subset_creator(idx+1, partial_subset)
            directed_subset_creator(idx+1, partial_subset+[nums[idx]])
        directed_subset_creator(0, [])
        return result