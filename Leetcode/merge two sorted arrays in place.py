class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tail1 = m -1
        tail2 = n- 1
        tail3 = m+n-1
        while tail1>=0 and tail2>=0:
            if nums1[tail1]>nums2[tail2]:
                nums1[tail3]=nums1[tail1]
                tail1-=1
            else:
                nums1[tail3] = nums2[tail2]
                tail2-=1
            tail3-=1
        while tail1>=0:
            nums1[tail3] = nums1[tail1]
            tail1-=1
            tail3-=1
        while tail2>=0:
            nums1[tail3] = nums2[tail2]
            tail2-=1
            tail3-=1