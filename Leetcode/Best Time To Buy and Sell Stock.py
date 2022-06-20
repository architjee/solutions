class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        msf = prices[0]
        maxProfit = 0
        for x in prices:
            msf = min(msf, x)
            maxProfit = max(maxProfit, x-msf)
        return maxProfit