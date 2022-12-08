from typing import *


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ## Second attempt I think we can do this via sorting both the nums1 and nums2
        ## Also keeping two pointers,
        nums1.sort()
        nums2.sort()
        ptr_1, ptr_2 = 0, 0
        result_set = []
        firstIteration = True
        while ptr_1<len(nums1) and ptr_2<len(nums2) and k>0:
            result_set.append([nums1[ptr_1], nums2[ptr_2]])
            
            if ptr_1<len(nums1)-1 and ptr_2<len(nums2)-1:
                if nums1[ptr_1+1]+nums2[ptr_2] < nums1[ptr_1]+nums2[ptr_2+1]:
                    ptr_1+=1
                else:
                    ptr_2+=1
            elif ptr_1<len(nums1)-1:
                ptr_1+=1
            else:
                ptr_2+=1
            
            k-=1
        print(ptr_1, ptr_2)

        while ptr_1<len(nums1) and k>0 and ptr_2<len(nums2):
            result_set.append([nums1[ptr_1], nums2[ptr_2]])
            ptr_1+=1
            k-=1
        while ptr_2<len(nums2) and k>0 and ptr_1<len(nums1):
            result_set.append([nums1[ptr_1], nums2[ptr_2]])
            ptr_2+=1
            k-=1
        
        return result_set    
            ## Select any one element: