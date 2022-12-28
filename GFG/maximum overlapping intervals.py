from typing import List

import collections
class Solution:
    def overlap(self, n : int, intervals : List[List[int]]) -> int:
        # code here
        endpoints = []
        Endpoint = collections.namedtuple('Endpoint', ('val', 'is_start'))
        for interval in intervals:
            u1 = Endpoint(interval[0], True)
            u2 = Endpoint(interval[1], False)
            endpoints.append(u1)
            endpoints.append(u2)
        endpoints.sort(key=lambda x: (x.val, not x.is_start))
        count = 0
        ans = 0
        for e in endpoints:
            if e.is_start:
                count+=1
                ans = max(ans, count)
            else:
                count -=1
        return ans