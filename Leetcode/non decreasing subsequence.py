class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def aux(idx, partial):
            if idx==len(nums):
                if len(partial)>=2:
                    result.add(partial[:])
                return 
            if not partial or partial[-1]<=nums[idx]:
                ### Can add
                aux(idx+1, partial+(nums[idx],))
                aux(idx+1, partial)
            else:
                aux(idx+1, partial)
        aux(0, ())
        return result