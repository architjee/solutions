class Solution:
    def minWindow(self, s: str, t: str) -> str:
        Subarray = collections.namedtuple('Subarray', ('start', 'end'))
        keywords_to_cover = collections.Counter(t)
        result = Subarray(-1,-1)
        remaining_to_cover = len(t)
        left = 0
        for right, c in enumerate(s):
            if c in keywords_to_cover:
                keywords_to_cover[c] -= 1
                if keywords_to_cover[c] >=0:
                    remaining_to_cover -=1
            # Now moving the left pointer till it stops covering the keywords.
            while remaining_to_cover==0:
                if result == (-1, -1) or right- left < result[1]-result[0]:
                    result = (left, right)
                left_ele = s[left]
                if left_ele in keywords_to_cover:
                    keywords_to_cover[left_ele] += 1
                    if keywords_to_cover[left_ele]>0:
                        remaining_to_cover += 1
                left +=1
        return s[result[0]: result[1]+1]