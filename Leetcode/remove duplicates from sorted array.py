class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## Given that nums is already sorted.
        write_idx = 1
        for cand in nums[1:]:
            if cand!=nums[write_idx-1]:
                nums[write_idx]= cand
                write_idx += 1
        return write_idx