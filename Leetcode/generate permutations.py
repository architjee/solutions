class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = [nums[:]]
        def next_permutation(nums, n):
            j=n-1
            for j in reversed(range(n)):
                if j==0:
                    nums.sort()
                    return nums
                elif nums[j-1]<nums[j]:
                    break
            e = j-1
            i=n-1
            for i in reversed(range(e+1, n)):
                if nums[i]> nums[e]:
                    break
            nums[i], nums[e] = nums[e], nums[i]
            def my_reverse(start_idx, end_idx):
                while start_idx < end_idx:
                    nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
                    start_idx +=1
                    end_idx -=1
            my_reverse(e+1, n-1)
            return nums
        new_perm = next_permutation(nums, len(nums))
        while new_perm != ans[0]:
            ans.append(new_perm[:])
            new_perm=next_permutation(new_perm, len(new_perm))
        return ans
