class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def createPermutations(nums, i):
            if i==len(nums)-1:
                permutations.append(nums[0:])
                return 
            for x in range(i, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                createPermutations(nums, i+1)
                nums[i], nums[x] = nums[x], nums[i]
        createPermutations(nums, 0)  
        return permutations
                