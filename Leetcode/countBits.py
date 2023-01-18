class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []
        for x in range(n+1):
            result = 0
            while x:
                result += x%2
                x = x//2
            nums.append(result)
        return nums