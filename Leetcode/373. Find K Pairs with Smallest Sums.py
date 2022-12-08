from typing import *


# This is the TLE solution
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ## Think the brute force solution, 
        ## if n is size of nums1 and m is size of nums2
        ## n*m(log(n*m))
        if not k:
            return []
        all_pairs = []
        for n1 in nums1:
            for n2 in nums2:
                all_pairs.append([n1,n2])
        all_pairs.sort(key=lambda x: sum(x))
        return all_pairs[:k]