class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i in range(len(nums)):
            remaining = target-nums[i]
            if remaining in num_to_index:
                return [num_to_index[remaining], i]
            num_to_index[nums[i]]=i

## Two sum problem hashmap approach.
